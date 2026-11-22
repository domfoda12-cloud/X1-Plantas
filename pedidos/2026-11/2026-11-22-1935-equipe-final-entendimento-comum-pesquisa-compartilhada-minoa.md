# Equipe final: entendimento comum, pesquisa compartilhada, MinoAI diretor, testes

**Estado:** fechada em 22/11/2026

**Prompt (palavra por palavra):** For each prompt: I call only the agents that matter. On the ticket I write one line per agent saying what it adds. An agent that gets work outside its role hands it back and says whose it is.
Even though you only call the ones that matter, i want them all to come to the same understanding of whats happening does that makes sense?
Make a share tab or whatever where all agents can web search make them keep it organised
You can have an editor and designer but make sure MinoAI its in both, later i would like a clear demonstration on what skills is connected to which agent 
You are the main maestro, MinoAI the director, you take the decisions he gives the main idea for content related things
2 3 yes, make this the final changes, tidy up everything make some tests and improve it based on feedback from the team

**O que ele pediu, parte por parte:** 1) Todos os agentes com o mesmo entendimento do que está acontecendo, mesmo os não chamados. 2) Um lugar compartilhado onde todos pesquisam na web, organizado. 3) Designer e Editor separados, mas a MinoAI nos dois; depois, uma demonstração clara de que skill liga a qual agente. 4) Ele (a conversa principal) é o Maestro e decide; a MinoAI é o Diretor e dá a ideia principal do conteúdo. 5) Sim às perguntas 2 (Revisor no Fable na peça final) e 3 (lembrete do gancho curto). 6) Mudanças finais: arrumar tudo, testar e melhorar com a opinião da equipe.

**Por que ele pediu, ou o que quer descobrir:** Continua a ficha 1924 (organizar os agentes). Ele quer uma equipe que pense junto sem gastar token: um entendimento comum barato, pesquisa que não se repete, e papéis claros de quem decide (o Maestro) e de quem dá a ideia do conteúdo (a MinoAI).

**Objetivo dele:** Fechar o desenho da equipe e voltar ao trabalho (arquivos, depois a E07).

**Ligação com as ideias gerais do projeto:** Fio 3 (nada se perde), fio 6 (economia onde ninguém vê), fio 7 (a MinoAI na frente), fio 9 (a regra mais nova vence: a MinoAI deixa de ser o Maestro).

**Perguntas que me fiz:** 'Mesmo entendimento' sem chamar todos? Agente só existe quando é chamado: o jeito barato é um bloco 'Agora' no quadro que todos leem primeiro. 'Share tab' é página web? Suposição: um caderno no repositório, que todo agente lê e escreve com um programa; página só se ele pedir. 'Demonstração clara depois': tabela agora (ECOSSISTEMA 2b), página visual oferecida. Diretor opina em código? Ele disse 'content related': não.

**Pronto quando:** Bloco 'Agora' no quadro; `pesquisas/` e `ferramentas/pesquisa.py` funcionando e no `checar.py`; todos os agentes com web e a regra do caderno; Maestro e Diretor trocados nos documentos atuais; Revisor no Fable na peça final; gancho curto; teste com a equipe feito e o retorno aplicado; `checar.py` e painel sem erro.

**Suposições (o dono não disse):** Caderno no repositório, não página web. O Diretor não opina em sistema e código. O Revisor ganhou leitura da web, mas não escreve no caderno (devolve o achado). O `ajudante` não grava no caderno (é pessoal). Registros antigos da seção 7 do CONSELHO mantêm 'Maestro' com o sentido da época.

**Quem executa:** Maestro (Opus, conversa principal): mudanças. Teste: redator, arquiteto, designer, editor-video, revisor-de-risco e pesquisador, cada um com o mesmo prompt de teste, resposta curta. Supervisor (Fable): auditoria das fichas fechadas, se for a hora. Conselho de bolso: Diretor neutro (é sistema); Estrategista SIM (menos busca repetida); Revisor SIM (o caderno exige fonte).

**Conferência:** teste com 6 agentes (Designer, Editor, Redator, Arquiteto, Revisor, Pesquisador), mesmo prompt de exemplo ('carrossel da C01'). Todos leram o 'Agora' igual e souberam a sua parte e a quem devolver. Acharam: agente e CLAUDE.md mudados só valem na próxima conversa (Arquiteto e Revisor sem web nesta); fatos repetidos entre agente e contexto (fotos do Designer, frases vetadas do Redator); vídeo 'só planeje' contra 'aberto em 21/11'; quem escreve o resumo de passagem; deep-research grátis x TinyFish pago; caderno sem ajuda nos campos, sem tipo de norma, sem filtro de dado pessoal. Tudo corrigido; guardas do caderno testadas uma a uma. `checar.py` e painel sem erro. Não conferido: as ferramentas de web do Arquiteto e do Revisor, que só aparecem na próxima conversa.

**Resultado:** Equipe final: Maestro e Diretor, Agora no quadro, caderno de pesquisa, skills por agente, Revisor no Fable, testada com 6 agentes

