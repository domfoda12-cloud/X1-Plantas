# dois agentes novos: planejador e organizador

**Estado:** fechada em 24/11/2026

**Prompt (palavra por palavra):** I want you to work on 2 things, idk it we have agents like those but I want something especialized in planning things, the step by step that has to be followed, what to do next what to do now etc etc
And someone who can organize large groups of things in smaller ones (smth like that)

**O que ele pediu, parte por parte:** 1) algo especializado em planejar: o passo a passo, o que fazer agora, o que fazer depois; 2) alguém que organize grupos grandes de coisas em grupos menores; 3) ele não sabe se já temos agentes assim.

**Por que ele pediu, ou o que quer descobrir:** Perguntou "how is progress?" e recebeu uma lista de pendências soltas. Quer ver ordem e pedaços tratáveis. Já tinha achado o quadro "meio simplista" e cansativo responder 5 perguntas juntas.

**Objetivo dele:** Saber sempre o que vem agora e tratar as coisas em grupos pequenos.

**Ligação com as ideias gerais do projeto:** "Sempre dê um objetivo à equipe; um plano passo a passo" (22/11); "uma coisa por vez" (20/11). Hoje não há esses papéis: o Maestro fazia os dois no meio da conversa e o `pedidos/PLANO.md` ficou velho.

**Perguntas que me fiz:** Já existe? (não: só o PLANO.md do Maestro.) Skill ou agente? (agente: ele disse "someone", e contexto próprio evita gastar o da conversa.) O júri de 23/11 disse para parar de crescer o sistema: vale? (o dono pediu direto, então entra; fica anotado.)

**Pronto quando:** Os dois agentes existem em `.claude/agents/`, estão no CONSELHO, ECOSSISTEMA e EQUIPE, o `checar.py` passa, e cada um rodou uma vez: plano até o primeiro Pix e as decisões pendentes do dono em grupos.

**Suposições (o dono não disse):** Os nomes (`planejador`, `organizador`); o modelo (Opus nos dois); que a primeira rodada é sobre o caminho até o primeiro Pix e sobre as decisões pendentes dele; que entra direto na `main` (2 arquivos de agente, não mexe em CLAUDE.md nem em settings).

**Quem executa:** Maestro escreve e registra; `planejador` e `organizador` fazem a primeira rodada; Supervisor confere na próxima auditoria.

**Conferência:** `checar.py` verde com os dois agentes registrados. Primeira rodada feita (como agente geral lendo o arquivo do papel, porque a sessão ainda não tinha carregado os nomes; eles apareceram depois). Li o topo do plano e do arquivo de grupos; corrigi no plano a frase "o e-book promete 2 bônus" (quem promete é a oferta; o PDF anuncia 0, pelo `checar.py`). Não conferi item por item as 90 entradas do Organizador nem os 32 do Planejador; os dois números diferem (38 e 32) e o plano explica por quê.

**Resultado:** Agentes planejador e organizador criados e registrados; primeira rodada: plano geral reescrito e decisões pendentes em 9 grupos

**O que aprendi:** maestro: agente novo avalia o próprio arquivo de papel na primeira rodada; as duas avaliações acharam falhas reais (limite de grupo, como contar, onde está o estado real).

