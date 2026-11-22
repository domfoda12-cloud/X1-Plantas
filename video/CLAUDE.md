# Vídeo: regras desta pasta

> O Claude Code carrega este arquivo sozinho quando trabalha aqui. As regras gerais estão no `CLAUDE.md` da raiz.

- **É a última frente** (e-book → animações → vídeo). O dono abriu em 21/11/2026 (principal e prévia).
- **Referência de edição do dono:** `REFERENCIA-CONDOR.md` (13 conceitos). Sempre texto no primeiro quadro.
- **3D a partir da planta:** `node render-planta.cjs --planta ID --so-imagens` (imagens) ou sem `--so-imagens` (animação). Os módulos `src/plantas/*.js` saem de `python3 ferramentas/planta3d.py`. Não edite à mão.
- **Vídeo sem apresentador** (principal e prévia do WhatsApp): `python3 video/montar.py video/roteiros/<nome>.json`. Texto e cenas ficam no roteiro; o aviso legal sai em todas as cenas. Clipe novo entra comprimido em `broll/clipes/`.
- **Os 5 anúncios em `saida/v1` a `v5` usam o 3D velho da C01:** refazer antes de usar.
- **Música:** anúncio pago só com faixa licenciada ou com a trilha original nossa (`musica/gerar_trilha.py`, 128 BPM, feita por síntese, sem samples; aprovada pelo Revisor em 21/11/2026). Áudio gerado pelos modelos de vídeo é descartado. A trilha "lofi" do toolkit de demonstração foi feita no ElevenLabs Music, e a licença para anúncio não foi conferida: não use em anúncio.
- **Edição final** é da MinoAI Frontier, no Mac do dono. **Gravação de páginas web** (calculadora, leitor do e-book): skill `product-demo`.
- **Condições do dono para todo vídeo (22/11/2026):**
  - **Antes de montar vídeo ou gastar crédito do OpenArt:** mandar o resumo da produção e a lista de instruções, e esperar o dono confirmar os dois.
  - **Ficha do pedido** (`PEDIDO-anuncio-locucao.md`): vai inteira em todo pedido a agente; a reconferência dela roda antes de cada etapa. **O destino do anúncio com locução é WhatsApp e Facebook Ads, não Instagram nem TikTok.**
  - **Prompt cinematográfico:** todo clipe usa os prompts de câmera de `principal-e07/PROMPTS.md`; prompt novo que der certo entra lá.
  - **Aviso legal pequeno, no canto da tela, parado. Sem o selo "Imagem ilustrativa"** (o dono tirou essa condição do Revisor).
  - **Recados no meio do trabalho entram todos juntos.**
