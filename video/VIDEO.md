# Vídeo: regras, pedidos do dono e conferência

> Tudo o que vale para qualquer vídeo: o guia, as instruções do dono (palavra por palavra, na seção dele) e a lista de revisão. Juntado em 22/11/2026 (ficha de organizar os arquivos): cada seção é um documento antigo, inteiro.

<!-- era: video/VIDEO.md -->
## Vídeo: o que existe hoje

> Parte do projeto X1-Plantas. Painel geral: [`../PAINEL.md`](../PAINEL.md). Regras desta pasta: [`CLAUDE.md`](CLAUDE.md). **Antes de mexer em vídeo, leia [`VIDEO.md`](VIDEO.md) inteiro.**
>
> Reorganizado em 22/11/2026 para dizer a verdade de hoje. O guia antigo do vídeo "Os R$ 1.000 do arquiteto" (teleprompter, gravação do apresentador, teste das 5 versões como reels) saiu: o vídeo usa o 3D velho da C01, o apresentador nunca gravou e o dono mudou o rumo do anúncio.

### 1. As regras que valem (dono, 22/11/2026)

- **Destino do anúncio com locução: WhatsApp e Facebook Ads**, não Instagram nem TikTok ([`ANUNCIO-LOCUCAO.md`](ANUNCIO-LOCUCAO.md), pedido 27).
- **Aviso legal pequeno, no canto da tela, parado. Sem o selo "Imagem ilustrativa"** (o dono tirou essa condição do Revisor). Em imagem parada (post, e-book) a legenda "imagem ilustrativa" continua.
- **Antes de montar vídeo ou gastar crédito do OpenArt:** mandar ao dono o resumo da produção e a lista de instruções, e esperar o "sim" dos dois. OpenArt pode, com o "sim" dele a cada uso.
- **Música:** faixa licenciada ou a trilha nossa de 128 BPM (`musica/gerar_trilha.py`), como diz o [`CLAUDE.md`](CLAUDE.md) desta pasta. Áudio dos modelos de vídeo é descartado.
- **Edição final:** MinoAI Frontier, no Mac do dono. Até 12 MB; versão do WhatsApp até 5 MB.
- **Continuam do método antigo:** texto no primeiro quadro; o narrador nunca para (só a pausa marcada no roteiro); uma ideia por cena; a imagem mostra o que a voz diz; chamada única no fim ("Comenta PLANTA").

### 2. O que está em `saida/` (22/11/2026)

Em 22/11 o dono mandou apagar os vídeos, clipes e renders para refazer do zero, guardando a informação e o último vídeo. Ficaram:

| Pasta | Arquivo | O que é |
|---|---|---|
| `convite/` | `x1-plantas-convite.mp4` | Passeio pela F03 (motor próprio, ilustração), o último feito; roteiro `roteiros/convite.json` |
| `principal/` | `x1-plantas-principal.mp4` | Principal de 21/11, com clipes do OpenArt e a C01 antiga; o último mostrado ao dono nesta conversa |

O resto (prévia do WhatsApp, principal com escaneamento, anúncio da E07 com locução, passeios da C06 e as versões `v1` a `v5`) volta pelo histórico do git se for preciso (`git checkout 079dae7 -- <caminho>`). Os roteiros em `roteiros/` apontam para clipes apagados: `montar.py` só monta de novo depois de gerar os clipes. A gravação da voz do dono está em `principal-e07/voz/`. O que refazer e em que ordem: [`../contexto/dono/RETROSPECTIVA.md`](../contexto/dono/RETROSPECTIVA.md).

### 3. Nesta pasta

| Arquivo | Para que serve |
|---|---|
| `VIDEO.md` (seção "Vídeo: tudo o que o dono pediu (não se perde)") | Tudo o que o dono pediu sobre vídeo, com as palavras dele |
| `ANUNCIO-LOCUCAO.md` (seção "Pedido do dono: anúncio do e-book com locução (ficha única)"), `ANUNCIO-LOCUCAO.md` (seção "Plano de criação: anúncio do e-book com locução, com a planta nova") | Ficha e plano do anúncio com locução (o que vale agora) |
| `PRINCIPAL-E07.md` (seção "Plano: vídeo principal "3 quartos em 8 m" (E07), quadro a quadro"), `principal-e07/` | Registro da versão de 21/11 da E07, prompts de câmera (`PROMPTS.md`) e o pacote para a MinoAI (`kit-minoai/`) |
| `PRINCIPAL-E07.md` (seção "Roteiro: vídeo de aquecimento do lançamento ("casas na mala")") | Vídeo de aquecimento do lançamento ("casas na mala"), com o roteiro original do dono |
| `REFERENCIAS.md` (seção "Referência de edição: CONDOR XIII (Payton Talbott)"), `REFERENCIAS.md` (seção "Referência: como um formato viraliza (oferta e demanda)") | Referências de edição e de formato |
| `ANUNCIO-LOCUCAO.md` (seção "Anúncios para o Facebook Ads") | Textos de anúncio por ângulo (pelo lote, erro caro, casa que cresce, pedreiro…) |
| `ANUNCIO-LOCUCAO.md` (seção "Brief criativo: anúncios de plantas de casas") | Brief dos criativos (formatos, estilo, variações) |
| `VIDEO.md` (seção "Checklist de revisão antes de subir o anúncio") | Revisão antes de subir qualquer anúncio |
| `montar.py`, `roteiros/`, `broll/` | Montador dos vídeos sem apresentador, os roteiros e as cenas |
| `scan.py`, `render-planta.cjs`, `render-passeio.cjs`, `render-rua.cjs`, `src/` | Escaneamento, 3D, passeio por dentro e vista da rua (esta foi recusada pelo dono: não é realista) |
| `musica/` | Trilha nossa de 128 BPM |

### 4. Como montar e gerar

- **Montar um vídeo sem apresentador:** `python3 video/montar.py video/roteiros/<nome>.json`. Mudou um texto? Mude no roteiro e monte de novo. O montador põe o texto, o aviso legal em todas as cenas e comprime.
- **Escaneamento:** `python3 video/scan.py ID` (números do validador). **3D da planta:** `node render-planta.cjs --planta ID` (com `--so-imagens`, só as imagens). **Passeio por dentro:** `node render-passeio.cjs --planta ID`.
- **Para rodar o código de vídeo** (dentro da pasta `video`): Node.js, ffmpeg e o Playwright com o Chromium.

```bash
npm install
```

```bash
npm install --no-save playwright
```

```bash
npx playwright install chromium
```

### 5. Decisões que ficam com o dono

- **Publicar** qualquer vídeo, e a **palavra da chamada** (PLANTA ou LOTE). Se for LOTE, troque no roteiro e monte de novo.
- **A planta prometida na chamada.** Quando o vídeo mostra uma casa e diz "essa planta", a pessoa tem de recebê-la; se a casa ainda não está no material gratuito, a chamada diz "uma planta de graça". A decisão segue em aberto no [`../CONTEXTO.md`](../CONTEXTO.md).
- **Quando o e-book tiver título** ([`../PAINEL.md`](../PAINEL.md), seção 9): a chamada passa a citar o e-book numa frase só ("Comenta PLANTA que eu te mando de graça essa planta do e-book [Título]"). Troque no roteiro e nos textos de [`ANUNCIO-LOCUCAO.md`](ANUNCIO-LOCUCAO.md#anúncios-para-o-facebook-ads).

<!-- era: video/PEDIDOS-DO-DONO.md -->
## Vídeo: tudo o que o dono pediu (não se perde)

> **Regra do dono (22/11/2026):** "Para todo vídeo, quando eu acrescentar uma informação, garanta que ela fique lá e não se perca na conversa."
> Por isso: **toda instrução dele sobre vídeo entra aqui na hora, com as palavras dele**, antes de qualquer edição. Quem edita lê este arquivo inteiro antes de mexer em roteiro ou clipe, e confere no fim se cada linha "vale" continua atendida. Nada sai daqui sem o dono mandar tirar.

### Ordens gerais (valem para todo vídeo)

Revisão de 22/11/2026, a pedido do dono ("reveja toda a nossa conversa, procure o que é de criação de vídeo e ponha no arquivo de vídeo"): entrou tudo desta conversa e tudo o que o histórico do projeto guarda sobre vídeo.

| Data | O dono disse | Estado |
|---|---|---|
| Início | Seguir o reel de referência; atenção na retenção; "o cliente precisa se interessar pelas plantas" | Vale. `instagram/MINOAI-FRONTIER.md`, `instagram/MINOAI-FRONTIER.md` |
| Início | Clipes menos travados: o blueprint azul ganhando vida | Vale como estilo do 3D próprio. O escaneamento **substitui a planta se desenhando**, mas entra depois do gancho e antes da chamada (fala do dono, seção "Sequência de escaneamento"); a abertura é o gancho |
| Início | Gancho "vou te salvar os R$ 1.000 que um arquiteto te salvaria" | Guardado como opção de gancho (`ESTRATEGIA.md`). O Revisor de risco confere antes de usar |
| Início | Narrador sempre falando, sem pausa; sempre um visual prendendo a atenção | Vale. `VIDEO.md` |
| Início | Roteiro "volto pro Brasil com casas na mala" | Guardado em `PRINCIPAL-E07.md` |
| 20/11 | "A edição de vídeo é responsabilidade [da MinoAI]" | Vale. Edição final da MinoAI Frontier, no Mac do dono |
| 20/11 | Referência de edição: CONDOR XIII ("melhor edição que já vi"); "preste muita atenção nos B-rolls e nas escolhas de música" | Vale. `REFERENCIAS.md` |
| 20/11 | "O Payton não produz música, no máximo usa remixes" | Vale como estilo de referência. **Ajustado em 21/11:** anúncio pago usa faixa licenciada (no máximo remixada) ou a trilha nossa de 128 BPM, que o próprio dono pediu (pedido 9 da ficha `ANUNCIO-LOCUCAO.md`) e o Revisor aprovou. Regra que vale: `CLAUDE.md` desta pasta |
| 20/11 | "A prioridade deve ser sempre a maior qualidade" | Vale. Peça final na melhor configuração |
| 21/11 | A prévia "vai para o cliente no WhatsApp, não é o principal, mas faça os dois" | Feitos: `saida/previa-whatsapp/` e `saida/principal/` |
| 21/11 | "O vídeo também deve ficar comprimido" | Vale |
| 21/11 | "Mande o Editor fazer o vídeo com estes vídeos de referência" (escolheu o estilo CONDOR) | Vale. `roteiros/principal-condor.json` |
| 21/11 | "Não use OpenArt" | Corrigido pelo dono em 22/11 (linha abaixo) |
| 22/11 | "Use o OPENART, que eu NÃO proibi, apenas necessita permissão para ser usado" | Vale. OpenArt pode, **com o "sim" do dono a cada uso** (resumo e custo antes) |
| 21/11 | "Quero o vídeo realista feito pelo motor Claude, não OpenArt"; "quero REALISTA"; "parece vida real" | Vale. O motor 3D próprio é ilustração, não foto; a vista da rua (`render-rua.cjs`) foi recusada por isso |
| 22/11 | Vai filmar com o celular: "consigo filmar daqui a alguns dias, mas não por enquanto" | Aguardando. O Editor recomendou filmar e deve mandar a lista de uns 8 planos de 5 s. Até lá: planta, 3D próprio e páginas do e-book |
| 22/11 | "Para todo vídeo, quando eu acrescentar uma informação, garanta que ela fique lá e não se perca na conversa" | Vale. É este arquivo |
| 22/11 | Prompt base para tomadas realistas, com umas 10 variáveis | Feito: seção "Prompt base" abaixo |
| 22/11 | "Reveja toda a nossa conversa, procure informação de criação de vídeo e ponha no arquivo de vídeo" | Feito nesta revisão |
| 22/11 | "Ao inves de um cachorro caramelo adicione esse video a lista de referencia, use o video para o video princiapl do ads/instagram" (reel https://www.instagram.com/reel/DTw4bqHE5zj/) | Vale. O reel entra em `REFERENCIAS.md` e substitui o caramelo no **principal (anúncio e Instagram)**. Ficha `2055-video-reel` |
| 22/11 | "no video do whatsapp mostre a casa pela perspectiva de um caramelo" | Vale. O vídeo do WhatsApp mostra a casa do ponto de vista de um vira-lata caramelo (câmera na altura do cachorro) |
| 22/11 | "em algum momento a camera diminua o zoom dando um efeito especial no video (you can look for one to use in the editor references)" | Vale. Um zoom out com efeito, tirado das referências de edição (kit da MinoAI e `REFERENCIAS.md`) |
| 22/11 | Onde entra o meme: "Sim, a crianca e o cachorro dancando na frente da casa" (resposta à pergunta "como gancho, nos primeiros segundos?") | Vale: o meme é o **gancho**, com uma criança e um cachorro dançando na frente da casa. Como fazer sem risco: ficha `2055-video-reel`, ramo R6 |
| 22/11 | "Sao 2 videos, 1 mostrando uma previa do que eles vao ver no ebook, outro fazendo a divulgacao do produto, o principal é a divulgacao mas a previa também é bem importante" | Vale. **Principal = divulgação do produto** (o meme como gancho); **prévia = o que a pessoa vai ver no e-book** (vai no WhatsApp, com o POV do caramelo). O principal vem primeiro; a prévia logo depois, com o mesmo cuidado |
| 22/11 | "a previa é o wpp a divulgacao é insta/ads" | Vale. **Prévia: WhatsApp. Divulgação (o principal): Instagram e Facebook Ads.** Muda a ordem anterior só para o principal; o anúncio com locução continua indo a WhatsApp e Facebook Ads |
| 22/11 | "uma crianca igual a do meme, é o caramelo também, interligando os 2 videos" | Vale o **caramelo nos dois vídeos** (liga a divulgação à prévia). A criança: igual **na cena** (idade, energia, dança, o caramelo ao lado, na frente da casa), **não na pessoa**: o menino do meme é uma pessoa real; copiar rosto, corpo ou roupa dele em anúncio é uso de imagem sem autorização (veto do Revisor, CF art. 5º, X; Código Civil art. 20). Ficha `2055-video-reel`, R6 |
| 22/11 | "Durante a procura de referencias procure memes brasileiros atemporais como esse" | Vale. Toda busca de referência inclui memes brasileiros atemporais; os achados vão ao caderno `pesquisas/video.md` |

**Em aberto, citado pelo dono e que não chegou ao Editor:** "o beat de prova que discutimos antes" (conversa anterior, provavelmente na página de chat). Se tinha mais detalhe, falta o dono repetir.

### Prompt base para tomadas realistas (22/11/2026)

Texto do dono, sem mudar:

> Using your motor art integration create a smooth cinematic real estate walkthrough, comes gliding steadily forward though each room like a professional steadicam shot, natural even lighting with warm golden tones. Realistic depth and parallax as the camera moves slow, fluid dolly motion,no shakiness or jump cuts. Seamless transitions between rooms through doorways and hallways. Clean polished high and architectural photograpfy style 4k quality, shar focus professional real estate videography, subtle motion blur on edges for cinematic smoothness. Consistent color grading throughout bright and inviting atmosphere

"Add this prompt as a pre based prompt for realistic takes, create more or less 10 variables that you can change on the prompt depending on the goal of the video."

**O prompt com as variáveis** (o que está entre chaves muda conforme o objetivo; o resto fica igual):

> Create a smooth cinematic real estate walkthrough of {CASA}. The camera {MOVIMENTO} through {PERCURSO}, like a professional steadicam shot. {LUZ}. Realistic depth and parallax as the camera moves at {VELOCIDADE}, fluid dolly motion, no shakiness or jump cuts. {TRANSICAO}. Clean, polished, high-end {ESTILO}, {FORMATO}, sharp focus, professional real estate videography, {BORRAO}. Consistent color grading throughout, {ATMOSFERA}. {PESSOAS}. {FOCO}.

| # | Variável | Padrão (as palavras do dono) | Trocas possíveis | Quando trocar |
|---|---|---|---|---|
| 1 | `{CASA}` | a casa do projeto, com o nome e os cômodos da ficha | "a 78 m² single-story Brazilian family house, 3 bedrooms"; acabamento simples de classe C | Sempre: é o que prende a tomada à planta de verdade |
| 2 | `{MOVIMENTO}` | "comes gliding steadily forward" | "pulls back slowly"; "rises like a drone"; "slides sideways" | Abertura (entrar), fim (recuar e mostrar tudo), vista do lote (drone) |
| 3 | `{PERCURSO}` | "each room" | "from the front gate to the living room"; "only the kitchen"; "living room → hallway → master suite" | Vídeo curto pede 1 a 3 cômodos; vídeo de apresentação pede a casa inteira |
| 4 | `{LUZ}` | "natural even lighting with warm golden tones" | "soft morning light"; "bright midday light"; "sunset glow through the windows" | Manhã = começo, obra, esperança; entardecer = família, casa pronta |
| 5 | `{VELOCIDADE}` | "slow" | "very slow" (detalhe); "medium" (anúncio de 15 s) | Quanto mais curto o vídeo, mais rápido o passo, sem tranco |
| 6 | `{TRANSICAO}` | "Seamless transitions between rooms through doorways and hallways" | "One continuous shot, no cuts"; "match cut from the floor plan to the room" | Corte pela planta quando o vídeo mistura planta 2D e casa |
| 7 | `{ESTILO}` | "architectural photography style" | "lived-in family home"; "magazine cover"; "construction site documentary" | Venda do sonho = revista; confiança = casa vivida, real |
| 8 | `{FORMATO}` | "4k quality" | "vertical 9:16" (reel, anúncio, WhatsApp); "16:9" (YouTube) | Sempre dizer o formato do destino |
| 9 | `{BORRAO}` | "subtle motion blur on edges for cinematic smoothness" | "no motion blur, everything crisp" | Sem borrão quando há texto ou medida para ler em cima |
| 10 | `{ATMOSFERA}` | "bright and inviting atmosphere" | "calm and cozy"; "fresh and airy"; "proud, achievement" | Conforme o sentimento do roteiro |
| 11 | `{PESSOAS}` | "No people" | "a family of four in the living room, seen from behind" | Pessoa só com cuidado: nada de rosto inventado passando por cliente real |
| 12 | `{FOCO}` | (vazio) | "linger on the kitchen counter"; "end on the bedroom window with sunlight" | Quando o roteiro fala de um detalhe: a imagem ilustra a frase |

**Como usar hoje (OpenArt só com o "sim" do dono a cada uso):**

- **No motor 3D próprio** (ilustração, não foto): `cd video && node render-passeio.cjs --planta F03`. As variáveis viram opções: percurso = lista `CAMINHOS` (ou `--caminho`), velocidade = `--vel`, luz e céu = `sol`, `ceu` e `exp` na página `src/passeio.html`, lente = `fov`, altura dos olhos = `olho`. O borrão e a cor quente entram no fim, pelo ffmpeg.
- **Na filmagem do dono com o celular:** o mesmo prompt vira instrução de filmagem (andar devagar e reto, celular na altura do peito, luz de fim de tarde, atravessar as portas sem parar).
- **No OpenArt** (o caminho que chega perto de "vida real"): só com o "sim" do dono a cada uso, com resumo e custo antes. Tomada gerada parte da nossa imagem 3D da casa (para não inventar cômodo). **Sem o selo "Imagem ilustrativa"** no vídeo (ordem do dono de 22/11, que vence a regra anterior); vale o aviso legal pequeno, no canto, parado.
- **Dúvida registrada:** "motor art integration" foi entendido primeiro como o motor 3D próprio, porque o Editor ainda não sabia da correção do dono sobre o OpenArt. É provável que ele tenha dito **OpenArt**. O passeio do motor próprio fica como rascunho e como guia de câmera; a versão realista no OpenArt espera o "sim" dele com o custo na mão.

### Próximo vídeo: o convite (22/11/2026)

Texto do dono, sem mudar:

"This is an initial video that should be extremely inviting, showing an example of what the customer can receive if he pays for more, Choose one of the house projects and make sure to add detail and keep the viewer attention with visuals"

"Do a mix of this prompt with the last made longer video"

O que isso obriga:

- É o **vídeo inicial**: o primeiro que a pessoa vê. Tem de ser **extremamente convidativo**.
- Mostra **um exemplo do que o cliente recebe se pagar por mais**.
- **Uma casa só**, escolhida entre os projetos, com **detalhe**.
- **Sempre um visual prendendo a atenção.**
- É uma **mistura** do passeio do prompt base com o último vídeo mais longo.

#### Estado

| Data | O que está feito | O que falta |
|---|---|---|
| 22/11 | **Casa escolhida: F03, Casa Família** (78 m², 3 quartos, 1 suíte, 2 banheiros, lote a partir de 11 × 15 m). Motivo: é casa de família, tem varanda, sala e cozinha abertas (bom de mostrar por dentro) e está **fora** da fila do redesenho (série E, compactas e F02). Passeio por dentro feito no motor 3D próprio (`render-passeio.cjs`, `src/passeio.html`): entra pelo jardim, varanda, sala, cozinha, corredor, suíte; movimento contínuo, luz quente, teto, borrão de movimento leve. Roteiro `roteiros/convite.json`: gancho "Todo lote é uma conta" com 11×15 em letra-janela → escaneamento da F03 (0,9 s) → passeio inteiro sem corte de imagem, com o nome e a medida de cada cômodo (números do validador) → página do e-book → chamada PLANTA. Saída: `saida/convite/x1-plantas-convite.mp4` (26 s). Sem OpenArt | **O dono dizer o que é "pagar por mais"** (qual produto ou pacote): hoje o vídeo só diz "veja por dentro" e não promete nada que não exista. O passeio é **ilustração 3D, não foto**: não chega a "fotografia de arquitetura 4K"; saiu em 1080 × 1920. Trocar por filmagem real quando o dono filmar. Música licenciada (no Mac). Revisor de risco ainda não viu |

### Vídeo principal

#### Sequência de "escaneamento" (22/11/2026): a prova no meio do vídeo

Texto do dono, sem mudar:

| Timestamp | Visual | Overlay detail |
|---|---|---|
| 0,0-0,3s | Static blueprint image, flat 2D plan | Dimension/measurement lines snap on one at a time, like CAD annotation marks appearing along the 8m frontage |
| 0,3-0,6s | Same blueprint, hard cut | Wireframe/3D mesh grid snaps over the 2D plan, suggesting the computer is "building" it |
| 0,6-0,9s | Same blueprint, hard cut | Room label tags pop in rapid-fire, one per beat: "72 m²" then "3 quartos" then "1 suíte" then "2 banheiros," stacking faster each time |
| 0,9-1,2s | Hard cut, no transition | Finished 3D render or real house photo, full reveal, overlays gone, clean shot |

"Keep every cut in this sequence a hard cut, no crossfade, that abruptness is what sells the "scanning" feeling from the reference. This whole sequence replaces your current blueprint-tracing opener and slots in as the mid-video proof beat we discussed earlier (after the hook lands, before the CTA)."

O que isso obriga:

- 4 tempos de 0,3 s; **só corte seco**, nenhuma fusão dentro da sequência.
- Tempo 1: cotas entram uma de cada vez, na frente de 8 m.
- Tempo 2: malha 3D de arame por cima da planta 2D.
- Tempo 3: etiquetas "72 m²", "3 quartos", "1 suíte", "2 banheiros", cada uma mais rápida que a anterior.
- Tempo 4: casa pronta em 3D (ou foto real), limpa, sem as marcações.
- **Substitui** a abertura da planta se desenhando; fica **depois do gancho e antes da chamada**.

Como foi feito: ver a seção "Estado" abaixo.

#### Estado

| Data | O que está feito | O que falta |
|---|---|---|
| 22/11 | Sequência de escaneamento feita com a planta **E07** (os números do dono batem com ela: 72 m², 3 quartos, 1 suíte, 2 banheiros, lote de 8 m de frente; todos saem do validador). `video/scan.py` gera os 3 primeiros tempos (`broll/clipes/scan-e07.mp4`, 0,9 s); o 4º tempo é a cena seguinte do roteiro (3D próprio da E07, limpo, 2,1 s). Encaixada em `roteiros/principal-condor.json` depois do gancho (4,8 s) e antes da chamada; a planta se desenhando saiu. O gancho passou da C01 (8×15) para a E07 (8×25), para o vídeo falar de uma casa só. O vídeo ficou sem nenhum clipe do OpenArt: 21 s, `saida/principal-condor/`. Conferido quadro a quadro | **É rascunho:** a E07 está na fila do redesenho das plantas (`contexto/QUADRO.md`); não publicar antes de o dono decidir entre esperar o redesenho ou trocar de casa. O dono assistir. Trocar o 4º tempo e o 3D por filmagem real quando ele filmar. Música licenciada (no Mac). O aviso legal e o selo "Ilustração do modelo 3D" ficam no 4º tempo, então ele não é 100% "limpo". **Pela ordem de 22/11 (sem selo; aviso legal pequeno, no canto, parado), o selo sai na próxima montagem**: o roteiro `roteiros/principal-condor.json` ainda o traz |

<!-- era: video/anuncios/checklist-revisao.md -->
## Checklist de revisão antes de subir o anúncio

> Use antes de publicar. Confira as regras atuais da Meta para anúncios de imóveis e construção no Gerenciador de Anúncios, porque elas mudam.

### Conteúdo

- [ ] Nenhuma promessa de prazo de obra
- [ ] Nenhum valor exato de custo de construção
- [ ] Nenhuma garantia de aprovação na prefeitura ou no banco
- [ ] Nada diz ou dá a entender que a planta dispensa pedreiro, engenheiro ou arquiteto
- [ ] Preço de concorrente citado foi conferido nesta semana
- [ ] Tom de voz da [estratégia](../ESTRATEGIA.md), seção 9: simples, sem jargão de arquiteto
- [ ] Área, quartos e banheiros batem com a planta final
- [ ] Preço e forma de pagamento conferidos
- [ ] Texto em português brasileiro, sem erros de digitação

### Imagem ou vídeo

- [ ] A casa 3D corresponde à planta vendida
- [ ] Sem acabamento que o projeto não tem
- [ ] Legenda na tela, para funcionar sem som
- [ ] Proporção certa para o destino: 4:5 no feed do Facebook, 9:16 leve (até 5 MB) no WhatsApp (proposta a confirmar com o dono, [`../ANUNCIO-LOCUCAO.md`](ANUNCIO-LOCUCAO.md), seção 2)
- [ ] Vídeo: aviso legal pequeno, no canto, parado; sem o selo "Imagem ilustrativa" (dono, 22/11/2026). Imagem parada (post, e-book) continua com a legenda "imagem ilustrativa"

### Público e oferta

- [ ] Público configurado para o Brasil
- [ ] Botão de chamada leva ao canal certo (WhatsApp)
- [ ] Material gratuito existe e está acessível antes de anunciar

### Depois de publicar

- [ ] Responder dúvidas em até 24 horas
- [ ] Parar de enviar mensagens para quem pediu para sair
- [ ] Anotar qual variação teve mais cadastros
