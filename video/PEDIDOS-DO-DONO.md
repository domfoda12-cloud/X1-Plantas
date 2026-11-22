# Vídeo: tudo o que o dono pediu (não se perde)

> **Regra do dono (22/11/2026):** "Para todo vídeo, quando eu acrescentar uma informação, garanta que ela fique lá e não se perca na conversa."
> Por isso: **toda instrução dele sobre vídeo entra aqui na hora, com as palavras dele**, antes de qualquer edição. Quem edita lê este arquivo inteiro antes de mexer em roteiro ou clipe, e confere no fim se cada linha "vale" continua atendida. Nada sai daqui sem o dono mandar tirar.

## Ordens gerais (valem para todo vídeo)

Revisão de 22/11/2026, a pedido do dono ("reveja toda a nossa conversa, procure o que é de criação de vídeo e ponha no arquivo de vídeo"): entrou tudo desta conversa e tudo o que o histórico do projeto guarda sobre vídeo.

| Data | O dono disse | Estado |
|---|---|---|
| Início | Seguir o reel de referência; atenção na retenção; "o cliente precisa se interessar pelas plantas" | Vale. `instagram/MINOAI-FRONTIER.md`, `instagram/referencias-mino-lee.md` |
| Início | Clipes menos travados: o blueprint azul ganhando vida | Vale como estilo do 3D próprio. Como **abertura** do principal foi trocado pelo escaneamento (22/11) |
| Início | Gancho "vou te salvar os R$ 1.000 que um arquiteto te salvaria" | Guardado como opção de gancho (`ESTRATEGIA.md`). O Revisor de risco confere antes de usar |
| Início | Narrador sempre falando, sem pausa; sempre um visual prendendo a atenção | Vale. `VIDEO.md` |
| Início | Roteiro "volto pro Brasil com casas na mala" | Guardado em `roteiro-lancamento.md` |
| 20/11 | "A edição de vídeo é responsabilidade [da MinoAI]" | Vale. Edição final da MinoAI Frontier, no Mac do dono |
| 20/11 | Referência de edição: CONDOR XIII ("melhor edição que já vi"); "preste muita atenção nos B-rolls e nas escolhas de música" | Vale. `REFERENCIA-CONDOR.md` |
| 20/11 | "O Payton não produz música, no máximo usa remixes" | Vale. Nada de música composta; faixa licenciada, no máximo remixada |
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

**Em aberto, citado pelo dono e que não chegou ao Editor:** "o beat de prova que discutimos antes" (conversa anterior, provavelmente na página de chat). Se tinha mais detalhe, falta o dono repetir.

## Prompt base para tomadas realistas (22/11/2026)

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
- **No OpenArt** (o caminho que chega perto de "vida real"): só com o "sim" do dono a cada uso, com resumo e custo antes. Tomada gerada parte da nossa imagem 3D da casa (para não inventar cômodo) e leva "Imagem ilustrativa".
- **Dúvida registrada:** "motor art integration" foi entendido primeiro como o motor 3D próprio, porque o Editor ainda não sabia da correção do dono sobre o OpenArt. É provável que ele tenha dito **OpenArt**. O passeio do motor próprio fica como rascunho e como guia de câmera; a versão realista no OpenArt espera o "sim" dele com o custo na mão.

## Próximo vídeo: o convite (22/11/2026)

Texto do dono, sem mudar:

"This is an initial video that should be extremely inviting, showing an example of what the customer can receive if he pays for more, Choose one of the house projects and make sure to add detail and keep the viewer attention with visuals"

"Do a mix of this prompt with the last made longer video"

O que isso obriga:

- É o **vídeo inicial**: o primeiro que a pessoa vê. Tem de ser **extremamente convidativo**.
- Mostra **um exemplo do que o cliente recebe se pagar por mais**.
- **Uma casa só**, escolhida entre os projetos, com **detalhe**.
- **Sempre um visual prendendo a atenção.**
- É uma **mistura** do passeio do prompt base com o último vídeo mais longo.

### Estado

| Data | O que está feito | O que falta |
|---|---|---|
| 22/11 | **Casa escolhida: F03, Casa Família** (78 m², 3 quartos, 1 suíte, 2 banheiros, lote a partir de 11 × 15 m). Motivo: é casa de família, tem varanda, sala e cozinha abertas (bom de mostrar por dentro) e está **fora** da fila do redesenho (série E, compactas e F02). Passeio por dentro feito no motor 3D próprio (`render-passeio.cjs`, `src/passeio.html`): entra pelo jardim, varanda, sala, cozinha, corredor, suíte; movimento contínuo, luz quente, teto, borrão de movimento leve. Roteiro `roteiros/convite.json`: gancho "Todo lote é uma conta" com 11×15 em letra-janela → escaneamento da F03 (0,9 s) → passeio inteiro sem corte de imagem, com o nome e a medida de cada cômodo (números do validador) → página do e-book → chamada PLANTA. Saída: `saida/convite/x1-plantas-convite.mp4` (26 s). Sem OpenArt | **O dono dizer o que é "pagar por mais"** (qual produto ou pacote): hoje o vídeo só diz "veja por dentro" e não promete nada que não exista. O passeio é **ilustração 3D, não foto**: não chega a "fotografia de arquitetura 4K"; saiu em 1080 × 1920. Trocar por filmagem real quando o dono filmar. Música licenciada (no Mac). Revisor de risco ainda não viu |

## Vídeo principal

### Sequência de "escaneamento" (22/11/2026): a prova no meio do vídeo

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

### Estado

| Data | O que está feito | O que falta |
|---|---|---|
| 22/11 | Sequência de escaneamento feita com a planta **E07** (os números do dono batem com ela: 72 m², 3 quartos, 1 suíte, 2 banheiros, lote de 8 m de frente; todos saem do validador). `video/scan.py` gera os 3 primeiros tempos (`broll/clipes/scan-e07.mp4`, 0,9 s); o 4º tempo é a cena seguinte do roteiro (3D próprio da E07, limpo, 2,1 s). Encaixada em `roteiros/principal-condor.json` depois do gancho (4,8 s) e antes da chamada; a planta se desenhando saiu. O gancho passou da C01 (8×15) para a E07 (8×25), para o vídeo falar de uma casa só. O vídeo ficou sem nenhum clipe do OpenArt: 21 s, `saida/principal-condor/`. Conferido quadro a quadro | **É rascunho:** a E07 está na fila do redesenho das plantas (`contexto/QUADRO.md`); não publicar antes de o dono decidir entre esperar o redesenho ou trocar de casa. O dono assistir. Trocar o 4º tempo e o 3D por filmagem real quando ele filmar. Música licenciada (no Mac). O aviso legal e o selo "Ilustração do modelo 3D" ficam no 4º tempo (regra de honestidade), então ele não é 100% "limpo" |
