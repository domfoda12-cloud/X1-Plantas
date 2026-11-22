# Resumo de passagem: e-book, rascunho 1 (20/11/2026)

**Tarefa:** fechar o rascunho 1 do e-book "Que casa cabe no seu lote?" (24 casas, 61 páginas, mais 6 PDFs de planta grátis).
**Feito:**
- Revisão final do Conselho (Revisor, Arquiteto, Redator) aplicada: paredes com espessura (`ferramentas/plantas.py`), desenhos de C03, E04, F02, S03 e S09 corrigidos (`ebook/plantas/projetos.py`), promessas vetadas retiradas (`ebook/gerador/paginas.py`, `livro.py`, `ebook/fichas/textos.py`).
- A casa em 3D entrou em cada página (`ebook/visual/3d/`, do motor `ferramentas/planta3d.py`); o sofá passou a ter três tamanhos.
- Porta e janelas da planta 2D vêm do motor 3D, iguais às da vista da rua; a foto da F01 perdeu duas aberturas falsas.
**Como conferir:** `python3 ferramentas/checar.py` (tudo certo) e `python3 ebook/gerador/livro.py` (sem aviso de página estourada).
**Não feito / ressalva:** o validador ainda não mede ventilação cruzada; 19 casas têm banheiro abaixo de 1,10 m livres; fotos de fachada só em 4 casas.
**Decisão do dono pendente:** título, preço, bônus, contato do parceiro, promessa de atualização; aplicar as correções da auditoria (calculadora do parceiro, `checar.py` sem o PDF).
**Próximo passo:** corrigir a calculadora do parceiro (`ebook/vendas/calculadora-lote.html`) gerando os dados a partir do validador.
