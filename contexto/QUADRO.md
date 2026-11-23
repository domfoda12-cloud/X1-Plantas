# Quadro de avisos: o que o dono acabou de pedir

> **Todo agente e toda conversa lê este quadro antes de trabalhar** (regra do dono, 22/11/2026: "depois de cada pedido, SEMPRE informe todo mundo do que está acontecendo, crie um contexto a partir disso e alimente todos"). Quem atende o pedido escreve aqui, no topo, e apaga o mais antigo: ficam os 5 últimos. O histórico inteiro está em [`CONTEXTO-HISTORICO.md`](../CONTEXTO-HISTORICO.md).

## Agora

- **O dono NÃO tem Mac** (23/11). Tudo que diz "no Mac do dono" é suposição errada (63 menções em 22 arquivos): não planeje nada que dependa de Mac; a correção espera ele dizer que equipamento tem. Noite: só aprendizado autônomo (ficha `0144`). **Desde 23/11, toda ficha fecha com `**O que aprendi:** papel: lição` (ou `nada novo`)**: o `fechar` grava no seu `contexto/<papel>.md` e em `pedidos/LICOES.md`; lição de veto e de prova sai por `pedido.py licao` (`pedidos/LEIA-ME.md`, "A ficha").

## 22/11 · cass vetado; fechar ficha não apaga mais; lições do Maestro

- **O dono pediu:** integrar o cass (busca nas conversas dos agentes). **Vetado pela licença** (nega direitos à Anthropic e à OpenAI e proíbe hospedar e executar para elas): não usar. O dono pode usá-lo à mão no Mac.
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

## 22/11 · Plano de trabalho; consertar de vez

- **O dono pediu:** um plano passo a passo, em tarefas grandes e pequenas, com objetivo para a equipe; e "não só conserte, remende".
- **Todos:** o plano está em [`../pedidos/PLANO.md`](../pedidos/PLANO.md) (5 fases, quem faz cada tarefa). Erro achado vira regra ou conferência no `checar.py` (`pedidos/LEIA-ME.md`).
- **Todos:** o `checar.py` agora confere todos os links e no máximo 3 resumos por contexto.
