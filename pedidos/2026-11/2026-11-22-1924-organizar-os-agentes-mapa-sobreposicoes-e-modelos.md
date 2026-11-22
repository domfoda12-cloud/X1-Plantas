# Organizar os agentes: mapa, sobreposições e modelos

**Estado:** fechada em 22/11/2026

**Prompt (palavra por palavra):** I need to organise my agents

*Recado de 22/11 19:25:* It means that every agent knows its function in the project, and with each prompt they know what advice needs to be added to give the result i desire, their information is all summered together and organised

*Recado de 22/11 19:26:* I want to create a system that can help me with anything at some point

*Recado de 22/11 19:26:* but to get to that level we gotta be as efficient as possible with our token and time usage

*Recado de 22/11 19:27:* or find new ways to save tokens

**O que ele pediu, parte por parte:** 1) "Organizar os agentes": escolheu, nas opções, mapa da equipe, consertar sobreposições e lacunas, e rever os modelos; antes das outras fichas. 2) Recado: cada agente sabe a sua função e, a cada prompt, o que acrescentar para o resultado que ele quer; a informação de todos resumida junta. 3) Recado: quer um sistema que o ajude em qualquer coisa com o tempo. 4) Recado: para chegar lá, o máximo de economia de token e tempo.

**Por que ele pediu, ou o que quer descobrir:** Os agentes cresceram em camadas (Conselho 20/11, fichas e modelos 22/11) e as instruções se contradiziam (ficha antiga `PEDIDO-*`, Sonnet no Estrategista, imagem com dois donos). Ele quer que cada prompt chegue ao resultado sem ele ter de explicar quem faz o quê.

**Objetivo dele:** Uma equipe que se organiza sozinha a cada prompt e que cresce para qualquer tipo de pedido.

**Ligação com as ideias gerais do projeto:** Fio 3 (nada se perde: tudo junto e organizado), fio 4 (não ser o gargalo), fio 6 (o modelo certo para cada tarefa).

**Perguntas que me fiz:** O que é 'organizar'? Perguntei (respondeu: mapa, sobreposições, modelos). Mudo modelos sozinho? Não: foram escolha dele em 22/11; só apontei o que contradizia. Crio o agente Maestro? Não sem ele: é roteiro do Conselho, seção 6; perguntei. 'Qualquer coisa' é para agora? Não: virou a regra de papel novo, sem abrir frente nova.

**Pronto quando:** `contexto/EQUIPE.md` existe e é citado por agentes, contextos, CONSELHO e LEIA-ME; as 6 contradições corrigidas; `checar.py` e `atualizar-painel.py` sem erro.

**Suposições (o dono não disse):** A divisão imagem parada = Designer, o que se move = Editor é nossa. 'Acrescenta a cada prompt' virou uma linha por agente em 'Quem executa'. Modelos mantidos.

**Quem executa:** Opus na conversa principal (é configuração do sistema, curta). Conselho de bolso: Maestro neutro (não toca gancho nem vídeo); Estrategista SIM (menos retrabalho); Revisor SIM (nenhuma regra de honestidade mudou).

**Conferência:** `checar.py` sem erro de orçamento (EQUIPE.md cabe no limite de 3500 caracteres); greps confirmam que nenhum agente cita mais a ficha `PEDIDO-*` sozinha nem 'Sonnet para o rotineiro'. Não conferido: um prompt real rodando pelo novo fluxo.

**Resultado:** Mapa da equipe em contexto/EQUIPE.md; contradições dos agentes corrigidas; agentes leem menos (CLAUDE.md não é reaberto)

