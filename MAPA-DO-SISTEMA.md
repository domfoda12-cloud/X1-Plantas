# Mapa do sistema: como uma parte alimenta a outra

> Em 22/11/2026 os vídeos, clipes e renders antigos foram apagados para refazer do zero (ficam no histórico do git); as pastas de saída abaixo voltam a encher quando os programas rodarem.
>
> Uma página para ver o projeto como um sistema: a planta entra, vira dados, e dos dados saem o PDF, o 3D, as imagens e o vídeo. Cada nome é um link para o arquivo, de propósito: é assim que o Graphify (e quem lê) enxerga as ligações que o código faz rodando um programa dentro do outro, e que não aparecem como `import`. **Programa novo entra aqui** (o `checar.py` confere). Onde ficam os documentos: [`INDICE.md`](INDICE.md).

## 1. A planta: de onde tudo sai

| Ordem | Arquivo | O que faz | Alimenta |
|---|---|---|---|
| 1 | [`ebook/plantas/projetos.py`](ebook/plantas/projetos.py) | as 24 plantas, em dados | 2 |
| 2 | [`ferramentas/plantas.py`](ferramentas/plantas.py) | valida as regras (medidas, janelas, lote, sol) e calcula as áreas | 3, 4, 5, 9 |
| 3 | [`ebook/plantas/dados/`](ebook/plantas/dados) e [`ebook/plantas/PLANTAS.md`](ebook/plantas/PLANTAS.md) | os números de cada casa (gerados: `plantas.py exportar` e `fichas`) | 5, 10, 13 |

## 2. O e-book

| Ordem | Arquivo | O que faz | Alimenta |
|---|---|---|---|
| 4 | [`ebook/fichas/textos.py`](ebook/fichas/textos.py) | o texto de cada casa | 5 |
| 5 | [`ebook/gerador/livro.py`](ebook/gerador/livro.py) | monta o e-book em HTML, com [`ebook/gerador/paginas.py`](ebook/gerador/paginas.py) (textos fixos) e [`ebook/config.json`](ebook/config.json) | 6, 7 |
| 6 | [`ebook/gerador/pdf.cjs`](ebook/gerador/pdf.cjs) | transforma o HTML em PDF e confere página estourada | [`ebook/saida/`](ebook/saida) (e-book e 5 plantas grátis) |
| 7 | [`ebook/vendas/calculadora-lote.html`](ebook/vendas/calculadora-lote.html) | a calculadora do parceiro; a lista de casas é reescrita pelo `livro.py` | funil no WhatsApp |

## 3. O 3D e as imagens

| Ordem | Arquivo | O que faz | Alimenta |
|---|---|---|---|
| 9 | [`ferramentas/planta3d.py`](ferramentas/planta3d.py) | converte cada planta num módulo do motor 3D | [`video/src/plantas/`](video/src/plantas) |
| 10 | [`video/src/casa3d.js`](video/src/casa3d.js) | o motor: blueprint, paredes subindo, casa mobiliada | 11, 12 |
| 11 | [`video/render-planta.cjs`](video/render-planta.cjs) (página [`video/src/casa.html`](video/src/casa.html)) | imagens e animação de cada casa | 12, `video/broll/clipes/` |
| 12 | [`ferramentas/imagens3d.py`](ferramentas/imagens3d.py) | recorta a imagem 3D de cada casa para o e-book | [`ebook/visual/3d/`](ebook/visual/3d) → 5 |
| 13 | [`ferramentas/imagens2d.py`](ferramentas/imagens2d.py) | planta, blueprint, vista da rua e lote em 2D, para posts | `animacoes-3d/plantas-2d/` → 15 |
| 14 | [`ferramentas/recortes.py`](ferramentas/recortes.py) e [`ferramentas/mockups.py`](ferramentas/mockups.py) | recortes 9:16 e 1:1 das fotos; e-book no celular e folheando | [`ebook/visual/`](ebook/visual) |
| 15 | [`instagram/posts/gerar-imagens.cjs`](instagram/posts/gerar-imagens.cjs) | as telas dos carrosséis | `instagram/posts/imagens/` |

## 4. O vídeo

| Ordem | Arquivo | O que faz | Alimenta |
|---|---|---|---|
| 16 | [`video/render-passeio.cjs`](video/render-passeio.cjs) ([`video/src/passeio.html`](video/src/passeio.html)), [`video/render-rua.cjs`](video/render-rua.cjs) ([`video/src/rua.html`](video/src/rua.html)) e [`video/scan.py`](video/scan.py) | passeio por dentro, vista da rua e o "escaneamento" | `video/broll/clipes/` |
| 17 | [`video/montar.py`](video/montar.py) | monta o vídeo a partir de um roteiro em [`video/roteiros/`](video/roteiros): cenas, texto, aviso, compressão | [`video/saida/`](video/saida) |
| 18 | [`video/musica/gerar_trilha.py`](video/musica/gerar_trilha.py) | a trilha nossa de 128 BPM | 17, 19 |
| 19 | [`video/principal-e07/montar_locucao.py`](video/principal-e07/montar_locucao.py), [`video/principal-e07/montar_e07.cjs`](video/principal-e07/montar_e07.cjs) e [`video/principal-e07/render_blueprint.cjs`](video/principal-e07/render_blueprint.cjs) | o anúncio da E07 com a voz do dono e o pacote da MinoAI Frontier | `video/saida/principal-e07/`, [`video/principal-e07/kit-minoai/`](video/principal-e07/kit-minoai) |

## 5. A conferência e a organização

| Arquivo | O que faz | Liga |
|---|---|---|
| [`ferramentas/checar.py`](ferramentas/checar.py) | roda tudo de uma vez e falha se algo quebrar | 2, 3, 5, 9, 21, 22, 23 |
| [`ferramentas/atualizar-painel.py`](ferramentas/atualizar-painel.py) (21) | conta casas, 3D, fotos, PDF e vídeos e escreve o [`PAINEL.md`](PAINEL.md) | dados, saídas |
| [`ferramentas/resumos.py`](ferramentas/resumos.py) (22) | gera o [`INDICE.md`](INDICE.md) e o `RESUMO.md` de cada pasta | todos os documentos |
| [`ferramentas/conversas.py`](ferramentas/conversas.py) | busca, só leitura, nas falas do dono nas conversas do Claude Code deste projeto, com máscara de dados (`buscar`, `testar`; o teste roda no `checar.py`) | `~/.claude/projects/<este projeto>/` (fora do repositório) |
| [`pedidos/anexos/conversas-para-o-autor.py`](pedidos/anexos/conversas-para-o-autor.py) | anexo, não roda no sistema: cópia limpa da busca nas conversas, para o e-mail ao autor do cass (ficha `2237`) | nada |
| [`ferramentas/salvar.py`](ferramentas/salvar.py) | salva e envia só com o `checar.py` verde (commit com atribuição, push na main e na branch) | git |
| [`ferramentas/placar.py`](ferramentas/placar.py) | placar do veto: soma as tabelas de veto das fichas de 23/11 em diante, as provas e as lições; `--conferir` no `checar.py` | [`contexto/PLACAR.md`](contexto/PLACAR.md) |
| [`ferramentas/pesquisa.py`](ferramentas/pesquisa.py) | caderno de pesquisa compartilhado: `buscar` antes da web, `nova` para registrar com fonte, `conferir` no `checar.py` | [`pesquisas/`](pesquisas) |
| [`ferramentas/pedido.py`](ferramentas/pedido.py) (23) e [`ferramentas/guardar-pedido.py`](ferramentas/guardar-pedido.py) | guardam cada prompt do dono e cuidam das fichas e da [`pedidos/FILA.md`](pedidos/FILA.md); o `licao` e o `fechar` gravam a lição no "Lições" do `contexto/<papel>.md` e no registro `pedidos/LICOES.md` | [`pedidos/`](pedidos), [`CONTEXTO-HISTORICO.md`](CONTEXTO-HISTORICO.md) |

## 6. As pessoas e as regras em volta

- **Regras de toda conversa:** [`CLAUDE.md`](CLAUDE.md) → [`CONTEXTO.md`](CONTEXTO.md), [`contexto/QUADRO.md`](contexto/QUADRO.md) e [`INDICE.md`](INDICE.md).
- **Pedidos do dono:** [`pedidos/LEIA-ME.md`](pedidos/LEIA-ME.md); o que liga um pedido ao outro: [`contexto/dono/IDEIAS-GERAIS.md`](contexto/dono/IDEIAS-GERAIS.md).
- **Quem decide e quem faz:** [`CONSELHO.md`](CONSELHO.md) e os agentes em [`.claude/agents/`](.claude/agents), cada um com o seu [`contexto/`](contexto/RESUMO.md). O que cada agente usa: [`ECOSSISTEMA.md`](ECOSSISTEMA.md).
- **Quem usa cada programa:** o Arquiteto (1 a 3, 9), o Redator (4, 7), o Designer (12 a 15), o Editor de vídeo e a MinoAI Frontier (16 a 19).
