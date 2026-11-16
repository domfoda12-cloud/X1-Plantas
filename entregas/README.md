# Entregas: o que o cliente recebe

Cada planta tem uma pasta com imagens estáticas e uma animação, geradas a partir da mesma planta usada no vídeo (`video/src/planta.js`).

| Arquivo | O que é | Para que serve |
|---|---|---|
| `01-blueprint.png` | Planta técnica azul, com cotas, portas, nomes e áreas | Mostrar as medidas; base para o construtor |
| `02-planta-humanizada.png` | Vista de cima com piso, móveis e jardim | O cliente entende a casa de uma olhada |
| `03-perspectiva.png` | Casa em 3D, de um ângulo | Mostrar como a casa fica "na vida real" |
| `04-perspectiva-lateral.png` | Casa em 3D, do outro lado | Segundo ângulo |
| `animacao.mp4` | 12 s, vertical: o blueprint se desenha, a casa ganha vida e a câmera desliza | Mandar no WhatsApp e postar nos stories |

As imagens têm 2000 x 2500 pixels (proporção 4:5), boas para WhatsApp, Instagram e impressão em A4.

## Referências de estilo

- **Planta humanizada:** versão da planta baixa com móveis, decoração e acabamentos, para facilitar a visualização ([QuintoAndar](https://www.quintoandar.com.br/guias/?p=2444657), [Planner 5D](https://planner5d.com/blog/pt/planta-baixa-humanizada-guia/)).
- **Animação de planta 3D:** vista de cima com câmera lenta, como os vídeos da página Virtual Floor Plan ([exemplo](https://www.facebook.com/watch/?v=2617867535326380)).
- **Blueprint virando casa:** sequência planta 2D, modelo mobiliado e câmera passeando ([TensorPix](https://tensorpix.ai/blog/2d-to-3d-floor-plan-video-ai), [YouMind](https://youmind.com/pt-BR/video-prompts/architectural-blueprint-house-transformation-4370)).

## Importante

- As medidas da Casa Compacta são provisórias até um arquiteto validar a planta.
- Os móveis e acabamentos são ilustrativos. Deixe isso claro para o cliente.
- O material é ilustração de projeto, não substitui o projeto aprovado na prefeitura.

## Como gerar de novo

Dentro da pasta `video`, com Node.js, ffmpeg e Playwright instalados (ver `video/guia-editor.md`):

```bash
node render-planta.cjs
```
