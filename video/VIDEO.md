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

## 2. O que está em `saida/` (conferido em 22/11/2026)

| Pasta | Arquivo | O que é | Situação |
|---|---|---|---|
| `previa-whatsapp/` | `x1-plantas-previa.mp4` (720 x 1280) | Prévia que o parceiro manda no WhatsApp antes do Pix. Roteiro `roteiros/previa-whatsapp.json` | Feita em 21/11, **antes do redesenho da C01**: a cena `broll/clipes/c01-3d.mp4` mostra a casa antiga e o roteiro ainda põe selo. Remontar antes de mandar |
| `principal/` | `x1-plantas-principal.mp4` (1080 x 1920) | "Todo lote é uma conta". Roteiro `roteiros/principal.json` | Rascunho de 21/11: usa a C01 antiga e o selo em toda cena. Não publicar assim |
| `principal-condor/` | `x1-plantas-principal-condor.mp4` (21 s) | Estilo CONDOR com a sequência de escaneamento da E07. Roteiro `roteiros/principal-condor.json` | **Rascunho, não publicar:** a E07 está na fila do redesenho ([`PEDIDOS-DO-DONO.md`](PEDIDOS-DO-DONO.md), "Vídeo principal") |
| `convite/` | `x1-plantas-convite.mp4` (26 s) | Vídeo-convite da F03, com o passeio por dentro. Roteiro `roteiros/convite.json` | **Rascunho:** falta o dono dizer o que é "pagar por mais"; Revisor ainda não viu ([`PEDIDOS-DO-DONO.md`](PEDIDOS-DO-DONO.md), "Próximo vídeo: o convite") |
| `principal-e07/` | `x1-plantas-e07.mp4` | Versão 2 de 21/11, "3 quartos em 8 m" ([`plano-principal-e07.md`](plano-principal-e07.md)) | **Antigo:** abre no blueprint, tem o selo e a E07 com os quartos em fila |
| `principal-e07/` | `x1-plantas-e07-locucao.mp4` e `x1-plantas-e07-locucao-whatsapp.mp4` | Montagem com a voz do dono sobre a E07 em fila | **Base que o plano novo refaz** ([`plano-anuncio-locucao.md`](plano-anuncio-locucao.md)): a planta muda, o selo sai, o aviso vai para o canto |
| `tour-c06/` | `tour-c06-casa-compacta-suite-v1.mp4` e `-v2.mp4` | Passeios da C06 Casa Compacta Suíte, vindos da antiga frente 3D | Sem plano nesta pasta; ilustração do motor 3D, não foto |
| `v1/` a `v5/`, `quadros/` | `rascunho.mp4`, `camada-transparente.webm` | "Os R$ 1.000 do arquiteto": camada para pôr sobre a gravação de um apresentador | **Antigo, não publicar:** 3D velho da C01 e nenhuma gravação do apresentador. O gancho dos R$ 1.000 fica guardado como opção ([`../ESTRATEGIA.md`](../ESTRATEGIA.md)); o código é `render.cjs`, `src/cena.js` e `src/planta.js` |

**Em andamento:** o anúncio com locução, para WhatsApp e Facebook Ads. Plano [`plano-anuncio-locucao.md`](plano-anuncio-locucao.md) e ficha [`PEDIDO-anuncio-locucao.md`](PEDIDO-anuncio-locucao.md). Espera o dono aprovar a planta nova da E07 e o plano; nada foi gerado.

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
| `render.cjs`, `carimbar.py` | Código do vídeo antigo dos R$ 1.000 |
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
