# Planta grátis: o que a pessoa recebe depois do comentário "PLANTA"

> Material do funil, para o parceiro. Parte da pasta E-book: [`../EBOOK.md`](../EBOOK.md). Painel: [`../../PAINEL.md`](../../PAINEL.md).
>
> A planta grátis é **uma página do e-book**, igual às que a pessoa vai comprar. Assim ela vê exatamente o que o e-book entrega.

## 1. O que vai

**Um PDF só:** [`../saida/planta-gratis-C01.pdf`](../saida/planta-gratis-C01.pdf) (3 páginas, gerado por `python3 ebook/gerador/livro.py`). Ele traz:

| Página | O que tem |
|---|---|
| 1 | A Casa Compacta (C01) mobiliada, com áreas e cotas, "para quem é" e "erros que evita" |
| 2 | A casa no lote mínimo, a "Informação da casa", a vista da rua, a casa em 3D, "por que esta planta é assim" e as perguntas para o engenheiro |
| 3 | "No seu lote cabem mais casas": as outras casas do e-book que cabem num lote de 8 x 15, a fita métrica e o convite para mandar a medida do lote |

**Mande a casa que cabe no lote do cliente.** Há 5 plantas grátis prontas em `ebook/saida/` (lista em `ebook/config.json`, chave `plantas_gratis`):

| Lote do cliente (frente) | Planta grátis |
|---|---|
| 5 m | `planta-gratis-E03.pdf` (Casa Fita) |
| 7 m | `planta-gratis-E02.pdf` (Casa Corredor) |
| 8 m, quer 2 quartos | `planta-gratis-C01.pdf` (Casa Compacta) |
| 8 m, quer 3 quartos | **[a definir pelo dono]**: a E07 saiu da lista em 22/11, porque o arranjo dela (3 quartos em fila) está na fila do redesenho. Até lá, mande a C01 e pergunte se 2 quartos servem |
| 9 m ou mais, quer suíte | `planta-gratis-C06.pdf` (Casa Compacta Suíte) |
| 10 m ou mais, 3 quartos | `planta-gratis-F01.pdf` (Casa Família Compacta) |

Sem a medida do lote, mande a C01. Confira o fundo na [calculadora de lote](calculadora-lote.html).

**Não mande as imagens antigas** de `animacoes-3d/plantas/casa-compacta/` (03-perspectiva, animação etc.) nem o mockup `../visual/mockups/casa-c01-celulares.png`: são do desenho antigo da C01, de antes do redesenho de 22/11/2026. A imagem 3D atual de cada casa está em `../visual/3d/<ID>.jpg` e já sai dentro do PDF. Animação ainda não existe para nenhuma casa.

> A vista da rua da C01 é o desenho simplificado da planta atual. A foto antiga foi retirada.

## 2. Ficha da Casa Compacta (para mandar em texto)

**C01 · Casa Compacta** · 50 m² fechados · 2 quartos · 1 banheiro · lote a partir de 8 x 15 m (com recuos de referência; confira os da sua cidade) · melhor com a rua ao norte

**Para quem é:** casal com 1 ou 2 filhos que quer dois quartos, varanda na entrada e banheiro largo, sem corredor comprido.

**Por que esta planta é assim:**
- Sem corredor comprido: a sala distribui, e a circulação é só 4% da casa.
- A varanda cobre a porta da sala, protegida da chuva e do sol direto.
- O banheiro passa de 1,50 m de largura. Ele não encosta na cozinha nem no serviço: pede uma tubulação própria, que custa mais. Pergunte ao engenheiro quanto isso pesa no orçamento.

**Cuidados antes de construir:**
- Confira os recuos da sua prefeitura para o seu lote.
- Veja de que lado nasce o sol no seu terreno.
- A obra precisa de um profissional habilitado (arquiteto ou engenheiro).

> Planta de referência, não é projeto executivo. Os móveis são ilustrativos.

## 3. O convite no fim da planta grátis

A página 3 do PDF abre com **"Essa foi 1 de [nº de casas do e-book]"** (hoje 24; o número sai do PDF) e fecha com o convite:

> **Me fala a frente do seu lote.** Responde aqui no WhatsApp com a medida que eu te digo quais casas cabem nele com os recuos de referência. Os da sua cidade, você confirma na prefeitura.

Esse convite leva para a pergunta do terreno, que é o centro da [sequência do WhatsApp](sequencia-whatsapp.md). Fonte do texto: `gerador/livro.py`, função `montar_gratis`.
