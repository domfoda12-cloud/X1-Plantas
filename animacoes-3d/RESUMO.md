# Resumo: Animações 3D e imagens

> O motor 3D, o OpenArt e as referências de planta que ganha vida. **Leia este resumo primeiro**; abra um documento inteiro só quando a tarefa pedir. Índice geral: [`INDICE.md`](../INDICE.md). Quem lê: arquiteto, designer, editor-video.

## O essencial

<!-- essencial: escrito à mão, o gerador não apaga -->
- Ordem das frentes: e-book → animações → vídeo; o motor 3D já está em uso pelo e-book e pelos vídeos (o "3D é o último passo" de 20/11 ficou para trás). (`CLAUDE.md` da raiz, `ANIMACOES-3D.md`)
- Cada planta recebe 5 arquivos em `plantas/<nome>/`: `01-blueprint.png`, `02-planta-humanizada.png`, `03-perspectiva.png`, `04-perspectiva-lateral.png` e `animacao.mp4` (12 s, vertical). Só existe `casa-compacta/`, e é da C01 antiga (55 m²): gerar de novo. (`ANIMACOES-3D.md`)
- C01 redesenhada em 22/11/2026: 50 m², 2 quartos, 1 banheiro, lote a partir de 8 x 15 m. E07 na fila do redesenho (3 quartos em fila). (`ebook/plantas/PLANTAS.md`)
- O motor fica em `video/src/` e já lê as 24 plantas (`video/src/plantas/<ID>.js`, de `ferramentas/planta3d.py`). Gerar, dentro de `video`: `node render-planta.cjs --planta ID`; sem `--planta` ele usa a C01 antiga. (`ANIMACOES-3D.md`, `video/CLAUDE.md`)
- Estilo: azul `#0B4FA8`, amarelo `#FFC857`, câmera lenta e contínua, frente da casa no alto, paredes cortadas a 1,1 m. (`ANIMACOES-3D.md`)
- A casa animada ou gerada é a mesma do e-book. No OpenArt, casa só a partir de imagem nossa: o Arquiteto vetou uma casa inventada por texto. (`OPENART-MINOAI.md`)
- Imagem parada leva a legenda "imagem ilustrativa da planta de referência"; em vídeo, sem o selo (dono, 22/11/2026), aviso legal pequeno no canto. A ordem "da obra" é efeito visual: não diga "é assim que se constrói". (`REFERENCIAS-BLUEPRINT.md`, `video/CLAUDE.md`)
- OpenArt: permitido, mas cada uso pede o "sim" do dono, com resumo e custo antes (22/11/2026). Conta: plano Pro, 21.137 créditos (medido em 22/11/2026). (`OPENART-MINOAI.md`, `video/PEDIDOS-DO-DONO.md`)
- Imagem final: GPT Image 2.5 Sunburst, imagem para imagem a partir do rascunho aprovado, 4K extra-alta, 4:5; recortes com `python3 ferramentas/recortes.py`. (`OPENART-MINOAI.md`)
- Falta: gerar a C01 nova no motor; fachada (`05-fachada.png`), medidas de cada cômodo no blueprint e `06-como-cresce.png`. (`ANIMACOES-3D.md`)
<!-- /essencial -->

## Os 3 documentos

### [Animações 3D: as plantas que o e-book vai conter](ANIMACOES-3D.md)

Banco de referências de planta que ganha vida, com o que adotar no motor: `REFERENCIAS-BLUEPRINT.md`.

Seções: Nesta pasta; 1. O que cada planta recebe; 2. Os três estágios da animação; 3. Regras de estilo; 4. Referências; 5. Como o motor funciona; 6. O que falta; 7. Cuidados.

Tamanho: 1122 palavras.

### [OpenArt + MinoAI Frontier: imagens e animações a partir das nossas plantas](OPENART-MINOAI.md)

Regra que vale (dono, 22/11/2026): o OpenArt é permitido, mas cada uso pede o "sim" do dono, com o resumo da produção e o custo antes (`../video/PEDIDOS-DO-DONO.md`). A liberação "sem limite" de 20/11 não vale mais. Conta: plano Pro, 21.137 créditos (medido em 22/11/2026).

Seções: A mesa (conselho completo, 20/11/2026); Situação das ferramentas; O fluxo; Prompts para o OpenArt (imagem → imagem); Regras; Economia de créditos (pedido do dono, 20/11/2026: "economizar o máximo, mas enfeitado; não usar o primeiro modelo"); Como tirar o máximo de cada crédito (preços medidos na conta em 20/11/2026).

Tamanho: 2465 palavras.

### [Banco de referências: planta que ganha vida em 3D](REFERENCIAS-BLUEPRINT.md)

Parte da pasta Animações 3D (`ANIMACOES-3D.md`). Pesquisa de 20/11/2026 (busca na web pelo TinyFish e biblioteca de ganchos virais da MinoAI Frontier). O 3D é o último passo (decisão do dono): este banco serve para quando ele for liberado e para os roteiros de agora. Acrescente aqui toda referência…

Seções: 1. As referências; 2. A anatomia do efeito (o que todos têm em comum); 3. Onde a nossa animação já está e o que falta; 4. Regras (Revisor de risco e Arquiteto); 5. Roteiro de 12 s revisado (para quando o 3D for liberado).

Tamanho: 1588 palavras.
