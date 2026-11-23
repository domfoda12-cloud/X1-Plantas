# Trabalho autônomo à noite: skills do e-book, atendimento, campanha de anúncio

**Estado:** aberta

**Prompt (palavra por palavra):** What really its your limit? I would like for the system to keep studying andi mproving afk now that im going to sleep, it can use all tokens as you want but what really its your limit? Can you add skills that are relevant for building the ebook, think of ways to improve the UI and costumer service, Create a ads campaign marketing. These are all examples that you can learn about, id really like if you were autosufficient

*Recado de 23/11 01:47:* Just stay awake 24h

*Recado de 23/11 01:49:* This night dont queue anything that you have to produce, simply focus on making the system autonomous on learning

*Recado de 23/11 01:49:* the IA inside the IA inside the IA inside the IA

**O que ele pediu, parte por parte:** 1) Qual é o meu limite de verdade. 2) O sistema seguir estudando e melhorando enquanto ele dorme, usando os tokens que quiser. 3) Exemplos: skills relevantes para construir o e-book; melhorar a interface e o atendimento ao cliente; criar uma campanha de anúncio. 4) Quer o sistema autossuficiente.

**Por que ele pediu, ou o que quer descobrir:** Quer que o tempo dele dormindo vire trabalho, e quer saber até onde pode confiar no sistema sozinho.

**Objetivo dele:** Um sistema que trabalha e melhora sem ele, e que de manhã tem coisas prontas para ele decidir.

**Ligação com as ideias gerais do projeto:** Fio 4 (não ser o gargalo; autonomia no fazer, confirmação no gastar e publicar), fio 6 (qualidade primeiro).

**Perguntas que me fiz:** Eu trabalho sozinho? Só quando algo me acorda: entre mensagens eu não rodo. Para trabalhar à noite, agendo mensagens que me acordam nesta conversa (tarefa agendada de hora em hora). O que posso fazer sem ele? Planejar, pesquisar, escrever, programar, testar e vetar; nada de gastar crédito, publicar, mandar mensagem, contratar ou decidir preço, título e nome (regras dele). Limites técnicos: o limite de uso da conta (semanal), o tamanho desta conversa (é resumida sozinha), o contêiner pode ser reiniciado (o trabalho fica salvo no git a cada passo).

**Pronto quando:** Fila da noite escrita; tarefa agendada criada; a cada acordar uma tarefa da fila, com plano vetado, `checar.py` e commit; de manhã um resumo para o dono com o que ficou pronto e o que espera o "sim" dele.

**Suposições (o dono não disse):** Que ele dorme umas 8 horas; acordar de hora em hora, até 8 vezes; nada pago nem publicado; tudo que é decisão dele vira opção para a manhã.

**Quem executa:** Maestro (Opus) conduz cada acordar; o time de cada assunto executa e veta; o Fable veta o plano da noite e audita no fim.

**Conferência:** (no fim)

**Resultado:** (a preencher)


## Fila da noite, versão 3 (recado do dono, 01:50: "esta noite não enfileire nada que você tenha de produzir; foque em deixar o sistema autônomo no aprendizado")

A versão 2 (E07, funil, campanha, interface, skills) fica para depois, com o "sim" dele. Esta noite só se constrói **como o sistema aprende sozinho**. Uma tarefa por acordar; plano curto vetado; até 6 chamadas de agente; regras da noite da versão 2 continuam (nada pago, nada publicado, nada instalado, texto público intocado).

| # | Tarefa | O que faz o sistema aprender sozinho | Pronto quando | Estado |
|---|---|---|---|---|
| A1 | Veto do Fable desta fila | — | fila aprovada | |
| A2 | **Lição automática ao fechar ficha:** o `pedido.py fechar` passa a exigir o campo "O que aprendi" e copia a lição para o "Lições" do contexto de quem errou (e do Maestro) | todo erro vira lição sem depender de memória | testado no `checar.py` | |
| A3 | **Placar do veto:** cada nota da régua vai para um placar (`contexto/PLACAR.md`, gerado), por agente e por ponto que caiu; o agente lê a sua linha antes de vetar | cada agente vê onde erra mais | placar gerado das fichas | |
| A4 | **Minerar correções antigas do dono:** com `conversas.py`, achar as vezes em que ele corrigiu o time ("não", "errado", "eu disse"), e transformar cada uma em lição ou regra (sem copiar trecho) | o que ele já corrigiu não se repete | lições novas, com data | |
| A5 | **Teste da equipe periódico:** um prompt de exemplo, 3 agentes, nota pela régua; o que sair confuso vira correção no contexto | o sistema se testa sem o dono pedir | rotina escrita e rodada uma vez | |
| A6 | **Método de cada papel com fonte:** o Pesquisador busca a melhor prática de um papel por vez (ex.: veto, redação de resposta direta, arranjo de planta), o papel propõe, o Maestro decide; vira regra no contexto com fonte | saber mais, com prova | um papel por acordar | |
| A7 | **Memória entre conversas:** um resumo do que foi aprendido no dia (lições, placar, regras novas) que a próxima conversa lê primeiro | o que se aprende hoje chega amanhã | arquivo curto, citado no quadro | |
| A8 | Auditoria do Fable do aprendizado da noite e resumo da manhã | — | resumo curto | |

| A9 | **Camadas** (recado do dono, 01:50: "the IA inside the IA inside the IA inside the IA"): cada camada confere a de baixo. Agentes trabalham e vetam → o Maestro dá nota e tira a lição → o Fable audita o Maestro e as lições → o placar e o resumo do aprendizado medem se o erro caiu com o tempo e ajustam a regra. O Fable também leva nota (quem audita é auditado). Limite técnico: agente não abre agente sozinho; toda camada passa pela conversa principal, e a tarefa agendada é o que faz girar | o sistema melhora o jeito de melhorar | as 4 camadas escritas em `contexto/EQUIPE.md`, com a medida de cada uma | |

Depois de A9: repetir A5 e A6 (um papel por vez) até completar 24 horas.

**Recado do dono (01:46): "Just stay awake 24h".** **Tarefa agendada:** "X1-Plantas: trabalho de 24 horas" (antes "da noite") (`trig_01JBJYsSkBLwfVLfmJyS1kvr`), de hora em hora no minuto 45 (UTC), a primeira às 02:45; acorda esta conversa e faz a próxima linha da fila; depois da fila, segue com o "Tempo livre" do `pedidos/PLANO.md` (alternando equipe e projeto) até 2026-11-24 01:45 UTC; então escreve o resumo das 24 horas e se apaga. Para se o dono escrever ou se aparecer aviso de limite de uso.
