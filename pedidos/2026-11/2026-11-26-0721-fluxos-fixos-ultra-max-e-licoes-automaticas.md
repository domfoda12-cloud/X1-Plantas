# fluxos fixos ultra max e licoes automaticas

**Estado:** fechada em 26/11/2026

**Prompt (palavra por palavra):** Are we having issues with the agents communicating? Thats and the juri its honestly the last things i can think about improving the system, the workflow looks like it has a foundation but doesnt exist yet

The jury rules that we implemented yesterday look better than those, Fact check looks nice
Each workflow ends by writing its lessons into each agent's file automatically, so their knowledge grows the way you asked. >Is it not doing this yet even though i asked?
1 YESSS, thats exactly what im looking for but a version ultra max!
2 Explain

**O que ele pediu, parte por parte:** (1) fluxos fixos salvos que rodam sempre igual, com passe estruturado entre agentes, "versão ultra max"; (2) explicar o passo 2 (testes baratos do júri); (3) manter as regras do júri de 25/11 e somar a conferência de fatos; (4) saber se as lições já vão sozinhas ao arquivo de cada agente.

**Por que ele pediu, ou o que quer descobrir:** A comunicação entre agentes e o júri são o que falta melhorar no sistema; o fluxo "tem base mas não existe".

**Objetivo dele:** Uma equipe que trabalha sempre do mesmo jeito, aprende sozinha com cada erro e gasta menos.

**Ligação com as ideias gerais do projeto:** Qualidade em primeiro lugar e custo por venda: menos retrabalho e menos tokens; e-book continua a frente principal.

**Perguntas que me fiz:** Lição entra sozinha ou o dono aprova? (suposição: entra sozinha, com desfazer pelo git, e o resumo mostra.) Quais fluxos primeiro? (texto público, página do e-book, decisão.)

**Pronto quando:** 3 fluxos salvos em .claude/workflows/, rodados uma vez sobre peça real, lições gravadas sozinhas, checar.py confere que existem, plano em pedidos/anexos/plano-fluxos-2026-11-26.md seguido.

**Suposições (o dono não disse):** (Decidido pelo dono, 26/11: lição entra sozinha, "Automatically".) Mudança de sistema vai na branch sistema/fluxos antes da main.

**Quem executa:** Paydon (Opus) monta; Olga (supervisor) audita; Vera lê o que for texto público nos testes.

**Conferência:** cada fluxo rodou uma vez sobre peça real (`pedidos/fluxos/RODADAS.md`): texto-publico no funil do sócio (Vera SIM SE, 2 condições aplicadas), pagina-ebook na pág. 11 da C01 (Vera SIM SE aplicado, prévia sem estouro), planta no rascunho C01V (0 de 11 com erro, pronto para aplicar), decisao na calibração (os 3 jurados pegaram os 3 erros plantados), prova de entrada (Caio, Rui e Vera: 5 de 6, sem alarme falso; item em disputa confirmado pela Olga). `checar.py` roda `fluxo.py testar` e o ensaio dos 5 fluxos com agentes de mentira. Olga auditou: 10 achados (3 altos: fluxo que aprovava com o programa quebrado, gasto só de saída, 6 furos no programa de texto), todos consertados com prova no `checar.py`. As "3 perguntas de entrada" do plano foram lidas como as 3 perguntas dos ângulos do júri (comprador, dinheiro, risco), escolha do Maestro.

**Resultado:** 5 fluxos fixos em .claude/workflows/ (texto-publico, pagina-ebook, planta, decisao, prova-de-entrada), programa antes do juízo (ferramentas/fluxo.py), gasto por rodada, lições sozinhas no contexto de cada agente, prova de entrada que endurece; cada fluxo rodado uma vez em peça real; auditoria da Olga aplicada

**O que aprendi:** maestro: Fluxo novo passa no ensaio estrito e com o programa quebrado antes da rodada real; erro plantado nunca vira lição.
supervisor: Quando todos os papéis deixam passar o mesmo item, a suspeita cai primeiro no gabarito; arbitre antes da nota.

**Papéis afetados:** maestro, redator, revisor-de-risco, designer, arquiteto, supervisor, planejador

