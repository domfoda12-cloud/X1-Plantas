# Registro dos resumos de passagem

> Todos os resumos de passagem, do mais antigo ao mais novo. O mais recente também fica em `ULTIMO.md`, que é o que os agentes leem. Juntado em 22/11/2026 (ficha de organizar os arquivos): cada seção é um documento antigo, inteiro.

<!-- era: contexto/entregas/REGISTRO.md -->
## 2026-11-20-contexto-enxuto

# Resumo de passagem: contexto enxuto, AgentScope e toolkit de demonstração

**Tarefa:** reduzir o contexto que cada agente carrega, avaliar o AgentScope e o product-demo-agent-toolkit.
**Feito:** `CONTEXTO.md` virou resumo, com o histórico em `CONTEXTO-HISTORICO.md`; um arquivo por agente em `contexto/`; resumos de passagem em `contexto/entregas/`; `CLAUDE.md` por área em `ebook/`, `video/` e `ferramentas/`; limites de tamanho conferidos no `checar.py`; AgentScope e toolkit registrados no `ECOSSISTEMA.md`.
**Como conferir:** `python3 ferramentas/checar.py` (confere o roteiro e os limites de tamanho).
**Não feito / ressalva:** o toolkit não foi instalado; a proteção automática do Claude Code bloqueou.
**Decisão do dono pendente:** instalar ou não o toolkit (precisa da permissão ou de rodar o comando ele mesmo).
**Próximo passo:** se ele disser sim, instalar só no projeto, pôr a seção "Neste projeto" e o "Prompt de entrada" nas 2 skills e registrar no Conselho (Editor de vídeo).

<!-- era: contexto/entregas/REGISTRO.md -->
## 2026-11-20-ebook-rascunho-1

# Resumo de passagem: e-book, rascunho 1 (20/11/2026)

**Tarefa:** fechar o rascunho 1 do e-book "Que casa cabe no seu lote?" (24 casas, 61 páginas, mais 6 PDFs de planta grátis).
**Feito:**
- Revisão final do Conselho (Revisor, Arquiteto, Redator) aplicada: paredes com espessura (`ferramentas/plantas.py`), desenhos de C03, E04, F02, S03 e S09 corrigidos (`ebook/plantas/projetos.py`), promessas vetadas retiradas (`ebook/gerador/paginas.py`, `livro.py`, `ebook/fichas/textos.py`).
- A casa em 3D entrou em cada página (`ebook/visual/3d/`, do motor `ferramentas/planta3d.py`); o sofá passou a ter três tamanhos.
- Porta e janelas da planta 2D vêm do motor 3D, iguais às da vista da rua; a foto da F01 perdeu duas aberturas falsas.
**Como conferir:** `python3 ferramentas/checar.py` (tudo certo) e `python3 ebook/gerador/livro.py` (sem aviso de página estourada).
**Não feito / ressalva:** o validador ainda não mede ventilação cruzada; 19 casas têm banheiro abaixo de 1,10 m livres; fotos de fachada só em 4 casas.
**Decisão do dono pendente:** título, preço, bônus, contato do parceiro, promessa de atualização; aplicar as correções da auditoria (calculadora do parceiro, `checar.py` sem o PDF).
**Próximo passo:** corrigir a calculadora do parceiro (`ebook/vendas/calculadora-lote.html`) gerando os dados a partir do validador.

<!-- era: contexto/entregas/REGISTRO.md -->
## 2026-11-21-1200-revisao-aplicada

# Resumo de passagem: os 26 achados da revisão de 21/11 aplicados

**Tarefa:** aplicar todos os achados da revisão de código e de instruções dos agentes.
**Feito (código):** parede para pátio, jardim e passagem aberta medida certo (`plantas.py`); `n0` único; ampliação conferida pelo validador; "erros evitados" sem troca automática; sofá medido na parede em que encosta; imagens sem ampliar (PDF de 30 para 22,6 MB); calculadora do parceiro reescrita pelo `livro.py`; `gerar.py` apagado; novo `ferramentas/imagens3d.py`.
**Feito (plantas):** E04 com só o quarto casal abrindo para o pátio (as janelas não ficam frente a frente); banheiro da F05 mais largo (a casa passou a 91 m²).
**Feito (instruções):** estado "em aberto" só em `contexto/<papel>.md`; Revisor só lê; skills registram em `CONTEXTO-HISTORICO.md`; skills de relatório não fazem commit; um só resumo por tarefa, copiado para este `ULTIMO.md`.
**Como conferir:** `python3 ferramentas/checar.py` (agora gera dados, fichas, 3D, PDF e calculadora, testa a regra das paredes e falha com página estourada).
**Não feito / ressalva:** as funções antigas de página em `ebook/gerador/paginas.py` continuam no arquivo, sem uso; imagens 2D dos posts seguem desatualizadas.
**Decisão do dono pendente:** ver "Em aberto" no `CONTEXTO.md`.
**Próximo passo:** frente de animações, quando o dono abrir.

<!-- era: contexto/entregas/REGISTRO.md -->
## 2026-11-21-1510-videos-principal-e-previa

**Tarefa:** fazer o vídeo principal (reel e anúncio) e a prévia do e-book para o parceiro mandar no WhatsApp.
**Feito:** `video/montar.py` (monta vídeo vertical de um roteiro em JSON: cenas, texto, aviso legal, compressão).
`video/roteiros/principal.json` e `previa-whatsapp.json` (texto e ordem das cenas).
`video/broll/clipes/` (8 clipes do OpenArt, Kling 3.0, e a animação 3D da C01 do motor novo) e `video/broll/paginas/` (4 páginas do e-book).
Saídas: `video/saida/principal/x1-plantas-principal.mp4` (29 s, 14,2 MB) e `video/saida/previa-whatsapp/x1-plantas-previa.mp4` (19 s, 1,2 MB).
**Como conferir:** `python3 video/montar.py video/roteiros/principal.json` monta de novo; assistir aos dois arquivos.
**Não feito / ressalva:** sem música e sem locução (a faixa licenciada entra na edição da MinoAI Frontier, no Mac do dono). O Revisor de risco aprovou os roteiros; os vídeos prontos foram conferidos por quem montou, não por ele. Os 5 anúncios antigos (`saida/v1` a `v5`) continuam com o 3D velho.
**Decisão do dono pendente:** aprovar os dois vídeos; palavra da chamada (PLANTA ou LOTE); publicar.
**Próximo passo:** ouvir o dono sobre os vídeos. OpenArt tem 115 créditos: não dá para outro clipe.

<!-- era: contexto/entregas/REGISTRO.md -->
## 2026-11-21-2340-video-e07-logo-musica

**Tarefa:** logo, música de 128 BPM e vídeo principal novo da E07 com OpenArt (liberado de novo pelo dono), mais o roteiro da versão 3 "Grupo da família".
**Feito:** `marca/logo/` (6 logos; recomendada a de perfil, BIG + dois D formando a casa). `video/musica/` (trilha original "BIG BIG", 30 s, sintetizada).
`video/PRINCIPAL-E07.md` (plano quadro a quadro e decisão do Conselho). `video/principal-e07/` (blueprint animado, montador, imagens).
`video/saida/principal-e07/x1-plantas-e07.mp4`: versão 2 (15 s, 11,4 MB), aprovada pelo Revisor depois de um veto por marcas na v1.
Roteiro da v3 e prompt para o roteirista (WhatsApp e Instagram) num documento do dono: https://claude.ai/artifact/Lr8SvUJPmvcZ5JAZvzywNU
**Como conferir:** `node video/principal-e07/render_blueprint.cjs` e `node video/principal-e07/montar_e07.cjs` montam de novo (precisam dos clipes em `principal-e07/openart/`, que não vão para o git; estão na pasta "X1 · Vídeo principal" do OpenArt).
**Não feito / ressalva:** v3 parada por ordem do dono, esperando ele aprovar o roteiro. Já feitos para ela: abertura com o balão do Tio Zé (no `blueprint.html`) e 3 imagens (almoço de domingo, cozinha com onigiri, fachada com luz rosa de GTA). Falta animar 3 cenas (~525 créditos), montar e passar pelo Revisor (camisa do menino no almoço; nada de marca do jogo). A música não foi ouvida por ninguém ainda.
**Decisão do dono pendente:** aprovar o roteiro da v3; escolher o logo; palavra da chamada (PLANTA ou LOTE); reel orgânico ou anúncio; publicar.
**Próximo passo:** ler a resposta do dono no documento; se aprovado, animar as 3 cenas no Kling 3 Omni e trocar as cenas no `montar_e07.cjs`. OpenArt: 21.849 créditos no começo da v3.

<!-- era: contexto/entregas/REGISTRO.md -->
## 2026-11-22-0010-anuncio-ebook-locucao

**Tarefa:** anúncio do e-book com a casa E07, agora com locução do dono (26 s), para a MinoAI Frontier editar no Mac.
**Feito:** `video/principal-e07/kit-minoai/` (20 MB): 9 clipes comprimidos, balão do tio, aviso legal e selo como camadas paradas, logo, música e `LEIA-ME.md` com o roteiro aprovado, o plano de corte e a frase para dizer à MinoAI.
`video/principal-e07/PROMPTS.md`: prompts de movimento de câmera (Kling 3 Omni) e de imagem, para repetir em outra casa.
Documento do dono (roteiro, prompt do roteirista, registro, prompts): https://claude.ai/artifact/Lr8SvUJPmvcZ5JAZvzywNU
Antes: logo em `marca/logo/`, trilha em `video/musica/`, vídeo sem voz versão 2 em `video/saida/principal-e07/` (aprovado pelo Revisor).
**Como conferir:** abrir o `LEIA-ME.md` do pacote; os clipes tocam direto. `python3 ferramentas/checar.py`.
**Atualização 22/11:** o dono mandou a voz (texto original dele). Vídeo com locução montado aqui por `video/principal-e07/montar_locucao.py`: `video/saida/principal-e07/x1-plantas-e07-locucao.mp4` (25,3 s, 8,1 MB) e `-whatsapp.mp4` (2,3 MB). Dois cortes no áudio por veto do Revisor ("mandei construir, olha o resultado" e "até provar que dava certo"); blueprint sem áreas por cômodo.
**Não feito / ressalva:** o Revisor só libera se o dono confirmar que o tio e a mensagem existem e que "volto pro Brasil em algumas semanas" é verdade; senão, regravar a abertura ("Todo grupo de família tem um tio que manda isso:") e a frase do Brasil. A abertura da gravação parece engolida ("Meu tio" em 0,2 s). A edição fina da MinoAI no Mac continua opcional, com o pacote. Ele não abriu o PDF da planta grátis da E07 (conferir se não sai com "[título]" e "[preço]"). Ninguém ouviu a trilha ainda.
**Decisão do dono pendente:** "o tio" ou "meu tio" (só se for verdade); confirmar "tô voltando pro Brasil"; PLANTA ou LOTE; logo; publicar (o Instagram ainda não existe, e o envio da planta precisa funcionar antes).
**Próximo passo:** receber a gravação da voz ou o vídeo editado e passar pelo Revisor. Regra nova do dono: recados no meio do trabalho entram todos juntos na mesma entrega.
**Parado em 22/11 por ordem do dono:** ele quer tirar o selo "Imagem ilustrativa" e considera erro a E07 ter os 3 quartos em fila. Regra nova: antes de qualquer vídeo ou crédito do OpenArt, mandar o resumo da produção e a lista de instruções, e esperar a confirmação dos dois. Não gerar nada antes disso.

<!-- era: contexto/entregas/REGISTRO.md -->
## 2026-11-22-1200-arquiteto-estuda-arranjo

**Tarefa:** fazer o Arquiteto estudar arranjo de planta em fontes que arquitetos usam (o dono reprovou o último layout).
**Feito:** `ebook/referencias/ARQUITETO.md` (apostila 2: diagnóstico das 24 plantas, o que ensinam a SEHAB-SP, a casa de referência da CAR-BA e a pesquisa da UFRGS, método de 10 passos).
`.claude/agents/arquiteto.md` e `contexto/arquiteto.md` (arranjo antes da medida; ler a apostila 2 e olhar a prévia antes de opinar).
`CONTEXTO.md` e `CONTEXTO-HISTORICO.md` (pedido registrado).
**Como conferir:** abrir a apostila 2; comparar `ebook/plantas/previas/E01.png` e `C01.png` com a seção 1.
**Não feito / ressalva:** nenhuma planta mudou. Não lidos: manual da CDHU (site fora do ar), ArchDaily, concursosdeprojeto.org, Vitruvius. O validador ainda não aponta arranjo ruim.
**Decisão do dono pendente:** quais casas refazer e quando (sugestão: série E, compactas, F02). Refazer reabre o e-book: dados, 3D, PDF, calculadora e posts.
**Próximo passo:** com o "sim" do dono, redesenhar a E01 pelo método da seção 6 e mostrar a prévia antes de seguir para as outras.

<!-- era: contexto/entregas/REGISTRO.md -->
## 2026-11-22-1200-escaneamento

**Tarefa:** pôr no vídeo principal a sequência de "escaneamento" que o dono descreveu e garantir que as ordens dele sobre vídeo não se percam.
**Feito:** `video/VIDEO.md` (toda ordem de vídeo, com as palavras dele; leitura obrigatória).
`video/scan.py` (gera `broll/clipes/scan-e07.mp4`: cotas, malha de arame, etiquetas; números do validador).
`video/roteiros/principal-condor.json` refeito com a E07: gancho, escaneamento, casa em 3D, e-book, chamada. Sem clipe do OpenArt.
Saída: `video/saida/principal-condor/x1-plantas-principal-condor.mp4` (21 s, 7,7 MB), conferida quadro a quadro.
**Como conferir:** `python3 video/scan.py E07 && python3 video/montar.py video/roteiros/principal-condor.json`; assistir.
**Não feito / ressalva:** É RASCUNHO: a E07 está na fila do redesenho das plantas (`contexto/QUADRO.md`); não publicar antes de o dono decidir. sem música (entra no Mac). O 3D é ilustração, não "vida real". Revisor de risco não foi chamado: os textos são os já aprovados, só os números mudaram para os da E07 (validador). Cada tempo dura 0,3 s, como o dono pediu; é rápido para ler.
**Decisão do dono pendente:** aprovar a sequência; PLANTA ou LOTE; quando filma.
**Próximo passo:** ouvir o dono; mandar a lista de 8 planos para a filmagem com o celular.

<!-- era: contexto/entregas/REGISTRO.md -->
## 2026-11-22-1400-pesquisa-layouts-e-etapas

**Tarefa:** pesquisar layouts de casa popular no Brasil e os grandes passos para construir (pedido do dono, 22/11).
**Feito:** `ebook/referencias/ARQUITETO.md` (régua federal da Portaria MCID 725, nossas 24 plantas contra ela, 18 passos da obra com parte do custo, dado CAU/Datafolha, 5 ideias de uso).
`contexto/QUADRO.md` (aviso para todos), `contexto/arquiteto.md`, `CONTEXTO.md`, `CONTEXTO-HISTORICO.md`.
No mesmo dia: apostila 2 do Arquiteto (`ebook/referencias/ARQUITETO.md`), com o diagnóstico do arranjo e o método de 10 passos.
**Como conferir:** abrir a pesquisa; a tabela "nossas plantas contra a régua" sai dos dados em `ebook/plantas/dados/` (lado menor menos 12 cm).
**Não feito / ressalva:** nenhuma planta mudou e nada foi ao público. Percentuais de custo são de blog. Não lidos: guia Reforma Casa Brasil, manual da CDHU, concursos, plantas do ArchDaily.
**Decisão do dono pendente:** quais casas refazer e quando; quais das 5 ideias da seção 5 seguem.
**Próximo passo:** com o "sim" do dono, redesenhar a E01 (método da apostila 2 + régua federal) e mostrar a prévia.

<!-- era: contexto/entregas/REGISTRO.md -->
## 2026-11-22-1500-main-unica-e-compressao

**Tarefa:** destravar o projeto: tudo na `main`, arquivos comprimidos e agrupados, Graphify atualizado.
**Feito:** PR #2 aprovado (projeto inteiro na `main`); PRs #4 e #5 fechados, sem perda (tours da C06 em `video/saida/tour-c06/`).
Fotos do OpenArt em JPEG (`ebook/visual/openart/**.jpg`); `ebook/gerador/livro.py` (`arquivo_foto`) e `ferramentas/recortes.py` leem JPEG.
26 vídeos reencodados (crf 23); `video/broll/ebook-folheando.mp4` foi para `video/broll/clipes/`.
`CLAUDE.md`: `main` é a única branch de trabalho; `sistema/<assunto>` para mudança de sistema; Graphify é mapa, não pedágio; agrupar por função.
**Como conferir:** `python3 ferramentas/checar.py`; `python3 ebook/gerador/livro.py` gera o PDF com as fotos; Graphify mostra o repositório com mais de mil itens.
**Não feito / ressalva:** as camadas `.webm` com transparência não foram reencodadas (risco de perder a transparência). O histórico do git ainda guarda as versões pesadas; só a cópia de trabalho ficou leve. A foto de fachada da C01 é da casa antiga.
**Decisão do dono pendente:** apagar as branches velhas (`frente-*`, `planta-de-casas-anuncio`); arquivar as conversas antigas.
**Próximo passo:** toda conversa nova parte da `main`. Refazer a fachada da C01 nova.

<!-- era: contexto/entregas/REGISTRO.md -->
## 2026-11-22-1600-c01-redesenhada

**Tarefa:** refazer 1 planta do vídeo (C01) e preparar o uso do OpenArt (pedido do dono, 22/11).
**Feito:** `ebook/plantas/projetos.py` (C01 nova: varanda, sala e jantar, cozinha nos fundos, hall curto, banheiro de 1,69 m livres, serviço com porta para o quintal; 50 m²).
Regenerados: dados, `PLANTAS.md`, `video/src/plantas/C01.js`, `ebook/visual/3d/C01.jpg`, PDFs de `ebook/saida/`, calculadora.
`ebook/fichas/textos.py` (gancho e "para quem é" da C01), `ferramentas/checar.py` (teste das paredes usa a sala da C05).
Registros: OpenArt não é proibido, pede o "sim" do dono a cada uso (`QUADRO.md`, `VIDEO.md`, `contexto/editor-video.md`, `CONTEXTO.md`).
**Como conferir:** `python3 ferramentas/plantas.py validar C01`; página 10 de `ebook/saida/ebook.pdf`.
**Não feito / ressalva:** nada gerado no OpenArt. Posts, imagem 2D e clipes antigos da C01 desatualizados. A sala não desenha a mesa. Textos novos da C01 sem o Revisor. A E07 do escaneamento segue antiga.
**Decisão do dono pendente:** aprovar a C01 nova e o que gerar no OpenArt (com o custo).
**Próximo passo:** com o "sim", gerar a partir de `ebook/visual/3d/C01.jpg` e conferir se a imagem bate com a planta.

<!-- era: contexto/entregas/REGISTRO.md -->
## 2026-11-22-1600-modelos-limpeza-auditorias

**Tarefa:** papéis dos modelos (Opus conduz, Fable socorre e audita), limpeza de mídias, retrospectiva, regras "pense antes" e "pergunte sempre", erro do Python 3.11 e as auditorias 1 e 2.
**Feito:** `.claude/settings.json` (Opus, esforço high); agente `supervisor`; `pedidos/AUDITORIAS.md`; `ferramentas/pedido.py` avisa a hora da auditoria.
Mídias e o vídeo antigo apagados (voltam com `git checkout 079dae7 -- <caminho>`); `contexto/dono/RETROSPECTIVA.md` com o plano para refazer.
`ebook/gerador/livro.py` abre no 3.11; a E07 saiu das plantas grátis (5); o `checar.py` avisa campo pendente no PDF.
**Como conferir:** `python3 ferramentas/checar.py`; `python3 ferramentas/pedido.py listar --fechadas`; `pedidos/AUDITORIAS.md`.
**Não feito / ressalva:** as branches velhas seguem no GitHub (apagar não é permitido daqui). Vários documentos ainda citam arquivo apagado pelo nome, sem link: entram na organização (ficha aberta). Os roteiros de vídeo apontam clipes que não existem mais.
**Decisão do dono pendente:** qual era "o último vídeo"; se as imagens dos posts entravam no "apague"; qual limite ("5 horas" ou semanal); a casa para "8 m, 3 quartos"; as 8 perguntas da retrospectiva.
**Próximo passo:** a organização dos arquivos (ficha aberta em `pedidos/`), depois refazer pelo plano da retrospectiva.

<!-- era: contexto/entregas/REGISTRO.md -->
## 2026-11-22-1600-video-convite

**Tarefa:** guardar o prompt base de tomada realista com variáveis e fazer o vídeo-convite (passeio por dentro de uma casa, misturado com o estilo do principal).
**Feito:** `video/VIDEO.md` (revisão de tudo o que o dono disse sobre vídeo, prompt base com 12 variáveis, regras do convite).
`video/render-passeio.cjs` e `video/src/passeio.html` (passeio na altura dos olhos, motor próprio; caminho por casa em `CAMINHOS`).
`video/scan.py` (escaneamento; a planta agora ocupa a tela em qualquer lote). `video/montar.py` ganhou `"leve": true`.
`video/roteiros/convite.json` → `video/saida/convite/x1-plantas-convite.mp4` (26 s, F03 Casa Família, sem OpenArt).
**Como conferir:** `cd video && node render-passeio.cjs --planta F03 --vel 1.3 && cd .. && python3 video/montar.py video/roteiros/convite.json`; assistir.
**Não feito / ressalva:** é ilustração 3D, não foto, e 1080 × 1920, não 4K. Sem música (Mac). Revisor de risco não viu. O principal com a E07 segue rascunho.
**Decisão do dono pendente:** o que é "pagar por mais"; se "motor art" era o motor próprio ou o OpenArt; E07 ou outra casa no principal; quando filma.
**Próximo passo:** ouvir o dono; mandar a lista de planos para a filmagem com o celular.

<!-- era: contexto/entregas/REGISTRO.md -->
## 2026-11-22-1700-indice-resumos-e-prompts

**Tarefa:** fazer os agentes pararem de esquecer: índice, resumo barato por pasta e os prompts do dono ao alcance de todos.
**Feito:** `ferramentas/resumos.py` gera o `INDICE.md` e um `RESUMO.md` por pasta (10 categorias). "O essencial" de cada resumo é escrito à mão e o gerador não apaga.
`contexto/<agente>.md`: seção "Leia barato" com os resumos das pastas de cada papel.
`contexto/dono/PROMPTS.md`: 166 prompts do dono, palavra por palavra. `contexto/dono/TEXTOS-DESATUALIZADOS.md`: cerca de 60 contradições entre documentos.
`ferramentas/checar.py`: falha se um documento ficar fora do índice ou um resumo ficar sem "O essencial"; limite do `CLAUDE.md` subiu para 6.500.
**Como conferir:** `python3 ferramentas/resumos.py --conferir`; abrir o `INDICE.md`.
**Não feito / ressalva:** as contradições estão listadas, não corrigidas (só 3 mecânicas). Os prompts de outras conversas não entraram palavra por palavra: estão resumidos no histórico.
**Decisão do dono pendente:** garantia de 7 dias; 12 ou 24 plantas; se a retirada do selo "Imagem ilustrativa" vale para todo vídeo e para imagem parada.
**Próximo passo:** corrigir os textos que vão ao cliente (primeira seção do `TEXTOS-DESATUALIZADOS.md`), com o Revisor de risco.

<!-- era: contexto/entregas/REGISTRO.md -->
## 2026-11-22-1930-equipe-organizada

**Tarefa:** organizar os agentes: cada um sabe a função e o que acrescenta a cada prompt, tudo junto, com economia de token.
**Feito:** `contexto/EQUIPE.md` (mapa numa página, fronteiras, economia, prompt sem papel).
**Feito:** 7 agentes: ficha em `pedidos/`, "devolva o que não é seu", formato de devolução; não releem o `CLAUDE.md`; `ULTIMO.md` só se a tarefa continua.
**Feito:** imagem parada = Designer, o que se move = Editor; Arquiteto pede web ao Pesquisador; passo 2 da pesquisa nomeado; Estrategista sem "Sonnet".
**Feito:** `pedidos/LEIA-ME.md` (linha "acrescenta" na ficha), `CONSELHO.md`, 10 contextos e o quadro.
**Como conferir:** `python3 ferramentas/checar.py`; abrir `contexto/EQUIPE.md`.
**Não feito / ressalva:** modelos mantidos (escolha do dono); agente do Maestro não criado; nenhum prompt real rodou ainda pelo fluxo novo.
**Decisão do dono pendente:** criar agente `maestro`? Revisor de risco no Fable para peça final? Encurtar o lembrete do gancho?
**Próximo passo:** ficha "Organizar os arquivos" (aberta), depois a E07.

<!-- era: contexto/entregas/REGISTRO.md -->
## 2026-11-22-2000-equipe-final

**Tarefa:** equipe final: mesmo entendimento, caderno de pesquisa, Maestro (Opus) e Diretor (MinoAI), Revisor no Fable, teste com a equipe.
**Feito:** bloco "Agora" no topo do quadro; todos leem igual, chamados ou não.
**Feito:** `pesquisas/` + `ferramentas/pesquisa.py` (buscar antes da web, nova com fonte, guardas de norma, dado pessoal e arquivo); no `checar.py`.
**Feito:** Maestro = conversa principal, decide; Diretor = MinoAI, ideia do conteúdo (CLAUDE, CONSELHO, MAESTRO, PAINEL, `contexto/diretor.md`).
**Feito:** web para todos; Designer e Editor com o Diretor; skills por agente em `ECOSSISTEMA.md` 2b; Revisor no Fable na peça final; gancho de uma linha.
**Feito:** correções do teste com 6 agentes (ficha, campo "Conferência").
**Como conferir:** `python3 ferramentas/checar.py`; `python3 ferramentas/pesquisa.py buscar agente`.
**Não feito / ressalva:** agentes mudados só valem na próxima conversa; a web do Arquiteto e do Revisor não foi vista funcionando.
**Decisão do dono pendente:** página visual de skills por agente (a tabela já existe).
**Próximo passo:** na próxima conversa, chamar o Arquiteto e confirmar que ele vê WebSearch; depois a ficha "Organizar os arquivos".

<!-- era: contexto/entregas/REGISTRO.md -->
## 2026-11-22-2100-pedidos-ideias-e-contradicoes

**Tarefa:** resolver as contradições entre documentos, montar o sistema de pedidos por modelo e reler todos os prompts do dono com "por que ele pediu?".
**Feito:** `pedidos/` (regras em `LEIA-ME.md`, fila em `FILA.md`, fichas em `2026-11/`); `ferramentas/pedido.py` e `guardar-pedido.py`; gancho em `.claude/settings.json`.
Agentes com modelo no cabeçalho (Opus; `pesquisador` no Sonnet; `ajudante` novo, no Haiku).
`contexto/dono/IDEIAS-GERAIS.md` (nove fios e o que o vídeo tem de ter) e `contexto/dono/intencoes/` (o porquê de cada prompt).
Documentos corrigidos em todas as pastas; apagados `ebook/PLANO-EBOOK.md`, `ebook/fichas/C01.md`, `video/roteiro-2-tres-quartos.md` e a nota `exigencias_legais.md`.
`ferramentas/atualizar-painel.py` conta pelos arquivos; `ebook/gerador/paginas.py` sem código morto; foto antiga de fachada da C01 fora do e-book (PDF gerado de novo).
**Como conferir:** `python3 ferramentas/checar.py`; `python3 ferramentas/pedido.py listar`; abrir `contexto/dono/IDEIAS-GERAIS.md`.
**Não feito / ressalva:** imagens e vídeos ainda com a C01 antiga (lista em `contexto/dono/TEXTOS-DESATUALIZADOS.md`). O Revisor não leu os textos de cada casa, a calculadora, os posts nem os roteiros. A divisão por modelo ainda não foi provada com o Haiku.
**Decisão do dono pendente:** as seis perguntas no fim de `IDEIAS-GERAIS.md`; preço, garantia, bônus, 12 ou 24 plantas.
**Próximo passo:** com as respostas do dono, remontar a prévia do WhatsApp e o anúncio pelas exigências de `IDEIAS-GERAIS.md`.

## 2026-11-22-2030-arquivos-juntados

**Tarefa:** organizar os arquivos, etapa 1: juntar documentos lidos pelos mesmos agentes.
**Feito:** 50 documentos viraram 12 (vídeo, Instagram, referências do e-book, WhatsApp, resumos de passagem, notas jurídicas); de 138 para 100 .md.
**Feito:** cada antigo entrou inteiro como seção (`<!-- era: ... -->`); links corrigidos em 64 arquivos; `MAESTRO.md` foi para `instagram/MINOAI-FRONTIER.md`.
**Feito:** resumos de passagem num registro só (`contexto/entregas/REGISTRO.md`) + `ULTIMO.md`; `CLAUDE.md`, `MODELO.md`, `checar.py` e `resumos.py` ajustados.
**Como conferir:** `python3 ferramentas/checar.py`; nenhum link quebrado (script na ficha).
**Não feito / ressalva:** etapas 2 (código repetido) e 3 (contextos com até 3 resumos); medir o Graphify depois do push.
**Decisão do dono pendente:** nenhuma nova.
**Próximo passo:** etapa 2 da ficha `1529-organizar-os-arquivos`.
