# melhorar o planejador

**Estado:** aberta

**Prompt (palavra por palavra):** Trabalhe no planejador mais,

**O que ele pediu, parte por parte:** "Trabalhe no planejador mais": melhorar o agente `planejador`, criado hoje. Ele não disse em quê.

**Por que ele pediu, ou o que quer descobrir:** Ele quer saber sempre o que fazer agora e o que vem depois; a primeira rodada devolveu um plano bom, mas que fica velho assim que um passo termina, e que deixou "Agora" vazio.

**Objetivo dele:** Um planejador em que dá para confiar: que diga o próximo passo de verdade e o que cada resposta dele destrava.

**Ligação com as ideias gerais do projeto:** "Um plano passo a passo, separado em tarefas grandes e pequenas" (22/11); "só relatar números que uma ferramenta devolveu": o que destrava o quê passa a ser conta, não opinião.

**Perguntas que me fiz:** O que faltou na primeira rodada? (o plano não se atualiza; "qual decisão destrava mais" era opinião; o PDF final ficou preso a 5 decisões, 3 só de bônus.) Como o dono vê o plano? (hoje só num arquivo: fica como pergunta para ele.)

**Pronto quando:** `ferramentas/plano.py` responde agora, destrava e caminho; o `checar.py` confere o plano; o papel do planejador tem o método novo; o planejador rodou a segunda vez com isso e "Agora" deixou de estar vazio, ou ele mostrou por que não dá.

**Suposições (o dono não disse):** Que "mais" quer dizer deixá-lo mais útil e confiável (ferramenta, método, segunda rodada), e não outro tipo de plano; que ele gostaria de ver o plano numa página (não fiz: pergunto).

**Quem executa:** Maestro (ferramenta, papel, conferência); `planejador` (segunda rodada).

**Conferência:** (a preencher)

**Resultado:** (a preencher)

**O que aprendi:** (a preencher)

