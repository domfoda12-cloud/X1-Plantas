# Ferramentas: regras desta pasta

> O Claude Code carrega este arquivo sozinho quando trabalha aqui. As regras gerais estão no `CLAUDE.md` da raiz.

- **Mudou `plantas.py` ou `ebook/plantas/projetos.py`?** Rode, nesta ordem: `python3 ferramentas/plantas.py validar` (0 erros) e `python3 ferramentas/checar.py` (exporta, gera as fichas, o 3D, o PDF e a calculadora); depois veja se as imagens 3D e as fotos ainda batem com a planta.
- **Medidas:** casa por fora, cômodo por dentro (`PAREDE_EXT` 15 cm, `PAREDE_INT` 12 cm). Mínimos em `MINIMOS_UTIL`, conforto em `CONFORTO_UTIL`.
- **Antes de entregar:** `python3 ferramentas/checar.py` sem erro e `python3 ferramentas/atualizar-painel.py` com zero avisos.
- **Código enxuto:** skill `ponytail`. Revisão de mudança: `ponytail-review`.
- **O `checar.py` regenera** os dados (`exportar`), as fichas (`PLANTAS.md`), os módulos 3D, o PDF e a calculadora do parceiro, e falha se houver página estourada. Mudou a geometria de uma casa? Refaça a imagem 3D dela: `python3 ferramentas/imagens3d.py ID`.
