# Sistema questionador: perguntar a si mesmo e ao dono

**Estado:** fechada em 22/11/2026

**Prompt (palavra por palavra):** Faca o sistema todo ser bem questionativo, sempre se fazendo perguntas para entender melhor a situacao, e sinta-se a vontade de me perguntar coisas que queira saber

**O que ele pediu, parte por parte:** 1) "Faça o sistema todo ser bem questionativo, sempre se fazendo perguntas para entender melhor a situação": todo agente, antes e durante o trabalho, se pergunta o que não sabe e vai atrás da resposta. 2) "sinta-se à vontade de me perguntar coisas que queira saber": perguntar ao dono é bem-vindo, não um incômodo.

**Por que ele pediu, ou o que quer descobrir:** A retrospectiva mostrou que os erros vieram de suposição passada como ordem (destino Reels, "não use OpenArt" lido como proibição, E07 com quartos em fila) e de ordem que ficou numa conversa só. Quem se pergunta "o que eu não sei aqui?" pega isso antes.

**Objetivo dele:** Menos retrabalho: entender antes de fazer, e saber dele o que só ele sabe.

**Ligação com as ideias gerais do projeto:** Lição 5 da retrospectiva (suposição vira erro) e fio 4 (ele não quer ser o gargalo): perguntar muito, mas sem parar o que não depende da resposta.

**Perguntas que me fiz:** O que "questionativo" quer dizer para ele: perguntar mais, ou também esperar a resposta? (Ele já disse que não quer ser o gargalo: perguntar sem parar.) Como ele prefere receber as perguntas: juntas no fim, ou uma por vez? (Perguntei.) Onde a regra precisa morar para todo agente segui-la sem lembrar? (No prompt de entrada de cada agente, no CLAUDE.md e no lembrete do gancho.) Que perguntas eu quero fazer a ele de verdade agora? (Três, na resposta.)

**Pronto quando:** Regra escrita no CLAUDE.md e no pedidos/LEIA-ME.md; a ficha ganha o campo "Perguntas que me fiz"; todo agente tem a regra no prompt de entrada; o gancho lembra a cada prompt; o checar.py passa.

**Suposições (o dono não disse):** Que "questionativo" não quer dizer parar e esperar por ele: as perguntas ao dono vão juntas, curtas, com opções e com o que eu faria se ele não responder, e o trabalho que não depende delas continua. Perguntei a ele como prefere receber as perguntas.

**Quem executa:** Opus na conversa principal (regra de sistema, curta).

**Conferência:** Rodei o checar.py (passa depois de encurtar o CLAUDE.md). Conferi por busca que os 9 agentes têm a linha "Pergunte sempre" no prompt de entrada e que o gancho devolve o lembrete novo (já apareceu nesta conversa). Não conferi se os agentes de fato perguntam: só dá para ver no próximo trabalho deles; fica para a auditoria do Fable.

**Resultado:** Regra "pergunte sempre" no CLAUDE.md, no pedidos/LEIA-ME.md, no prompt de entrada dos 9 agentes e no lembrete do gancho; a ficha ganhou o campo "Perguntas que me fiz". Perguntas ao dono vão juntas no fim, curtas, com opções, sem parar o trabalho que não depende delas.

