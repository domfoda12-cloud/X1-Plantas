**Tarefa:** everything-claude-code, pedaços E1, E2, trava e F (ficha `0209`, branch `sistema/everything-claude-code`).
**Feito:** `ferramentas/abrir-sessao.py` (SessionStart): fichas abertas, "## Agora", títulos dos avisos e começo do `ULTIMO.md`, até 2000 caracteres.
**Feito:** `ferramentas/contar-arquivos.py` (PostToolUse "Read|Edit|Write"): aviso ao passar de 30 e de 45 arquivos; lembrete de `.md` novo fora do git, uma vez por caminho; nunca bloqueia.
**Feito:** `.claude/settings.json` nega `npx`, `npm install`, `npm ci` e `rm -rf` (tirar só com ficha); UserPromptSubmit intacto.
**Feito:** `ebook/vendas/testar-calculadora.cjs`: 24 casas, 73 medições pela tela contra o validador; prova negativa falhou certo.
**Como conferir:** `python3 ferramentas/checar.py`; `echo '{"source":"startup"}' | python3 ferramentas/abrir-sessao.py`; `node ebook/vendas/testar-calculadora.cjs`.
**Não feito / ressalva:** ganchos só valem em conversa nova: falta a sessão de prova ao vivo (pedaço G: linha injetada, três `.md` com Write, os 7 agentes e a `/verificacao`); o `rodar(...)` do teste da calculadora no `checar.py` não entrou.
**Aprendido nesta tarefa:** nada novo.
**Decisão do dono pendente:** levar a branch à main (só com o sim dele).
**Próximo passo:** abrir uma conversa nova na branch e fazer o pedaço G; depois o pull request para a main.
