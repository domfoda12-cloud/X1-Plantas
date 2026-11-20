# Ferramentas: regras desta pasta

> O Claude Code carrega este arquivo sozinho quando trabalha aqui. As regras gerais estão no `CLAUDE.md` da raiz.

- **Mudou `plantas.py` ou `ebook/plantas/projetos.py`?** Rode, nesta ordem: `python3 ferramentas/plantas.py validar` (0 erros), `python3 ferramentas/plantas.py exportar`, `python3 ferramentas/planta3d.py`, gere o PDF de novo e veja se as imagens 3D e as fotos ainda batem com a planta.
- **Medidas:** casa por fora, cômodo por dentro (`PAREDE_EXT` 15 cm, `PAREDE_INT` 12 cm). Mínimos em `MINIMOS_UTIL`, conforto em `CONFORTO_UTIL`.
- **Antes de entregar:** `python3 ferramentas/checar.py` sem erro e `python3 ferramentas/atualizar-painel.py` com zero avisos.
- **Código enxuto:** skill `ponytail`. Revisão de mudança: `ponytail-review`.
- **Pendentes da auditoria de 20/11 (esperam o "sim" do dono):** a calculadora do parceiro gerada a partir do validador, e o `checar.py` gerando o PDF.
