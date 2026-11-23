---
description: Caso que falha antes do conserto, para mudança em cálculo de planta que vai ao e-book. Conduzido pelo agente guia-de-testes.
argument-hint: <o que vai mudar>
---

# /tdd

Adaptado de everything-claude-code (MIT, Copyright (c) 2026 Affaan Mustafa); licença em `.claude/LICENCA-everything-claude-code.txt`.

Mudança: $ARGUMENTS

1. Obrigatório só para os arquivos da lista única da skill `ponytail` (seção "Neste projeto", "Caso antes do conserto"); confira lá se a mudança entra.
2. Chame o agente `guia-de-testes` com a ficha e o valor esperado (da planta ou de fonte citada). As regras e proibições estão no arquivo dele.
3. Depois: o Maestro confere o `git diff` (o `checar.py` regrava arquivos), pede ao Arquiteto que confira medida que vai ao público e faz o commit só com "Tudo certo".

## Neste projeto (X1-Plantas)

- O caso fica na lista `_casos` do `ferramentas/checar.py`, para sempre.
- **Prompt de entrada:** "Caso antes do conserto para <mudança>, ficha <caminho>; esperado <valor> tirado de <fonte>." Quem usa: o Maestro.
