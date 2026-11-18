# Vídeo de anúncio: "Os R$ 1.000 do arquiteto"

[Painel](../PAINEL.md) · 38 s, 9:16, 5 versões (só o gancho muda).

**Arquivos:** `saida/v1` a `saida/v5`, cada uma com `rascunho.mp4` (boneco no lugar do apresentador) e `camada-transparente.webm` (cartões e legendas para pôr por cima da gravação). Nos trechos de tela cheia (0 a 3 s e 27 a 34 s) a camada cobre a gravação de propósito; a voz continua.

## Teleprompter

| Versão | Texto no alto (fixo) | Fala do gancho (0 a 3 s) |
|---|---|---|
| v1 | Vou te economizar os R$ 1.000 que um arquiteto te economizaria | "Sete erros de planta que saem caro na obra. O último é o pior." |
| v2 | Os R$ 1.000 que um arquiteto te faria economizar, de graça | "Olha o que um arquiteto ia te cobrar pra te mostrar." |
| v3 | Antes de pagar R$ 1.000 a um arquiteto, veja isso | "São sete erros. Quase todo mundo comete o último." |
| v4 | 7 erros que um arquiteto te cobraria R$ 1.000 pra achar | "Confere a sua planta comigo. O último é o pior." |
| v5 | Um arquiteto cobraria R$ 1.000 pra te mostrar isso | "Fica até o final, que o último é o mais caro." |

| Tempo | Fala (igual nas 5) |
|---|---|
| 0:03 | "Um: ignorar o sol. Quarto virado pro nascente fica fresco à tarde." |
| 0:07 | "Dois: corredor comprido. Corredor custa por metro, e ninguém mora nele." |
| 0:11 | "Três: banheiro de frente pra sala. A porta tem que abrir pro hall." |
| 0:15 | "Quatro: banheiro sem janela. Sem ventilação natural, o mofo aparece rápido." |
| 0:19 | "Cinco: esquecer os recuos. Cada prefeitura tem a sua regra, confira antes." |
| 0:23 | "Seis: não prever ampliação. Deixe pronto por onde a casa vai crescer." |
| 0:27 | "E o mais caro de todos: construir sem ver a casa pronta. *(pausa curta)* Olha só: cada cômodo, cada móvel, antes do primeiro tijolo." |
| 0:34 | "Comenta PLANTA que eu te mando essa planta humanizada de graça no WhatsApp." |

Sem pausas além da marcada. Grave no celular, na vertical, 1080 x 1920, 30 fps, com o rosto do meio da tela para baixo.

## Alterar e renderizar

Textos e tempos: `src/cena.js`. Precisa de Node.js, ffmpeg e Playwright. Na pasta `video`: `npm install`, depois `node render.cjs`.
