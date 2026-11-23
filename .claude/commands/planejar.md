---
description: Plano de uma tarefa grande (mais de uns 30 arquivos ou mais de uma frente), feito pelo agente planejador e escrito na ficha.
argument-hint: <o que planejar>
---

# /planejar

Adaptado de everything-claude-code (MIT, Copyright (c) 2026 Affaan Mustafa); licença em `.claude/LICENCA-everything-claude-code.txt`. Nome em português: o `/plan` colide com o modo plano do Claude Code.

Tarefa: $ARGUMENTS

1. Ache ou abra a ficha (`python3 ferramentas/pedido.py nova` ou a que já existe em `pedidos/`).
2. Chame o agente `planejador` com o caminho da ficha. As regras do plano estão no arquivo dele.
3. O plano vai só na ficha. Suposição e o que é do dono (preço, título, gasto, publicação) esperam o "sim" dele; entrega ao público passa pelo `/conselho`.
4. Decisão de sistema que o planejador devolver: o Maestro registra no `CONSELHO.md`, seção 7.

## Neste projeto (X1-Plantas)

- Tamanho em pequeno, médio ou grande, nunca em horas. Ordem das frentes: e-book, animações, vídeo.
- **Prompt de entrada:** "Planeje a ficha <caminho>: pedido, por quê, suposições, quem faz, pedaços de até 30 arquivos e a conferência de cada um." Quem usa: o Maestro; o dono pode digitar `/planejar`.
