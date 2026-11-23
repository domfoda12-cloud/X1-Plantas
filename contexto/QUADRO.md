# Quadro de avisos: o que o dono acabou de pedir

> **Todo agente e toda conversa lê este quadro antes de trabalhar** (regra do dono, 22/11/2026: "depois de cada pedido, SEMPRE informe todo mundo do que está acontecendo, crie um contexto a partir disso e alimente todos"). Quem atende o pedido escreve aqui, no topo, e apaga o mais antigo: ficam os 5 últimos. O histórico inteiro está em [`CONTEXTO-HISTORICO.md`](../CONTEXTO-HISTORICO.md).

## Agora

- **O computador do dono é um PC com Windows** (23/11), não Mac: a MinoAI roda nele pelo WSL; as menções a Mac foram corrigidas (A10) e o `checar.py` barra a volta. Noite: só aprendizado autônomo (ficha `0144`). **Desde 23/11, toda ficha fecha com `**O que aprendi:** papel: lição` (ou `nada novo`)**: o `fechar` grava no seu `contexto/<papel>.md` e em `pedidos/LICOES.md`; lição de veto e de prova sai por `pedido.py licao` (`pedidos/LEIA-ME.md`, "A ficha").

## 23/11 · Design system da marca

- **O dono pediu:** tirar o design system do código e montar um novo. **Feito:** artefato "X1 Plantas" (privado, https://claude.ai/artifact/FMbvtEZcoKTyGbQzXTZDPw): 45 cores (papel, tela clara e escura, lote, cômodos), as 3 fontes, espaços, raios, logos, os 4 ícones e o guia da marca em português.
- **Designer e Editor:** antes de peça nova, leia o `README.md` do artefato (cor, tipo, o que não fazer). Fonte continua sendo o código: `ebook/gerador/livro.css` e `ebook/visual/plano-visual.html`; mudou lá, refaça o artefato.
- **Arquiteto:** o rótulo RUA e o texto AMPLIAÇÃO do `livro.py` dão 4,4:1, pouco abaixo de 4,5:1; vale escurecer numa próxima geração.

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
