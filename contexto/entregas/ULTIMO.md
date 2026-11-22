**Tarefa:** resolver as contradições entre documentos, montar o sistema de pedidos por modelo e reler todos os prompts do dono com "por que ele pediu?".
**Feito:** `pedidos/` (regras em `LEIA-ME.md`, fila em `FILA.md`, fichas em `2026-11/`); `ferramentas/pedido.py` e `guardar-pedido.py`; gancho em `.claude/settings.json`.
Agentes com modelo no cabeçalho (Opus; `pesquisador` no Sonnet; `ajudante` novo, no Haiku).
`contexto/dono/IDEIAS-GERAIS.md` (nove fios e o que o vídeo tem de ter) e `contexto/dono/intencoes/` (o porquê de cada prompt).
Documentos corrigidos em todas as pastas; apagados `ebook/PLANO-EBOOK.md`, `ebook/fichas/C01.md`, `video/roteiro-2-tres-quartos.md` e a nota `exigencias_legais.md`.
`ferramentas/atualizar-painel.py` conta pelos arquivos; `ebook/gerador/paginas.py` sem código morto; foto antiga de fachada da C01 fora do e-book (PDF gerado de novo).
**Como conferir:** `python3 ferramentas/checar.py`; `python3 ferramentas/pedido.py listar`; abrir `contexto/dono/IDEIAS-GERAIS.md`.
**Não feito / ressalva:** imagens e vídeos ainda com a C01 antiga (lista em `contexto/dono/TEXTOS-DESATUALIZADOS.md`). O Revisor não leu os textos de cada casa, a calculadora, os posts nem os roteiros. A divisão por modelo ainda não foi provada com o Haiku.
**Decisão do dono pendente:** as seis perguntas no fim de `IDEIAS-GERAIS.md`; preço, garantia, bônus, 12 ou 24 plantas.
**Próximo passo:** com as respostas do dono, remontar a prévia do WhatsApp e o anúncio pelas exigências de `IDEIAS-GERAIS.md`.
