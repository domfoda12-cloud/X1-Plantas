# Testar as ferramentas novas, achar funções que faltam na equipe (ex.: ensinar) e deixar os agentes mais inteligentes

**Estado:** aberta

**Prompt (palavra por palavra):** Faça os testes, also look for gaps in agente that we need, some function that we don't got cover (for example teaching) and look to add them in the system
As always, better the functionality of the agents make them smarter, idk how to properly do that but i trust your best

*Recado de 23/11 09:52:* Also críticize my way of prompting, the project in general, and look for ways to improve

*Recado de 23/11 10:47:* Agora é a hora que você tem para me mandar todas as perguntas pendentes

**O que ele pediu, parte por parte:** (1) Fazer os três testes de funcionamento real das ferramentas novas que propus (marketing-psychology num texto real; everything-claude-code na cópia separada; como se encaixam). (2) Achar funções que a equipe não cobre (ele deu o exemplo "ensinar") e pôr no sistema. (3) Deixar os agentes mais inteligentes; ele não sabe como e confia no Maestro.

**Por que ele pediu, ou o que quer descobrir:** Voltou, achou pouco o trabalho da noite e perguntou se as ferramentas de ontem foram testadas de verdade (não foram).

**Objetivo dele:** Um sistema que funcione de verdade e cubra tudo o que o negócio precisa.

**Ligação com as ideias gerais do projeto:** Fio 6 (qualidade) e fio 4 (autonomia); o júri alertou: sistema demais e venda de menos.

**Perguntas que me fiz:** "Ensinar" quem? O dono (explicar para decidir) e o comprador (ler a planta, construir por etapas): os dois. Agente novo ou linha num que existe? O mais barato que resolve. Mudar `tools:` de agente pede o dono? Ele autorizou melhorar os agentes; a trava só tira ferramenta paga, e é reversível.

**Pronto quando:** [ ] 3 testes com resultado (código/Maestro); [ ] lacunas mapeadas e as baratas aplicadas, com veto do Revisor (Fable); [ ] relatório ao dono em palavras simples (dono).

**Suposições (o dono não disse):** Que ele quer as lacunas aplicadas já (ele disse "look to add them"); agente novo só se nenhum existente couber.

**Quem executa:** Maestro (testes 2 e 3, código, skill); `redator` (teste da marketing-psychology); geral no Opus (mapa de lacunas); `arquiteto` (lote da C01 e "por etapas"); `revisor-de-risco` (veto).

**Conferência:** Teste 1 (marketing-psychology, Redator, na sequência do WhatsApp): carregou e a trava funcionou; valeu como conferência (achou o Dia 1 sem pergunta e o Dia 3 sem o lote da pessoa), pouco como ideia nova; 5 consertos na seção "Neste projeto", aplicados. Teste 2 (everything-claude-code na cópia separada, com a main junta): `checar.py` verde, ficha nova criada e `pedido.py conferir` ok, chave falsa acusada pela conferência de segredos; o contexto do Maestro estourava e foi consertado. Teste 3 (encaixe): marketing-psychology não estava em agente nenhum (agora no Redator e no Estrategista); o método do júri só existia numa ficha (agora `CONSELHO.md`, 5b). Lacunas (geral no Opus): ensinar o dono (skill nova `explicar-ao-dono`), ensinar o comprador a construir por etapas (não existe no e-book: pergunta ao dono), dúvidas do comprador que não voltam, Designer e Editor com todas as ferramentas (fechado). Nenhum agente novo: nenhuma lacuna é recorrente e sem dono. Arquiteto: o lote 8 x 15 contra 8 x 13 é arredondamento de propósito, mas "a partir de" junto do número arredondado engana (24 casas). Revisor: SIM SE nas 3 mudanças, correções aplicadas.

**Resultado:** (a preencher)

**O que aprendi:** (a preencher)

