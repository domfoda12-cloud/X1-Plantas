# Contexto do Designer

> Só o que importa para este papel. **Antes de trabalhar, leia o [quadro](QUADRO.md).** O resumo geral está em [`CONTEXTO.md`](../CONTEXTO.md); o histórico completo, em [`CONTEXTO-HISTORICO.md`](../CONTEXTO-HISTORICO.md) (abra só se precisar de um detalhe antigo). O resumo da última tarefa: [`entregas/ULTIMO.md`](entregas/ULTIMO.md), só se a sua tarefa continua a anterior.

## Decisões do dono que valem para você
- A MinoAI Frontier é o Diretor também da imagem: puxe a ideia principal dela antes de propor (22/11/2026).
- Imagem parada (capa, página, carrossel, post, capa do reel) é sua; o que se move é do Editor de vídeo (22/11/2026).
- **Quem faz o quê na equipe e o que cada um acrescenta a cada prompt:** [`EQUIPE.md`](EQUIPE.md) (22/11/2026).

- Qualidade máxima na peça final: imagem final em 4K extra-alta a partir do rascunho aprovado; "max" só na imagem principal.
- O dono quer o e-book "mais inovador": capa com fita métrica, a casa dentro do lote, ficha no estilo da tabela nutricional.
- Animações 3D completas ficam por último; as imagens 3D estáticas já entraram no e-book.

## Em aberto com você

- Foto realista de fachada existe em 3 casas (C03, E07, F01); as outras 21 usam o desenho (a da C01 saiu em 22/11, era a casa antiga). Fazer as 20 gasta créditos do OpenArt: decisão do dono.
- Imagens 2D dos posts e as imagens dos carrosséis: apagadas em 22/11/2026 para refazer do zero; volta pelo git (commit 079dae7). Refazer com as plantas atuais quando a frente de imagens abrir.
- Título, bônus e contato do e-book ainda são espaço reservado na página 61.

## Onde olhar

sistema visual `ebook/referencias/VISUAL.md` (seção "Linguagem, visual e animação do e-book"), gerador `ebook/gerador/livro.py`, referência `ebook/referencias/VISUAL.md` (seção "Referência: livros de plantas com 3D e um guia de apresentação").

## Leia barato

Os nove fios do que o dono quer estão em [`dono/IDEIAS-GERAIS.md`](dono/IDEIAS-GERAIS.md). Primeiro o resumo da pasta; o documento inteiro só quando a tarefa pedir. Seus resumos: [Produto: o e-book](../ebook/RESUMO.md), [Instagram](../instagram/RESUMO.md), [Animações 3D e imagens](../animacoes-3d/RESUMO.md). Tudo: [`INDICE.md`](../INDICE.md).

## Lições

O que deu errado e não pode voltar (uma linha cada, com data; vem das auditorias e das correções do dono).
- **23/11, dono:** Imagens de teste do gerador ficaram no repositório, e o dono mandou apagar quando soube o que eram. Teste fica fora do repositório ou sai ao terminar; só fica o que tem função. Vale também para clipe de teste (leitura nossa da fala de 21/11)
- **26/11, fluxo:** (pagina-ebook) Ao fundir dois textos aprovados num só, confira que a frase que era condição do Revisor sobreviveu inteira (aqui: menos ar, e o engenheiro confere se ventilação e luz bastam), não só os números.
- **26/11, fluxo:** (pagina-ebook) Espessura de parede só se imprime depois de conferir o desconto dos dois lados no validador: quando a linha encosta na varanda, ela não é a interna de 12 cm. Saída sugerida: 'na parede do quarto da frente', sem o número.
- **26/11, fluxo:** (pagina-ebook) Folha que continua outra ganha manchete própria com a conclusão dela (por exemplo, o que se decide nos 7 lugares), nunca só o sobretítulo repetido.
