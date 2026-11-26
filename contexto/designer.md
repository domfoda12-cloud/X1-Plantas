# Contexto do Designer

> Só o que importa para este papel; as regras fixas estão no seu arquivo de agente. **Antes de trabalhar, leia o [quadro](QUADRO.md).** Resumo geral: [`CONTEXTO.md`](../CONTEXTO.md); histórico, só para detalhe antigo: [`CONTEXTO-HISTORICO.md`](../CONTEXTO-HISTORICO.md). Resumo da última tarefa: [`entregas/ULTIMO.md`](entregas/ULTIMO.md), só se a sua continua a anterior.

## O que está decidido

- O Diretor (MinoAI Frontier) dá a ideia principal também da imagem; imagem parada é sua, o que se move é do Editor de vídeo. Quem faz o quê: [`EQUIPE.md`](EQUIPE.md) (dono, 22/11).
- Qualidade máxima na peça final: imagem final em 4K extra-alta a partir do rascunho aprovado; "max" só na imagem principal.
- O dono quer o e-book "mais inovador": capa com fita métrica, a casa dentro do lote, ficha no estilo da tabela nutricional.
- **O e-book à venda tem 3 casas** (C01, E03, F01; `ebook/config.json`); título "Antes do primeiro tijolo" (dono, 26/11 07:01), já no `config.json` com os bônus e o contato.
- **Identidade: a Placa** (dono, 26/11 06:44, ficha `2026-11-25-1613`): manual em `ebook/referencias/VISUAL.md`, seção 2; só na prévia (`--previa <pasta> --duas-partes --placa`) até o "gera" do dono; falas das placas são do Caio.
- Animações 3D completas ficam por último; as imagens 3D estáticas já entraram no e-book.

## Antes de dizer que a página está pronta

A lista que o fluxo `pagina-ebook` manda a autora conferir, item por item:
1. Prévia numa pasta fora do repositório e `fluxo.py pagina` sem erro; o teste sai ao terminar (dono, 23/11; auditoria da Olga, 26/11).
2. Folha que continua outra tem manchete própria com a conclusão dela, nunca só o sobretítulo repetido (fluxo, 26/11, pág. 11 da C01).
3. Número da lista que mora em outra folha fica no lugar dele ("4 · Hall, na pág. 10"); nunca pula em silêncio (fluxo, 26/11).
4. Cada fato uma vez na folha, onde pesa mais; nota que vale para o par entra só na primeira folha (fluxo, 26/11: a veneziana 3 vezes, a alvenaria nas duas folhas).
5. No pé, um estilo só de caixa de apoio, na letra e na cor do corpo; aviso que importa não fica em cinza pequeno (fluxo, 26/11: 5 estilos empilhados).
6. Ao fundir dois textos aprovados, a condição do Revisor sobrevive inteira, não só os números; e a conferência do `livro.py` passa a conferir o texto novo sem afrouxar (fluxo e dono, 26/11: a veneziana perdeu "menos ar" e o que o engenheiro confere).
7. Espessura de parede só se imprime depois de conferir no validador o desconto dos dois lados; a linha que encosta na varanda não é a interna de 12 cm. Na dúvida, "na parede do quarto da frente", sem o número (fluxo, 26/11).
8. A voz do Lote só na placa e na tira; o aviso e o selo "Imagem ilustrativa" inteiros, sem nada por cima (dono, 26/11; regra fixa).

## Em aberto com você

- **A Placa no PDF oficial** espera o "gera" do dono; falta ele dizer se "tudo o que criamos" inclui WhatsApp e Instagram de IA (ficha `1613`).
- **Propostas da passada do e-book guardadas para você** ([`passada-do-ebook-2026-11-26.md`](../pedidos/anexos/passada-do-ebook-2026-11-26.md), itens 4 a 10; a faixa de recuo da capa e da pág. 16, no item 3, esperava a identidade, que já veio).
- Foto realista de fachada existe em 3 casas (C03, E07, F01; `ebook/visual/openart/fachadas/`); das 3 à venda, só a F01; as outras, desenho. Fazer mais gasta créditos do OpenArt: decisão do dono.
- Imagens 2D dos posts e dos carrosséis: apagadas em 22/11 (voltam pelo git, commit 079dae7); refazer com as plantas atuais quando a frente de imagens abrir.
- O que falta no plano com o seu nome: [`pedidos/PLANO.md`](../pedidos/PLANO.md) (D27 nome e licença das letras, D45 "Como mobiliar", D11 posts, D24 telas da prévia).

## Onde olhar

`ebook/referencias/VISUAL.md`: o sistema e a Placa (seção "Linguagem, visual e animação do e-book") e os livros de referência (seção "Referência: livros de plantas com 3D..."). Gerador: `ebook/gerador/livro.py` e `placa.css`. Fluxos: `pedidos/fluxos/LEIA-ME.md`.

## Leia barato

Os nove fios do que o dono quer estão em [`dono/IDEIAS-GERAIS.md`](dono/IDEIAS-GERAIS.md). Primeiro o resumo da pasta; o documento inteiro só quando a tarefa pedir. Seus resumos: [Produto: o e-book](../ebook/RESUMO.md), [Instagram](../instagram/RESUMO.md), [Animações 3D e imagens](../animacoes-3d/RESUMO.md). Tudo: [`INDICE.md`](../INDICE.md).

## Lições

O que deu errado e não pode voltar (uma linha cada, com data; vem das auditorias e das correções do dono).
- **Lições antigas:** [`pedidos/historico/licoes-designer.md`](../pedidos/historico/licoes-designer.md), inteiras; leia antes de trabalho grande.
- **23/11, dono:** Imagens de teste do gerador ficaram no repositório, e o dono mandou apagar quando soube o que eram. Teste fica fora do repositório ou sai ao terminar; só fica o que tem função. Vale também para clipe de teste (leitura nossa da fala de 21/11)
