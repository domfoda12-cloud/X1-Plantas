# Tempo livre: deixar a equipe mais inteligente

**Estado:** fechada em 22/11/2026

**Prompt (palavra por palavra):** When not working in a concrete project try to make the agents/team more intelligent

**O que ele pediu, parte por parte:** Regra permanente: quando não houver projeto concreto em andamento, usar o tempo para deixar os agentes e a equipe mais inteligentes.

**Por que ele pediu, ou o que quer descobrir:** Ele quer um sistema que um dia ajude em qualquer coisa (fichas 1935 e 1944) e viu hoje que cada teste e auditoria deixa a equipe melhor. Tempo parado é tempo perdido.

**Objetivo dele:** Uma equipe que melhora sozinha, entre um trabalho e outro, sem ele pedir.

**Ligação com as ideias gerais do projeto:** Fio 4 (não ser o gargalo), fio 6 (economia onde ninguém vê), fio 8 (mostrar o que melhorou).

**Perguntas que me fiz:** O que é 'mais inteligente', na prática? Errar menos (lições guardadas), entender melhor (testes com pedido de exemplo), saber mais (método de cada papel com fonte) e gastar menos (medido). Tempo livre quando? Quando a fila espera o dono ou não há ficha aberta executável. Limite de gasto? O mesmo da rodada de melhoria: até 6 chamadas de agente por vez. O que eu medi: no teste da equipe, agente com todas as ferramentas custou cerca de 80 mil tokens por chamada (Designer 80.655, Editor 80.878, Redator 81.052, Pesquisador 81.793); com lista curta, cerca de 25 mil (Arquiteto 25.040, Revisor 27.604). A lista de ferramentas é o maior custo de cada chamada.

**Pronto quando:** Rotina escrita em `pedidos/PLANO.md` e citada em `contexto/EQUIPE.md`; seção 'Lições' em cada contexto; lista curta de ferramentas nos agentes que não precisam de tudo; teste na próxima conversa de que cada agente vê as suas ferramentas.

**Suposições (o dono não disse):** Designer e Editor ficam com todas as ferramentas (usam MinoAI, OpenArt e skills de vídeo, muitas). A rotina não gasta crédito pago nem publica nada. O Diretor (MinoAI) entra quando a melhoria toca conteúdo.

**Quem executa:** Maestro (Opus): rotina e listas de ferramentas. Agentes de cada papel nos testes; `supervisor` (Fable) confere a rotina na próxima auditoria.

**Conferência:** Listas de ferramentas postas em redator, estrategista, pesquisador, supervisor e ajudante; `checar.py` sem erro. Não conferido: se cada agente vê as suas ferramentas, porque o arquivo do agente só vale na próxima conversa; é o primeiro passo da rotina.

**Resultado:** Rotina de tempo livre (L1 a L6) em pedidos/PLANO.md; seção Lições em cada contexto; ferramentas enxutas em 5 agentes (cerca de 80 mil para 25 mil tokens por chamada, a confirmar na próxima conversa)

