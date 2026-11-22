# Vídeo: regras desta pasta

> O Claude Code carrega este arquivo sozinho quando trabalha aqui. As regras gerais estão no `CLAUDE.md` da raiz.

- **Antes de mexer em qualquer vídeo, leia `PEDIDOS-DO-DONO.md` inteiro.** Toda instrução nova do dono sobre vídeo entra lá na hora, com as palavras dele, e nunca sai sem ele mandar (ordem de 22/11/2026).
- **Prompt base das tomadas realistas (12 variáveis) e as regras do vídeo-convite** estão no `PEDIDOS-DO-DONO.md`. **Passeio por dentro da casa:** `node render-passeio.cjs --planta ID` (caminho de cada casa em `CAMINHOS`; ilustração, não foto).
- **Sequência de escaneamento:** `python3 video/scan.py ID` gera `broll/clipes/scan-<id>.mp4` com os números do validador.
- **É a última frente** (e-book → animações → vídeo). O dono abriu em 21/11/2026 (principal e prévia).
- **Referência de edição do dono:** `REFERENCIA-CONDOR.md` (13 conceitos). Sempre texto no primeiro quadro.
- **3D a partir da planta:** `node render-planta.cjs --planta ID --so-imagens` (imagens) ou sem `--so-imagens` (animação). Os módulos `src/plantas/*.js` saem de `python3 ferramentas/planta3d.py`. Não edite à mão.
- **Vídeo sem apresentador** (principal e prévia do WhatsApp): `python3 video/montar.py video/roteiros/<nome>.json`. Texto e cenas ficam no roteiro; o aviso legal sai em todas as cenas. Clipe novo entra comprimido em `broll/clipes/`.
- **Os 5 anúncios em `saida/v1` a `v5` usam o 3D velho da C01:** refazer antes de usar.
- **Música:** anúncio pago só com faixa licenciada. A trilha "lofi" do toolkit de demonstração foi feita no ElevenLabs Music, e a licença para anúncio não foi conferida: não use em anúncio.
- **Edição final** é da MinoAI Frontier, no Mac do dono. **Gravação de páginas web** (calculadora, leitor do e-book): skill `product-demo`.
