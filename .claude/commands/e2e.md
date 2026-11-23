---
description: Teste da calculadora de lote pela tela, como o comprador usa. Conduzido pelo agente testador-de-paginas.
argument-hint: [página]
---

# /e2e

Adaptado de everything-claude-code (MIT, Copyright (c) 2026 Affaan Mustafa); licença em `.claude/LICENCA-everything-claude-code.txt`.

Página: $ARGUMENTS (sem nada: `ebook/vendas/calculadora-lote.html`)

1. Rode antes o `python3 ferramentas/checar.py` (ele regera a calculadora).
2. Chame o agente `testador-de-paginas` com a ficha e a página. As regras estão no arquivo dele.
3. Calculadora dizendo "cabe" onde o validador diz que não: vai ao Arquiteto e ao Revisor, sem ajustar o teste.

## Neste projeto (X1-Plantas)

- O script de teste pela tela (`ebook/vendas/testar-calculadora.cjs`) é o pedaço F e ainda não existe; até lá o resultado diz "não testado na tela". As páginas de `video/src` ficam adiadas.
- **Prompt de entrada:** "Teste a página <caminho> pela tela, ficha <caminho>; devolva casa, lote digitado, esperado e visto." Quem usa: o Maestro ao mexer na calculadora.
