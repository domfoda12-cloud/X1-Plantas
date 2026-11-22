# Vídeo: o que existe hoje

> Parte do projeto X1-Plantas. Painel geral: [`../PAINEL.md`](../PAINEL.md). Regras desta pasta: [`CLAUDE.md`](CLAUDE.md). **Antes de mexer em vídeo, leia [`PEDIDOS-DO-DONO.md`](PEDIDOS-DO-DONO.md) inteiro.**
>
> Reorganizado em 22/11/2026 para dizer a verdade de hoje. O guia antigo do vídeo "Os R$ 1.000 do arquiteto" (teleprompter, gravação do apresentador, teste das 5 versões como reels) saiu: o vídeo usa o 3D velho da C01, o apresentador nunca gravou e o dono mudou o rumo do anúncio.

## 1. As regras que valem (dono, 22/11/2026)

- **Destino do anúncio com locução: WhatsApp e Facebook Ads**, não Instagram nem TikTok ([`PEDIDO-anuncio-locucao.md`](PEDIDO-anuncio-locucao.md), pedido 27).
- **Aviso legal pequeno, no canto da tela, parado. Sem o selo "Imagem ilustrativa"** (o dono tirou essa condição do Revisor). Em imagem parada (post, e-book) a legenda "imagem ilustrativa" continua.
- **Antes de montar vídeo ou gastar crédito do OpenArt:** mandar ao dono o resumo da produção e a lista de instruções, e esperar o "sim" dos dois. OpenArt pode, com o "sim" dele a cada uso.
- **Música:** faixa licenciada ou a trilha nossa de 128 BPM (`musica/gerar_trilha.py`), como diz o [`CLAUDE.md`](CLAUDE.md) desta pasta. Áudio dos modelos de vídeo é descartado.
- **Edição final:** MinoAI Frontier, no Mac do dono. Até 12 MB; versão do WhatsApp até 5 MB.
- **Continuam do método antigo:** texto no primeiro quadro; o narrador nunca para (só a pausa marcada no roteiro); uma ideia por cena; a imagem mostra o que a voz diz; chamada única no fim ("Comenta PLANTA").

## 2. O que está em `saida/` (22/11/2026)

Em 22/11 o dono mandou apagar os vídeos, clipes e renders para refazer do zero, guardando a informação e o último vídeo. Ficaram:

| Pasta | Arquivo | O que é |
|---|---|---|
| `convite/` | `x1-plantas-convite.mp4` | Passeio pela F03 (motor próprio, ilustração), o último feito; roteiro `roteiros/convite.json` |
| `principal/` | `x1-plantas-principal.mp4` | Principal de 21/11, com clipes do OpenArt e a C01 antiga; o último mostrado ao dono nesta conversa |

O resto (prévia do WhatsApp, principal com escaneamento, anúncio da E07 com locução, passeios da C06 e as versões `v1` a `v5`) volta pelo histórico do git se for preciso (`git checkout 079dae7 -- <caminho>`). Os roteiros em `roteiros/` apontam para clipes apagados: `montar.py` só monta de novo depois de gerar os clipes. A gravação da voz do dono está em `principal-e07/voz/`. O que refazer e em que ordem: [`../contexto/dono/RETROSPECTIVA.md`](../contexto/dono/RETROSPECTIVA.md).

## 3. Nesta pasta

| Arquivo | Para que serve |
|---|---|
| `PEDIDOS-DO-DONO.md` | Tudo o que o dono pediu sobre vídeo, com as palavras dele |
| `PEDIDO-anuncio-locucao.md`, `plano-anuncio-locucao.md` | Ficha e plano do anúncio com locução (o que vale agora) |
| `plano-principal-e07.md`, `principal-e07/` | Registro da versão de 21/11 da E07, prompts de câmera (`PROMPTS.md`) e o pacote para a MinoAI (`kit-minoai/`) |
| `roteiro-lancamento.md` | Vídeo de aquecimento do lançamento ("casas na mala"), com o roteiro original do dono |
| `REFERENCIA-CONDOR.md`, `REFERENCIA-VIRAL.md` | Referências de edição e de formato |
| `anuncios/anuncio-facebook.md` | Textos de anúncio por ângulo (pelo lote, erro caro, casa que cresce, pedreiro…) |
| `anuncios/brief-criativo.md` | Brief dos criativos (formatos, estilo, variações) |
| `anuncios/checklist-revisao.md` | Revisão antes de subir qualquer anúncio |
| `montar.py`, `roteiros/`, `broll/` | Montador dos vídeos sem apresentador, os roteiros e as cenas |
| `scan.py`, `render-planta.cjs`, `render-passeio.cjs`, `render-rua.cjs`, `src/` | Escaneamento, 3D, passeio por dentro e vista da rua (esta foi recusada pelo dono: não é realista) |
| `musica/` | Trilha nossa de 128 BPM |

## 4. Como montar e gerar

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

## 5. Decisões que ficam com o dono

- **Publicar** qualquer vídeo, e a **palavra da chamada** (PLANTA ou LOTE). Se for LOTE, troque no roteiro e monte de novo.
- **A planta prometida na chamada.** Quando o vídeo mostra uma casa e diz "essa planta", a pessoa tem de recebê-la; se a casa ainda não está no material gratuito, a chamada diz "uma planta de graça". A decisão segue em aberto no [`../CONTEXTO.md`](../CONTEXTO.md).
- **Quando o e-book tiver título** ([`../PAINEL.md`](../PAINEL.md), seção 9): a chamada passa a citar o e-book numa frase só ("Comenta PLANTA que eu te mando de graça essa planta do e-book [Título]"). Troque no roteiro e nos textos de [`anuncios/anuncio-facebook.md`](anuncios/anuncio-facebook.md).
