# Quadro de avisos: o que o dono acabou de pedir

> **Todo agente e toda conversa lê este quadro antes de trabalhar** (regra do dono, 22/11/2026: "depois de cada pedido, SEMPRE informe todo mundo do que está acontecendo, crie um contexto a partir disso e alimente todos"). Quem atende o pedido escreve aqui, no topo, e apaga o mais antigo: ficam os 5 últimos. O histórico inteiro está em [`CONTEXTO-HISTORICO.md`](../CONTEXTO-HISTORICO.md).

## Agora

- **Pedido grande do dono** (24/11, ficha `2026-11-24-1119`): casas cômodo a cômodo (Arquiteto), visita 3D (feita), Canteiro reformado como lugar de trabalho (abas Hoje, Decisões, Problemas, Plano, Quadro; ele responde por botão), auditoria das regras (feita: 13 de 32 sem mecanismo), skills novas (pesquisa feita). **Respostas dele no quadro:** vende com CPF; a tarefa de hora em hora continua; e-book com uma parte por casa e uma parte geral; quer @ e bio com humor pelo absurdo. **Ele avisou: não baixar a qualidade em troca de tokens;** os limites de tamanho esperam a decisão dele.
- **Preço e título, respostas do dono no quadro** (24/11): **R$ 47 na primeira semana e o PDF não fala de preço** (só no WhatsApp; o `checar.py` confere). **Título:** ele quer 3 opções novas no lugar de "Antes do primeiro tijolo"; o Redator escreve, o título atual fica até ele escolher. Nenhuma peça põe preço no PDF.
- **Dois papéis novos, pedido do dono** (24/11): `planejador` (passo a passo: agora, depois, esperando o dono; dono do `pedidos/PLANO.md`) e `organizador` (separa um monte em grupos de 3 a 7; só propõe). **Para todos:** trabalho com mais de 3 passos pede o plano ao `planejador` antes; monte misturado vai ao `organizador`. Nenhum dos dois executa nem decide pelo dono.
- **O computador do dono é um PC com Windows** (23/11), não Mac: a MinoAI roda nele pelo WSL; as menções a Mac foram corrigidas (A10) e o `checar.py` barra a volta. Noite: só aprendizado autônomo (ficha `0144`). **Desde 23/11, toda ficha fecha com `**O que aprendi:** papel: lição` (ou `nada novo`)**: o `fechar` grava no seu `contexto/<papel>.md` e em `pedidos/LICOES.md`; lição de veto e de prova sai por `pedido.py licao` (`pedidos/LEIA-ME.md`, "A ficha").
- **Prévia do e-book não grava mais o PDF oficial** (24/11): `livro.py --previa <pasta>` e `--conferir` geram numa pasta temporária e não tocam em `ebook/saida/` nem na calculadora; o PDF oficial e a calculadora só saem com `python3 ebook/gerador/livro.py` puro.

## 23/11 · Lançamento com 3 casas; título, preço e entrega decididos

- **O dono pediu:** refazer o e-book com 3 casas (Casa Compacta com hall, Casa Fita com 2 quartos, Família Compacta), "capriche bem nessas 3". Título **"Antes do primeiro tijolo"**; R$ 47 x R$ 67 em semanas alternadas; Pix direto no WhatsApp; entrega por link do Drive; garantia de 7 dias da entrega do link. Tudo em [`decisoes-do-dono-2026-11-23.md`](../pedidos/anexos/decisoes-do-dono-2026-11-23.md).
- **Todos:** a C01 agora tem **51 m², com hall** (não 50). E03 (2 quartos, lote 5 x 25) e F01 novas são oficiais. Em aberto com o dono: a amostra grátis. O dono acompanha pelo quadro de tarefas (ficha `1946-quadro`).
- **Arquiteto, Designer:** a 3D não espelha mais; refazer a imagem de cada casa. **Redator:** dados do vendedor no Pix (Decreto 7.962). **Júri:** regras novas em `CONSELHO.md` 5b.
