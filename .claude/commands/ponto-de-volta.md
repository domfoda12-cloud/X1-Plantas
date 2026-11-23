---
description: Marca um ponto seguro para voltar numa frente longa (commit conferido, enviado e anotado), ou lista, confere e limpa os pontos.
argument-hint: criar <nome> | conferir <nome> | listar | limpar
---

# /ponto-de-volta

Adaptado de everything-claude-code (MIT, Copyright (c) 2026 Affaan Mustafa); licença em `.claude/LICENCA-everything-claude-code.txt`. Era o `/checkpoint`; renomeado para o jeito que o dono pede ("faz um ponto de volta").

Pedido: $ARGUMENTS

Padrão seguro (pergunta 18 do veto): o ponto fica **só anotado**. Nada de etiqueta (tag) no GitHub até o dono pedir.

- **criar <nome>:** rode a `verificacao` no modo rápido. Falhou: nada de commit, leve ao `/build-fix`. Passou: commit "ponto de volta: <nome>", `git push origin HEAD` (o ponto não pode existir só nesta máquina) e uma linha em `.claude/pontos-de-volta.log` com data, nome e branch. O código do commit se acha com `git log --grep 'ponto de volta: <nome>'`.
- **conferir <nome>:** `git diff --stat <commit>` e o `checar.py` agora.
- **listar:** o `.claude/pontos-de-volta.log` e o `git log --grep 'ponto de volta:'`.
- **limpar:** mostre as linhas do log e pergunte antes de apagar; o commit fica no histórico.

Voltar a um ponto: `git revert` ou uma branch nova a partir do commit. Nunca `git stash`, `reset --hard` nem push forçado.

## Neste projeto (X1-Plantas)

- Commit só com "Tudo certo" (regra do `CLAUDE.md`). Português nos commits, com as linhas de atribuição.
- **Prompt de entrada:** "Crie o ponto de volta <nome> na branch atual, só anotado." Quem usa: o Maestro numa frente longa; o dono pode pedir.
