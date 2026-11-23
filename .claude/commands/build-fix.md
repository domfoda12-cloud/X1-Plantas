---
description: Conserta o que deixou o checar.py, o atualizar-painel.py ou um render vermelho, um erro por vez. Conduzido pelo agente consertador.
---

# /build-fix

Adaptado de everything-claude-code (MIT, Copyright (c) 2026 Affaan Mustafa); licença em `.claude/LICENCA-everything-claude-code.txt`.

1. Rode `python3 ferramentas/checar.py` e copie as linhas `[ERRO]`.
2. Chame o agente `consertador` com a ficha e essas linhas. As regras e proibições estão no arquivo dele.
3. Depois: o Maestro confere o diff do conserto separado do que o checar regravou, roda a `verificacao` e faz o commit só com "Tudo certo". Na segunda falha igual, chama o `supervisor`.

## Neste projeto (X1-Plantas)

- A causa do erro vira regra escrita ou conferência automática (`pedidos/LEIA-ME.md`).
- **Prompt de entrada:** "Conserte o primeiro [ERRO] do checar.py, ficha <caminho>: <linhas>." Quem usa: o Maestro.
