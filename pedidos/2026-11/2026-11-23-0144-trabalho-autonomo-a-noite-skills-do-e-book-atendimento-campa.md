# Trabalho autônomo à noite: skills do e-book, atendimento, campanha de anúncio

**Estado:** aberta

**Prompt (palavra por palavra):** What really its your limit? I would like for the system to keep studying andi mproving afk now that im going to sleep, it can use all tokens as you want but what really its your limit? Can you add skills that are relevant for building the ebook, think of ways to improve the UI and costumer service, Create a ads campaign marketing. These are all examples that you can learn about, id really like if you were autosufficient

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


## Fila da noite (uma por acordar; plano vetado antes; nada pago, nada publicado)

| # | Tarefa | Quem | Entrega para a manhã |
|---|---|---|---|
| N1 | Veto do plano da noite e L1 (cada agente confirma as ferramentas) | Fable; todos | plano aprovado; ferramentas conferidas |
| N2 | **Skills para construir o e-book:** procurar skills e ferramentas que ajudam (gerar PDF de qualidade, revisar páginas, imagens), passar pelo roteiro de entrada (licença lida, Revisor, Conselho) e propor as boas | Pesquisador acha; Designer e Arquiteto concluem; Revisor | lista com o que entra e por quê; nada instalado sem o veto |
| N3 | **Atendimento ao cliente:** rever o funil do WhatsApp (mensagens, objeções, planta grátis) com as casas e regras de hoje; propor melhorias | Redator e Estrategista; Revisor | textos novos como proposta |
| N4 | **Interface:** rever a calculadora do parceiro e as páginas do e-book (o que confunde o comprador) e propor melhorias | Designer; Arquiteto confere números | lista de melhorias com antes e depois |
| N5 | **Campanha de anúncio (plano, sem gastar):** público, ângulos, peças, orçamento de teste em opções, o que medir | Estrategista com o Diretor; Redator; Revisor | plano de campanha para o dono aprovar verba |
| N6 | Tempo livre: lições das auditorias para os contextos; cortar repetido numa pasta | Maestro | números de antes e depois |
| N7 | Auditoria do Fable da noite e resumo da manhã | Fable; Maestro | resumo curto: pronto, em veto, esperando o dono |

**Tarefa agendada:** "X1-Plantas: trabalho da noite" (`trig_01JBJYsSkBLwfVLfmJyS1kvr`), de hora em hora no minuto 45 (UTC), a primeira às 02:45; acorda esta conversa e faz a próxima linha da fila; apaga a si mesma quando a fila acabar.
