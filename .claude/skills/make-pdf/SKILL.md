---
name: make-pdf
description: |
  Turn any markdown file into a publication-quality PDF: 1in margins, page
  breaks, page numbers, cover page, running headers, curly quotes, clickable
  TOC, diagonal DRAFT watermark. Use when asked to "make a PDF", "export to
  PDF", "turn this markdown into a PDF" or "generate a document". (gstack)
allowed-tools:
  - Bash
  - Read
  - AskUserQuestion
---

# make-pdf: PDF de qualidade a partir de markdown

Vem do gstack. Aqui entrou **só o uso da ferramenta**: o preâmbulo original (checagem de atualização, telemetria,
sincronização de memória com um repositório no GitHub, regras de roteamento escritas no `CLAUDE.md`) ficou de fora,
porque grava fora do projeto e manda dados para fora.

## Antes de qualquer comando: o binário existe?

```bash
_ROOT=$(git rev-parse --show-toplevel 2>/dev/null)
P=""
[ -n "$MAKE_PDF_BIN" ] && [ -x "$MAKE_PDF_BIN" ] && P="$MAKE_PDF_BIN"
[ -z "$P" ] && [ -n "$_ROOT" ] && [ -x "$_ROOT/.claude/skills/gstack/make-pdf/dist/pdf" ] && P="$_ROOT/.claude/skills/gstack/make-pdf/dist/pdf"
[ -z "$P" ] && P="$HOME/.claude/skills/gstack/make-pdf/dist/pdf"
[ -x "$P" ] && echo "MAKE_PDF_READY: $P" || echo "MAKE_PDF_NOT_AVAILABLE"
```

`MAKE_PDF_NOT_AVAILABLE`: o binário do gstack não está instalado. Não improvise outro caminho em silêncio: diga ao dono
que falta instalar (clonar o gstack e rodar `./setup`, o que só se faz com o "sim" dele).

## Comandos

- `$P generate <entrada.md> [saida.pdf]`: markdown para PDF (o caso comum).
- `$P generate --cover --toc --title "..." --author "..." texto.md saida.pdf`: capa, sumário clicável, capítulo novo a cada H1.
- `$P generate --watermark RASCUNHO texto.md rascunho.pdf`: marca d'água na diagonal.
- `$P generate --no-confidential texto.md saida.pdf`: sem o rodapé CONFIDENTIAL (use sempre aqui).
- `$P preview <entrada.md>`: HTML com o mesmo CSS de impressão, para iterar rápido.
- `$P setup`: confere navegador, Chromium e `pdftotext` e faz um teste.

Opções: `--margins 1in|25mm`, `--page-size a4|letter` (aqui sempre `a4`), `--no-chapter-breaks`, `--page-numbers`,
`--header-template`, `--footer-template`, `--allow-network` (busca imagem externa; desligado por padrão), `--date`.

Saída: no `stdout` só o caminho do PDF; progresso no `stderr`. Código 0 certo, 1 argumento errado, 2 erro de render,
3 tempo esgotado (tire o `--toc` se o texto não tem títulos), 4 navegador indisponível.

## Neste projeto (X1-Plantas)

Antes de usar esta skill aqui, alcance o projeto:
- Leia `CLAUDE.md`, `CONTEXTO.md` e o último resumo, `contexto/entregas/ULTIMO.md`.
- Responda e escreva em português do Brasil, com palavras simples.
- Ela segue o Conselho (`CONSELHO.md`); o Revisor de risco tem veto em tudo que toca honestidade e lei.
- **O e-book não passa por aqui.** O PDF do e-book e das plantas grátis sai de `python3 ebook/gerador/livro.py`, que confere página estourada e o aviso legal.
- Antes de entregar: `python3 ferramentas/checar.py`, `python3 ferramentas/atualizar-painel.py`, linha no fim de `CONTEXTO-HISTORICO.md`, commit e push na branch `planta-de-casas-anuncio`.
- **Prompt de entrada:** você serve para os documentos em markdown do projeto que vão para alguém ler fora do repositório: o guia do parceiro do WhatsApp, o relatório jurídico, a apostila do Arquiteto, o resumo para o arquiteto revisor. Sempre `--page-size a4 --no-confidential`. Documento que vai ao público passa antes pelo Revisor de risco, e nenhum aviso de "planta de referência" some na conversão: abra o PDF e confira. Salve em `ebook/saida/documentos/`, nunca em `/tmp`. Se o binário não existir, pare e avise.
