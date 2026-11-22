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

> Seções abaixo restauradas em 22/11 depois da auditoria 4: o `pedido.py fechar` apagava tudo o que vinha depois do "Resultado" (consertado, com teste no `checar.py`).

## Plano (que foi ao veto)

| # | Tipo | Passo | Quem |
|---|---|---|---|
| 1 | P | Ler o que ele roda (README, comandos, o que lê e escreve, rede) **e a licença** | Maestro |
| 2 | P | Veto de privacidade | `revisor-de-risco` |
| 3 | P | Instalar e rodar uma vez | Maestro (**não foi feito na ordem: ver "Erro do Maestro"**) |
| 4 | G | `pesquisa.py buscar` também nas conversas, se o cass existir | Maestro (NÃO do Estrategista) |
| 5 | P | Regra de uso | Maestro |
| 6 | P | Guia do Mac | Maestro |
| 7 | P | Registro em ECOSSISTEMA e CONSELHO | Maestro |

## O que ele roda (README do repositório)

"Alpha"; compila com Rust nightly; licença MIT com adendo; instala por Homebrew (binário pronto), Scoop ou um `install.sh` remoto (não usado). Lê as conversas locais de 34 ferramentas de agente (Claude Code em `~/.claude/projects`, Codex, Cursor...), de **todos** os projetos; escreve um banco em `~/.local/share/coding-agent-search/`; diz que nada sai da máquina; embedder externo opcional e desligado; modo `--robot`/`--json` para agentes.

## Veto

- **Estrategista (5/5):** SIM, SE; NÃO ao passo 4 (conversa bruta no caderno curado polui e expõe dado pessoal; na nuvem não acha nada); medir no Mac antes (3 perguntas que o dono já repetiu); ler o adendo da licença antes de instalar.
- **Revisor (5/5):** SE; a licença decide ("se restringe o uso por agentes dessas empresas, é VETO"); `install.sh` remoto e embedder externo: VETO; para o passo 4: só leitura, nada gravado, só o caminho do X1-Plantas, trecho de até 200 caracteres com e-mail, telefone, CPF e chaves mascarados, sem caminho do arquivo da sessão, teste com trecho falso; regra do passo 5: "A busca nas conversas serve para lembrar o que o dono decidiu sobre o X1-Plantas, não para copiar. Ao repositório só vai a decisão, reescrita em uma linha, com a data e 'conversa anterior'. Nunca vai trecho literal, dado de pessoa, senha, chave, token, dado de outro projeto, assunto pessoal ou caminho de arquivo. Na dúvida, pergunte ao dono. O banco do cass nunca entra no repositório."

## A licença (`LICENSE`, 73 linhas, lida inteira)

- Linhas 18 a 22: "Restricted Parties" são a OpenAI, a Anthropic, as afiliadas e quem age "on behalf of, for the benefit of, or under the direction of" elas (ali, "agent" é representante).
- Linhas 24 a 27: nenhum direito para elas, salvo permissão escrita do autor.
- Linhas 29 a 32: proibido "host, make available, or otherwise permit access to the Software [...] to or for any Restricted Party".
- Linhas 34 a 39: "use" inclui "executing", "indexing" e incorporar em "pipeline for [...] automated systems".
- **Leitura cautelosa nossa, não parecer jurídico.** O que sustenta o veto é hospedar e executar em máquina da Anthropic (29 a 32) e pôr num sistema automático (34 a 39). Três casos: **nuvem da Anthropic (esta sessão): veto claro**; **Claude Code no Mac do dono: dúvida, então não usamos**; **o dono, à mão, no Mac: pode** (ele não é parte restrita).

## Erro do Maestro

Antes desta ficha o dono pediu, nesta ordem: "Can you run this code for me? brew install dicklesworthstone/tap/cass" (21:50:16), "cargo install coding_agent_session_search", "Check it", "It should be similar to what I've been trying to do" e "Try to integrate cass in the system". Às 21:50:58 o Maestro rodou `cargo install --git <repositório>`, que começou a **baixar o código-fonte** (544 MB em `~/.cargo/git`; parou em "Updating git repository", nada compilado nem aberto) e foi morto às 21:53:08. Também leu a fórmula do Homebrew. 

Ordem real (registro da conversa): 21:50 a primeira tentativa de instalar (cargo), antes de a ficha existir (21:51); 21:53:08 o binário v0.11.0 instalado (checksum da fórmula do Homebrew conferido) e **`cass --version` executado uma vez**, com o veto ainda rodando; 21:53:12 chega o Revisor. Não foi "contra o pedido do Revisor": foi **sem esperar o veto**. Removido logo depois (binário, arquivo baixado; nenhum índice criado); as cópias do README e da LICENSE na pasta de rascunho também foram apagadas (a licença manda destruir as cópias).

## Qualidade do veto

| Agente | Nota | Por quê |
|---|---|---|
| Estrategista | 5 | Alavanca honesta, NÃO ao passo 4 com motivo, pediu a licença |
| Revisor | 5 | Fez da licença a condição; regras de privacidade exatas |
| Maestro | 1 | Começou a instalar antes da ficha e rodou o programa antes do veto |

## Para o dono (objetivo dele sem saída ainda)

Ele quer uma memória que alcance o que disse a qualquer agente. Opções: (a) ele usa o cass à mão no Mac; (b) pedir permissão escrita ao autor (a licença prevê, linhas 24 a 27); (c) uma busca nossa, simples, nos registros do Claude Code (`~/.claude/projects/*.jsonl`), com as regras de privacidade do Revisor (o Fable fez a auditoria 4 com um script de 20 linhas assim). Pergunta feita ao dono.
