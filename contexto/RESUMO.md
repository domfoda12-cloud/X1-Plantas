# Resumo: Contexto por papel

> O que cada agente precisa saber, o quadro de avisos e os prompts do dono. **Leia este resumo primeiro**; abra um documento inteiro só quando a tarefa pedir. Índice geral: [`INDICE.md`](../INDICE.md). Quem lê: todos.

## O essencial

<!-- essencial: escrito à mão, o gerador não apaga -->
- Leia o quadro antes de trabalhar. Quem atende um pedido do dono escreve no topo e apaga o mais antigo: ficam os 5 últimos (`QUADRO.md`).
- Trabalhe e envie na `main`, com `git pull --rebase` antes; a `planta-de-casas-anuncio` acabou (`QUADRO.md`).
- Regra do dono: confira todo número contra a fonte antes de repassar (`QUADRO.md`).
- OpenArt não é proibido: cada uso pede o "sim" do dono, com resumo e custo antes (`QUADRO.md`, `diretor.md`).
- O Diretor (MinoAI Frontier) dá a ideia principal de todo conteúdo e opina primeiro nele; o Maestro é a conversa principal, que decide (`diretor.md`, `EQUIPE.md`).
- A C01 foi redesenhada (50 m²) e é o modelo; o material antigo dela não vale, use `ebook/visual/3d/C01.jpg`. As outras 23 esperam o dono (`QUADRO.md`, `arquiteto.md`).
- O dono reprovou o arranjo das 24 plantas. O método novo está em `ebook/referencias/ARQUITETO.md` (seção "Apostila 2 do Arquiteto: como arquiteto de verdade arma uma planta"); refazer espera ele dizer quais e quando (`arquiteto.md`).
- Imagens 2D dos posts desatualizadas: C03, E04, F02, F05, S03, S09 e a C01 redesenhada (`designer.md`, `arquiteto.md`).
- A frente de vídeo foi aberta pelo dono em 21/11. Toda instrução dele sobre vídeo fica em `video/VIDEO.md` (seção "Vídeo: tudo o que o dono pediu (não se perde)"). O convite (F03) e o principal (E07) são rascunhos e não passaram pelo Revisor (`editor-video.md`).
- O selo "Imagem ilustrativa" saiu dos vídeos; continua em imagem parada. O aviso "Planta de referência…" continua obrigatório (`revisor-de-risco.md`).
- Em aberto com o dono: título, preço, garantia, bônus, 12 ou 24 plantas, contato do parceiro; PLANTA ou LOTE no comentário. R$ 67 e 7 dias não são fato (`estrategista.md`, `redator.md`).
- O que liga um pedido ao outro (nove fios) e o que o dono exige dos vídeos, com o que é firme e o que é leitura nossa: `dono/IDEIAS-GERAIS.md`; o porquê de cada prompt: `pedidos/historico/intencoes/` (`dono/IDEIAS-GERAIS.md`).
- O que o dono escreveu, palavra por palavra, está em `pedidos/historico/PROMPTS.md`; na dúvida sobre um pedido, leia o trecho da data (`pedidos/historico/PROMPTS.md`).
- Documentos que se contradizem estão listados em `dono/TEXTOS-DESATUALIZADOS.md`: enquanto o item estiver lá, vale a regra mais recente (`dono/TEXTOS-DESATUALIZADOS.md`).
<!-- /essencial -->

## Os 20 documentos

### [Conversa da equipe](CONVERSA.md)

Dono, 26/11/2026: "faca eles interagem uns com os outros como amigos/colegas de trabalho, ver essa interacao me parece interessante". Cada agente lê as últimas 10 falas ao começar e fecha o relatório com `Falas:` (1 a 3 falas curtas). O Paydon copia para cá e para o Canteiro (documento `tipo:…

Seções: Falas.

Tamanho: 1378 palavras.

### [Regras de convivência da equipe](CONVIVENCIA.md)

Dono, 22/11/2026: "se ver algum erro de sintonia, não sinta medo em criar alguma regra de convivência para cobrir o erro; apenas faça um relatório e me fale depois". O Maestro cria a regra na hora, escreve aqui (o erro visto, a regra, quem muda) e conta ao dono no fim da tarefa. Todo agente lê esta…

Tamanho: 759 palavras.

### [A equipe: quem faz o quê e o que cada um acrescenta](EQUIPE.md)

Dono, 22/11/2026: cada agente sabe a sua função e o que acrescentar a cada prompt; todos com o mesmo entendimento; tudo junto e organizado; gastando o mínimo de token e tempo. Agente: `.claude/agents/<nome>.md` e `contexto/<nome>.md`. Skills de cada um: `ECOSSISTEMA.md`, seção 2b.

Seções: A cada prompt; Os papéis; Nomes e conversa; Veto; Fronteiras; Economia; Tempo livre; Prompt sem papel.

Tamanho: 723 palavras.

### [Placar do veto (gerado: não edite)](PLACAR.md)

Saída de `python3 ferramentas/placar.py`. Quem chama um veto cola no pedido a linha do agente. Nota = a que o Maestro deu ao veto pela régua, de 0 a 5 (a do maestro é dele para si mesmo); n = quantas vezes foi medido; com n menor que 5, nenhuma regra muda por causa do número. Prova = erros…

Tamanho: 442 palavras.

### [Quadro de avisos: o que o dono acabou de pedir](QUADRO.md)

Todo agente e toda conversa lê este quadro antes de trabalhar (regra do dono, 22/11/2026: "depois de cada pedido, SEMPRE informe todo mundo do que está acontecendo, crie um contexto a partir disso e alimente todos"). Quem atende o pedido escreve aqui, no topo, e apaga o mais antigo: ficam os 5…

Seções: 26/11 · O e-book vai ter a identidade da Placa (Canteiro, cartão n1; ficha `2026-11-25-1613`); 26/11 · Funil do sócio simulado, textos novos em rascunho (fila da noite, item 6; ficha `2026-11-26-0058`); 26/11 · O lado do sol estava espelhado (fila da noite, item 3; ficha `2026-11-26-0114`); 26/11 · Pasta `contexto/` enxuta (fila da noite, item 11; ficha `2026-11-26-0114`); 26/11 · A equipe tem nome e conversa (ficha `2026-11-26-0116`).

Tamanho: 719 palavras.

### [Contexto do Ajudante](ajudante.md)

Só o que importa para este papel. Se a tarefa tocar o projeto, leia antes o quadro. Você é o modelo mais barato do projeto e existe para o dono não gastar modelo caro com tarefa simples.

Seções: Decisões do dono que valem para você; Em aberto com você; Leia barato; Lições.

Tamanho: 170 palavras.

### [Contexto do Arquiteto](arquiteto.md)

Só o que importa para este papel. Antes de trabalhar, leia o quadro. O resumo geral está em `CONTEXTO.md`; o histórico completo, em `CONTEXTO-HISTORICO.md` (abra só se precisar de um detalhe antigo). O resumo da última tarefa: `entregas/ULTIMO.md`, só se a sua tarefa continua a anterior.

Seções: Decisões do dono que valem para você; Em aberto com você; Onde olhar; Leia barato; Lições.

Tamanho: 583 palavras.

### [Contexto do Designer](designer.md)

Só o que importa para este papel. Antes de trabalhar, leia o quadro. O resumo geral está em `CONTEXTO.md`; o histórico completo, em `CONTEXTO-HISTORICO.md` (abra só se precisar de um detalhe antigo). O resumo da última tarefa: `entregas/ULTIMO.md`, só se a sua tarefa continua a anterior.

Seções: Decisões do dono que valem para você; Em aberto com você; Onde olhar; Leia barato; Lições.

Tamanho: 518 palavras.

### [Contexto do Diretor (MinoAI Frontier)](diretor.md)

Só o que importa para este papel. Antes de trabalhar, leia o quadro. Resumo geral em `CONTEXTO.md`; histórico em `CONTEXTO-HISTORICO.md`. O Diretor não tem arquivo de agente: a opinião dele sai das ferramentas da MinoAI Frontier, citando a fonte, chamadas pelo Maestro, pelo Designer ou pelo Editor…

Seções: Decisões do dono que valem para você; Em aberto com você; Onde olhar; Leia barato; Lições.

Tamanho: 357 palavras.

### [As ideias gerais do projeto: o que liga um pedido ao outro](dono/IDEIAS-GERAIS.md)

Escrito pelo Fable em 22/11/2026, depois de reler todos os prompts do dono com a pergunta "por que ele pediu, e qual o objetivo?". É leitura nossa, não fala dele. O porquê de cada prompt está em `intencoes/`; as palavras dele, em `PROMPTS.md` e em `video/VIDEO.md`. Toda ficha de pedido diz qual…

Seções: A ideia central; Os nove fios; O que isso exige dos vídeos (prioridade dele agora); Perguntas que só o dono responde; O que não deu para saber.

Tamanho: 1121 palavras.

### [Perfil do dono e a voz do Paydon](dono/PERFIL.md)

Montado em 26/11/2026 (fila da noite, item 7) a partir das falas e correções do dono (`pedidos/historico/PROMPTS.md`, lições em `contexto/maestro.md` e `pedidos/LICOES.md`). Só jeito de trabalhar, nenhum dado pessoal (nada de nome, conta, lugar ou vida dele). Quem lê: o Paydon, antes de responder;…

Seções: Como ele trabalha; O que irrita e o que agrada; A voz do Paydon com ele.

Tamanho: 609 palavras.

### [O que ainda não bate: pendências depois da limpeza de 22/11/2026](dono/TEXTOS-DESATUALIZADOS.md)

Em 22/11/2026 quatro agentes leram todos os documentos e acharam cerca de 60 contradições. Três agentes no Opus resolveram as que dependiam só de texto (a regra mais recente do dono vence; texto de venda só promete o que existe; documento superado foi apagado). Aqui ficou só o que depende do dono,…

Seções: Decisões do dono (os textos estão com o campo entre colchetes, esperando); Revisor de risco; Já revisado em 22/11 (apagar quando conferir que ficou certo); Imagem e vídeo que ainda mostram a casa velha (texto já corrigido); Para o Revisor e o dono (achados da auditoria de 22/11, sem veredito); Ainda não conferido.

Tamanho: 701 palavras.

### [Contexto do Editor de vídeo](editor-video.md)

Só o que importa para este papel. Antes de trabalhar, leia o quadro. Resumo geral: `CONTEXTO.md`; histórico, só para detalhe antigo: `CONTEXTO-HISTORICO.md`; última tarefa, se a sua continua: `entregas/ULTIMO.md`.

Seções: Decisões do dono que valem para você; Em aberto com você; Onde olhar; Leia barato; Lições.

Tamanho: 527 palavras.

### [Contexto do Estrategista](estrategista.md)

Só o que importa para este papel. Antes de trabalhar, leia o quadro. O resumo geral está em `CONTEXTO.md`; o histórico completo, em `CONTEXTO-HISTORICO.md` (abra só se precisar de um detalhe antigo). O resumo da última tarefa: `entregas/ULTIMO.md`, só se a sua tarefa continua a anterior.

Seções: Decisões do dono que valem para você; Em aberto com você; Onde olhar; Leia barato; Lições.

Tamanho: 538 palavras.

### [Contexto do Maestro (a conversa principal)](maestro.md)

O Maestro é a conversa principal (Opus): decide, rege a equipe, escreve as fichas e o resumo de passagem (dono, 22/11/2026). Antes de trabalhar, o quadro; a equipe, `EQUIPE.md`; as regras de pedido, `../pedidos/LEIA-ME.md`.

Seções: Decisões do dono que valem para você; Lições.

Tamanho: 1044 palavras.

### [Contexto do Pesquisador](pesquisador.md)

Só o que importa para este papel. Antes de trabalhar, leia o quadro. O resumo geral está em `CONTEXTO.md`; o histórico completo, em `CONTEXTO-HISTORICO.md` (abra só se precisar de um detalhe antigo). O resumo da última tarefa: `entregas/ULTIMO.md`, só se a sua tarefa continua a anterior.

Seções: Decisões do dono que valem para você; Em aberto com você; Onde olhar; Leia barato; Lições.

Tamanho: 392 palavras.

### [Contexto do Planejador](planejador.md)

Só o que importa para este papel. Leia antes o quadro. Você diz o passo a passo: o que fazer agora, o que vem depois e o que espera o dono. Desde 26/11 você também separa um monte grande em grupos pequenos. Você não executa: propõe; não move nem apaga.

Seções: Decisões do dono que valem para você; Em aberto com você; Leia barato; Lições.

Tamanho: 839 palavras.

### [Contexto do Redator](redator.md)

Só o que importa para este papel; as regras fixas estão no seu arquivo de agente. Antes de trabalhar, leia o quadro. Resumo geral: `CONTEXTO.md`; histórico, só para detalhe antigo: `CONTEXTO-HISTORICO.md`.

Seções: Antes de mandar ao Revisor, confira (e diga que conferiu); Em aberto com você; Leia barato; Lições.

Tamanho: 643 palavras.

### [Contexto do Revisor de risco](revisor-de-risco.md)

Só o que importa para este papel. Antes de trabalhar, leia o quadro. O resumo geral está em `CONTEXTO.md`; o histórico completo, em `CONTEXTO-HISTORICO.md` (abra só se precisar de um detalhe antigo). O resumo da última tarefa: `entregas/ULTIMO.md`, só se a sua tarefa continua a anterior.

Seções: Decisões do dono que valem para você; Em aberto com você; Decisão do dono (22/11/2026); Onde olhar; Leia barato; Lições.

Tamanho: 615 palavras.

### [Contexto do Supervisor (Fable)](supervisor.md)

Só o que importa para este papel. Antes de trabalhar, leia o quadro.

Seções: Decisões do dono que valem para você; Em aberto com você; Leia barato; Lições.

Tamanho: 235 palavras.
