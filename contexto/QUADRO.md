# Quadro de avisos: o que o dono acabou de pedir

> **Todo agente e toda conversa lê este quadro antes de trabalhar** (regra do dono, 22/11/2026: "depois de cada pedido, SEMPRE informe todo mundo do que está acontecendo, crie um contexto a partir disso e alimente todos"). Quem atende o pedido escreve aqui, no topo, e apaga o mais antigo: ficam os 5 últimos. O histórico inteiro está em [`CONTEXTO-HISTORICO.md`](../CONTEXTO-HISTORICO.md).

## Agora

- **O computador do dono é um PC com Windows** (23/11), não Mac: a MinoAI roda nele pelo WSL; as menções a Mac foram corrigidas (A10) e o `checar.py` barra a volta. Noite: só aprendizado autônomo (ficha `0144`). **Desde 23/11, toda ficha fecha com `**O que aprendi:** papel: lição` (ou `nada novo`)**: o `fechar` grava no seu `contexto/<papel>.md` e em `pedidos/LICOES.md`; lição de veto e de prova sai por `pedido.py licao` (`pedidos/LEIA-ME.md`, "A ficha").

## 23/11 · Avisos automáticos e trava de comandos (everything-claude-code)

- **O dono pediu:** "levar e terminar tudo"; avisos automáticos "esse e o contador"; travar npx, npm install, npm ci e rm -rf: "sim".
- **Todos (conversa principal):** cada conversa já abre com as fichas abertas, o "## Agora" deste quadro e o começo do `ULTIMO.md` (`ferramentas/abrir-sessao.py`); passou de 30 arquivos, vem o aviso de dividir; `.md` novo fora do git lembra o `resumos.py`. Nada disso bloqueia. Os agentes seguem lendo o quadro pelo próprio arquivo.
- **Todos:** `npx`, `npm install`, `npm ci` e `rm -rf` estão negados no `.claude/settings.json`; tirar só com ficha.
- **Maestro, testador-de-paginas:** mexeu na calculadora, rode `node ebook/vendas/testar-calculadora.cjs`; divergência vai ao Arquiteto e ao Revisor, sem ajustar o teste.

## 22/11 · cass vetado; fechar ficha não apaga mais; lições do Maestro

- **O dono pediu:** integrar o cass (busca nas conversas dos agentes). **Vetado pela licença** (nega direitos à Anthropic e à OpenAI e proíbe hospedar e executar para elas): não usar. O dono pode usá-lo à mão no computador dele.
- **Todos:** ferramenta nova: nada se baixa, instala ou roda antes da ficha e do veto, e a licença é lida inteira (`CONSELHO.md`, seção 6; convivência 13). Arquivo de agente mudado vale já; `CLAUDE.md`, na próxima conversa.
- **Maestro:** `pedido.py fechar` apagava o que vinha depois do "Resultado" (consertado e testado no `checar.py`); as lições dele estão em [`maestro.md`](maestro.md).

## 22/11 · Veto com régua; memes atemporais; convivência

- **O dono pediu:** plano vetado pelo time várias vezes e pelo Fable uma; nota em cada veto e repreensão quando não for relevante; regras de convivência quando houver erro de sintonia; memes brasileiros atemporais em toda busca de referência.
- **Todos:** régua do veto em `pedidos/LEIA-ME.md`; regras em [`CONVIVENCIA.md`](CONVIVENCIA.md) (12 até agora). Nota abaixo de 4 vira lição no seu contexto.
- **Pesquisador, Diretor, Editor:** memes brasileiros atemporais em toda busca, com a coluna "dá para recriar em anúncio?".

## 22/11 · Tempo livre deixa a equipe mais inteligente

- **O dono pediu:** sem projeto concreto, deixar os agentes e a equipe mais inteligentes.
- **Todos:** rotina L1 a L6 em `pedidos/PLANO.md` ("Tempo livre"). Cada contexto ganhou a seção "Lições": erro de auditoria ou correção do dono entra lá.
- **Redator, Estrategista, Pesquisador, Supervisor, Ajudante:** lista curta de ferramentas (custa um terço por chamada). Na próxima conversa, confirme que vê as suas.
