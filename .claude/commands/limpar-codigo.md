---
description: Tira código morto (.py, .cjs, .js) apontado pela auditoria, uma exclusão por commit. Conduzido pelo agente limpador.
---

# /limpar-codigo

Adaptado de everything-claude-code (MIT, Copyright (c) 2026 Affaan Mustafa); licença em `.claude/LICENCA-everything-claude-code.txt`.

1. Primeiro a `/ponytail-audit` (sem knip, depcheck, ts-prune nem npx).
2. Chame o agente `limpador` com a ficha e os achados. A lista SEGURO, CUIDADO e PERIGO e as proibições estão no arquivo dele.
3. Depois: o Maestro faz uma exclusão por commit, com a `verificacao` em "Tudo certo", e registra no `CONTEXTO-HISTORICO.md`.

## Neste projeto (X1-Plantas)

- Prioridade baixa: e-book primeiro. Arquivo criado pelo dono só sai com o "sim" dele.
- **Prompt de entrada:** "Classifique os achados da auditoria em SEGURO, CUIDADO e PERIGO e prepare a primeira exclusão SEGURA, ficha <caminho>." Quem usa: o Maestro.
