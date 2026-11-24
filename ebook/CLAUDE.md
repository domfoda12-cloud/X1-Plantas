# E-book: regras desta pasta

> O Claude Code carrega este arquivo sozinho quando trabalha aqui. As regras gerais estão no `CLAUDE.md` da raiz.

- **Gerar:** `python3 ebook/gerador/livro.py` (PDF só com as casas de `casas_lancamento` do `config.json` e as plantas grátis de `plantas_gratis`, em `ebook/saida/`); com `--previa <pasta>`, salva um PNG de cada página para conferir, numa pasta temporária: **não regrava** `ebook/saida/` nem a calculadora (o mesmo vale para `--conferir`). O PDF oficial e a calculadora só são gravados sem `--previa` e sem `--conferir`.
- **E-book em duas partes (só prévia):** `python3 ebook/gerador/livro.py --previa <pasta> --duas-partes` (casas pela frente do lote; parte 1, cada casa, com 2 páginas "cômodo a cômodo" depois da dupla dela: texto em `paginas.py` (`COMODOS`), desenho em `paginas_comodo` do `livro.py`, estilos presos em `.ca` no fim do `livro.css`; parte 2, casas em geral, com a aba azul; sumário na página 2). Sem `--previa`, recusa: não grava `ebook/saida/` nem a calculadora.
- **Página estourada é erro:** o detector mede em modo de impressão. O aviso legal ("Planta de referência…") nunca pode ficar coberto.
- **Números vêm do validador**, arredondados com `PL.n0` (0,5 sobe; a mesma função no PDF, nas fichas, na calculadora e nas imagens), nunca digitados à mão. Textos das casas: `fichas/textos.py`; textos fixos: `gerador/paginas.py`. Toda mudança de texto passa pelo Revisor de risco.
- **Imagens:** foto de fachada em `visual/openart/fachadas/` (só 3 casas: C03, E07, F01); casa em 3D em `visual/3d/` (do motor próprio). Toda imagem bate com a planta: porta e janelas no mesmo lugar.
- **A calculadora do parceiro** (`vendas/calculadora-lote.html`) tem a lista de casas reescrita pelo `livro.py` a cada geração oficial (sem `--previa` e sem `--conferir`): não edite a lista à mão.
- **Imagem 3D de uma casa:** `python3 ferramentas/imagens3d.py ID`.
- O e-book está no rascunho 1 e fechado. Faltam os campos do dono em `config.json`: título, preço, bônus, WhatsApp e promessa de atualização.
