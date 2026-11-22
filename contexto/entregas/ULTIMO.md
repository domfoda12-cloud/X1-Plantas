**Tarefa:** fazer os agentes pararem de esquecer: índice, resumo barato por pasta e os prompts do dono ao alcance de todos.
**Feito:** `ferramentas/resumos.py` gera o `INDICE.md` e um `RESUMO.md` por pasta (10 categorias). "O essencial" de cada resumo é escrito à mão e o gerador não apaga.
`contexto/<agente>.md`: seção "Leia barato" com os resumos das pastas de cada papel.
`contexto/dono/PROMPTS.md`: 166 prompts do dono, palavra por palavra. `contexto/dono/TEXTOS-DESATUALIZADOS.md`: cerca de 60 contradições entre documentos.
`ferramentas/checar.py`: falha se um documento ficar fora do índice ou um resumo ficar sem "O essencial"; limite do `CLAUDE.md` subiu para 6.500.
**Como conferir:** `python3 ferramentas/resumos.py --conferir`; abrir o `INDICE.md`.
**Não feito / ressalva:** as contradições estão listadas, não corrigidas (só 3 mecânicas). Os prompts de outras conversas não entraram palavra por palavra: estão resumidos no histórico.
**Decisão do dono pendente:** garantia de 7 dias; 12 ou 24 plantas; se a retirada do selo "Imagem ilustrativa" vale para todo vídeo e para imagem parada.
**Próximo passo:** corrigir os textos que vão ao cliente (primeira seção do `TEXTOS-DESATUALIZADOS.md`), com o Revisor de risco.
