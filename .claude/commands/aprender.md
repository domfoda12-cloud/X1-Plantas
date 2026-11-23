---
description: No fim de uma tarefa, transforma o que se aprendeu em regra, conferência ou linha de contexto, no lugar certo do projeto.
argument-hint: [o que se aprendeu]
---

# /aprender

Adaptado de everything-claude-code (MIT, Copyright (c) 2026 Affaan Mustafa); licença em `.claude/LICENCA-everything-claude-code.txt`. Sem gancho automático e nada em `~/.claude`.

Lição: $ARGUMENTS (sem nada: a linha "Aprendido nesta tarefa" do resumo de passagem)

Escreve só o Maestro. Pergunte ao dono antes de salvar, se a lição vem de fala dele. Ordem:

1. Erro que pode voltar: vira conferência no `ferramentas/checar.py`.
2. Fato de um papel: uma linha no `contexto/<agente>.md`. Meça o tamanho antes (limite de 3500 caracteres); se passar, mova o mais antigo ao `CONTEXTO-HISTORICO.md`.
3. Método repetível: skill nova em `.claude/skills/<nome>/`, com "## Neste projeto (X1-Plantas)", "Prompt de entrada" e crases no `CONSELHO.md` e no `ECOSSISTEMA.md`; só se usa depois do roteiro de entrada inteiro (`CONSELHO.md`, seção 6).

Destino fixo por tipo: correção do dono, `contexto/<papel>.md`; erro de sintonia, `contexto/CONVIVENCIA.md`; contorno de ferramenta, `ferramentas/CLAUDE.md` ou o caderno `pesquisas/`; convenção de pasta, o trecho "O essencial" do `RESUMO.md` dela.

## Neste projeto (X1-Plantas)

- Nunca grave fora do repositório, nem dado pessoal, chave ou token. Lição sobre medida ou texto ao público passa pelo Arquiteto ou pelo Revisor.
- **Prompt de entrada:** "Leve a lição <texto> ao lugar certo, medindo o tamanho antes, e mostre a linha antes de salvar." Quem usa: o Maestro no fim de cada tarefa.
