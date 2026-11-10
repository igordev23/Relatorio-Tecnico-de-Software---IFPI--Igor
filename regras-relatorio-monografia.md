# Regras — Relatório técnico adaptado a monografia (IFPI/BIA)

Checklist numerado para validação do PDF (`artigo_bia.pdf` / `anexos/2026_tcc_fisSantos.pdf`) antes do reenvio ao BIA.

## Fontes

| Código | Documento |
|--------|-----------|
| IFPI | `regrasABNT/MANUALDETRABALHOSACADMICOS2024-….pdf` (seções 3.1–3.7, 4.1, 5, 9) |
| NBR10719 | `REGISTRO_BIA/nbr-10719-atualizada.pdf` (ABNT NBR 10719:2015) |
| TPL | `REGISTRO_BIA/MONOGRAFIATEMPLATE.pdf` |
| BIA | 5 devoluções do bibliotecário Júlio César (ago–nov/2026) |
| SEC | Referência secundária: `regrasABNT/MANUAL-ABNT-GRADUCAO-2026-at.pdf` (Unihorizontes) |

Este trabalho é um **relatório técnico** (NBR 10719) apresentado no **padrão visual de monografia IFPI** (NBR 14724 via manual IFPI). Em conflito de apresentação, prevalece o que o BIA já exigiu nas devoluções; a estrutura textual segue o relatório.

---

## A. Estrutura e ordem dos elementos

### R01 — Ordem pré-textual (monografia IFPI + adaptação)
**Fonte:** IFPI §5.2.1; NBR10719 §4.2.1; BIA (ficha).  
Ordem observada no PDF:

1. Capa  
2. Folha de rosto  
3. Ficha catalográfica (verso da folha de rosto)  
4. Resumo (português) + palavras-chave  
5. Abstract (inglês) + keywords  
6. Lista de figuras / quadros / tabelas (se houver)  
7. Lista de abreviaturas e siglas (se houver)  
8. Sumário  

### R02 — Elementos textuais obrigatórios
**Fonte:** IFPI §5 / §9.1; NBR10719 §4.2.2.  
Devem existir, nesta ordem lógica: Introdução → Desenvolvimento (capítulos 2–4) → Considerações finais.

### R03 — Elementos pós-textuais
**Fonte:** IFPI §5.2.3; NBR10719 §4.2.3; BIA.  
Obrigatório: Referências. Presente: Anexos. Títulos **sem indicativo numérico**, caixa alta, negrito, centralizados.

### R04 — Ficha catalográfica
**Fonte:** IFPI §5.2.1.2; BIA (devolução).  
Deve existir página com “Dados Internacionais de Catalogação” / CIP e registro CRB do bibliotecário.  
**Nota:** o documento oficial da biblioteca (ex.: “81 f.”) **não deve ser editado**; divergência de contagem de folhas vs. PDF é aviso, não correção local.

---

## B. Capa e identificação (devoluções BIA)

### R05 — Capa em caixa alta (exceto subtítulo)
**Fonte:** BIA; IFPI §5.1 (capa); TPL.  
Instituição, campus, curso, autor, local e ano em **MAIÚSCULAS**.  
Título principal **CERTIFYHUB** em maiúsculas.

### R06 — Subtítulo: minúsculo e negrito
**Fonte:** BIA (devolução explícita).  
Após os dois-pontos: `sistema para emissão, gestão e autenticação de certificados` em minúsculas (sentence case do subtítulo) e tipografia em negrito.

### R07 — Folha de rosto
**Fonte:** IFPI §5.2.1.1.  
Contém autor, título/subtítulo, natureza do trabalho, orientador, local e ano.

---

## C. Resumo

### R08 — Extensão do resumo
**Fonte:** IFPI §4.1.  
Trabalhos acadêmicos e relatórios técnicos: **150 a 500 palavras**.

### R09 — Forma do resumo e palavras-chave
**Fonte:** IFPI §4; NBR 6028 (citada no manual).  
Parágrafo único; “Palavras-chave:” após o resumo; termos separados por ponto e vírgula.

---

## D. Sumário e listas

### R10 — Sumário alinhado à esquerda (mesma coluna de títulos)
**Fonte:** BIA (devolução); IFPI §5.1.2.14 / NBR 6027.  
Indicativos à margem; **todos os títulos do sumário na mesma abscissa** (coluna única à esquerda).  
REFERÊNCIAS e ANEXOS constam **sem número** de seção.

### R11 — Listas pré-textuais
**Fonte:** BIA; IFPI §3.6.1.  
“LISTA DE FIGURAS”, “LISTA DE QUADROS”, “LISTA DE TABELAS”, “LISTA DE ABREVIATURAS E SIGLAS”: caixa alta, negrito, centralizados (títulos sem indicativo).

---

## E. Formatação geral

### R12 — Formato A4
**Fonte:** IFPI §3.4.  
Página A4 (≈ 595,27 × 841,89 pt).

### R13 — Margens (anverso)
**Fonte:** IFPI §3.2; NBR10719 §5.1.  
Esquerda e superior: **3 cm**; direita e inferior: **2 cm** (±2 mm de tolerância na medição do PDF).

### R14 — Fonte do corpo
**Fonte:** IFPI §3.1.  
Arial ou Times New Roman, tamanho **12** (no PDF: NimbusSans ≈ Arial, ~11,96 pt).  
Títulos de seção também em tamanho 12 (IFPI §3.6 OBS.).

### R15 — Espaçamento entre linhas
**Fonte:** IFPI §3.3 (1,5 para monografia); NBR10719 §5.1 (**simples** recomendado para relatório).  
**Decisão deste trabalho (híbrido):** mantém espaçamento simples (`\setstretch{1.0}`), alinhado à NBR 10719 e às 5 devoluções BIA (nenhuma citou entrelinha). Testes verificam consistência do corpo (~14–15 pt de leading tipográfico), não forçam 1,5.

### R16 — Parágrafo
**Fonte:** IFPI §3.4.  
Recuo de primeira linha **1,25 cm**; texto justificado.

### R17 — Paginação
**Fonte:** IFPI §3.5; NBR10719 §5.2.  
Pré-textuais contadas, não numeradas. Numeração arábica a partir da primeira folha da parte textual, canto superior direito.  
**Tolerância BIA:** posição medida ≈ 1,64 cm do topo / ~3,3 cm da direita — aceitar se numeração existir no topo direito a partir da parte textual (não exigir 2,00 cm exatos).

---

## F. Numeração progressiva e hierarquia tipográfica

### R18 — Numeração progressiva
**Fonte:** IFPI §3.7 / NBR 6024.  
Algarismos arábicos; sem ponto/hífen entre indicativo e título; texto da seção começa em nova linha.

### R19 — Toda seção deve ter texto
**Fonte:** IFPI §3.7(d); BIA (texto entre 1.1 e 1.1.1; texto entre capítulo/seção e subdivisões).  
Nenhum título pode ser seguido imediatamente por outro título sem corpo textual entre eles.

### R20 — Seção primária
**Fonte:** IFPI §3.7(j); exemplo IFPI (1 INTRODUÇÃO).  
Caixa alta + negrito + tamanho 12; indicativo numérico.

### R21 — Seção secundária
**Fonte:** BIA; exemplo IFPI (2.1 SEÇÃO SECUNDÁRIA).  
**Caixa alta, sem negrito** (regular).

### R22 — Seção terciária
**Fonte:** BIA; exemplo IFPI (2.1.1 Seção terciária).  
**Minúsculas (sentence case) com negrito**. Nomes próprios / marcas (React, PDFKit, shadcn/ui) preservam grafia convencional.

### R23 — Títulos sem indicativo
**Fonte:** IFPI §3.6.1; BIA.  
Sumário, listas, referências, anexos: centralizados, maiúsculas, negrito, mesmo destaque das primárias.

---

## G. Ilustrações e tabelas

### R24 — Identificação e fonte
**Fonte:** IFPI §3.11.  
Ilustração citada no texto; rótulo “Figura/Quadro/Tabela N – título” acima; **Fonte:** abaixo (obrigatória, mesmo se do autor).

---

## H. Referências e anexos

### R25 — Referências
**Fonte:** IFPI §5.2.3.1; NBR 6023.  
Título REFERÊNCIAS centralizado, maiúsculo, negrito; lista presente no PDF.

### R26 — Anexos
**Fonte:** IFPI §5.2.3; NBR10719 §4.2.3.4.  
Título ANEXOS centralizado; cada anexo identificado (ANEXO A, ANEXO B, …).

---

## I. Devoluções BIA (checklist anti-reincidência)

| ID | Exigência | Regra |
|----|-----------|-------|
| D1 | Título CERTIFYHUB maiúsculo | R05 |
| D2 | Texto da capa em maiúscula (exceto subtítulo) | R05 |
| D3 | Ficha catalográfica presente | R04 |
| D4 | Texto entre seção e subdivisão (ex.: 1.1 → 1.1.1) | R19 |
| D5 | Subtítulo minúsculo e negrito | R06 |
| D6 | Fonte dos títulos padronizada (12 / hierarquia) | R14, R20–R22 |
| D7 | Sumário alinhado à esquerda (coluna única) | R10 |
| D8 | Secundárias caixa alta sem negrito | R21 |
| D9 | Terciárias minúsculas com negrito | R22 |

---

## J. Arquivos e branch

### R27 — Entrega
PDF final em `anexos/2026_tcc_fisSantos.pdf`, idêntico a `artigo_bia.pdf`. Trabalho na branch `bia` (não `main`).

### R28 — Fora de escopo (não alterar sem nova devolução)
Estrutura duplicada de 2.1 (Zod / Arquitetura e Padrões repetidos) — nenhuma devolução citou; mudar renumeraria 2.x.
