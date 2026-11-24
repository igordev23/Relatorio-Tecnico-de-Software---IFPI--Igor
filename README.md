# Relatório Técnico de Software — IFPI

**Sistema para Emissão, Gestão e Autenticação de Certificados**

Relatório técnico de software desenvolvido como Trabalho de Conclusão de Curso do Tecnólogo em Análise e Desenvolvimento de Sistemas do Instituto Federal do Piauí (IFPI) — Campus Piripiri.

---

## Publicado na BIA

Este TCC foi aprovado pela biblioteca e publicado no **BIA — Repositório Institucional do IFPI**.

- **Trabalho:** CERTIFYHUB: sistema para emissão, gestão e autenticação de certificados
- **Coleção:** Tecnologia em Análise e Desenvolvimento de Sistemas — Piripiri
- **Endereço permanente:** https://bia.ifpi.edu.br/handle/123456789/6145

Use este endereço para citar e divulgar o trabalho (por exemplo, no currículo Lattes).

---

## Tipo de documento

Este trabalho é um **relatório técnico apresentado como TCC**, com estrutura de relatório (IFPI cap. 9 e NBR 10719) e apresentação adaptada ao modelo de monografia de TCC do IFPI (cap. 5 e template). Por ser uma adaptação, **pode diferir um pouco do documento oficial da disciplina** — quando há divergência entre as fontes, a regra e a decisão adotada são registradas explicitamente em `regras-relatorio-monografia.md`.

---

## Nome conforme os anexos do TCC

Conforme definido nos anexos do trabalho e nas devoluções da BIA (bibliotecário Júlio César, ago–nov/2026):

- **Título principal (maiúsculo):** `CERTIFYHUB`
- **Subtítulo (minúsculo, negrito):** `sistema para emissão, gestão e autenticação de certificados`
- **Nome completo:** `CERTIFYHUB: sistema para emissão, gestão e autenticação de certificados`
- **Autor:** Francisco Igor Silva Santos
- **Orientador:** Prof. Me. Mayllon Veras da Silva
- **Curso:** Tecnólogo em Análise e Desenvolvimento de Sistemas — IFPI Campus Piripiri
- **Data de aprovação:** 15/07/2026

O título segue o formato aceito pela BIA: palavra principal em caixa alta, subtítulo em minúsculo e negrito, todo o restante da capa em maiúsculas (exceto o subtítulo).

---

## Formato aceito pela BIA (repositório para submissão à BIA)

Este repositório é o canal de entrega do TCC à BIA (Biblioteca) do IFPI. O modelo final aprovado está na branch `main`, preparado a partir da branch `bia` (a última modificada antes do modelo aprovado).

### Regras aplicadas (checklist R01–R36)

Documentadas em `regras-relatorio-monografia.md`, com base em:

- Manual de Trabalhos Acadêmicos do IFPI (cap. 3, 5, 9, 10, 11)
- ABNT NBR 10719:2015 (`REGISTRO_BIA/nbr-10719-atualizada.pdf`)
- Template de monografia do IFPI (`REGISTRO_BIA/MONOGRAFIATEMPLATE.pdf`)
- 5 devoluções do BIA (checklist anti-reincidência D1–D9)

### Principais exigências da BIA (D1–D9)

| ID | Exigência | Onde está |
|----|-----------|-----------|
| D1 | Título `CERTIFYHUB` maiúsculo | Capa (`artigo_bia.tex`, linha 229) |
| D2 | Texto da capa em maiúscula (exceto subtítulo) | Capa (`artigo_bia.tex`) |
| D3 | Ficha catalográfica presente | `anexos/ficha_catalografica.pdf` |
| D4 | Texto entre seção e subdivisão (ex.: 1.1 → 1.1.1) | Partes textuais |
| D5 | Subtítulo minúsculo e negrito | Capa (`artigo_bia.tex`) |
| D6 | Fonte dos títulos padronizada (12 pt / hierarquia) | `artigo_bia.tex` |
| D7 | Sumário alinhado à esquerda (coluna única) | `artigo_bia.tex` |
| D8 | Secundárias: caixa alta, sem negrito | `artigo_bia.tex` |
| D9 | Terciárias: minúsculas com negrito | `artigo_bia.tex` |

### Arquivos de entrega

- `artigo_bia.tex` — fonte LaTeX do modelo de TCC conforme formato aprovado pela BIA
- `artigo_bia.pdf` — PDF final do artigo/modelo
- `anexos/2026_tcc_fisSantos.pdf` — PDF de entrega (idêntico a `artigo_bia.pdf`, regra R27)
- `anexos/Processo-requerimento.pdf` — processo/requerimento do TCC
- `anexos/ficha_catalografica.pdf` — ficha catalográfica (obrigatória para TCC)
- `anexos/requerimento.pdf` — requerimento
- `regras-relatorio-monografia.md` — checklist de regras (fonte: Manual IFPI, NBR 10719, devoluções BIA)
- `REGISTRO_BIA/` — registro do artigo, template e documentação da BIA/NIT
- `testes/test_formato_tcc.py` — suíte de validação de formato (R01–R27)

> **Nota:** arquivos com dados sensíveis (termo de autorização de arquivamento, ficha com dados pessoais e termo `2026_termo_fisSantos.pdf`) foram removidos do histórico do repositório e não constam no `main`.

---

## Como os testes funcionam

A suíte de validação está em `testes/test_formato_tcc.py` e verifica 25 requisitos (R01–R27) do formato aceito pela BIA contra o PDF `artigo_bia.pdf` / `anexos/2026_tcc_fisSantos.pdf`, usando `pymupdf`.

### O que os testes cobrem

- **R01** — Ordem pré-textual (capa, rosto, ficha, resumo, abstract, sumário)
- **R02** — Capítulos textuais (Introdução → Desenvolvimento → Considerações finais)
- **R04** — Ficha catalográfica presente
- **R05** — Capa em caixa alta (exceto subtítulo)
- **R06** — Subtítulo minúsculo e negrito
- **R07** — Folha de rosto
- **R08** — Resumo entre 150 e 500 palavras
- **R09** — Palavras-chave (3 a 5 termos, iniciais minúsculas)
- **R10** — Sumário alinhado à esquerda, coluna única
- **R11** — Listas pré-textuais (figuras, quadros, tabelas, siglas)
- **R12** — Formato A4
- **R13** — Margens (3 cm esquerda/superior, 2 cm direita/inferior)
- **R14** — Fonte do corpo 12 pt (Arial-like)
- **R15** — Espaçamento entre linhas consistente
- **R17** — Paginação parte textual (canto superior direito)
- **R19** — Texto entre seção e subdivisão
- **R20** — Primárias: caixa alta + negrito
- **R21** — Secundárias: caixa alta, sem negrito
- **R22** — Terciárias: minúsculas (sentence case) com negrito
- **R23** — Referências e anexos centralizados
- **R24** — Figuras com fonte
- **R25** — Referências presentes
- **R26** — Anexos identificados (ANEXO A, ANEXO B…)
- **R27** — PDF de entrega idêntico a `artigo_bia.pdf`

### Como rodar

```bash
python3 testes/test_formato_tcc.py
# ou
python3 -m unittest testes.test_formato_tcc -v
```

Resultado esperado:

```
Ran 25 tests in ~4s
OK
```

> Alguns requisitos (R03, R16, R18, R29–R36) não são verificados automaticamente; conferir manualmente em `regras-relatorio-monografia.md`.

---

## Estrutura do repositório

```
Relatorio-Tecnico-de-Software---IFPI--Igor/
├── artigo_bia.tex              # Fonte LaTeX do modelo aprovado pela BIA
├── artigo_bia.pdf              # PDF final do modelo
├── README.md                   # Este arquivo
├── regras-relatorio-monografia.md  # Checklist de regras (R01–R36)
├── testes/
│   └── test_formato_tcc.py     # Suíte de validação de formato (R01–R27)
├── anexos/
│   ├── 2026_tcc_fisSantos.pdf  # PDF de entrega (idêntico a artigo_bia.pdf)
│   ├── 2026_termo_fisSantos.pdf
│   ├── Processo-requerimento.pdf
│   ├── ficha_catalografica.pdf
│   └── requerimento.pdf
├── REGISTRO_BIA/
│   ├── artigo_bia.tex
│   ├── copy_of_Artigo_template.docx
│   ├── copy_of_Artigo_template.pdf
│   ├── nbr-10719-atualizada.pdf
│   ├── page_11.png
│   ├── page_12.png
│   └── page_13.png
├── partes/
│   ├── anexos.tex
│   ├── capa.tex
│   ├── consideracoes.tex
│   ├── diagramas/
│   │   ├── arquitetura-backend.tex
│   │   ├── arquitetura-frontend.tex
│   │   ├── casos_de_uso.tex
│   │   ├── casos_de_uso_descricao.tex
│   │   ├── deploy.tex
│   │   ├── der.tex
│   │   ├── der BACKUP.tex
│   │   ├── Diagrama_de_Classes.tex
│   │   └── interfaces.tex
│   ├── folha_rosto.tex
│   ├── introducao.tex
│   ├── modelagem.tex
│   ├── plano_testes.tex
│   ├── requisitos/
│   │   ├── criterios_aceitacao.tex
│   │   ├── mvp_quadro.tex
│   │   ├── rastreabilidade.tex
│   │   ├── regras_negocio.tex
│   │   ├── rf.tex
│   │   └── rfn.tex
│   ├── resumo.tex
│   ├── siglas.tex
│   ├── software.tex
│   └── tecnologias.tex
├── partes/diagramas/
├── imagens/
├── registro NIT/
│   ├── campo_de_aplicacao.pdf
│   └── tipos_de_programa.pdf
├── regrasABNT/
│   ├── MANUAL-ABNT-GRADUCAO-2026-at.pdf
│   └── MANUALDETRABALHOSACADMICOS2024-eb6489917ee640b985f6c0a5efc585c9.pdf
├── REGISTRO_BIA/
│   ├── artigo_bia.tex
│   ├── copy_of_Artigo_template.docx
│   ├── copy_of_Artigo_template.pdf
│   ├── nbr-10719-atualizada.pdf
│   ├── page_11.png
│   ├── page_12.png
│   └── page_13.png
├── testes/
│   └── test_formato_tcc.py
├── artigo_bia.tex
├── artigo_bia.pdf
├── referencias.bib
├── regras-relatorio-monografia.md
└── README.md
```

### Branches

- **`main`** — modelo final aprovado pela BIA, pronto para submissão
- **`bia`** — branch de trabalho que originou o modelo aprovado (última modificada antes do merge)

---

## Quick Start — Compilar localmente

### 1. Baixe o repositório

```bash
git clone https://github.com/igordev23/Relatorio-Tecnico-de-Software---IFPI--Igor.git
cd Relatorio-Tecnico-de-Software---IFPI--Igor
```

### 2. Instale o LaTeX (se ainda não tiver)

**Ubuntu/Debian:**
```bash
sudo apt-get install texlive-full
```

**Fedora:**
```bash
sudo dnf install texlive-scheme-full
```

**macOS:** instale o [MacTeX](https://www.tug.org/mactex/)  
**Windows:** instale o [TeX Live](https://tug.org/texlive/) ou [MiKTeX](https://miktex.org/)

### 3. Compile o documento

Na raiz do repositório, rode:

```bash
pdflatex artigo_bia.tex
bibtex artigo_bia
pdflatex artigo_bia.tex
pdflatex artigo_bia.tex
```

O PDF gerado será `artigo_bia.pdf` (idêntico a `anexos/2026_tcc_fisSantos.pdf`, regra R27).

> **Nota:** são necessárias 3 passagens do `pdflatex` (uma antes e duas depois do `bibtex`) para que referências, citações e sumário fiquem corretos.

---

## Autor

**Francisco Igor Silva Santos**  
Orientador: Prof. Me. Mayllon Veras da Silva  
IFPI — Campus Piripiri, 2026