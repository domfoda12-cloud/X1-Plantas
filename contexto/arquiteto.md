# Contexto do Arquiteto

> Só o que importa para este papel; as regras fixas estão no seu arquivo de agente. **Antes de trabalhar, leia o [quadro](QUADRO.md).** Resumo geral: [`CONTEXTO.md`](../CONTEXTO.md); histórico, só para detalhe antigo: [`CONTEXTO-HISTORICO.md`](../CONTEXTO-HISTORICO.md). Resumo da última tarefa: [`entregas/ULTIMO.md`](entregas/ULTIMO.md), só se a sua continua a anterior.

## O que está decidido

- **O e-book à venda tem 3 casas** (C01, E03, F01; `ebook/config.json`, `casas_lancamento`); as 24 são o catálogo. As 3 foram refeitas pelo método novo, com mesa de 4 (23 e 24/11); refazer é uma por vez, com o máximo de cuidado (dono, 23/11).
- A voz da Placa (o Lote Carente) fica só nas placas: nunca na planta, na ficha, no aviso ou nos números (dono, 26/11, ficha `2026-11-25-1613`).
- A calculadora do lote é do dono, que atende o WhatsApp sozinho; os dados saem do validador (ficha `2026-11-26-0926`).
- Pesquisa a fundo vai ao `pesquisador`; você usa a conclusão dele (dono, 26/11). Quem faz o quê: [`EQUIPE.md`](EQUIPE.md).

## Antes de entregar o rascunho

A lista que o fluxo `planta` manda conferir, item por item:
1. `conferir-rascunho.py <arq.py> [variante]` com código 0 e "Passou nas conferências: 0 de N" (auditoria da Olga, 26/11: o fluxo dizia "pronto" com o programa quebrado).
2. A prévia olhada: porta, móvel e passagem não se batem (passo A6, 24/11: a porta nova batia na bancada).
3. O arranjo da apostila 2: caminho do dia, sem corredor se der, mesa, serviço nos fundos, banheiro por dentro (dono, 22/11).
4. O aviso ao comprador continua verdade com o desenho novo; se não, a frase nova entra no mesmo rascunho e passa na conferência junto (fluxo `planta`, 26/11: na C01V o aviso dizia "tracejada" com a parede já cheia).
5. Lado do sol, frente e lote, do `PLANTAS.md` ou do validador (26/11: a tabela do sol estava espelhada).
6. Nada em `projetos.py` nem em `ebook/saida/`. Pronto para aplicar ganha cópia em `pedidos/anexos/rascunhos-prontos/`, porque a pasta de rascunhos o git ignora (fluxo `planta`, 26/11). Aplicar é outro passo: validar, `checar.py` e o que arrasta junto (seu agente).

## Em aberto com você

- **C01V** (parede cheia da varanda da C01 na divisa): pronto para aplicar (`pedidos/anexos/rascunhos-prontos/C01V.py`), com a frase nova do aviso no rascunho. Espera a Vera fechar a frase (opções (a), (b) e (c) na rodada `pedidos/fluxos/rodadas/2026-11-26-084008-planta.json`). Ao aplicar: `projetos.py`, a frase e o comentário de `plantas.py`, a imagem 3D da C01 e o PDF.
- **Arranjo reprovado (22/11):** as 21 de fora do lançamento saem de 3 fôrmas, com corredor de fora a fora, e na série E (menos a E03 refeita e a E04) o banheiro só se alcança por fora. Método na apostila 2; refazer espera o dono dizer quais e quando.
- **Régua federal (Portaria MCID 725) e as 5 regras das 51 plantas de referência:** o que está fora em cada casa sai de `python3 ferramentas/plantas.py referencias` (`ebook/plantas/CONSERTOS.md`).
- Banheiros abaixo de 1,10 m livres (18 casas, contagem de 22/11) e nota de clima por zona bioclimática (janela maior, veneziana e beiral na zona 8): decidir ao refazer cada casa; a nota no e-book é do dono.
- Validador: ensinar a apontar arranjo ruim (apostila 2, seção 7) e a medir ventilação cruzada (ainda não mede); ler as fontes que faltam (seção 5).
- Imagens 2D dos posts e dos carrosséis: apagadas em 22/11 (voltam pelo git, commit 079dae7); refazer com as plantas atuais quando a frente de imagens abrir.
- Arquiteto registrado ainda não revisou as 24; ele confere as apertadas (E02, E03, suítes da E01, E05 e E07).

## Onde olhar

`ebook/referencias/ARQUITETO.md`: apostila 2 (arranjo), apostila 1 (clima e móveis) e "Regras de projeto". Fichas: `ebook/plantas/PLANTAS.md`. Validador: `python3 ferramentas/plantas.py validar`. Fluxos: `pedidos/fluxos/LEIA-ME.md`.

## Leia barato

Primeiro o resumo da pasta; o documento inteiro só quando a tarefa pedir. Seus resumos: [Produto: o e-book](../ebook/RESUMO.md), [Pesquisa e técnica](../ebook/referencias/RESUMO.md), [Código](../ferramentas/RESUMO.md). Tudo: [`INDICE.md`](../INDICE.md).

## Lições

Uma linha cada, com data.
- **Lições antigas:** [`pedidos/historico/licoes-arquiteto.md`](../pedidos/historico/licoes-arquiteto.md), inteiras; leia antes de trabalho grande.
