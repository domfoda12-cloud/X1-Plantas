# Animações 3D

[Painel](../PAINEL.md) · Imagens e animações de cada planta, para o e-book, os posts e o vídeo.

**Por planta**, em `plantas/<nome>/`: `01-blueprint.png`, `02-planta-humanizada.png`, `03-perspectiva.png`, `04-perspectiva-lateral.png` (2000 x 2500) e `animacao.mp4` (12 s: o blueprint se desenha, a casa ganha vida e a câmera desliza). Pronta: `casa-compacta`.

**Código** (em `../video/`): dados da planta em `src/planta.js`, motor em `src/casa3d.js`, render com `node render-planta.cjs`.

**Falta para várias plantas:** um arquivo de dados por planta (cômodos, paredes, janelas, portas e móveis), nome e ficha vindo dos dados em vez de fixos, e render em lote. Sobrados, edícula e geminadas precisam de ajuste extra no motor.

**Cuidados:** só plantas originais; medidas provisórias até um arquiteto validar; móveis ilustrativos; não substitui projeto aprovado na prefeitura.
