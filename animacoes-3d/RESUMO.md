# Resumo: Animações 3D e imagens

> O motor 3D, o OpenArt e as referências de planta que ganha vida. **Leia este resumo primeiro**; abra um documento inteiro só quando a tarefa pedir. Índice geral: [`INDICE.md`](../INDICE.md). Quem lê: arquiteto, designer, editor-video.

## O essencial

<!-- essencial: escrito à mão, o gerador não apaga -->
- O 3D é o último passo (decisão do dono). (`REFERENCIAS-BLUEPRINT.md`)
- Cada planta recebe 5 arquivos em `plantas/<nome>/`: `01-blueprint.png`, `02-planta-humanizada.png`, `03-perspectiva.png`, `04-perspectiva-lateral.png` e `animacao.mp4` (12 s, vertical). Pronta: só `casa-compacta/`. (`ANIMACOES-3D.md`)
- O motor fica em `video/src/` e já lê as 24 plantas via `ferramentas/planta3d.py`. Gerar, dentro de `video`: `node render-planta.cjs --planta ID`. (`REFERENCIAS-BLUEPRINT.md`, `video/CLAUDE.md`)
- Estilo: azul `#0B4FA8`, amarelo `#FFC857`, câmera lenta e contínua, frente da casa no alto, paredes cortadas a 1,1 m. (`ANIMACOES-3D.md`)
- A casa animada ou gerada é a mesma do e-book. No OpenArt, casa só a partir de imagem nossa: o Arquiteto vetou uma casa inventada por texto. (`OPENART-MINOAI.md`)
- A legenda diz "imagem ilustrativa da planta de referência". A ordem "da obra" é efeito visual: não diga "é assim que se constrói". (`REFERENCIAS-BLUEPRINT.md`)
- OpenArt: em 20/11/2026 o dono liberou os créditos sem limite; a regra mais recente (22/11/2026) é o "sim" dele a cada uso, com resumo e custo antes. (`video/PEDIDOS-DO-DONO.md`)
- Imagem final: GPT Image 2.5 Sunburst, imagem para imagem a partir do rascunho aprovado, 4K extra-alta, 4:5; recortes com `python3 ferramentas/recortes.py`. (`OPENART-MINOAI.md`)
- Falta no motor: fachada (`05-fachada.png`), medidas de cada cômodo no blueprint e `06-como-cresce.png`. (`ANIMACOES-3D.md`)
<!-- /essencial -->

## Os 3 documentos

### [Animações 3D: as plantas que o e-book vai conter](ANIMACOES-3D.md)

Banco de referências de planta que ganha vida, com o que adotar no motor: `REFERENCIAS-BLUEPRINT.md`.

Seções: Nesta pasta; 1. O que cada planta recebe; 2. Os três estágios da animação; 3. Regras de estilo; 4. Referências; 5. Como o motor funciona; 6. O que falta para gerar dezenas de plantas; 7. Cuidados.

Tamanho: 1032 palavras.

### [OpenArt + MinoAI Frontier: imagens e animações a partir das nossas plantas](OPENART-MINOAI.md)

Exemplo do Conselho em ação. Guia da frente: `ANIMACOES-3D.md`. Editor: MinoAI Frontier.

Seções: A mesa (conselho completo, 20/11/2026); Situação das ferramentas; O fluxo; Prompts para o OpenArt (imagem → imagem); Regras; Economia de créditos (pedido do dono, 20/11/2026: "economizar o máximo, mas enfeitado; não usar o primeiro modelo"); Como tirar o máximo de cada crédito (preços medidos na conta em 20/11/2026).

Tamanho: 2348 palavras.

### [Banco de referências: planta que ganha vida em 3D](REFERENCIAS-BLUEPRINT.md)

Parte da pasta Animações 3D (`ANIMACOES-3D.md`). Pesquisa de 20/11/2026 (busca na web pelo TinyFish e biblioteca de ganchos virais da MinoAI Frontier). O 3D é o último passo (decisão do dono): este banco serve para quando ele for liberado e para os roteiros de agora. Acrescente aqui toda referência…

Seções: 1. As referências; 2. A anatomia do efeito (o que todos têm em comum); 3. Onde a nossa animação já está e o que falta; 4. Regras (Revisor de risco e Arquiteto); 5. Roteiro de 12 s revisado (para quando o 3D for liberado).

Tamanho: 1588 palavras.
