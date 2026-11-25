# prompt audit (skill claude-api): relatorio e diff, nada aplicado

**Estado:** aberta

**Prompt (palavra por palavra):** prompt audit

https://www.instagram.com/reel/Dd15NcHvlNl/?hvrq=aXZ4Mm5yMWszaHlq
Era isso que quis dizer, mas acho que está faltando algum /
1. Vou olhar quando o limite resetar
2 ok
4pause

*Recado de 25/11 23:04:* git apply -p1 pedidos/anexos/prompt-audit-2026-11-25.diff

**O que ele pediu, parte por parte:** 1) "prompt audit". 2) Com o reel do comando prompt-audit da skill claude-api: "Era isso que quis dizer, mas acho que está faltando algum /" (faltou a barra: /claude-api prompt-audit).

**Por que ele pediu, ou o que quer descobrir:** O reel diz que instruções escritas para modelos antigos pioram o Opus 5.5 e gastam mais; ele trocou a sessão para o Opus 5.5 e quer economizar.

**Objetivo dele:** Arquivos de regra limpos, que gastem menos e funcionem melhor no modelo novo.

**Ligação com as ideias gerais do projeto:** Economia de tokens (24/11) sem perder qualidade (20/11).

**Perguntas que me fiz:** Aplicar ou só propor? A skill só propõe, e CLAUDE.md muda só com o sim dele: só propor. Escopo? Os arquivos de regra do projeto; skills de terceiros só olhadas.

**Pronto quando:** Relatório e diff em pedidos/anexos/prompt-audit-2026-11-25.*; o diff aplica limpo (git apply --check).

**Suposições (o dono não disse):** Que o alvo é o Opus 5.5 (a sessão dele). Que "prompt audit" é o da skill, não auditoria dos pedidos.

**Quem executa:** Maestro.

**Conferência:** `git apply --check -p1 pedidos/anexos/prompt-audit-2026-11-25.diff`.

**Resultado:** aplicado a pedido do dono ("git apply -p1 ...", 25/11 15:53): achados 1 a 8 em `ce87722`; `salvar.py` assina pelo modelo da sessão (`a554953`); `plano.py` com no máximo 2 em "Agora".

**O que aprendi:** maestro: registrar na ficha a fala do dono que muda o pedido (aqui, de "só propor" para "aplicar") no mesmo momento.

**Papéis afetados:** planejador, redator, maestro

