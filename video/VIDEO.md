# Vídeo de anúncio: "Os R$ 1.000 do arquiteto"

> Parte do projeto X1-Plantas. Painel geral: [`../PAINEL.md`](../PAINEL.md).
>
> **Esta pasta é o vídeo de anúncio** (Facebook Ads e reels): roteiro, teleprompter, arquivos para o editor e textos de anúncio.
> As regras de retenção e as referências de edição (Robert McKeaveney e Mino Lee) ficam em [`../instagram/INSTAGRAM.md`](../instagram/INSTAGRAM.md).
> A casa em 3D que aparece no vídeo vem do mesmo motor das [`../animacoes-3d/`](../animacoes-3d/ANIMACOES-3D.md).

## Nesta pasta

| Arquivo | Para que serve |
|---|---|
| `VIDEO.md` | Este guia: estrutura, teleprompter, gravação, edição, teste |
| `saida/v1` a `saida/v5` | As 5 versões prontas (rascunho e camada para o editor) |
| `anuncios/anuncio-facebook.md` | Três variações de texto de anúncio |
| `anuncios/brief-criativo.md` | Brief dos criativos (formatos, estilo, variações) |
| `anuncios/checklist-revisao.md` | Revisão antes de publicar qualquer anúncio |
| `src/`, `render.cjs`, `carimbar.py` | Código que gera o vídeo |

## 1. Por que este vídeo prende quem quer construir

- **A planta aparece desde o primeiro quadro.** O gancho mostra, em tela cheia, a planta azul se desenhando e a casa ganhando vida.
- **Todos os itens usam a mesma casa.** A pessoa vai montando a casa na cabeça: sala, cozinha, quartos, banheiro, terreno. No fim, ela conhece a planta e quer recebê-la.
- **A resposta só vem no item 7**, em tela cheia: o blueprint vira a planta humanizada, com móveis, piso e jardim. É a parte mais bonita do vídeo.
- **A chamada mostra a planta que a pessoa vai receber** (foto da planta humanizada), grátis, pelo WhatsApp.

## 1.1. Estrutura visual

| Tempo | Tela | O que aparece |
|---|---|---|
| 0:00 a 0:03 | **Tela cheia** | Blueprint azul se desenha, paredes sobem, cômodos começam a ganhar vida |
| 0:03 a 0:27 | Apresentador + cartão | Cartões blueprint (planta azul) com o erro destacado em amarelo |
| 0:27 a 0:34 | **Tela cheia** | Casa ganha vida por completo: planta humanizada com câmera deslizando |
| 0:34 a 0:38 | Apresentador + cartão | Foto da planta humanizada e "Comente PLANTA" |

Nos trechos de **tela cheia**, a camada cobre a tela inteira: o apresentador não aparece, mas **a voz dele continua** por cima (como imagem de apoio).

## 2. Arquivos

Cada versão fica em `video/saida/v1` a `video/saida/v5`:

- **`camada-transparente.webm`**: só os cartões e as legendas, com fundo transparente (VP9 com canal alfa). Coloque **por cima** da gravação do apresentador.
- **`rascunho.mp4`**: o mesmo vídeo com um boneco no lugar do apresentador, para ver o resultado antes de gravar.

As 5 versões são iguais depois dos 3 primeiros segundos. Nos trechos de tela cheia a camada não é transparente (cobre a gravação de propósito). Se o seu editor não abrir o `.webm` com transparência, peça para eu exportar em outro formato (sequência PNG ou ProRes 4444).

## 3. Roteiro de fala (teleprompter)

### Gancho (0:00 a 0:03), um por versão

O texto na tela e a fala são diferentes de propósito, como nas referências: o texto promete, a voz puxa para o final.

| Versão | Texto na tela (fica no alto o vídeo todo) | Fala |
|---|---|---|
| v1 | Vou te economizar os R$ 1.000 que um arquiteto te economizaria | "Sete erros de planta que saem caro na obra. O último é o pior." |
| v2 | Os R$ 1.000 que um arquiteto te faria economizar, de graça | "Olha o que um arquiteto ia te cobrar pra te mostrar." |
| v3 | Antes de pagar R$ 1.000 a um arquiteto, veja isso | "São sete erros. Quase todo mundo comete o último." |
| v4 | 7 erros que um arquiteto te cobraria R$ 1.000 pra achar | "Confere a sua planta comigo. O último é o pior." |
| v5 | Um arquiteto cobraria R$ 1.000 pra te mostrar isso | "Fica até o final, que o último é o mais caro." |

### Corpo (igual em todas as versões)

| Tempo | Item na tela | Fala |
|---|---|---|
| 0:03 a 0:07 | 1. Ignorar o sol | "Um: ignorar o sol. Quarto virado pro nascente fica fresco à tarde." |
| 0:07 a 0:11 | 2. Corredor comprido | "Dois: corredor comprido. Corredor custa por metro, e ninguém mora nele." |
| 0:11 a 0:15 | 3. Banheiro de frente pra sala | "Três: banheiro de frente pra sala. A porta tem que abrir pro hall." |
| 0:15 a 0:19 | 4. Banheiro sem janela | "Quatro: banheiro sem janela. Sem ventilação natural, o mofo aparece rápido." |
| 0:19 a 0:23 | 5. Esquecer os recuos | "Cinco: esquecer os recuos. Cada prefeitura tem a sua regra, confira antes." |
| 0:23 a 0:27 | 6. Não prever ampliação | "Seis: não prever ampliação. Deixe pronto por onde a casa vai crescer." |
| 0:27 a 0:34 | 7. O mais caro: não ver a casa em 3D | "E o mais caro de todos: construir sem ver a casa pronta. *(pausa curta)* Olha só: cada cômodo, cada móvel, antes do primeiro tijolo." |
| 0:34 a 0:38 | Comente PLANTA | "Comenta PLANTA que eu te mando essa planta humanizada de graça no WhatsApp." |

### Regras da fala

- **O narrador nunca para.** O fim de cada frase emenda no número do item seguinte ("…fresco à tarde. Dois: …"). Corte qualquer respiração, "é…" ou silêncio na edição.
- **Só uma pausa, de propósito:** depois de "construir sem ver a casa pronta", por cerca de meio segundo, enquanto a casa ganha vida na tela. É o momento da revelação.
- **Glossário na tela:** quando a fala usa um termo técnico (nascente, hall, peitoril, recuo, planta humanizada), a explicação aparece em letra miúda abaixo da legenda.
- **A legenda é a própria fala**, em blocos de 2 a 3 palavras, com a palavra-chave em amarelo. Se mudar o texto falado, me avise que eu ajusto a legenda e renderizo de novo.
- O ritmo é de 3 a 4 palavras por segundo, como na referência. Se uma frase não couber, encurte a frase; não estique o item.

### O que prende o olho em cada momento

| Tempo | Movimento na tela |
|---|---|
| 0:00 a 0:03 | Blueprint se desenhando, paredes subindo, cômodos ganhando vida (tela cheia) |
| 0:03 a 0:27 | Planta do cartão se desenhando, destaque amarelo pulsando, zoom lento contínuo, blocos da legenda entrando com um "pulo" leve |
| 0:03 a 0:38 | Gancho dos R$ 1.000 fixo no alto, lembrando a promessa |
| Sempre | Barra de progresso no alto, enchendo item a item (mostra quantos faltam) |
| 0:27 a 0:34 | Casa ganhando vida e câmera deslizando (tela cheia) |
| 0:34 a 0:38 | Foto da planta humanizada e botão PLANTA pulsando |

## 4. Como gravar

- Celular na vertical, 1080 x 1920, 30 fps.
- Rosto entre 45% e 75% da altura da tela: o terço de cima fica livre para o cartão e a legenda fica na altura do peito.
- Microfone de lapela ou fone com microfone, como na referência.
- Grave o corpo uma vez e os 5 ganchos separados. Assim as 5 versões saem da mesma gravação.

## 5. Edição

1. Gravação do apresentador na trilha de baixo, `camada-transparente.webm` na trilha de cima, começando no mesmo ponto.
2. Corte a gravação para que cada fala caiba no tempo do item (tabela acima). Sem pausas entre os itens.
3. Música de fundo baixa, sem letra.
4. Exporte em 1080 x 1920.

## 6. Como testar

O método de teste vem das referências (ver [`../instagram/INSTAGRAM.md`](../instagram/INSTAGRAM.md)).

1. Publique as 5 versões como **reels de teste** (só para quem não segue).
2. Depois de 24 a 48 horas, compare o **tempo médio assistido** e quantas pessoas chegaram aos 27 s (o desfecho).
3. Publique para todos só a melhor versão.
4. Se ela for bem, repita o formato daqui a um mês com outra planta (Casa Família ou Casa Estreita).

## 7. Antes de publicar

Passe pelo [`anuncios/checklist-revisao.md`](anuncios/checklist-revisao.md). As medidas da Casa Compacta são provisórias até o arquiteto validar a planta.

## 8. Como alterar o vídeo

Os ganchos, textos, tempos e cartões estão em `video/src/cena.js` (listas `GANCHOS` e `cenas` no início). A planta está em `video/src/planta.js`.

Para renderizar de novo, o computador precisa de Node.js, ffmpeg e do Playwright com o Chromium. Dentro da pasta `video`:

```bash
npm install
```

```bash
npm install --no-save playwright
```

```bash
npx playwright install chromium
```

```bash
node render.cjs
```

Para conferir só alguns quadros: `node render.cjs --amostras 1,5,30 --versao 2`.
