# Quadro de avisos: o que o dono acabou de pedir

> **Todo agente e toda conversa lê este quadro antes de trabalhar** (regra do dono, 22/11/2026: "depois de cada pedido, SEMPRE informe todo mundo do que está acontecendo, crie um contexto a partir disso e alimente todos"). Quem atende o pedido escreve aqui, no topo, e apaga o mais antigo: ficam os 5 últimos. O histórico inteiro está em [`CONTEXTO-HISTORICO.md`](../CONTEXTO-HISTORICO.md).

## Agora

- **Peça livre a pedido do dono** (24/11): ele quis ver algo fora do projeto, feito do zero; saiu a "Revoada" (bando de pássaros simulado; link na ficha `2026-11-24-08..-peca-livre`). Não muda nada para nenhum papel.
- **A vitrine em texto não serviu** (24/11): o dono quer peça bonita de ver; saiu a casa 3D que se constrói na tela (link na ficha `2026-11-24-07..-vitrine-bonita`). Lição para todos: "cool" é para ver e mexer, não para ler.
- **Vitrine para um amigo do dono** (24/11): ele pediu um artifact para mostrar o sistema; saiu "A Obra do X1-Plantas" (privado, link na ficha `2026-11-24-0646`). Não muda nada no e-book nem no trabalho de nenhum papel. Sem comentário novo no quadro de tarefas às 06:46 UTC: a fila segue esperando as decisões dele.
- **O computador do dono é um PC com Windows** (23/11), não Mac: a MinoAI roda nele pelo WSL; as menções a Mac foram corrigidas (A10) e o `checar.py` barra a volta. Noite: só aprendizado autônomo (ficha `0144`). **Desde 23/11, toda ficha fecha com `**O que aprendi:** papel: lição` (ou `nada novo`)**: o `fechar` grava no seu `contexto/<papel>.md` e em `pedidos/LICOES.md`; lição de veto e de prova sai por `pedido.py licao` (`pedidos/LEIA-ME.md`, "A ficha").
- **Prévia do e-book não grava mais o PDF oficial** (24/11): `livro.py --previa <pasta>` e `--conferir` geram numa pasta temporária e não tocam em `ebook/saida/` nem na calculadora; o PDF oficial e a calculadora só saem com `python3 ebook/gerador/livro.py` puro.

## 23/11 · Lançamento com 3 casas; título, preço e entrega decididos

- **O dono pediu:** refazer o e-book com 3 casas (Casa Compacta com hall, Casa Fita com 2 quartos, Família Compacta), "capriche bem nessas 3". Título **"Antes do primeiro tijolo"**; R$ 47 x R$ 67 em semanas alternadas; Pix direto no WhatsApp; entrega por link do Drive; garantia de 7 dias da entrega do link. Tudo em [`decisoes-do-dono-2026-11-23.md`](../pedidos/anexos/decisoes-do-dono-2026-11-23.md).
- **Todos:** a C01 agora tem **51 m², com hall** (não 50). E03 (2 quartos, lote 5 x 25) e F01 novas são oficiais. Em aberto com o dono: a amostra grátis. O dono acompanha pelo quadro de tarefas (ficha `1946-quadro`).
- **Arquiteto, Designer:** a 3D não espelha mais; refazer a imagem de cada casa. **Redator:** dados do vendedor no Pix (Decreto 7.962). **Júri:** regras novas em `CONSELHO.md` 5b.

## 22/11 · cass vetado; fechar ficha não apaga mais; lições do Maestro

- **O dono pediu:** integrar o cass (busca nas conversas dos agentes). **Vetado pela licença** (nega direitos à Anthropic e à OpenAI e proíbe hospedar e executar para elas): não usar. O dono pode usá-lo à mão no computador dele.
- **Todos:** ferramenta nova: nada se baixa, instala ou roda antes da ficha e do veto, e a licença é lida inteira (`CONSELHO.md`, seção 6; convivência 13). Arquivo de agente mudado vale já; `CLAUDE.md`, na próxima conversa.
- **Maestro:** `pedido.py fechar` apagava o que vinha depois do "Resultado" (consertado e testado no `checar.py`); as lições dele estão em [`maestro.md`](maestro.md).
