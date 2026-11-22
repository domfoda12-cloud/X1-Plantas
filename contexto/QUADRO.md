# Quadro de avisos: o que o dono acabou de pedir

> **Todo agente e toda conversa lê este quadro antes de trabalhar** (regra do dono, 22/11/2026: "depois de cada pedido, SEMPRE informe todo mundo do que está acontecendo, crie um contexto a partir disso e alimente todos"). Quem atende o pedido escreve aqui, no topo, e apaga o mais antigo: ficam os 5 últimos. O histórico inteiro está em [`CONTEXTO-HISTORICO.md`](../CONTEXTO-HISTORICO.md).

## 22/11 · A equipe organizada: quem faz o quê e o que cada um acrescenta

- **O dono pediu:** organizar os agentes: cada um sabe a sua função e, a cada prompt, o que acrescentar para o resultado dele; tudo resumido junto; com o tempo, um sistema que ajude em qualquer coisa.
- **Todos:** o mapa está em [`EQUIPE.md`](EQUIPE.md). A ficha passa a ter, em "Quem executa", uma linha por agente: o que ele acrescenta. O que não é seu, devolva dizendo de quem é; agente não chama agente.
- **Designer e Editor:** imagem parada é do Designer; o que se move é do Editor.
- **Arquiteto, Estrategista e Pesquisador:** o Pesquisador acha a fonte; o Arquiteto (norma, planta) ou o Estrategista (mercado, preço) conclui. O Estrategista não usa mais Sonnet.

## 22/11 · Pense antes; Python 3.11; auditorias 1 e 2

- **O dono pediu:** pensar antes de qualquer trabalho, mais quanto maior ele for; corrigir o erro do gerador no Python 3.11 (revisão do PR #3).
- **Todos:** regra "pense antes, na medida do trabalho" em `pedidos/LEIA-ME.md`; esforço padrão "high". `ebook/gerador/livro.py` abre no Python 3.11.
- **Redator e parceiro:** a E07 saiu das plantas grátis (5 agora); o PDF ainda tem campo pendente e não vai ao cliente (o `checar.py` avisa).

## 22/11 · Opus responde, Fable audita; mídias antigas apagadas; pergunte sempre

- **O dono pediu:** Opus na conversa e Fable de socorro e auditoria; apagar vídeos e renders (guardar o último vídeo e a informação); reler tudo para refazer do zero; perguntar sempre; organizar os arquivos na próxima sessão.
- **Todos:** chame o `supervisor` (Fable) quando travar ou errar. Pergunte a si mesmo o que foi pedido, o que supõe e o que não sabe; ao dono, no fim, sem travar ([`pedidos/LEIA-ME.md`](../pedidos/LEIA-ME.md)).
- **Editor de vídeo e Designer:** saíram vídeos, clipes, renders 3D e 2D, as imagens dos carrosséis e o código do vídeo antigo (voltam com `git checkout 079dae7 -- <caminho>`); ficaram o convite, o principal de 21/11, a voz do dono e a trilha. O `calendario.md` tem o post 5 parado por isso. Antes de refazer, leia [`dono/RETROSPECTIVA.md`](dono/RETROSPECTIVA.md).
- **Todos:** a próxima sessão começa organizando os arquivos (ficha em `pedidos/`); depois, refazer do zero.
