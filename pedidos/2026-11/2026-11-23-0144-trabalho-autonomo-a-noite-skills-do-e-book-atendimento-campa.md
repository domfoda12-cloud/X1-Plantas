# Trabalho autônomo à noite: skills do e-book, atendimento, campanha de anúncio

**Estado:** aberta

**Prompt (palavra por palavra):** What really its your limit? I would like for the system to keep studying andi mproving afk now that im going to sleep, it can use all tokens as you want but what really its your limit? Can you add skills that are relevant for building the ebook, think of ways to improve the UI and costumer service, Create a ads campaign marketing. These are all examples that you can learn about, id really like if you were autosufficient

*Recado de 23/11 01:47:* Just stay awake 24h

*Recado de 23/11 01:49:* This night dont queue anything that you have to produce, simply focus on making the system autonomous on learning

*Recado de 23/11 01:49:* the IA inside the IA inside the IA inside the IA

*Recado de 23/11 01:54:* I dont have a mac

*Recado de 23/11 01:55:* Thats too simple of a task, its one simple command per run

*Recado de 23/11 01:55:* Can I create a private web that the IA can use?

*Recado de 23/11 01:55:* wdym the night routine will update it on every run

*Recado de 23/11 01:55:* No, i mean like that the agents can use to search on the WWW

*Recado de 23/11 02:04:* https://github.com/vercel-labs/skills/blob/main/skills%2Ffind-skills%2FSKILL.md add

*Recado de 23/11 02:04:* the add of these new agents

*Recado de 23/11 02:04:* Or right before every hour

*Recado de 23/11 02:09:* Make sure that the night queue is aware that the task followed will be done for the next hour

*Recado de 23/11 07:11:* I hit my usage limit while you were working, but it has reset now. Please continue from where you left off.

**O que ele pediu, parte por parte:** 1) Qual é o meu limite de verdade. 2) O sistema seguir estudando e melhorando enquanto ele dorme, usando os tokens que quiser. 3) Exemplos: skills relevantes para construir o e-book; melhorar a interface e o atendimento ao cliente; criar uma campanha de anúncio. 4) Quer o sistema autossuficiente.

**Por que ele pediu, ou o que quer descobrir:** Quer que o tempo dele dormindo vire trabalho, e quer saber até onde pode confiar no sistema sozinho.

**Objetivo dele:** Um sistema que trabalha e melhora sem ele, e que de manhã tem coisas prontas para ele decidir.

**Ligação com as ideias gerais do projeto:** Fio 4 (não ser o gargalo; autonomia no fazer, confirmação no gastar e publicar), fio 6 (qualidade primeiro).

**Perguntas que me fiz:** Eu trabalho sozinho? Só quando algo me acorda: entre mensagens eu não rodo. Para trabalhar à noite, agendo mensagens que me acordam nesta conversa (tarefa agendada de hora em hora). O que posso fazer sem ele? Planejar, pesquisar, escrever, programar, testar e vetar; nada de gastar crédito, publicar, mandar mensagem, contratar ou decidir preço, título e nome (regras dele). Limites técnicos: o limite de uso da conta (semanal), o tamanho desta conversa (é resumida sozinha), o contêiner pode ser reiniciado (o trabalho fica salvo no git a cada passo).

**Pronto quando:** Fila da noite escrita; tarefa agendada criada; a cada acordar uma tarefa da fila, com plano vetado, `checar.py` e commit; de manhã um resumo para o dono com o que ficou pronto e o que espera o "sim" dele.

**Suposições (o dono não disse):** Leitura nossa dos recados: "uma tarefa por acordar é simples demais" virou: cada acordar trabalha uns 40 a 50 minutos, várias tarefas, em paralelo só o que é leitura e pesquisa, e cria sozinho o próximo ciclo. 24 horas (até 24/11 01:45 UTC). Nada pago nem publicado; tudo que é decisão dele vira opção.

**Quem executa:** Maestro (Opus) conduz cada acordar; o time de cada assunto executa e veta; o Fable veta o plano da noite e audita no fim.

**Conferência:** (no fim)

**Resultado:** (a preencher)


## Fila da noite, versão 4 (recados do dono, 02:0x: "make the jury criticise it a lot of times, and improve at each time"; "the add of these new agents"; "update the night queue after every hour, or right before every hour")

**Como funciona agora:** no fim de cada acordar, o Maestro **reescreve esta fila** para a hora seguinte, com o que aconteceu (resultado do júri, recados do dono, lições). A fila abaixo é a da próxima hora.

| # | Tarefa | Estado |
|---|---|---|
**PRÓXIMA HORA (07:45 a 08:45 UTC), escrita às 07:36:** A0, A2 e A3 estão feitos e na main (prova de base, lição ao fechar ficha, placar). A tarefa desta hora é o **A4, minerar correções antigas do dono**, com as condições do Fable (abaixo, "A4"): ler `contexto/dono/PROMPTS.md` e a pasta `intencoes/` (e `pedidos/entrada/`, filtrando a mensagem da tarefa agendada e os avisos automáticos) atrás das vezes em que o dono corrigiu o time ("não", "errado", "eu disse", "mas não", "remember", "don't"); **uma palavra por busca**, com `python3 ferramentas/conversas.py buscar <palavra>` também (na nuvem ele só vê esta conversa). Para cada correção achada: conferir se já existe lição ou regra (grep nos `contexto/*.md` e na `CONVIVENCIA.md`); se não existe, gravar com `python3 ferramentas/pedido.py licao <papel> "texto" --origem dono` com a data da fala e "leitura nossa" no texto, **sem copiar trecho** do dono; se o contexto do papel estiver cheio (o `arquiteto.md` está), consolidar antes, movendo as lições mais antigas ao `CONTEXTO-HISTORICO.md`. Lista do que foi achado, do que já existia e do que virou lição, na ficha 0144. Revisor (dado pessoal, citação) e Fable uma vez antes do commit; `checar.py` verde; push na main. **Não fazer:** criar regra de convivência nova sem o dono (só lição); mexer em `CLAUDE.md`, `settings.json`, ganchos, agentes; tocar a branch `sistema/everything-claude-code`; texto público. Nos últimos 10 minutos, escreve aqui a tarefa da hora seguinte (sugestão: A6, método de um papel com fonte, começando pelo veto; ou a prova 2 com casos de omissão, se o placar precisar de n).

| J1 | Júri, rodada 1, sobre `pedidos/anexos/integracao-novos-v1.md` (as 5 adições: llm-council, chief-of-staff, marketing-psychology, last30days, find-skills): 4 opiniões, revisão anônima, presidente; depois o Maestro escreve a v2 com as críticas | **em andamento** (etapa 1 rodando às 02:05) |
| J2 | Rodada 2 sobre a v2; v3 | |
| J3 | Rodada 3 sobre a v3; v4 | |
| Jn | Repetir até a nota do júri parar de subir duas rodadas seguidas; então o que é interno e passou no júri é aplicado (com o veto do Revisor), e o que é do dono vira opção para a manhã | |
| Depois | A0 (prova de base), A2, A3, A10 da versão 3, se o dono não mudar a direção; o veredito do júri de 23/11 (parar de crescer o sistema) fica como pergunta para ele | |

## Fila da noite, versão 3 (recado do dono, 01:50: "esta noite não enfileire nada que você tenha de produzir; foque em deixar o sistema autônomo no aprendizado")

A versão 2 (E07, funil, campanha, interface, skills) fica para depois, com o "sim" dele. Esta noite só se constrói **como o sistema aprende sozinho**. Cada acordar trabalha uns 40 a 50 minutos (várias tarefas); plano curto vetado; regras da noite da versão 2 continuam (nada pago, nada publicado, nada instalado, texto público intocado).

| # | Tarefa | O que faz o sistema aprender sozinho | Pronto quando | Estado |
|---|---|---|---|---|
| A1 | Veto do Fable desta fila | — | fila aprovada | **Feito:** SIM, SE para A2 a A9 (92 mil tokens); condições abaixo |
| A2 | **Lição automática ao fechar ficha:** o `pedido.py fechar` passa a exigir o campo "O que aprendi" e copia a lição para o "Lições" do contexto de quem errou (e do Maestro) | todo erro vira lição sem depender de memória | testado no `checar.py` | **Feito 06:20:** `pedido.py licao` e o campo "O que aprendi" no `fechar` (de 23/11 em diante); registro `pedidos/LICOES.md`; 2 testes no `checar.py` (funções e 9 casos de ponta a ponta com fichas falsas, que falham com o código antigo). Veto: revisão de código SIM SE e Fable SIM SE (7), correções aplicadas. O "(e do Maestro)" ficou de fora a pedido do Fable: o `LICOES.md` é a visão do Maestro, e copiar tudo encheria o `maestro.md`. Processo: o commit "em veto" foi para a branch da sessão antes do veto (o gancho de fim de turno pediu commit); a main só recebeu depois |
| A3 | **Placar do veto:** cada nota da régua vai para um placar (`contexto/PLACAR.md`, gerado), por agente e por ponto que caiu; o agente lê a sua linha antes de vetar | cada agente vê onde erra mais | placar gerado das fichas | **Feito 07:35:** `ferramentas/placar.py` gera `contexto/PLACAR.md` (nota de 0 a 5 com n, ponto da régua que mais cai, provas, lições); o `--conferir` no `checar.py` falha com placar velho e com tabela de veto fora do formato fixo (escrito no `pedidos/LEIA-ME.md`); quem chama o veto cola a linha do agente no pedido (pacote do executor, item 6). Veto: revisão de código SIM SE e Fable SIM SE (6); correções aplicadas (prova repetida não soma em dobro, ponto mapeado na régua, alarme falso da prova 1 "não medido"). **Regra criada à noite, o dono não viu;** o júri de 23/11 recomendou parar placar e nota: pergunta a ele na manhã |
| A4 | **Minerar correções antigas do dono:** com `conversas.py`, achar as vezes em que ele corrigiu o time ("não", "errado", "eu disse"), e transformar cada uma em lição ou regra (sem copiar trecho) | o que ele já corrigiu não se repete | lições novas, com data | |
| A5 | **Teste da equipe periódico:** um prompt de exemplo, 3 agentes, nota pela régua; o que sair confuso vira correção no contexto | o sistema se testa sem o dono pedir | rotina escrita e rodada uma vez | |
| A6 | **Método de cada papel com fonte:** o Pesquisador busca a melhor prática de um papel por vez (ex.: veto, redação de resposta direta, arranjo de planta), o papel propõe, o Maestro decide; vira regra no contexto com fonte | saber mais, com prova | um papel por acordar | |
| A7 | **Memória entre conversas:** um resumo do que foi aprendido no dia (lições, placar, regras novas) que a próxima conversa lê primeiro | o que se aprende hoje chega amanhã | arquivo curto, citado no quadro | |
| A8 | Auditoria do Fable do aprendizado da noite e resumo da manhã | — | resumo curto | |

| A9 | **Camadas** (recado do dono, 01:50: "the IA inside the IA inside the IA inside the IA"): cada camada confere a de baixo. Agentes trabalham e vetam → o Maestro dá nota e tira a lição → o Fable audita o Maestro e as lições → o placar e o resumo do aprendizado medem se o erro caiu com o tempo e ajustam a regra. O Fable também leva nota (quem audita é auditado). Limite técnico: agente não abre agente sozinho; toda camada passa pela conversa principal, e a tarefa agendada é o que faz girar | o sistema melhora o jeito de melhorar | as 4 camadas escritas em `contexto/EQUIPE.md`, com a medida de cada uma | |

| A0 | **Prova de base (antes de qualquer lição):** 6 a 8 planos com erro plantado, tirados das auditorias (promessa de aprovação, número sem fonte, sugestão usada sem o "sim", texto público mexido, instalar antes do veto, resumo contra a fala do dono...), com gabarito guardado fora do alcance dos agentes; 3 agentes vetam; nota = erros achados sobre plantados, e alarmes falsos; resultado em `pedidos/PROVAS.md`. Roda de novo no fim da noite | é a régua: sem ela não se sabe se aprendeu | nota de base registrada | **Feito 04:55:** 39 de 40 achados, 0 alarme falso inteiro; o que escapa é a omissão (Diretor ausente); `pedidos/PROVAS.md` |
| A10 | **Suposição do Mac:** o dono não tem Mac (23/11). Quando ele disser o que tem (PC com Windows, só celular...), corrigir as 63 menções em 22 arquivos (guia da MinoAI, editor, pesquisador, busca nas conversas, plano) e criar a conferência no `checar.py` que pega "Mac do dono" | erro de suposição não volta | zero menção a Mac do dono; conferência testada | espera a resposta |

**Condições do Fable (A1), valem para cada tarefa:**
- A2: `pedido.py licao <papel> "texto" --ficha --ponto --origem` grava num registro só de acréscimo (`pedidos/LICOES.md`) e no "Lições" do contexto; `fechar` chama esse comando; "O que aprendi" obrigatório só em ficha fechada de 23/11 em diante; contexto perto do limite: o comando recusa e manda consolidar (nunca subir o limite); conferência no `checar.py` com ficha falsa.
- A3: `ferramentas/placar.py` gera `contexto/PLACAR.md` com o n ao lado de cada média; formato fixo das tabelas de veto de 23/11 em diante: `| Rodada | Agente | Nota | Ponto que caiu | Por quê |`; nenhuma regra muda com n menor que 5; entra no mapa.
- A4: na nuvem o `conversas.py` só vê esta conversa: minerar também `contexto/dono/PROMPTS.md` e `intencoes/`; uma palavra por busca; cada lição com a data da fala e "leitura nossa"; conferir se a mensagem da tarefa agendada cai em `pedidos/entrada/` e, se cair, filtrar.
- A5 = a prova do A0, repetida; cada erro novo de auditoria vira caso novo.
- A6: um papel por ciclo, pesquisa em dois passos, regra no `contexto/<papel>.md` com fonte, data e "noite, o dono não viu"; só vale com um caso novo na prova.
- A7: não à mão: o topo do `PLACAR.md` gerado, citado no quadro.
- A9: `contexto/CAMADAS.md` (o `EQUIPE.md` não cabe), medida por fato contado: prova (agentes), renota às cegas e erros por auditoria (Maestro), achados confirmados e erro que escapou (Fable), reincidência da lição (camada 4).
- A8: o resumo lista toda regra criada à noite, para o dono manter ou desfazer.
- Paralelo só leitura e pesquisa; só o Maestro escreve e faz commit. Ordem: A0 → A2 e A3 (com A4 e A6 ao lado) → prova de novo → A7, A9 → A8.
- **Segurança:** não mudam à noite `CLAUDE.md`, configuração, ganchos, `tools:` e modelo dos agentes, palavras do dono, a tarefa agendada; no `checar.py` só se acrescenta; um commit por tarefa; falhou duas vezes: desfaz, anota, pula; uns 40 minutos de trabalho e 10 para conferir e salvar.
- **Branch:** o `CLAUDE.md` manda mudança grande de sistema para `sistema/<assunto>` com pull request; o que a noite faz são conferências e ferramentas pequenas, uma por commit, reversíveis: fica na `main`, como todo o trabalho de 22/11 que o dono aprovou levar à main.

Depois de A9: repetir A5 e A6 (um papel por vez) até completar 24 horas.

**Recado do dono (01:46): "Just stay awake 24h".** **Tarefa agendada:** "X1-Plantas: trabalho de 24 horas" (antes "da noite") (`trig_01JBJYsSkBLwfVLfmJyS1kvr`), de hora em hora no minuto 45 (UTC), a primeira às 02:45; acorda esta conversa e faz a próxima linha da fila; depois da fila, segue com o "Tempo livre" do `pedidos/PLANO.md` (alternando equipe e projeto) até 2026-11-24 01:45 UTC; então escreve o resumo das 24 horas e se apaga. Para se o dono escrever ou se aparecer aviso de limite de uso.

**Limite de uso (23/11, 06:50 a 07:10 UTC):** o veto do A3 caiu no limite de 5 horas (2 agentes, 149 mil tokens antes do corte). O dono avisou às 07:11 que o limite voltou; o veto roda de novo (`wf_9fb12177-6be`, retomado). Gasto medido desta noite até aqui, só subagentes de workflow: júri 2,95 milhões; everything-claude-code 1,67 milhão (leitura) e a implementação parada; v6 536 mil; prova A0 536 mil; veto A2 256 mil.
