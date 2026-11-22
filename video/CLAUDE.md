# Vídeo: regras desta pasta

> O Claude Code carrega este arquivo sozinho quando trabalha aqui. As regras gerais estão no `CLAUDE.md` da raiz.

- **Antes de mexer em qualquer vídeo, leia `VIDEO.md` inteiro.** Toda instrução nova do dono sobre vídeo entra lá na hora, com as palavras dele, e nunca sai sem ele mandar (ordem de 22/11/2026).
- **Prompt base das tomadas realistas (12 variáveis) e as regras do vídeo-convite** estão no `VIDEO.md`. **Passeio por dentro da casa:** `node render-passeio.cjs --planta ID` (caminho de cada casa em `CAMINHOS`; ilustração, não foto).
- **Sequência de escaneamento:** `python3 video/scan.py ID` gera `broll/clipes/scan-<id>.mp4` com os números do validador.
- **Referências:** `REFERENCIAS.md` (edição) e `REFERENCIAS.md` (formato). Sempre texto no primeiro quadro.
- **3D a partir da planta:** `node render-planta.cjs --planta ID --so-imagens` (imagens) ou sem `--so-imagens` (animação). Os módulos `src/plantas/*.js` saem de `python3 ferramentas/planta3d.py`. Não edite à mão.
- **Vídeo sem apresentador** (principal e prévia do WhatsApp): `python3 video/montar.py video/roteiros/<nome>.json`. Texto e cenas ficam no roteiro; o aviso legal sai em todas as cenas. Clipe novo entra comprimido em `broll/clipes/`.
- **Vídeos antigos:** apagados em 22/11 (git, commit 079dae7).
- **Música:** anúncio pago só com faixa licenciada ou a trilha nossa (`musica/gerar_trilha.py`, aprovada pelo Revisor em 21/11). Áudio dos modelos de vídeo é descartado. A trilha "lofi" do toolkit (ElevenLabs, licença não conferida) não vai em anúncio.
- **Edição final** é da MinoAI Frontier, no Mac do dono. **Gravação de páginas web** (calculadora, leitor do e-book): skill `product-demo`.
- **Condições do dono para todo vídeo (22/11/2026):**
  - **Antes de montar vídeo ou gastar crédito do OpenArt:** mandar o resumo da produção e a lista de instruções, e esperar o dono confirmar os dois.
  - **Ficha do pedido** (`ANUNCIO-LOCUCAO.md`): vai inteira em todo pedido a agente; a reconferência dela roda antes de cada etapa. **O destino do anúncio com locução é WhatsApp e Facebook Ads, não Instagram nem TikTok.**
  - **Prompt cinematográfico:** todo clipe usa os prompts de câmera de `principal-e07/PROMPTS.md`; prompt novo que der certo entra lá.
  - **Aviso legal pequeno, no canto da tela, parado. Sem o selo "Imagem ilustrativa"** (o dono tirou essa condição do Revisor).
  - **Recados no meio do trabalho entram todos juntos.**
