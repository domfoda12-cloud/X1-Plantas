# Resumo: Código

> Os programas que validam as plantas e geram PDF, 3D, fichas e painel. **Leia este resumo primeiro**; abra um documento inteiro só quando a tarefa pedir. Índice geral: [`INDICE.md`](../INDICE.md). Quem lê: arquiteto, designer.

## O essencial

<!-- essencial: escrito à mão, o gerador não apaga -->
- (falta escrever: os 5 a 10 fatos desta pasta que todo agente precisa saber)
<!-- /essencial -->

## Os 12 programas

### [`ebook/fichas/textos.py`](../ebook/fichas/textos.py)

Textos de cada casa do e-book, escritos pelo método do Redator (.claude/agents/redator.md).

### [`ebook/gerador/livro.py`](../ebook/gerador/livro.py)

Gera o e-book "Que casa cabe no seu lote?" (PDF A4) a partir das 24 plantas validadas.

Funções: `m`, `m1`, `svg_planta`, `svg_fachada`, `svg_lote`, `icone`, `svg_fita`, `arquivo_foto`, `foto`, `fachada_bloco`, `capa_fundo`, `galeria`, `Livro`, `lote_frente`, `montar`, `melhor_lado`, `avisos_juntos`, `dupla`.

### [`ebook/gerador/paginas.py`](../ebook/gerador/paginas.py)

Textos e modelos de cada página do e-book. Cada função devolve uma lista de páginas em HTML.

Funções: `ph`, `md`, `pagina`, `pg`, `numero_quartos`, `capa`, `capa_interna`, `como_usar`, `como_ler`, `sete_erros`, `indice`, `pagina_dupla`, `enchimento`, `terreno`, `proximos_passos`, `bonus`.

### [`ebook/plantas/projetos.py`](../ebook/plantas/projetos.py)

As 24 plantas do 1º e do 2º lançamento, desenhadas como um arquiteto organiza a casa.

Funções: `todas`.

### [`ferramentas/atualizar-painel.py`](atualizar-painel.py)

Atualiza a seção "Situação agora" do PAINEL.md a partir dos arquivos do projeto.

Funções: `pasta_da_planta`, `ler_catalogo`, `conferir_links`, `barra`, `montar_situacao`, `main`.

### [`ferramentas/checar.py`](checar.py)

Confere se o código do projeto tem erro, de uma vez só.

Funções: `rodar`.

### [`ferramentas/imagens2d.py`](imagens2d.py)

Imagens 2D das plantas para posts e anúncios (sem 3D): planta mobiliada, blueprint, vista da rua e casa no lote.

Funções: `pasta`, `quadro`, `main`.

### [`ferramentas/imagens3d.py`](imagens3d.py)

Gera a imagem "A casa em 3D" do e-book (ebook/visual/3d/<ID>.jpg) a partir do motor 3D.

Funções: `recortar`, `main`.

### [`ferramentas/mockups.py`](mockups.py)

Mockups do e-book no celular e B-roll do e-book folheado, em alta resolução.

Funções: `pagina`, `celular`, `fundo`, `colar`, `mockups`, `broll`.

### [`ferramentas/planta3d.py`](planta3d.py)

Converte as plantas validadas (ebook/plantas/projetos.py) em módulos para o motor 3D.

Funções: `fechado`, `arestas`, `subtrair`, `unir`, `trecho_livre`, `construir`, `mobiliar`, `ordem`, `modulo`, `main`.

### [`ferramentas/plantas.py`](plantas.py)

Biblioteca e validador de plantas: o ponto de vista do arquiteto, em código.

Funções: `R`, `linha`, `coluna`, `area`, `lados`, `util`, `parede_comum`, `trecho_externo`, `F`, `H`, `V`, `monta`, `casa`, `auto_janelas`, `Relatorio`, `casa_fechada`, `validar`, `melhor_orientacao`.

### [`ferramentas/recortes.py`](recortes.py)

Recorta cada imagem final 4:5 em 9:16 (reel e story, 1080 x 1920 ou maior) e 1:1 (WhatsApp e feed), sem gerar de novo.

Funções: `main`.
