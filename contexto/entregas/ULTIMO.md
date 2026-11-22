**Tarefa:** guardar o prompt base de tomada realista com variáveis e fazer o vídeo-convite (passeio por dentro de uma casa, misturado com o estilo do principal).
**Feito:** `video/PEDIDOS-DO-DONO.md` (revisão de tudo o que o dono disse sobre vídeo, prompt base com 12 variáveis, regras do convite).
`video/render-passeio.cjs` e `video/src/passeio.html` (passeio na altura dos olhos, motor próprio; caminho por casa em `CAMINHOS`).
`video/scan.py` (escaneamento; a planta agora ocupa a tela em qualquer lote). `video/montar.py` ganhou `"leve": true`.
`video/roteiros/convite.json` → `video/saida/convite/x1-plantas-convite.mp4` (26 s, F03 Casa Família, sem OpenArt).
**Como conferir:** `cd video && node render-passeio.cjs --planta F03 --vel 1.3 && cd .. && python3 video/montar.py video/roteiros/convite.json`; assistir.
**Não feito / ressalva:** é ilustração 3D, não foto, e 1080 × 1920, não 4K. Sem música (Mac). Revisor de risco não viu. O principal com a E07 segue rascunho.
**Decisão do dono pendente:** o que é "pagar por mais"; se "motor art" era o motor próprio ou o OpenArt; E07 ou outra casa no principal; quando filma.
**Próximo passo:** ouvir o dono; mandar a lista de planos para a filmagem com o celular.
**Outra entrega do mesmo dia (anúncio com a E07 e locução, da frente de vídeo):** `contexto/entregas/2026-11-22-0010-anuncio-ebook-locucao.md`.
