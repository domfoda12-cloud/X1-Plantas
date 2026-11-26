# desacelerar: uma tarefa por vez

**Estado:** fechada em 26/11/2026

**Prompt (palavra por palavra):** "What used the most storage last time?" (20:42, mensagem que a caixa de entrada não guardou)

Slow down on it, if we work on all the tasks at the same time, none will be done

**O que ele pediu, parte por parte:** 1) Saber o que mais gastou na última janela (ele escreveu "storage"; leio como o limite de uso). 2) Desacelerar: não trabalhar em todas as tarefas ao mesmo tempo, senão nenhuma termina.

**Por que ele pediu, ou o que quer descobrir:** O limite de uso acabou duas vezes hoje (13:40 e 19:00) com tarefas pela metade: 3 agentes pararam no meio às 19:00.

**Objetivo dele:** Ver coisas prontas, uma depois da outra, em vez de muitas abertas.

**Ligação com as ideias gerais do projeto:** É o "Uma coisa por vez" do CLAUDE.md (20/11). Corrige a regra de 23/11 de 4 a 6 agentes em paralelo para gastar o limite inteiro.

**Perguntas que me fiz:** "Storage" é disco ou uso? Suponho uso; respondo com os tokens dos relatórios e pergunto. "Slow down" vale para sempre ou só agora? Trato como regra até ele dizer o contrário. Quantos agentes juntos? Decidi: no máximo 2 (quem faz e quem confere).

**Pronto quando:** A tarefa de hora em hora diz "uma tarefa por vez"; o quadro avisa todos; o plano tem a ordem das próximas 5, uma por vez; só o D20 roda.

**Suposições (o dono não disse):** Que "storage" quer dizer limite de uso. Que 2 agentes juntos (fazer e conferir) cabem no "slow down".

**Quem executa:** Maestro (regra, quadro, tarefa agendada); Planejador (ordem no plano).

**Conferência:** `python3 ferramentas/checar.py`; ler o prompt novo da tarefa agendada.

**Resultado:** Regra aplicada: uma tarefa principal por vez, no máximo 2 agentes; tarefa de hora em hora reescrita e depois pausada pelo dono

**O que aprendi:** nada novo

**Papéis afetados:** maestro, planejador

