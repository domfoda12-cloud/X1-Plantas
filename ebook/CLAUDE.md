# E-book: regras desta pasta

> O Claude Code carrega este arquivo sozinho quando trabalha aqui. As regras gerais estão no `CLAUDE.md` da raiz.

- **Gerar:** `python3 ebook/gerador/livro.py` (PDF só com as casas de `casas_lancamento` do `config.json` e as plantas grátis de `plantas_gratis`, em `ebook/saida/`; junto sai o PDF dos bônus, `bonus.pdf`, montado por `gerador/bonus.py` a partir dos dois `pedidos/anexos/bonus-*.md`, com os estilos presos em `.bn` no fim do `livro.css`); com `--previa <pasta>`, salva um PNG de cada página para conferir (as dos bônus em `<pasta>/bonus/`) e uma cópia dos 2 PDFs, numa pasta temporária: **não regrava** `ebook/saida/` nem a calculadora (o mesmo vale para `--conferir`). O PDF oficial e a calculadora só são gravados sem `--previa` e sem `--conferir`.
- **E-book em duas partes (só prévia):** `python3 ebook/gerador/livro.py --previa <pasta> --duas-partes` (casas pela frente do lote; parte 1, cada casa, com 2 páginas "cômodo a cômodo" depois da dupla dela: texto em `paginas.py` (`COMODOS`), desenho em `paginas_comodo` do `livro.py`, estilos presos em `.ca` no fim do `livro.css`; parte 2, casas em geral, com a aba azul; sumário na página 2). Sem `--previa`, recusa: não grava `ebook/saida/` nem a calculadora.
- **Opção desconhecida** (ex.: `--help`): o `livro.py` recusa e não gera nada (26/11: `--help` tinha regravado `ebook/saida/`); o `checar.py` confere.
- **A Placa (só prévia):** `--previa <pasta> --placa`; estilos em `gerador/placa.css`, falas em `PLACAS` (`paginas.py`). Sem `--previa`, recusa.
- **Página estourada é erro:** o detector mede em modo de impressão. O aviso legal ("Planta de referência…") nunca pode ficar coberto.
- **Números vêm do validador**, arredondados com `PL.n0` (0,5 sobe; a mesma função no PDF, nas fichas, na calculadora e nas imagens), nunca digitados à mão. Textos das casas: `fichas/textos.py`; textos fixos: `gerador/paginas.py`. Toda mudança de texto passa pelo Revisor de risco.
- **Imagens:** foto de fachada em `visual/openart/fachadas/` (só 3 casas: C03, E07, F01); casa em 3D em `visual/3d/` (do motor próprio). Toda imagem bate com a planta: porta e janelas no mesmo lugar.
- **A calculadora do parceiro** (`vendas/calculadora-lote.html`) tem a lista de casas reescrita pelo `livro.py` a cada geração oficial (sem `--previa` e sem `--conferir`): não edite a lista à mão.
- **Imagem 3D de uma casa:** `python3 ferramentas/imagens3d.py ID`.
- Faltam no `config.json` os campos do dono: o título (fica o atual até ele escolher), o WhatsApp e a promessa de atualização. Preço (R$ 47, que o PDF não imprime) e bônus (em `bonus.pdf`) já estão.
