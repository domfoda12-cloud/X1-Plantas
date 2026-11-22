# Plano mestre da equipe e melhoria contínua

**Estado:** aberta

**Prompt (palavra por palavra):** Put this in queue:
Give a main plan, function and objective for the team and make them come out with the plan that should be obvious by the entire context given in the very main branch, Have them think about it for a bit together and keep finding improvements in the system, project, plan, whatever its noticed on the code

*Recado de 22/11 19:44:* i want to give them a lot of liberty of thought...

**O que ele pediu, parte por parte:** Na fila, não agora. 1) Um plano principal, a função e o objetivo da equipe. 2) A equipe chega sozinha ao plano que deveria ser óbvio por todo o contexto da branch principal. 3) Pensar juntos por um tempo. 4) Continuar achando melhorias no sistema, no projeto, no plano e no código.

**Por que ele pediu, ou o que quer descobrir:** Com a equipe organizada (fichas 1924 e 1935), ele quer saber se ela entendeu o projeto sem ele explicar: se o plano que sai dela bate com o que ele tem na cabeça, o contexto está bom. E quer que a melhoria vire rotina, não pedido.

**Objetivo dele:** Um plano mestre único que todos seguem, e uma equipe que se melhora sozinha.

**Ligação com as ideias gerais do projeto:** Fio 4 (não ser o gargalo), fio 5 (uma coisa de cada vez, na ordem), fio 8 (ele confere: o plano mostra se entenderam), fio 3 (nada se perde).

**Perguntas que me fiz:** 'Branch principal' = `main`; esta sessão trabalha em `claude/wonderful-hopper-rmqtyy`, então antes juntar na `main` (precisa do ok dele). 'Pensar juntos' com agentes que não conversam entre si: rodada 1 cada papel propõe; rodada 2 cada um lê as propostas dos outros e critica; o Maestro junta; o Fable audita. 'Continuar achando melhorias' sem gastar demais: rotina com limite (ex.: uma rodada a cada N fichas fechadas), não um laço infinito. Quanto de token ele aceita para isso? Perguntar.

**Pronto quando:** `PLANO.md` (ou seção do `CONTEXTO.md`) com missão, objetivo, função de cada papel e a sequência de frentes, tirado só do contexto da `main`, com fonte por item; críticas cruzadas registradas; lista de melhorias priorizada (venda, custo, risco) com dono de cada uma; a rotina de melhoria escrita em `pedidos/LEIA-ME.md` e no `checar.py` se couber; o dono conferiu se o plano bate com o que ele quer.

**Suposições (o dono não disse):** Entra na fila depois de "Organizar os arquivos" e antes da E07 (confirmado pelo dono, 22/11). Orçamento: o dono não sabe; padrão de até 16 chamadas de agente no plano e até 6 por rodada de melhoria. A rodada usa os papéis do projeto no modelo de cada um, no máximo umas 8 chamadas por rodada. **Liberdade de pensamento (recado dele):** o pedido a cada agente vai aberto (contexto e objetivo, sem roteiro de resposta nem formato de uma linha); cada um pode discordar do plano atual, das regras e do próprio papel, e propor o que quiser. Os limites que continuam: honestidade e lei (veto do Revisor), gasto e publicação com o "sim" do dono. Melhoria em código passa pelo Ponytail; nada público sai sem o Revisor.

**Quem executa:** Maestro (Opus): enquadra e junta. Rodada 1 e 2: estrategista (plano e prioridade), arquiteto (código e plantas), redator, designer, editor-video (com o Diretor MinoAI), revisor-de-risco; pesquisador só se faltar fonte. Supervisor (Fable): confere o plano contra o contexto e aponta o que ficou óbvio e não entrou.

**Conferência:** na fila; ainda não executado.

**Resultado:** (a preencher)

