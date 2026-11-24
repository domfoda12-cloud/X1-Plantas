# Quadro de avisos: o que o dono acabou de pedir

> **Todo agente e toda conversa lê este quadro antes de trabalhar** (regra do dono, 22/11/2026: "depois de cada pedido, SEMPRE informe todo mundo do que está acontecendo, crie um contexto a partir disso e alimente todos"). Quem atende o pedido escreve aqui, no topo, e apaga o mais antigo: ficam os 5 últimos. O histórico inteiro está em [`CONTEXTO-HISTORICO.md`](../CONTEXTO-HISTORICO.md).

## 24/11 · O e-book mostra a dor e dá a solução (ficha `2026-11-24-2130`)

- **O dono pediu:** "No conteudo do pdf no geral quero saber mostrar a dor que o usuario tem ou teria, e dar a solucao pra ele".
- **O que mudou:** critério novo para todo o conteúdo do PDF: cada página nomeia uma dor real do comprador e entrega a saída. Primeiro sai o mapa página por página; texto só muda depois de o dono ver.
- **Todos:** dor só da pesquisa do comprador ou dos dados da casa, nunca inventada nem com medo exagerado. **Planejador:** faz o mapa. **Redator:** reescreve só o que o dono marcar, com plano. **Designer:** o formato das páginas não muda sem pedido.

## 24/11 · Redator sempre com o Planejador; todos planejam antes de fazer (ficha `2026-11-24-2119`)

- **O dono pediu:** "O redator sempre com a ajuda do planejador, quero todo mundo planejando as coisas muito bem".
- **O que mudou:** todo texto do Redator começa por um plano (para quem, o que precisa conter, fonte de cada número, o que depende do dono, "pronto quando"), montado ou conferido pelo Planejador; texto sem plano não vai ao Revisor. Convivência, linha 17.
- **Todos:** plano curto antes de fazer; trabalho com mais de 3 passos passa pelo Planejador. **Redator:** plano no começo do anexo. **Planejador:** monta ou confere o plano de cada texto. **Maestro:** manda o plano junto do pedido ao Redator.

## 24/11 · Terminar o e-book, um por um (ficha `2026-11-24-2050`)

- **O dono pediu:** "Quero terminar o ebook o que falta. Falta uma separacao exata do que estamos trabalhando e vamos implementar pro cliente, temos que terminar tudo 1 por 1 comecando pelo E book".
- **O que mudou:** existe a separação em `pedidos/anexos/o-que-vai-ao-cliente-2026-11-24.md`: o que o cliente recebe, o que é só ferramenta nossa, e os 10 passos que faltam para o e-book.
- **Todos:** só se trabalha nos 10 passos do e-book, na ordem, um por vez. Sistema, Instagram, vitrines e vídeo esperam. **Planejador:** a ordem do topo do plano segue essa tabela.

## 24/11 · Visita 3D mais realista: guardada para depois (ficha `2026-11-24-2046`)

- **O dono pediu:** gosta da visita 3D e quer saber se dá para usar modelos mais realistas; "Dont start working on it if yes, i think it costs a lot of credit, save it for later".
- **O que mudou:** nada no produto. O pedido ficou guardado; ninguém trabalha nele até ele mandar.
- **Todos:** não mexer na visita 3D agora. Quando ele liberar, toda biblioteca de modelos passa pelo roteiro de entrada (licença lida, veto) antes de baixar qualquer coisa.

## 24/11 · Desacelerar: uma tarefa por vez (ficha `2026-11-24-2043`)

- **O dono pediu:** "Slow down on it, if we work on all the tasks at the same time, none will be done". E perguntou o que mais gastou o limite de uso da última janela.
- **O que mudou:** acabou a regra de 23/11 de rodar 4 a 6 agentes em paralelo para gastar o limite. Agora é UMA tarefa principal de cada vez, até o fim (feita, conferida, salva), com no máximo 2 agentes juntos (quem faz e quem confere). A tarefa de hora em hora foi reescrita com isso. A tarefa atual é o D20 (cômodo a cômodo das 3 casas no gerador, prévia).
- **Todos:** ninguém abre tarefa nova enquanto a atual não fechou; "Agora" tem uma tarefa, nunca zero. **Planejador:** escreve no topo do plano a ordem das próximas 5, uma por vez. **Maestro:** não lança agente em paralelo fora do par fazer/conferir.

## Agora

- **Regra nova do dono** (24/11): **"Agora" do `pedidos/PLANO.md` nunca fica vazio, e agente fora do projeto trabalha nele mesmo, no sistema ou em outro agente.** Pediu também a visita 3D com mais móveis, quadros e personalização (ficha `2026-11-24-1144`).
- **Pedido grande do dono** (24/11, ficha `2026-11-24-1119`): casas cômodo a cômodo (Arquiteto), visita 3D (feita), Canteiro reformado como lugar de trabalho (abas Hoje, Decisões, Problemas, Plano, Quadro; ele responde por botão), auditoria das regras (feita: 13 de 32 sem mecanismo), skills novas (pesquisa feita). **Respostas dele no quadro:** vende com CPF; a tarefa de hora em hora continua; e-book com uma parte por casa e uma parte geral; quer @ e bio com humor pelo absurdo. **Ele avisou: não baixar a qualidade em troca de tokens;** os limites de tamanho esperam a decisão dele.
- **Preço e título, respostas do dono no quadro** (24/11): **R$ 47 na primeira semana e o PDF não fala de preço** (só no WhatsApp; o `checar.py` confere). **Título:** ele quer 3 opções novas no lugar de "Antes do primeiro tijolo"; o Redator escreve, o título atual fica até ele escolher. Nenhuma peça põe preço no PDF.
- **Dois papéis novos, pedido do dono** (24/11): `planejador` (passo a passo: agora, depois, esperando o dono; dono do `pedidos/PLANO.md`) e `organizador` (separa um monte em grupos de 3 a 7; só propõe). **Para todos:** trabalho com mais de 3 passos pede o plano ao `planejador` antes; monte misturado vai ao `organizador`. Nenhum dos dois executa nem decide pelo dono.
- **O computador do dono é um PC com Windows** (23/11), não Mac: a MinoAI roda nele pelo WSL; as menções a Mac foram corrigidas (A10) e o `checar.py` barra a volta. Noite: só aprendizado autônomo (ficha `0144`). **Desde 23/11, toda ficha fecha com `**O que aprendi:** papel: lição` (ou `nada novo`)**: o `fechar` grava no seu `contexto/<papel>.md` e em `pedidos/LICOES.md`; lição de veto e de prova sai por `pedido.py licao` (`pedidos/LEIA-ME.md`, "A ficha").

## 23/11 · Lançamento com 3 casas; título, preço e entrega decididos

- **O dono pediu:** refazer o e-book com 3 casas (Casa Compacta com hall, Casa Fita com 2 quartos, Família Compacta), "capriche bem nessas 3". Título **"Antes do primeiro tijolo"**; R$ 47 x R$ 67 em semanas alternadas; Pix direto no WhatsApp; entrega por link do Drive; garantia de 7 dias da entrega do link. Tudo em [`decisoes-do-dono-2026-11-23.md`](../pedidos/anexos/decisoes-do-dono-2026-11-23.md).
- **Todos:** a C01 agora tem **51 m², com hall** (não 50). E03 (2 quartos, lote 5 x 25) e F01 novas são oficiais. Em aberto com o dono: a amostra grátis. O dono acompanha pelo quadro de tarefas (ficha `1946-quadro`).
- **Arquiteto, Designer:** a 3D não espelha mais; refazer a imagem de cada casa. **Redator:** dados do vendedor no Pix (Decreto 7.962). **Júri:** regras novas em `CONSELHO.md` 5b.
