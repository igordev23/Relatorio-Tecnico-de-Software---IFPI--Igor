#!/usr/bin/env python3
"""Valida artigo_bia.pdf contra regras-relatorio-monografia.md (R01–R28).

Uso:
  python3 -m unittest testes.test_formato_tcc -v
  python3 testes/test_formato_tcc.py
"""

from __future__ import annotations

import hashlib
import re
import statistics
import sys
import unittest
from pathlib import Path

try:
    import pymupdf
except ImportError:  # pragma: no cover
    import fitz as pymupdf  # type: ignore

ROOT = Path(__file__).resolve().parents[1]
PDF_MAIN = ROOT / "artigo_bia.pdf"
PDF_ENTREGA = ROOT / "anexos" / "2026_tcc_fisSantos.pdf"

CM = 72 / 2.54  # pt por cm
A4 = (595.27, 841.89)
MARGIN_TOL = 0.25 * CM  # ±2,5 mm


def _letters(s: str) -> str:
    return "".join(c for c in s if c.isalpha())


def _is_all_upper(s: str) -> bool:
    letters = _letters(s)
    return bool(letters) and letters == letters.upper()


def _is_sentence_case(s: str) -> bool:
    """Primeira letra maiúscula e ao menos uma minúscula (marcas/siglas ok)."""
    letters = [c for c in s if c.isalpha()]
    if not letters:
        return False
    if letters[0].islower():
        return False
    # Marcas só com minúsculas no meio (shadcn/ui, date-fns, qrcode) ou title case
    return any(c.islower() for c in letters) or "/" in s or "-" in s


def _page_lines(page) -> list[dict]:
    lines = []
    for block in page.get_text("dict")["blocks"]:
        if block.get("type") != 0:
            continue
        for line in block["lines"]:
            spans = line["spans"]
            text = "".join(s["text"] for s in spans).strip()
            if not text:
                continue
            lines.append(
                {
                    "text": text,
                    "y": line["bbox"][1],
                    "x": spans[0]["bbox"][0],
                    "x1": spans[-1]["bbox"][2],
                    "font": spans[0]["font"],
                    "title_font": spans[1]["font"] if len(spans) > 1 else spans[0]["font"],
                    "size": spans[0]["size"],
                    "spans": spans,
                }
            )
    return lines


def _find_page(doc, predicate, start=0, end=None) -> int | None:
    end = doc.page_count if end is None else end
    for i in range(start, end):
        if predicate(doc[i].get_text()):
            return i
    return None


def _first_textual_page(doc) -> int:
    """Índice 0-based da primeira página da parte textual (1 INTRODUÇÃO)."""
    for i in range(doc.page_count):
        lines = _page_lines(doc[i])
        for j, line in enumerate(lines):
            if line["text"] == "1" and line["x"] < 120 and "Bold" in line["font"]:
                if j + 1 < len(lines) and lines[j + 1]["text"].startswith("INTRODU"):
                    return i
    return 0


def _extract_body_titles(doc) -> list[tuple]:
    """[(page, num, title, level, num_font, title_font, y), ...] só na parte textual.

    Ignora sequências densas (tabelas/listas numeradas com ~1 linha de entrelinha).
    """
    raw = []
    start = _first_textual_page(doc)
    for i in range(start, doc.page_count):
        lines = _page_lines(doc[i])
        for j, line in enumerate(lines):
            if line["x"] > 400:
                continue
            if not re.fullmatch(r"\d+(?:\.\d+){0,2}", line["text"]):
                continue
            if j + 1 >= len(lines):
                continue
            nxt = lines[j + 1]
            if nxt["y"] - line["y"] > 30:
                continue
            if nxt["text"].count(".") > 8:
                continue
            level = line["text"].count(".") + 1
            num = line["text"]
            title = nxt["text"]
            if level == 1:
                if not re.fullmatch(r"[1-9]", num):
                    continue
                if "Bold" not in nxt["font"]:
                    continue
                if not _is_all_upper(title):
                    continue
            elif level == 2:
                if not re.match(r"^[1-9]\.\d+$", num):
                    continue
            elif level == 3:
                if not re.match(r"^[1-9]\.\d+\.\d+$", num):
                    continue
            else:
                continue
            raw.append((i + 1, num, title, level, line["font"], nxt["font"], nxt["y"]))

    # Remove blocos densos na mesma página (gap < 40 pt ⇒ tabela, não heading+corpo)
    titles = []
    for idx, item in enumerate(raw):
        page, y = item[0], item[6]
        dense = False
        if idx + 1 < len(raw):
            nxt = raw[idx + 1]
            if nxt[0] == page and (nxt[6] - y) < 40:
                dense = True
        if idx > 0:
            prev = raw[idx - 1]
            if prev[0] == page and (y - prev[6]) < 40:
                dense = True
        if dense:
            continue
        titles.append(item[:6])  # sem y no retorno público
    return titles


class TestFormatoTCC(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not PDF_MAIN.exists():
            raise unittest.SkipTest(f"PDF não encontrado: {PDF_MAIN}")
        cls.doc = pymupdf.open(PDF_MAIN)
        cls.titles = _extract_body_titles(cls.doc)
        cls.cover = cls.doc[0].get_text()
        cls.toc_idx = _find_page(cls.doc, lambda t: t.lstrip().startswith("SUMÁRIO"))
        cls.resumo_idx = _find_page(cls.doc, lambda t: "RESUMO" in t[:800] and "Palavras-chave" in t)
        cls.ref_idx = _find_page(cls.doc, lambda t: t.lstrip().startswith("REFERÊNCIAS") or "\nREFERÊNCIAS\n" in t[:200], start=50)
        cls.anexo_idx = _find_page(cls.doc, lambda t: "ANEXOS" in t[:300] and "ANEXO A" in t, start=50)

    @classmethod
    def tearDownClass(cls):
        cls.doc.close()

    # --- R27 entrega ---
    def test_R27_pdf_entrega_identico(self):
        self.assertTrue(PDF_ENTREGA.exists(), "Falta anexos/2026_tcc_fisSantos.pdf")
        h1 = hashlib.md5(PDF_MAIN.read_bytes()).hexdigest()
        h2 = hashlib.md5(PDF_ENTREGA.read_bytes()).hexdigest()
        self.assertEqual(h1, h2, "artigo_bia.pdf e anexos/2026_tcc_fisSantos.pdf diferem")

    # --- R12 A4 ---
    def test_R12_formato_A4(self):
        rect = self.doc[0].rect
        self.assertAlmostEqual(rect.width, A4[0], delta=1.0)
        self.assertAlmostEqual(rect.height, A4[1], delta=1.0)

    # --- R13 margens ---
    def test_R13_margens_anverso(self):
        page = self.doc[14]  # parte textual
        words = page.get_text("words")
        # ignora número de página (topo direito)
        body = [w for w in words if not (w[1] < 70 and w[0] > 450)]
        self.assertTrue(body)
        left = min(w[0] for w in body)
        right = page.rect.width - max(w[2] for w in body)
        bottom = page.rect.height - max(w[3] for w in body)
        self.assertAlmostEqual(left, 3 * CM, delta=MARGIN_TOL)
        self.assertAlmostEqual(right, 2 * CM, delta=MARGIN_TOL)
        self.assertAlmostEqual(bottom, 2 * CM, delta=MARGIN_TOL + 0.15 * CM)

    # --- R14 fonte corpo ---
    def test_R14_fonte_corpo_12pt_arial_like(self):
        page = self.doc[14]
        sizes, fonts = [], set()
        for block in page.get_text("dict")["blocks"]:
            if block.get("type") != 0:
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    if len(span["text"].strip()) < 20:
                        continue
                    sizes.append(span["size"])
                    fonts.add(span["font"])
        self.assertTrue(sizes)
        self.assertAlmostEqual(statistics.median(sizes), 12.0, delta=0.2)
        self.assertTrue(
            any("NimbusSan" in f or "Arial" in f or "Times" in f for f in fonts),
            f"Fonte inesperada: {fonts}",
        )

    # --- R15 espaçamento (NBR 10719 / stretch 1.0) ---
    def test_R15_entrelinha_corpo_consistente(self):
        page = self.doc[14]
        baselines = []
        for block in page.get_text("dict")["blocks"]:
            if block.get("type") != 0:
                continue
            for line in block["lines"]:
                text = "".join(s["text"] for s in line["spans"]).strip()
                if len(text) < 40:
                    continue
                for span in line["spans"]:
                    if len(span["text"].strip()) > 20:
                        baselines.append(span["origin"][1])
                        break
        baselines.sort()
        gaps = [b - a for a, b in zip(baselines, baselines[1:]) if 12 < b - a < 18]
        self.assertGreaterEqual(len(gaps), 5, "Poucas linhas de corpo para medir entrelinha")
        med = statistics.median(gaps)
        # stretch 1.0 → ~14,45 pt (simples); não exige 1,5 (ver R15 no .md)
        self.assertGreater(med, 13.5)
        self.assertLess(med, 16.0)

    # --- R01 / R04 ordem e ficha ---
    def test_R01_ordem_pretextual(self):
        self.assertIn("INSTITUTO FEDERAL", self.cover)
        self.assertIn("Francisco Igor", self.doc[1].get_text())
        ficha = self.doc[2].get_text()
        self.assertRegex(ficha, r"Catalogação|CIP|catalogação", re.I)
        self.assertIsNotNone(self.resumo_idx)
        self.assertLess(self.resumo_idx, self.toc_idx)
        listas = [
            _find_page(self.doc, lambda t: t.lstrip().startswith(name))
            for name in (
                "LISTA DE FIGURAS",
                "LISTA DE QUADROS",
                "LISTA DE TABELAS",
                "LISTA DE ABREVIATURAS",
            )
        ]
        for idx in listas:
            self.assertIsNotNone(idx)
            self.assertLess(idx, self.toc_idx)

    def test_R04_ficha_catalografica(self):
        text = self.doc[2].get_text()
        self.assertIn("CRB", text)
        self.assertRegex(text, r"J[uú]lio C[eé]sar|bibliotec", re.I)

    # --- R05 / R06 capa ---
    def test_R05_capa_maiusculas(self):
        lines = [ln.strip() for ln in self.cover.splitlines() if ln.strip()]
        for key in (
            "INSTITUTO FEDERAL",
            "CAMPUS PIRIPIRI",
            "FRANCISCO IGOR SILVA SANTOS",
            "PIRIPIRI",
            "2026",
        ):
            self.assertTrue(any(key in ln for ln in lines), f"Falta na capa: {key}")
        for ln in lines:
            if ln.startswith("CERTIFYHUB"):
                continue
            if "sistema para" in ln.lower():
                continue
            if not _letters(ln):
                # ano / só dígitos — ok se numérico
                continue
            self.assertTrue(_is_all_upper(ln), f"Capa não está em maiúsculas: {ln!r}")

    def test_R06_subtitulo_minusculo_negrito(self):
        title_line = None
        title_font = None
        for line in _page_lines(self.doc[0]):
            if "CERTIFYHUB" in line["text"]:
                title_line = line["text"]
                title_font = line["font"]
                break
        self.assertIsNotNone(title_line)
        self.assertIn(":", title_line)
        main, sub = title_line.split(":", 1)
        self.assertEqual(main.strip(), "CERTIFYHUB")
        self.assertTrue(any(c.islower() for c in sub), f"Subtítulo deveria ter minúsculas: {sub!r}")
        self.assertFalse(_is_all_upper(sub.strip()))
        self.assertIn("Bold", title_font or "", f"Subtítulo/título sem negrito: {title_font}")

    # --- R07 folha de rosto ---
    def test_R07_folha_de_rosto(self):
        text = self.doc[1].get_text()
        self.assertIn("Francisco Igor Silva Santos", text)
        self.assertIn("CERTIFYHUB", text)
        self.assertRegex(text, r"Orientador", re.I)
        self.assertIn("2026", text)

    # --- R08 / R09 resumo ---
    def test_R08_resumo_150_a_500_palavras(self):
        text = self.doc[self.resumo_idx].get_text()
        m = re.search(r"RESUMO\s*(.*?)\s*Palavras-chave", text, re.S | re.I)
        self.assertIsNotNone(m, "Não achou bloco RESUMO…Palavras-chave")
        n = len(re.findall(r"\w+", m.group(1), flags=re.UNICODE))
        self.assertGreaterEqual(n, 150, f"Resumo com {n} palavras (<150)")
        self.assertLessEqual(n, 500, f"Resumo com {n} palavras (>500)")

    def test_R09_palavras_chave(self):
        text = self.doc[self.resumo_idx].get_text()
        self.assertRegex(text, r"Palavras-chave\s*:")
        self.assertIn(";", text)

    # --- R10 sumário ---
    def test_R10_sumario_coluna_unica_e_sem_numero_pos(self):
        self.assertIsNotNone(self.toc_idx)
        title_xs = []
        has_ref = has_anexo = False
        for i in range(self.toc_idx, min(self.toc_idx + 5, self.doc.page_count)):
            page = self.doc[i]
            if i > self.toc_idx and page.get_text().lstrip()[:20].startswith("1"):
                # já entrou na parte textual
                if "INTRODUÇÃO" in page.get_text()[:80] and i > self.toc_idx + 2:
                    break
            for line in _page_lines(page):
                t = line["text"]
                if t in ("REFERÊNCIAS", "ANEXOS") or t.startswith("REFERÊNCIAS") or t.startswith("ANEXOS"):
                    if "REFER" in t:
                        has_ref = True
                    if "ANEXO" in t:
                        has_anexo = True
                    # sem indicativo: x deve ser o da coluna de títulos ou centralizado-ish left
                    continue
                # título do sumário: começa com letra, não é só número, não é SUMÁRIO
                if re.fullmatch(r"\d+", t) or re.fullmatch(r"\d+(?:\.\d+){0,2}", t):
                    continue
                if t == "SUMÁRIO" or t.startswith("SUMÁRIO"):
                    continue
                if re.fullmatch(r"\.+", t.replace(" ", "")):
                    continue
                # linhas de título (com ou sem leaders)
                if re.search(r"[A-Za-zÀ-ÿ]", t) and line["x"] < 200:
                    # exclui número de página à direita
                    if line["x"] > 400:
                        continue
                    # títulos ficam ~4.5em da margem (~138 pt)
                    if 120 <= line["x"] <= 160:
                        title_xs.append(line["x"])
        self.assertTrue(has_ref, "Sumário sem REFERÊNCIAS")
        self.assertTrue(has_anexo, "Sumário sem ANEXOS")
        self.assertGreaterEqual(len(title_xs), 20, "Poucos títulos de sumário medidos")
        spread = max(title_xs) - min(title_xs)
        self.assertLessEqual(spread, 2.0, f"Títulos do sumário desalinhados: xs={sorted(set(round(x,1) for x in title_xs))}")

    # --- R11 / R23 listas e títulos sem número ---
    def test_R11_listas_centralizadas_maiusculas_negrito(self):
        names = (
            "LISTA DE FIGURAS",
            "LISTA DE QUADROS",
            "LISTA DE TABELAS",
            "LISTA DE ABREVIATURAS E SIGLAS",
        )
        page_mid = self.doc[0].rect.width / 2
        for name in names:
            idx = _find_page(self.doc, lambda t, n=name: n in t[:200])
            self.assertIsNotNone(idx, f"Falta {name}")
            found = False
            for line in _page_lines(self.doc[idx]):
                if name in line["text"]:
                    mid = (line["x"] + line["x1"]) / 2
                    self.assertTrue(_is_all_upper(line["text"].split("\n")[0][: len(name) + 5]))
                    self.assertIn("Bold", line["font"])
                    self.assertAlmostEqual(mid, page_mid, delta=25)
                    found = True
                    break
            self.assertTrue(found, f"Título não tipografado: {name}")

    def test_R23_referencias_anexos_centralizados(self):
        self.assertIsNotNone(self.ref_idx)
        self.assertIsNotNone(self.anexo_idx)
        page_mid = self.doc[0].rect.width / 2
        for idx, label in ((self.ref_idx, "REFERÊNCIAS"), (self.anexo_idx, "ANEXOS")):
            for line in _page_lines(self.doc[idx]):
                if line["text"].startswith(label):
                    mid = (line["x"] + line["x1"]) / 2
                    self.assertIn("Bold", line["font"])
                    self.assertTrue(_is_all_upper(label))
                    self.assertAlmostEqual(mid, page_mid, delta=25)
                    break
            else:
                self.fail(f"Não achou título {label}")

    # --- R02 textuais ---
    def test_R02_capitulos_textuais(self):
        nums = {t[1] for t in self.titles if t[3] == 1}
        for n in ("1", "2", "3", "4", "5"):
            self.assertIn(n, nums)
        names = {t[1]: t[2] for t in self.titles if t[3] == 1}
        self.assertIn("INTRODUÇÃO", names["1"])
        self.assertIn("CONSIDERAÇÕES", names["5"])

    # --- R17 paginação ---
    def test_R17_paginacao_parte_textual(self):
        # pré-textuais sem número no topo direito
        for i in range(0, 9):
            words = self.doc[i].get_text("words")
            nums = [w for w in words if re.fullmatch(r"\d+", w[4]) and w[1] < 70 and w[0] > 450]
            self.assertEqual(nums, [], f"Página pré-textual {i+1} numerada: {nums}")
        # textual: primeira página com número
        found = False
        for i in range(10, 20):
            words = self.doc[i].get_text("words")
            nums = [w for w in words if re.fullmatch(r"\d+", w[4]) and w[1] < 70 and w[0] > 450]
            if nums:
                found = True
                self.assertLess(nums[0][1], 70)
                self.assertGreater(nums[0][0], 450)
                break
        self.assertTrue(found, "Numeração da parte textual não encontrada")

    # --- R19 texto entre títulos ---
    def test_R19_texto_entre_titulos(self):
        empty = []
        for i, (page, num, title, level, _, _) in enumerate(self.titles[:-1]):
            page2, num2, title2, level2, _, _ = self.titles[i + 1]
            if page != page2:
                # título no fim da página + próximo no início: exige texto residual ou aceita se há corpo após o primeiro
                pg = self.doc[page - 1]
                lines = _page_lines(pg)
                # acha y do título atual
                y_title = None
                for j, ln in enumerate(lines):
                    if ln["text"] == num and j + 1 < len(lines) and lines[j + 1]["text"] == title:
                        y_title = lines[j + 1]["y"]
                        break
                if y_title is None:
                    continue
                after = [
                    ln["text"]
                    for ln in lines
                    if ln["y"] > y_title + 2
                    and not re.fullmatch(r"\d+(?:\.\d+){0,2}", ln["text"])
                    and ln["x"] < 400
                ]
                meaningful = [t for t in after if len(_letters(t)) > 3]
                if not meaningful:
                    # verifica início da próxima página antes do próximo título
                    lines2 = _page_lines(self.doc[page2 - 1])
                    before = []
                    for ln in lines2:
                        if ln["text"] == num2:
                            break
                        before.append(ln["text"])
                    meaningful = [t for t in before if len(_letters(t)) > 3]
                if not meaningful:
                    empty.append((num, title, num2, title2))
                continue

            # mesma página: texto entre y do título e y do próximo
            lines = _page_lines(self.doc[page - 1])
            y1 = y2 = None
            for j, ln in enumerate(lines):
                if (
                    y1 is None
                    and ln["text"] == num
                    and j + 1 < len(lines)
                    and lines[j + 1]["text"] == title
                ):
                    y1 = lines[j + 1]["y"]
                if (
                    y2 is None
                    and ln["text"] == num2
                    and j + 1 < len(lines)
                    and lines[j + 1]["text"] == title2
                ):
                    y2 = lines[j + 1]["y"]
            if y1 is None or y2 is None:
                continue
            if y2 - y1 < 40:
                # residual de tabela; extração já deveria ter filtrado
                continue
            between = [
                ln["text"]
                for ln in lines
                if y1 + 5 < ln["y"] < y2 - 2
                and not re.fullmatch(r"\d+(?:\.\d+){0,2}", ln["text"])
            ]
            # aceita qualquer corpo com letras (seções curtas de 1 parágrafo)
            meaningful = [t for t in between if len(_letters(t)) > 3]
            if len(meaningful) < 1:
                empty.append((num, title, num2, title2))

        # caso crítico da devolução BIA
        pair = [e for e in empty if e[0] == "1.1" and e[2] == "1.1.1"]
        self.assertEqual(pair, [], "Falta texto entre 1.1 e 1.1.1 (devolução BIA)")
        self.assertEqual(
            empty,
            [],
            "Títulos sem texto entre eles:\n"
            + "\n".join(f"  {a} {b} → {c} {d}" for a, b, c, d in empty[:20]),
        )

    def test_R19_texto_entre_1_1_e_1_1_1(self):
        text = self.doc[14].get_text()  # página dos objetivos
        # pode estar na 15 (índice 14)
        blob = "\n".join(self.doc[i].get_text() for i in range(13, 16))
        m = re.search(r"OBJETIVOS\s*(.*?)\s*1\.1\.1", blob, re.S)
        self.assertIsNotNone(m)
        words = re.findall(r"\w+", m.group(1), flags=re.UNICODE)
        self.assertGreaterEqual(len(words), 20, "Texto entre 1.1 e 1.1.1 insuficiente")

    # --- R20–R22 hierarquia ---
    def test_R20_primarias_caixa_alta_negrito(self):
        prim = [t for t in self.titles if t[3] == 1]
        self.assertGreaterEqual(len(prim), 5)
        for page, num, title, _, nf, tf in prim:
            self.assertTrue(_is_all_upper(title), f"{num} {title}")
            self.assertIn("Bold", tf, f"{num} sem negrito")

    def test_R21_secundarias_caixa_alta_sem_negrito(self):
        secs = [t for t in self.titles if t[3] == 2]
        self.assertGreaterEqual(len(secs), 15)
        for page, num, title, _, nf, tf in secs:
            self.assertTrue(_is_all_upper(title), f"{num} não está em caixa alta: {title}")
            self.assertNotIn("Bold", tf, f"{num} secundária com negrito: {title} ({tf})")

    def test_R22_terciarias_sentence_case_negrito(self):
        ters = [t for t in self.titles if t[3] == 3]
        self.assertGreaterEqual(len(ters), 50)
        bad_case, bad_bold = [], []
        for page, num, title, _, nf, tf in ters:
            if not _is_sentence_case(title) and _is_all_upper(title):
                bad_case.append((num, title))
            if "Bold" not in tf:
                bad_bold.append((num, title, tf))
        self.assertEqual(bad_case, [], f"Terciárias em caixa alta: {bad_case[:10]}")
        self.assertEqual(bad_bold, [], f"Terciárias sem negrito: {bad_bold[:10]}")

    # --- R24 ilustrações ---
    def test_R24_figuras_com_fonte(self):
        missing = []
        for i in range(13, min(85, self.doc.page_count)):
            text = self.doc[i].get_text()
            figs = re.findall(r"Figura\s+\d+", text)
            if not figs:
                continue
            if not re.search(r"Fonte\s*:", text):
                missing.append(i + 1)
        # tolerar no máx. 1 página ambígua (figura só citada)
        self.assertLessEqual(len(missing), 1, f"Páginas com Figura sem 'Fonte:': {missing}")

    # --- R25 / R26 ---
    def test_R25_referencias_presentes(self):
        self.assertIsNotNone(self.ref_idx)
        text = self.doc[self.ref_idx].get_text()
        self.assertRegex(text, r"\[\d+\]")

    def test_R26_anexos_identificados(self):
        self.assertIsNotNone(self.anexo_idx)
        blob = "\n".join(self.doc[i].get_text() for i in range(self.anexo_idx, self.doc.page_count))
        self.assertIn("ANEXO A", blob)
        self.assertIn("ANEXO B", blob)


if __name__ == "__main__":
    # permite: python3 testes/test_formato_tcc.py
    sys.path.insert(0, str(ROOT))
    unittest.main(verbosity=2)
