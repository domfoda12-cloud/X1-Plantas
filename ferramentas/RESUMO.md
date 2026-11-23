# Resumo: Código

> Os programas que validam as plantas e geram PDF, 3D, fichas e painel. **Leia este resumo primeiro**; abra um documento inteiro só quando a tarefa pedir. Índice geral: [`INDICE.md`](../INDICE.md). Quem lê: arquiteto, designer.

## O essencial

<!-- essencial: escrito à mão, o gerador não apaga -->
- Mudou `plantas.py` ou `ebook/plantas/projetos.py`: `python3 ferramentas/plantas.py validar` (0 erros), depois `python3 ferramentas/checar.py` (ferramentas/CLAUDE.md).
- `checar.py` confere sintaxe, skills, comandos e agentes, o `.claude/settings.json`, chave gravada no repositório (aviso, só arquivo:linha), tamanho dos contextos, índice e resumos e a regra das paredes, e **regrava** dados, fichas, módulos 3D, a calculadora do parceiro e a "Situação agora" do painel. O PDF ele só confere, numa pasta temporária (checar.py).
- Gerado, não edite à mão: `ebook/plantas/dados/*.json`, `ebook/plantas/PLANTAS.md` (`plantas.py fichas`), `video/src/plantas/<ID>.js`, a lista `CASAS` de `ebook/vendas/calculadora-lote.html`, `ebook/saida/` e a "Situação agora" do `PAINEL.md` (código).
- PDF de verdade: `python3 ebook/gerador/livro.py` grava `ebook/saida/ebook.pdf`, as plantas grátis e a calculadora; `--previa <pasta>` salva um PNG por página; `--conferir` não mexe em `ebook/saida`, mas regrava a calculadora (livro.py).
- "Situação agora" do painel conta pela coluna Situação do `ebook/catalogo.md` e pelos 5 arquivos em `animacoes-3d/plantas/<nome>/`, não pelas 24 casas validadas: por isso diz "0 de 12 prontas" (atualizar-painel.py).
- Mudou a geometria: `python3 ferramentas/imagens3d.py ID` refaz `ebook/visual/3d/<ID>.jpg`. Lê `video/src/plantas/<ID>.js`: rode `planta3d.py` antes (imagens3d.py).
- Medidas: casa por fora, cômodo por dentro. Parede externa tira 15 cm; interna, 6 cm por lado; passagem aberta, nada (plantas.py, `_desconto`).
- Mínimos em `MINIMOS_UTIL`; conforto em `CONFORTO_UTIL` (vira aviso). `MINIMOS` só serve às janelas automáticas. A regra da cidade manda (plantas.py).
- As regras são as de projeto do X1-Plantas, não revisão de arquiteto; nenhuma docstring pode dizer o contrário (plantas.py, projetos.py).
- Número ao público sai do validador com `PL.n0` (0,5 sobe). Textos das casas: `ebook/fichas/textos.py`; fixos: `ebook/gerador/paginas.py` (ebook/CLAUDE.md).
<!-- /essencial -->

## Os 17 programas

### [`ebook/fichas/textos.py`](../ebook/fichas/textos.py)

Textos de cada casa do e-book, escritos pelo método do Redator (.claude/agents/redator.md).

### [`ebook/gerador/livro.py`](../ebook/gerador/livro.py)

Gera o e-book "Que casa cabe no seu lote?" (PDF A4) a partir das 24 plantas validadas.

Funções: `m`, `m1`, `svg_planta`, `svg_fachada`, `svg_lote`, `icone`, `svg_fita`, `arquivo_foto`, `foto`, `fachada_bloco`, `capa_fundo`, `galeria`, `Livro`, `lote_frente`, `montar`, `melhor_lado`, `avisos_juntos`, `dupla`.

### [`ebook/gerador/paginas.py`](../ebook/gerador/paginas.py)

Textos fixos do e-book que o gerador (livro.py) usa: o aviso completo, os 7 erros, o glossário e a legenda de leitura.

### [`ebook/plantas/projetos.py`](../ebook/plantas/projetos.py)

As 24 plantas do 1º e do 2º lançamento, desenhadas pelas regras de projeto do X1-Plantas (não são projeto de arquiteto).

Funções: `todas`.

### [`ferramentas/atualizar-painel.py`](atualizar-painel.py)

Atualiza a seção "Situação agora" do PAINEL.md a partir dos arquivos do projeto.

Funções: `pasta_da_planta`, `ler_catalogo`, `ancoras`, `conferir_links`, `barra`, `montar_situacao`, `main`.

### [`ferramentas/checar.py`](checar.py)

Confere se o código do projeto tem erro, de uma vez só.

Funções: `rodar`.

### [`ferramentas/conversas.py`](conversas.py)

Escrito do zero; não usa nem contém código do cass (vetado pela licença, ficha 2151).

Funções: `sem_acento`, `mascarar`, `pasta_do_projeto`, `falas`, `buscar`, `testar`.

### [`ferramentas/guardar-pedido.py`](guardar-pedido.py)

Guarda cada prompt do dono, palavra por palavra, em pedidos/entrada/ (um arquivo por prompt).

### [`ferramentas/imagens2d.py`](imagens2d.py)

Imagens 2D das plantas para posts e anúncios (sem 3D): planta mobiliada, blueprint, vista da rua e casa no lote.

Funções: `pasta`, `quadro`, `main`.

### [`ferramentas/imagens3d.py`](imagens3d.py)

Gera a imagem "A casa em 3D" do e-book (ebook/visual/3d/<ID>.jpg) a partir do motor 3D.

Funções: `recortar`, `main`.

### [`ferramentas/mockups.py`](mockups.py)

Mockups do e-book no celular e B-roll do e-book folheado, em alta resolução.

Funções: `pagina`, `celular`, `fundo`, `colar`, `mockups`, `broll`.

### [`ferramentas/pedido.py`](pedido.py)

Fichas dos pedidos do dono: criar, listar, fechar e conferir (regras em pedidos/LEIA-ME.md).

Funções: `fichas`, `campo`, `trocar`, `ultimos_prompts`, `achar`, `nova`, `recado`, `listar`, `quadro`, `fechar`, `indice`, `conferir`.

### [`ferramentas/pesquisa.py`](pesquisa.py)

Caderno de pesquisa compartilhado: toda busca na web de qualquer agente fica em pesquisas/<tema>.md.

Funções: `arquivo`, `limpo`, `main`.

### [`ferramentas/planta3d.py`](planta3d.py)

Converte as plantas validadas (ebook/plantas/projetos.py) em módulos para o motor 3D.

Funções: `fechado`, `arestas`, `subtrair`, `unir`, `trecho_livre`, `construir`, `mobiliar`, `ordem`, `modulo`, `main`.

### [`ferramentas/plantas.py`](plantas.py)

Biblioteca e validador de plantas: as regras de projeto do X1-Plantas, em código.

Funções: `R`, `linha`, `coluna`, `area`, `lados`, `util`, `parede_comum`, `trecho_externo`, `F`, `H`, `V`, `monta`, `casa`, `auto_janelas`, `Relatorio`, `casa_fechada`, `validar`, `melhor_orientacao`.

### [`ferramentas/recortes.py`](recortes.py)

Recorta cada imagem final 4:5 em 9:16 (reel e story, 1080 x 1920 ou maior) e 1:1 (WhatsApp e feed), sem gerar de novo.

Funções: `main`.

### [`ferramentas/resumos.py`](resumos.py)

Gera o índice do projeto e o resumo de cada pasta de documentos, para os agentes lerem barato.

Funções: `rastreados`, `limpar`, `do_que_trata`, `ficha_md`, `ficha_py`, `essencial`, `docs_da`, `gerar`, `conferir`.
