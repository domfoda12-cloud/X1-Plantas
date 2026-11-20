# Apostila do Arquiteto: o que as fontes brasileiras ensinam

> Pedido do dono (20/11/2026): "ensine mais ao arquiteto, use fontes brasileiras famosas para estudar". Esta apostila é leitura obrigatória do agente [`arquiteto`](../../.claude/agents/arquiteto.md) antes de criar ou mudar planta. As regras em uso estão em [`regras-do-arquiteto.md`](regras-do-arquiteto.md).
>
> Só entrou aqui o que foi lido na fonte (20/11/2026). Onde a fonte não foi lida, isso está dito.

## 1. As fontes

| Fonte | Quem | O que ensina | Lido? |
|---|---|---|---|
| **ABNT NBR 15220-3:2005**, Zoneamento bioclimático brasileiro e diretrizes para habitações unifamiliares de interesse social | ABNT; texto publicado pelo [LabEEE/UFSC](https://labeee.ufsc.br/sites/default/files/publicacoes/15220_3.pdf) | Divide o Brasil em 8 zonas e diz, para cada uma, o tamanho das aberturas, o sombreamento, a parede, a cobertura e a estratégia de conforto | Sim, o texto inteiro |
| **Nota técnica do LabEEE sobre a NBR 15575** (Sorgato, Marinoski, Melo, **Roberto Lamberts**) | LabEEE/UFSC, o laboratório de eficiência energética mais citado do país | Faixa de abertura para ventilação que dá melhor desempenho; o código municipal prevalece quando pede mais | Sim, as partes de abertura e sombreamento ([PDF](https://labeee.ufsc.br/sites/default/files/publicacoes/notas_tecnicas/NT_15575_FINAL.pdf)) |
| **ABNT NBR 15575-1, Anexo G** (informativo), Dimensões mínimas e organização funcional, lido pelo estudo de caso de habitação social em Porto Velho (RO) | Estudo publicado na Blucher Proceedings | Os móveis mínimos de cada cômodo e as folgas de circulação | Sim, o estudo ([PDF](https://proceedings.blucher.com.br/download-pdf/aplicabilidade-da-nbr-15575-habitao-de-interesse-social-quanto-funcionalidade-e-acessibilidade-das-reas-privativas-habitacionais-estudo-de-caso-porto-velho-ro-22617)). A norma original não foi lida |
| **João Filgueiras Lima, o Lelé** (1932–2014), arquiteto dos hospitais da Rede Sarah | Artigo "João Filgueiras Lima, Lelé: o conforto ambiental como o principal…", Revista Jatobá (UFG), 2022, com falas do próprio Lelé | Luz e ventilação naturais, a "grande sombra", o colchão de ar sob o telhado, vegetação e água | Sim ([PDF](https://revistas.ufg.br/revjat/article/download/74780/39353)) |
| **Eficiência Energética na Arquitetura**, Lamberts, Dutra e Pereira, 3ª ed., Eletrobras/Procel, 2014 | O livro-texto brasileiro de conforto e eficiência | Base teórica de tudo acima | **Não lido.** Download gratuito no [LabEEE](https://labeee.ufsc.br/sites/default/files/apostilas/eficiencia_energetica_na_arquitetura.pdf). Próxima leitura |
| **História da casa brasileira**, Carlos Lemos, Contexto, 1989 | Historiador da arquitetura (USP) | A tradição da casa brasileira: varanda, beiral, quintal | **Não lido.** Citado em várias teses; próxima leitura |

## 2. NBR 15220-3: o clima manda na janela

A norma diz, com todas as letras, que essas diretrizes "não têm caráter normativo, mas apenas orientativo". Ou seja: é a melhor referência técnica do país, mas não é lei; o código de obras da cidade é que obriga.

**Tamanho das aberturas para ventilação** (Anexo C, em % da área de piso dos cômodos de longa permanência: sala, dormitório e cozinha). Vale a abertura **efetiva**, a parte por onde o ar passa, e não o tamanho da janela:

| Abertura | % do piso |
|---|---|
| Pequena | 10% a 15% |
| Média | 15% a 25% |
| Grande | mais de 40% |

**O que cada zona pede** (Tabelas 1 a 24):

| Zona | Exemplo de cidade (Anexo A) | Abertura | Sombreamento | Parede / cobertura | Estratégia no verão |
|---|---|---|---|---|---|
| 1 | Curitiba, Caxias do Sul, Campos do Jordão | Média | Deixar o sol entrar no frio | Leve / leve isolada | (frio: aquecimento solar e massa térmica interna) |
| 2 | Três Corações (MG) | Média | Deixar o sol entrar no inverno | Leve / leve isolada | Ventilação cruzada |
| 3 | São Paulo, Belo Horizonte, Rio Grande | Média | Deixar o sol entrar no inverno | Leve refletora / leve isolada | Ventilação cruzada |
| 4 | Brasília | Média | Sombrear | Pesada / leve isolada | Massa térmica e ventilação seletiva |
| 5 | Santos, Morro do Chapéu (BA) | Média | Sombrear | Leve refletora / leve isolada | Ventilação cruzada |
| 6 | Goiânia | Média | Sombrear | Pesada / leve isolada | Massa térmica e ventilação seletiva |
| 7 | (semiárido e Centro-Oeste quente e seco) | **Pequena** | Sombrear | Pesada / pesada | Massa térmica e ventilação seletiva |
| 8 | Rio de Janeiro, Salvador, Recife, Fortaleza, Manaus, Belém | **Grande** | Sombrear | Leve refletora / leve refletora | Ventilação cruzada permanente |

Duas notas da zona 8 que valem para muita casa popular:
- Telha de barro sem forro é aceita na zona 8, desde que a telha não seja pintada nem esmaltada.
- O telhado pode ter transmitância maior se tiver aberturas de ventilação em pelo menos dois beirais opostos, ocupando toda a extensão das fachadas.

**O que isso muda no nosso trabalho:**
1. Nossa regra de janela com **1/6 do piso** mede o **tamanho da janela**. Uma janela de correr de duas folhas deixa passar o ar por mais ou menos metade dela, então a abertura efetiva fica perto de 8% do piso. Isso está dentro da faixa de melhor desempenho da nota do LabEEE (8% a 15%), mas abaixo do que a NBR 15220-3 sugere como "média" (15% a 25%) e muito abaixo da "grande" da zona 8.
2. **Para quem constrói em clima quente e úmido** (zona 8, boa parte do litoral do Nordeste, Norte e o Rio), o arquiteto da obra pode aumentar as janelas, usar veneziana ou janela de abrir por inteiro, beiral largo e ventilação no telhado. A planta aceita isso sem mudar as paredes.
3. **No Sul e em São Paulo** (zonas 1 a 3), o sol de inverno é bem-vindo: a orientação da sala e dos quartos para o norte pesa mais do que o tamanho da janela.

## 3. NBR 15575-1, Anexo G: o que tem que caber em cada cômodo

Móveis mínimos e folgas, como o estudo de Porto Velho lista a partir do Anexo G (informativo):

| Cômodo | Móveis (largura x profundidade, em metros) | Folga |
|---|---|---|
| Sala de estar | Sofá de 2 lugares com braço 1,20 x 0,70; estante ou armário para TV 0,50 x 0,80 | |
| Sala de estar e jantar | Mesa redonda para 4, diâmetro 0,95 | 0,75 m a partir da borda da mesa |
| Cozinha | Pia 1,20 x 0,50; fogão 0,55 x 0,60; geladeira 0,70 x 0,70 | 0,85 m livres na frente de pia, fogão e geladeira |
| Dormitório de casal | Cama 1,40 x 1,90; 2 criados 0,50 x 0,50; guarda-roupa 1,60 x 0,50 | 0,50 m entre móveis e paredes |
| Dormitório para 2 | 2 camas 0,80 x 1,90; criado 0,50 x 0,50; guarda-roupa 1,50 x 0,50 | 0,60 m entre as camas |
| Banheiro | Lavatório 0,39 x 0,29; vaso 0,60 x 0,60 | Largura mínima de 1,10 m (fora o box), segundo o estudo |
| Área de serviço | Tanque 0,52 x 0,53; máquina de lavar 0,60 x 0,65 | |
| Circulação (NBR 9050) | | Faixa livre de 0,90 m; giro de cadeira de rodas, círculo de 1,50 m |

**O que isso muda no nosso trabalho:**
1. O quarto de casal precisa de **1,40 + 0,50 + 0,50 = 2,40 m livres** para a cama com passagem dos dois lados. É exatamente o nosso limite de conforto (`CONFORTO_UTIL` no validador). As casas que o validador marca como apertadas (E02 e E03 com 2,30 m; as suítes da E01, E05 e E07) ficam abaixo desse folga: a cama vai encostada numa parede, e a ficha já avisa.
2. **Banheiro: atenção.** O estudo cita largura mínima de 1,10 m fora o box. Nossos banheiros de 1,20 m de eixo dão cerca de **1,08 m livres** com a parede de 12 cm do modelo. São 2 cm abaixo. Com bloco de 9 cm mais reboco a parede real fica perto de 14 cm, e aí a diferença aumenta. **Item aberto para o arquiteto registrado:** decidir se os banheiros passam a ter pelo menos 1,10 m livres. Hoje 19 das 24 casas têm um banheiro abaixo disso (C01, C03 a C07, E01, E02, E04, E05, E07, F02 a F05, S04, S05, S07 e S09). Não foi mudado no rascunho 1.
3. A cozinha linear tem de deixar **0,85 m livres** na frente da bancada. Numa cozinha de 1,80 m de largura, com bancada de 0,60 m, sobram cerca de 1,08 m livres, o que cumpre.
4. O motor 3D (`ferramentas/planta3d.py`) já põe esses móveis. O sofá passou a ter 3 tamanhos (2,10, 1,80 e 1,50 m); o mínimo do Anexo G é 1,20 m.

## 4. Lelé: luz, sombra e ar antes de máquina

Nas palavras dele (LIMA, 2008, citado pelo artigo):
- "O que me motivou foi a questão da humanização dos ambientes através da luz natural e da ventilação natural. Eu sempre achei que isso era mais sadio para o ser humano do que a iluminação artificial e o ar condicionado."
- "Para você se defender do calor o melhor lugar é embaixo de uma árvore. Então, o conceito básico ali é você criar uma grande sombra."
- "Entre a cobertura dos sheds e os basculantes fica um colchão de ar que atenua todas as ações de calor, e quanto maior esse espaço, melhor."

Segundo o artigo, ele também orientava as aberturas pelos ventos dominantes, para que funcionassem como captadores ou extratores de ar, e usava vegetação e água para criar um microclima mais ameno.

**O que isso muda numa casa térrea de autoconstrução:**
1. **A grande sombra:** beiral largo e varanda na fachada que pega o sol da tarde. Muitas plantas nossas já têm varanda na frente; a ficha pode dizer em que orientação ela mais rende.
2. **O colchão de ar:** forro mais telhado com ventilação nos beirais opostos. É a mesma solução que a NBR 15220-3 aceita na zona 8. É barato e deixa o quarto mais fresco do que qualquer janela maior.
3. **O vento entra por um lado e sai pelo outro:** janelas em paredes opostas. Hoje o validador não mede isso; é a próxima regra a acrescentar.
4. **A árvore no lote:** uma árvore no lado oeste do quintal sombreia a casa à tarde. Cabe como dica no e-book e na conversa com o comprador, sem promessa de temperatura.

## 5. O que o Arquiteto passa a fazer

1. **Antes de afirmar qualquer coisa sobre conforto** ("casa fresca", "ventilação cruzada"), conferir na planta: janelas em paredes opostas, tamanho efetivo da abertura, sombreamento. Sem isso, a frase não vai para o público.
2. **Quando o comprador disser a cidade**, achar a zona no Anexo A da NBR 15220-3 e dizer o que o arquiteto da obra pode ajustar: tamanho da janela, beiral, forro e telhado.
3. **Ao criar ou mudar uma planta**, conferir os móveis do Anexo G com as folgas (quarto de casal com 2,40 m livres, 0,85 m na frente da pia).
4. **Nunca citar uma norma como lei.** A NBR 15220-3 é orientativa, o Anexo G da NBR 15575 é informativo e o código de obras da cidade é o que obriga.

## 6. Próximas leituras

- Lamberts, Dutra e Pereira, *Eficiência Energética na Arquitetura*, 3ª ed. ([PDF gratuito](https://labeee.ufsc.br/sites/default/files/apostilas/eficiencia_energetica_na_arquitetura.pdf)).
- Carlos Lemos, *História da casa brasileira* (Contexto, 1989).
- Joana Perén Montero, *Ventilação e iluminação naturais na obra de João Filgueiras Lima, Lelé* (tese, USP, 2006) ([registro](https://repositorio.usp.br/item/001577631)).
- O texto oficial da NBR 15575-1 (Anexo G) e da NBR 9050, para conferir os números acima na fonte original.
