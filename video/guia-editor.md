# Guia para o editor: vídeo "8 erros na planta"

> Referência principal: reel de Robert McKeaveney, "10/10 content strategies (niche edition)", 52 s, 9:16.
> Link: https://www.instagram.com/reel/DfY-8rETTPs/
> Copiamos o **formato**, não o conteúdo nem a imagem dele.

## 1. O que copiar da referência

| Elemento | Como é na referência | Como fica no nosso vídeo |
|---|---|---|
| Apresentador | Fala direto para a câmera, enquadramento do peito para cima, fundo de casa simples | Você (ou o parceiro) gravando no celular, fundo claro e arrumado |
| Ritmo | Um item novo a cada 4 a 6 s, sem pausa | 8 itens + abertura + chamada final, 50 s no total |
| Cartão no terço superior | Cartão branco com diagrama, print ou gráfico, troca a cada item | Cartão branco com a planta 2D ou a casa em 3D |
| Legenda no meio | Título do item em negrito ("1. Watch time") e uma palavra da fala por vez embaixo | Título do item ("1. Construir sem ver em 3D") e uma palavra da fala por vez |
| Abertura | Título grande no alto, sem cartão, nos 3 primeiros segundos | "8 erros na planta que custam caro (antes de construir)" |
| Fecho | Último item marcado como "Most important!" | "8. Mais importante!" antes da chamada |

## 2. Arquivos

Todos na pasta `video/saida/`:

- **`camada-transparente.webm`**: só os cartões e as legendas, com fundo transparente (VP9 com canal alfa). Coloque **por cima** da gravação do apresentador.
- **`rascunho.mp4`**: o mesmo vídeo com um boneco no lugar do apresentador, para ver o resultado antes de gravar.

Se o seu editor não abrir o `.webm` com transparência, peça para eu exportar em outro formato (sequência PNG ou ProRes 4444).

## 3. Roteiro de fala (teleprompter)

O texto abaixo é para o apresentador ler. As palavras que aparecem na legenda são um resumo de cada fala; ajuste a legenda se mudar o texto.

| Tempo | Item na tela | Fala |
|---|---|---|
| 0:00 a 0:03,5 | Abertura | "Antes de construir sua casa, veja esses 8 erros na planta que custam caro." |
| 0:03,5 a 0:09 | 1. Construir sem ver em 3D | "Primeiro: construir sem ver a casa em 3D. Você precisa ver a casa antes do primeiro tijolo." |
| 0:09 a 0:14 | 2. Ignorar o sol | "Dois: ignorar o sol. Quarto com sol da manhã fica mais fresco à tarde." |
| 0:14 a 0:19 | 3. Corredor comprido | "Três: corredor comprido. Corredor também custa por metro, e ninguém mora no corredor." |
| 0:19 a 0:24 | 4. Banheiro de frente pra sala | "Quatro: banheiro de frente para a sala. A porta tem que abrir para o hall." |
| 0:24 a 0:29 | 5. Banheiro sem janela | "Cinco: banheiro sem janela. Ventilação natural evita mofo." |
| 0:29 a 0:34 | 6. Esquecer os recuos | "Seis: esquecer os recuos. Quem manda na planta é o terreno, e cada prefeitura tem a sua regra." |
| 0:34 a 0:39 | 7. Não prever ampliação | "Sete: não prever ampliação. Pense na sua casa daqui a cinco anos." |
| 0:39 a 0:45 | 8. Mais importante! | "E o mais importante: escolha a planta pelo seu jeito de viver, não pela foto bonita." |
| 0:45 a 0:50 | Comente PLANTA | "Comenta PLANTA que eu te mando o material grátis no WhatsApp." |

## 4. Como gravar

- Celular na vertical, 1080 x 1920, 30 fps.
- Rosto entre 45% e 75% da altura da tela: o terço de cima fica livre para o cartão e a legenda fica na altura do peito.
- Microfone de lapela ou fone com microfone, como na referência.
- Grave cada item separado. Fica mais fácil cortar no ritmo do cartão.

## 5. Edição

1. Coloque a gravação na trilha de baixo e a `camada-transparente.webm` na trilha de cima, começando no mesmo ponto.
2. Corte a gravação para que cada fala caiba no tempo do item (tabela acima). Se uma fala ficar maior, me avise o novo tempo que eu renderizo de novo.
3. Música de fundo baixa, sem letra.
4. Exporte em 1080 x 1920.

## 6. Antes de publicar

Passe pelo `checklist-revisao-anuncio.md` na raiz do repositório. As medidas da Casa Compacta são provisórias até o arquiteto validar a planta.

## 7. Como alterar o vídeo

Os textos, tempos e cartões estão em `video/src/cena.js` (lista `cenas` no início). A planta está em `video/src/planta.js`.

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

Para conferir só alguns quadros, sem renderizar tudo: `node render.cjs --amostras 6,20,43`.
