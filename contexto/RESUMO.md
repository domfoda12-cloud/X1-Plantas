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
- O que liga um pedido ao outro (nove fios) e o que o dono exige dos vídeos, com o que é firme e o que é leitura nossa: `dono/IDEIAS-GERAIS.md`; o porquê de cada prompt: `dono/intencoes/` (`dono/IDEIAS-GERAIS.md`).
- O que o dono escreveu, palavra por palavra, está em `dono/PROMPTS.md`; na dúvida sobre um pedido, leia o trecho da data (`dono/PROMPTS.md`).
- Documentos que se contradizem estão listados em `dono/TEXTOS-DESATUALIZADOS.md`: enquanto o item estiver lá, vale a regra mais recente (`dono/TEXTOS-DESATUALIZADOS.md`).
<!-- /essencial -->

## Os 22 documentos

### [Regras de convivência da equipe](CONVIVENCIA.md)

Dono, 22/11/2026: "se ver algum erro de sintonia, não sinta medo em criar alguma regra de convivência para cobrir o erro; apenas faça um relatório e me fale depois". O Maestro cria a regra na hora, escreve aqui (o erro visto, a regra, quem muda) e conta ao dono no fim da tarefa. Todo agente lê esta…

Tamanho: 759 palavras.

### [A equipe: quem faz o quê e o que cada um acrescenta](EQUIPE.md)

Dono, 22/11/2026: cada agente sabe a sua função e o que acrescentar a cada prompt; todos com o mesmo entendimento; tudo junto e organizado; gastando o mínimo de token e tempo. Agente: `.claude/agents/<nome>.md` e `contexto/<nome>.md`. Skills de cada um: `ECOSSISTEMA.md`, seção 2b.

Seções: A cada prompt; Os papéis; Veto; Fronteiras; Economia; Tempo livre; Prompt sem papel.

Tamanho: 623 palavras.

### [Placar do veto (gerado: não edite)](PLACAR.md)

Saída de `python3 ferramentas/placar.py`. Quem chama um veto cola no pedido a linha do agente. Nota = a que o Maestro deu ao veto pela régua, de 0 a 5 (a do maestro é dele para si mesmo); n = quantas vezes foi medido; com n menor que 5, nenhuma regra muda por causa do número. Prova = erros…

Tamanho: 442 palavras.

### [Quadro de avisos: o que o dono acabou de pedir](QUADRO.md)

Todo agente e toda conversa lê este quadro antes de trabalhar (regra do dono, 22/11/2026: "depois de cada pedido, SEMPRE informe todo mundo do que está acontecendo, crie um contexto a partir disso e alimente todos"). Quem atende o pedido escreve aqui, no topo, e apaga o mais antigo: ficam os 5…

Seções: 26/11 · Noite de autonomia: melhorar cada detalhe (ficha `2026-11-26-0114`); 24 e 25/11 · Fechamento de três pedidos (fichas `2026-11-24-2043`, `2026-11-24-2046`, `2026-11-25-1544`); 25/11 · Júri mais estrito e a segunda olhada (fichas `2026-11-25-1625` e `2026-11-25-1623`); 25/11 · Identidade visual forte em tudo, antes do reset (ficha `2026-11-25-1613`); 25/11 · Tudo pronto para o reset; Instagram de IA com repositório próprio (ficha `2026-11-25-1612`); 24/11 · O e-book mostra a dor e dá a solução (ficha `2026-11-24-2130`).

Tamanho: 969 palavras.

### [Contexto do Ajudante](ajudante.md)

Só o que importa para este papel. Se a tarefa tocar o projeto, leia antes o quadro. Você é o modelo mais barato do projeto e existe para o dono não gastar modelo caro com tarefa simples.

Seções: Decisões do dono que valem para você; Em aberto com você; Leia barato; Lições.

Tamanho: 170 palavras.

### [Contexto do Arquiteto](arquiteto.md)

Só o que importa para este papel. Antes de trabalhar, leia o quadro. O resumo geral está em `CONTEXTO.md`; o histórico completo, em `CONTEXTO-HISTORICO.md` (abra só se precisar de um detalhe antigo). O resumo da última tarefa: `entregas/ULTIMO.md`, só se a sua tarefa continua a anterior.

Seções: Decisões do dono que valem para você; Em aberto com você; Onde olhar; Leia barato; Lições.

Tamanho: 540 palavras.

### [Contexto do Designer](designer.md)

Só o que importa para este papel. Antes de trabalhar, leia o quadro. O resumo geral está em `CONTEXTO.md`; o histórico completo, em `CONTEXTO-HISTORICO.md` (abra só se precisar de um detalhe antigo). O resumo da última tarefa: `entregas/ULTIMO.md`, só se a sua tarefa continua a anterior.

Seções: Decisões do dono que valem para você; Em aberto com você; Onde olhar; Leia barato; Lições.

Tamanho: 406 palavras.

### [Contexto do Diretor (MinoAI Frontier)](diretor.md)

Só o que importa para este papel. Antes de trabalhar, leia o quadro. Resumo geral em `CONTEXTO.md`; histórico em `CONTEXTO-HISTORICO.md`. O Diretor não tem arquivo de agente: a opinião dele sai das ferramentas da MinoAI Frontier, citando a fonte, chamadas pelo Maestro, pelo Designer ou pelo Editor…

Seções: Decisões do dono que valem para você; Em aberto com você; Onde olhar; Leia barato; Lições.

Tamanho: 357 palavras.

### [As ideias gerais do projeto: o que liga um pedido ao outro](dono/IDEIAS-GERAIS.md)

Escrito pelo Fable em 22/11/2026, depois de reler todos os prompts do dono com a pergunta "por que ele pediu, e qual o objetivo?". É leitura nossa, não fala dele. O porquê de cada prompt está em `intencoes/`; as palavras dele, em `PROMPTS.md` e em `video/VIDEO.md`. Toda ficha de pedido diz qual…

Seções: A ideia central; Os nove fios; O que isso exige dos vídeos (prioridade dele agora); Perguntas que só o dono responde; O que não deu para saber.

Tamanho: 1121 palavras.

### [Os prompts do dono, palavra por palavra](dono/PROMPTS.md)

O que o dono escreveu na conversa principal do projeto, na ordem e sem correção. Serve para tirar dúvida sobre o que ele realmente pediu: o `CONTEXTO.md` e o `QUADRO.md` são resumos, e resumo perde nuance. Leia o trecho da data que interessa, não o arquivo inteiro. Quem atende um pedido novo…

Seções: 16/11/2026; 18/11/2026; 19/11/2026; 20/11/2026; 21/11/2026; 22/11/2026.

Tamanho: 3509 palavras.

### [Retrospectiva: o que foi feito no e-book e nos vídeos, o que o dono reclamou, o que funcionou](dono/RETROSPECTIVA.md)

Escrito em 22/11/2026 a pedido do dono: "Quero que faça uma leitura de cada trabalho feito no e-book e vídeos, veja o que foi reclamado, o que funcionou, e refaça tudo do zero assim que o limite reiniciar". Ficha:…

Seções: E-book; Vídeos; Imagens e 3D; O que se repete; Plano para refazer do zero; O que esta leitura não conseguiu avaliar.

Tamanho: 4681 palavras.

### [O que ainda não bate: pendências depois da limpeza de 22/11/2026](dono/TEXTOS-DESATUALIZADOS.md)

Em 22/11/2026 quatro agentes leram todos os documentos e acharam cerca de 60 contradições. Três agentes no Opus resolveram as que dependiam só de texto (a regra mais recente do dono vence; texto de venda só promete o que existe; documento superado foi apagado). Aqui ficou só o que depende do dono,…

Seções: Decisões do dono (os textos estão com o campo entre colchetes, esperando); Revisor de risco; Já revisado em 22/11 (apagar quando conferir que ficou certo); Imagem e vídeo que ainda mostram a casa velha (texto já corrigido); Para o Revisor e o dono (achados da auditoria de 22/11, sem veredito); Ainda não conferido.

Tamanho: 701 palavras.

### [O porquê dos prompts de 16 a 20/11/2026](dono/intencoes/2026-11-16-a-20.md)

Leitura nossa (interpretação), não fala do dono. As palavras dele estão em `../PROMPTS.md`. Pergunta passada em cada prompt: por que essa mudança foi pedida, ou o que ele quer descobrir, e qual o objetivo dele?

Seções: 16/11 · Começo do produto, ferramentas de vídeo e as primeiras referências; 18/11 · O produto vira catálogo e o projeto ganha pastas; 19/11 · MinoAI no comando, roteiro do lançamento e ferramentas de pesquisa; 20/11 · E-book do rascunho 1, Conselho, OpenArt, qualidade e contexto; Padrões deste período.

Tamanho: 5945 palavras.

### [O porquê dos prompts de 21 e 22/11/2026](dono/intencoes/2026-11-21-a-22.md)

Leitura nossa (interpretação), não fala do dono. As palavras dele estão em `../PROMPTS.md` e em `video/VIDEO.md` (seção "Vídeo: tudo o que o dono pediu (não se perde)"). Pergunta passada em cada prompt: por que essa mudança foi pedida, ou o que ele quer descobrir, e qual o objetivo dele?

Seções: Parte 1 · Produção criativa (vídeo do WhatsApp, vídeo do anúncio, Instagram); Parte 2 · Sistema e organização (branches, índice, resumos, pedidos, modelos); Parte 3 · O que ele quer ver no vídeo, juntando tudo.

Tamanho: 6829 palavras.

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

Tamanho: 670 palavras.

### [Contexto do Pesquisador](pesquisador.md)

Só o que importa para este papel. Antes de trabalhar, leia o quadro. O resumo geral está em `CONTEXTO.md`; o histórico completo, em `CONTEXTO-HISTORICO.md` (abra só se precisar de um detalhe antigo). O resumo da última tarefa: `entregas/ULTIMO.md`, só se a sua tarefa continua a anterior.

Seções: Decisões do dono que valem para você; Em aberto com você; Onde olhar; Leia barato; Lições.

Tamanho: 392 palavras.

### [Contexto do Planejador](planejador.md)

Só o que importa para este papel. Leia antes o quadro. Você diz o passo a passo: o que fazer agora, o que vem depois e o que espera o dono. Desde 26/11 você também separa um monte grande em grupos pequenos (era o organizador). Você não executa: propõe; não move nem apaga.

Seções: Decisões do dono que valem para você; Em aberto com você; Leia barato; Lições.

Tamanho: 836 palavras.

### [Contexto do Redator](redator.md)

Só o que importa para este papel. Antes de trabalhar, leia o quadro. O resumo geral está em `CONTEXTO.md`; o histórico completo, em `CONTEXTO-HISTORICO.md` (abra só se precisar de um detalhe antigo). O resumo da última tarefa: `entregas/ULTIMO.md`, só se a sua tarefa continua a anterior.

Seções: Decisões do dono que valem para você; Em aberto com você; Onde olhar; Leia barato; Lições.

Tamanho: 433 palavras.

### [Contexto do Revisor de risco](revisor-de-risco.md)

Só o que importa para este papel. Antes de trabalhar, leia o quadro. O resumo geral está em `CONTEXTO.md`; o histórico completo, em `CONTEXTO-HISTORICO.md` (abra só se precisar de um detalhe antigo). O resumo da última tarefa: `entregas/ULTIMO.md`, só se a sua tarefa continua a anterior.

Seções: Decisões do dono que valem para você; Em aberto com você; Decisão do dono (22/11/2026); Onde olhar; Leia barato; Lições.

Tamanho: 579 palavras.

### [Contexto do Supervisor (Fable)](supervisor.md)

Só o que importa para este papel. Antes de trabalhar, leia o quadro.

Seções: Decisões do dono que valem para você; Em aberto com você; Leia barato; Lições.

Tamanho: 235 palavras.
