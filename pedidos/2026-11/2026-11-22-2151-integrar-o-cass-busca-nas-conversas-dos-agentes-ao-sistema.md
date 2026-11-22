# Integrar o cass (busca nas conversas dos agentes) ao sistema

**Estado:** fechada em 22/11/2026

**Prompt (palavra por palavra):** Try to integrate cass in the system since it's similar

**O que ele pediu, parte por parte:** Integrar ao sistema o cass (Coding Agent Session Search, de Jeffrey Emanuel), que indexa e busca as conversas de mais de 30 ferramentas de agente num banco local; ele acha que é parecido com o que o projeto já faz.

**Por que ele pediu, ou o que quer descobrir:** O fio que mais volta: "nada do que eu disse se perde". O projeto guarda os prompts e as decisões (curado); o cass guarda as conversas inteiras (bruto). Juntos, qualquer agente acha o que o dono disse em qualquer conversa.

**Objetivo dele:** Uma memória que alcança tudo o que ele já disse a qualquer agente.

**Ligação com as ideias gerais do projeto:** Fio 3 (nada se perde), fio 6 (economia: achar em vez de perguntar de novo).

**Perguntas que me fiz:** Onde ele serve? Na nuvem, cada conversa é um contêiner novo: o cass só vê a conversa atual. No Mac do dono vê tudo. Então: integração opcional (usa se existir, nada quebra se não existir). É seguro? O README diz que tudo é local e nada sai da máquina; o embedder externo é opcional e desligado. Mas ele lê as conversas de **todos** os projetos e de assuntos pessoais: o Revisor diz o que pode ir para o repositório. Cabe no roteiro de entrada (CONSELHO, seção 6)? Sim: é ferramenta nova.

**Pronto quando:** Roteiro de entrada cumprido (lido, vetado, registrado em ECOSSISTEMA e CONSELHO, projeto ensinado); `pesquisa.py buscar` também busca nas conversas quando o cass existe; regra de uso no LEIA-ME e no guia do Mac; rodado uma vez aqui; `checar.py` sem erro.

**Suposições (o dono não disse):** Que 'integrar' é: o sistema usa o cass quando ele existe, sem depender dele. Que o uso principal é no Mac do dono. Que o cass não vai para dentro do repositório (é programa instalado, como o ffmpeg).

**Quem executa:** Maestro (Opus): plano e código. Veto: `revisor-de-risco` (privacidade), `estrategista` (vale o custo?), depois o Fable. Conselho de bolso no registro.

**Conferência:** licença lida inteira (73 linhas); veto aplicado; binário removido e `which cass` vazio; nenhum índice criado em `~/.local/share/coding-agent-search`; nada do cass no repositório.

**Resultado:** Vetado: a licença do cass proíbe uso e hospedagem para a Anthropic e quem age por ela; binário removido; roteiro de entrada agora exige ler a licença antes de instalar; o dono pode usá-lo à mão no Mac

