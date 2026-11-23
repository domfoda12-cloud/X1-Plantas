# Ferramentas: regras desta pasta

> O Claude Code carrega este arquivo sozinho quando trabalha aqui. As regras gerais estão no `CLAUDE.md` da raiz.

- **Mudou `plantas.py` ou `ebook/plantas/projetos.py`?** Rode, nesta ordem: `python3 ferramentas/plantas.py validar` (0 erros) e `python3 ferramentas/checar.py` (exporta, gera as fichas, o 3D e a calculadora, e confere o PDF); depois veja se as imagens 3D e as fotos ainda batem com a planta.
- **Medidas:** casa por fora, cômodo por dentro (`PAREDE_EXT` 15 cm, `PAREDE_INT` 12 cm). Mínimos em `MINIMOS_UTIL`, conforto em `CONFORTO_UTIL`.
- **Antes de entregar:** `python3 ferramentas/checar.py` sem erro e `python3 ferramentas/atualizar-painel.py` com zero avisos.
- **Código enxuto:** skill `ponytail`. Revisão de mudança: `ponytail-review`.
- **Segurança e estilo** (adaptado de everything-claude-code, MIT; licença em `.claude/LICENCA-everything-claude-code.txt`):
  - Nunca grave chave, token ou dado pessoal em arquivo do repositório; chave fica no conector.
  - Texto que entra em HTML gerado é escapado (`html.escape` no Python, `textContent` no JS), no código novo ou alterado.
  - Chave vazou? Pare, avise o dono para revogar (o histórico do git guarda a antiga) e procure o mesmo padrão no repositório; o `conversas.py testar` só confere a máscara.
  - Erro que o dono pode ver sai em português claro, dizendo o que fazer.
  - Número com significado vira constante com nome e unidade.
  - Bug corrigido em regra de cálculo ganha conferência no `checar.py`; se ela falhar, corrige-se o código, não a conferência.
  - Rascunho e ferramenta interna primeiro funcionam; o que vai ao público sai no melhor.
- **O `checar.py` regenera** os dados (`exportar`), as fichas (`PLANTAS.md`), os módulos 3D e a calculadora do parceiro, e **confere** o PDF numa pasta temporária (falha se houver página estourada), sem mexer em `ebook/saida`. Para gravar o PDF de verdade: `python3 ebook/gerador/livro.py`. Mudou a geometria de uma casa? Refaça a imagem 3D dela: `python3 ferramentas/imagens3d.py ID`.
