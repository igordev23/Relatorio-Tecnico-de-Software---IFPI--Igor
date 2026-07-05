# Relatório Técnico de Software — IFPI

**Sistema para Emissão, Gestão e Autenticação de Certificados**

Relatório técnico de software desenvolvido como Trabalho de Conclusão de Curso do Tecnólogo em Análise e Desenvolvimento de Sistemas do Instituto Federal do Piauí (IFPI) — Campus Piripiri.

## Resumo

Sistema web SaaS com arquitetura multi-tenant para emissão, gestão, envio e validação de certificados digitais. O sistema substitui processos manuais por uma plataforma centralizada com suporte a templates configuráveis, importação em lote, autenticação via QR Code e dashboard gerencial.

## Tecnologias

| Frontend | Backend | Banco de Dados | Infraestrutura |
|---|---|---|---|---|
| React 19 | Next.js | PostgreSQL (Supabase) | Docker |
| TypeScript | Node.js | — | Render |
| Tailwind CSS | API REST | — | Git/GitHub |
| — | qrcode 1.5 | — | — |

## Funcionalidades Principais

- Autenticação e controle de acesso por perfis (RBAC)
- Templates configuráveis com campos dinâmicos
- Emissão individual e em lote (CSV/Excel)
- Envio automático de e-mails
- Validação pública via código único e QR Code
- Dashboard com indicadores e logs de auditoria

## Compilação

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

## Estrutura

```
├── main.tex                  # Documento principal
├── referencias.bib           # Referências bibliográficas
├── partes/
│   ├── capa.tex
│   ├── folha_rosto.tex
│   ├── resumo.tex
│   ├── introducao.tex
│   ├── tecnologias.tex
│   ├── modelagem.tex
│   ├── software.tex
│   ├── consideracoes.tex
│   └── anexos.tex
├── requisitos/
│   ├── rf.tex                 # Requisitos funcionais
│   └── rfn.tex                # Requisitos não funcionais
├── diagramas/
│   ├── casos_de_uso.tex
│   ├── Diagrama_de_Classes.tex
│   ├── arquitetura-backend.tex
│   ├── arquitetura-frontend.tex
│   └── der.tex
└── imagens/
```

## Autor

**Francisco Igor Silva Santos**  
Orientador: Prof. Mayllon Veras da Silva  
IFPI — Campus Piripiri, 2025
