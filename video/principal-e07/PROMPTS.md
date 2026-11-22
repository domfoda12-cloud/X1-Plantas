# Prompts do vídeo da E07 (OpenArt)

> Parte da frente Vídeo. Plano: [`../plano-principal-e07.md`](../plano-principal-e07.md). Guardados para repetir o mesmo movimento em outra casa: troque só a imagem de partida.
>
> **Regra:** toda imagem parte de uma imagem nossa (blueprint, 3D ou prévia da planta). Todo clipe é imagem → vídeo no **Kling 3 Omni**, resolução `pro`, 5 s, **sem som** (`generateSound: false`). Em todos: nada de texto, logo, marca nem gente que não estava na imagem.

## 1. Movimento de câmera da casa (imagem → vídeo)

| Cena | Imagem de partida | Prompt |
|---|---|---|
| **Blueprint vira casa** (quadro inicial = blueprint limpo, quadro final = vista de cima realista) | `limpo-blueprint.png` → `a-vista-cima` | Architectural transformation, vertical, top-down view that never rotates. The blue blueprint paper comes alive: the white chalk wall lines rise up into real white walls cut at 1.1 m, the blue paper turns into green grass, wood floors and tiles spread room by room, furniture grows in place, warm late-afternoon sunlight sweeps in from the right replacing the blue light. The camera slowly pushes in toward the house. The house layout, walls, doors and windows stay exactly in place the whole time, nothing new is added. Smooth, elegant, satisfying, no text. |
| **Voo de cima pela casa** | `a-vista-cima` | Slow, smooth top-down drone glide over this cutaway house, moving from the front (top of frame) toward the back (bottom), slightly descending, the house layout never changes. Warm late-afternoon light, soft shadows slowly moving, curtains and plant leaves moving gently, the caramel dog on the sofa breathing. Realistic, cinematic, no text, no people. *(Só o 1º segundo presta: depois de 1,7 s aparece um pano branco inventado.)* |
| **Fachada: câmera recua e mostra o lote** | `d-fachada` (entardecer) ou `d-fachada-rosa` | Slow camera dolly backward and slightly up from the street, revealing the whole narrow lot at dusk. The colorful hammock sways gently, the green and yellow paper bunting flutters in a light breeze, warm interior lights glow, the sky shifts from orange to deep blue, a street light flickers on. The house, window, side corridor and front wall stay exactly the same. Realistic, cinematic, no text, no people, no cars. |
| **Fachada rosa (trend GTA VI)** | `d-fachada-rosa` | Slow camera dolly backward and slightly up from the wet street, revealing the whole narrow lot under a vivid pink and magenta sunset sky. The hammock sways gently, the green and yellow paper bunting flutters, the palm tree fronds move in the breeze, pink light ripples in the puddles on the asphalt, warm interior lights glow. The house, window, side corridor and front wall stay exactly the same. Realistic, cinematic, no text, no logos, no people, no cars. |
| **Sala com o caramelo** | `b-sala-final` | Slow, gentle handheld push-in toward the sofa. The caramel mutt dog lifts its head, perks its ears and wags its tail happily looking at the camera. The TV shows only a plain green football pitch with tiny players, no scoreboard, no text, no logos. Warm late-afternoon light patches shimmer softly on the wall. Everything else stays exactly in place: door, TV, rack, rug, sofa, plain flip-flops, kitchen at the back. Realistic smartphone video, cozy, no text, no people. |
| **Almoço de domingo** | `e-almoco-limpo` | Slow, gentle handheld push-in toward the table. The family laughs and passes the dishes, the grandmother serves rice onto a plate, the father smiles, the little boy reaches for food. The caramel mutt dog under the table wags its tail and looks up hopefully. Warm afternoon light. The kitchen, table and people stay consistent, no new people appear, plain clothes with no logos. Realistic smartphone video, cozy, no text. |
| **Bancada da cozinha** | `c-cozinha-onigiri` | Slow cinematic push-in on this kitchen counter, shallow depth of field. Steam rises gently from the small glass of black coffee, warm sunlight shimmers on the rice balls on the plate, light flickers softly through the window grille as leaves move outside. Everything stays in place, plain objects with no text or logos, realistic, no hands, no people. |

**O que aprendemos sobre o movimento:**
- Diga sempre o que **não** muda ("the house layout never changes", "stay exactly the same"); sem isso o modelo entorta parede e inventa objeto.
- Movimento **lento e um só** por clipe (avanço, recuo ou deslize). Dois movimentos juntos dão tremor.
- Para a transformação blueprint → casa, use **quadro inicial e quadro final**: é o que mantém a casa no lugar.
- Confira o clipe quadro a quadro. Use só o trecho bom.

## 2. Imagens (Nano Banana 2.1, imagem → imagem, 9:16, 2K)

- **Vista de cima realista:** referências = blueprint limpo + 3D + prévia da planta. Pedir "EXACTLY the same house: same position, same size and same framing", paredes cortadas a 1,1 m, móveis no lugar da planta, luz de fim de tarde.
- **Interior:** "Realistic smartphone photo", câmera no canto a 1,5 m, lente 24–28 mm, luz lateral 3.500–4.000 K, "lived-in, not a catalog photo". Porta, janela e móveis onde a planta manda (lista do Arquiteto no plano, seção 7).
- **Fachada:** partir da fachada do e-book (`ebook/visual/openart/fachadas/E07.png`) e pedir "Change only" a luz e os enfeites.
- **Limpeza de marca** (o Revisor veta): pedir "Edit this exact photo and keep everything else identical. Change only: …" para tirar logo, placar, rótulo, relevo de chinelo, listras de camisa.

## 3. Peso dos arquivos

- Clipe do OpenArt chega com 10 a 20 MB. No pacote da edição entra comprimido (H.264, CRF 23, sem áudio).
- Vídeo final 1080 x 1920: CRF 23, alvo **até 12 MB** para 35 s. Versão para WhatsApp: 720 x 1280, CRF 28 ou mais, alvo **até 5 MB**.
