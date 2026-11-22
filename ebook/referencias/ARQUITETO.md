# Apostila do Arquiteto

> As regras, as fontes brasileiras, os sites de profissionais e a pesquisa de layouts e etapas da obra. Juntado em 22/11/2026 (ficha de organizar os arquivos): cada seção é um documento antigo, inteiro.

<!-- era: ebook/referencias/ARQUITETO.md -->
## Regras de projeto: como o arquiteto decide cada planta

> Parte da pasta E-book ([`../EBOOK.md`](../EBOOK.md)). As regras estão em código em [`../../ferramentas/plantas.py`](../../ferramentas/plantas.py): cada planta só vira `dados` se passar pelo validador (`python3 ferramentas/plantas.py validar`).
>
> **São regras de referência.** Recuo, taxa de ocupação, iluminação e áreas mínimas mudam por cidade e por zona bioclimática (NBR 15220). Elas não substituem o código de obras local nem um projeto assinado por arquiteto ou engenheiro. Um arquiteto registrado deve revisar as 24 plantas e este texto antes da venda.

### 1. Dimensões (medidas **por dentro** das paredes)

Desde o rascunho 1, as medidas da casa são **por fora** e cada cômodo perde a parede por dentro: parede externa de 15 cm inteira, metade da interna de 12 cm (`PAREDE_EXT` e `PAREDE_INT` em `ferramentas/plantas.py`). Os mínimos abaixo (`MINIMOS_UTIL`) são de área e lado **livres**. Abaixo do limite de conforto (`CONFORTO_UTIL`), a casa passa com aviso para o engenheiro conferir a mobília.

| Cômodo | Mínimo livre (erro abaixo disso) | Conforto (aviso abaixo disso) | Origem |
|---|---|---|---|
| Sala | 8 m², lado 2,30 m | 9 m², lado 2,50 m | NBR 15575 Anexo G: sofá de 2 lugares 1,20 x 0,70 e estante |
| Quarto de casal | 7 m², lado 2,30 m | 8 m², lado **2,40 m** | Cama 1,40 + 0,50 + 0,50 de passagem (Anexo G) |
| Quarto | 6 m², lado 2,00 m | | Cama 0,80 x 1,90, guarda-roupa 1,50 x 0,50 |
| Cozinha | 4 m², lado 1,50 m | | 0,85 m livres na frente de pia, fogão e geladeira (Anexo G) |
| Banheiro | 1,8 m², lado 1,00 m | (estudo cita 1,10 m fora o box: ver a [apostila](ARQUITETO.md), seção 3) | Vaso 0,60 x 0,60, lavatório |
| Serviço | 1,5 m², lado 0,95 m | | Tanque 0,52 x 0,53 e máquina 0,60 x 0,65 |
| Circulação | 0,80 m livres; **no máximo 14%** da área | | Corredor não pode virar a casa |
| Casa acessível (S03) | Banheiro e circulação com **1,50 m livres** | | Giro de cadeira de rodas (NBR 9050); o resto da norma é do engenheiro |
| Pé-direito | 2,50 m em cômodo de permanência | | COE-SP; verificar no município |

### 2. Luz e ventilação

- Janela de **1/6 do piso** em sala, quarto e escritório; **1/8** em cozinha, serviço e banheiro (valores típicos de códigos de obras).
- Janela só em parede que dá para fora **e** que não seja a divisa. A parede da esquerda das plantas é divisa (sem janela), salvo as que declaram recuo dos dois lados.
- Banheiro sem janela só com exaustão mecânica (aparece como aviso, e nenhuma das 24 depende disso).
- **O clima manda na janela** (NBR 15220-3, orientativa): abertura **efetiva** de ventilação de 15% a 25% do piso nas zonas 1 a 6, pequena (10% a 15%) na zona 7 e grande (mais de 40%) na zona 8 (Rio, Salvador, Recife, Fortaleza, Manaus, Belém). Nossa janela de 1/6 do piso, de correr, dá perto de 8% de abertura efetiva: o arquiteto da obra aumenta a janela, usa veneziana e beiral onde o clima pede. Detalhes na [apostila](ARQUITETO.md), seção 2.

### 3. Circulação e privacidade

- **Todo cômodo é alcançável a partir da entrada.**
- **Quarto e banheiro social nunca ficam no caminho de outro quarto.** A suíte só se alcança pelo quarto.
- A circulação vem **depois** da zona social: sala e cozinha na frente, corredor no meio, quartos nos fundos.
- Banheiro social não abre direto para a cozinha.

### 4. Áreas molhadas juntas

Cozinha, serviço e banheiros ficam **encostados**, para uma prumada só (o encanamento mais barato). Quando um banheiro fica longe do núcleo molhado, o validador avisa. Hoje é o caso da suíte de E07, F03, F04 e S09, que a gente aceita porque a suíte pede privacidade, e do banheiro da C01 (redesenhada em 22/11/2026), que não encosta em cozinha, serviço nem outro banheiro e pede prumada própria. Nos dois casos custa mais tubulação: a ficha manda perguntar ao engenheiro quanto.

### 5. Vãos e estrutura

Cômodos de permanência com lado acima de 4,5 m pedem conferência de laje e vigas. O validador anota isso. A grade estrutural e o cálculo são do engenheiro.

### 6. O lote

Lote mínimo = largura da casa + recuos, e fundo = profundidade + recuo de frente + recuo de fundos. Usamos **frente 3 m, fundos 1,5 m, lateral direita 1,5 m e esquerda 0** (parede na divisa) salvo na casa estreita, que recua dos dois lados. O lote nunca pode ter menos de 5 m de frente (Lei 6.766/1979, art. 4º, II).

### 7. Orientação do sol (hemisfério sul)

Não existe orientação perfeita. O validador compara as quatro orientações da frente da casa e indica a melhor para as janelas daquela planta, assim:

- **Quarto:** sol da manhã (leste) é bom; sol da tarde (oeste) esquenta.
- **Sala:** norte tem sol durante boa parte do ano; leste é agradável pela manhã.
- **Cozinha:** sul e leste, sem sol forte.
- **Serviço:** oeste, para secar a roupa.

É um critério simplificado. Cada região tem sua zona bioclimática (NBR 15220) e cada terreno tem as suas sombras; o arquiteto da obra decide. O e-book mostra a recomendação e o **porquê**.

### 8. O que o validador confere (24 plantas, 0 erros)

Geometria sem sobreposição nem vão solto · dimensões mínimas · janelas (proporção e posição) · alcance a partir da entrada · circulação até 14% · privacidade · núcleo molhado · lote mínimo · orientação.
Rodar: `python3 ferramentas/plantas.py validar`. Desenhar: `python3 ferramentas/plantas.py previa`. Exportar JSON: `python3 ferramentas/plantas.py exportar`.

### 9. O que o validador NÃO faz

Não calcula estrutura, instalações, conforto térmico detalhado, taxa de ocupação nem coeficiente de aproveitamento do município. Não confere acessibilidade além do giro de 1,50 m da S03, nem a NBR 9050 inteira. Não mede ainda a ventilação cruzada (janelas em paredes opostas) nem a abertura efetiva por zona bioclimática. E não sabe o recuo da sua cidade.

### Fontes

Apostila com as fontes brasileiras lidas (NBR 15220-3, nota técnica do LabEEE/UFSC, Anexo G da NBR 15575, Lelé): [`ARQUITETO.md`](ARQUITETO.md). IBGE (Censo 2022); Lei 6.766/1979; Portaria MCID 725/2023; COE São Paulo 2017 e NBR 15575 (dimensões, pelo resumo de um arquiteto); Gelker Ribeiro, arquiteto, sobre orientação solar; NBR 15220 (zonas bioclimáticas). Confira os textos oficiais antes de afirmar em anúncio.

<!-- era: ebook/referencias/ARQUITETO.md -->
## Apostila do Arquiteto: o que as fontes brasileiras ensinam

> Pedido do dono (20/11/2026): "ensine mais ao arquiteto, use fontes brasileiras famosas para estudar". Esta apostila é leitura obrigatória do agente [`arquiteto`](../../.claude/agents/arquiteto.md) antes de criar ou mudar planta. As regras em uso estão em [`ARQUITETO.md`](ARQUITETO.md).
>
> Só entrou aqui o que foi lido na fonte (20/11/2026). Onde a fonte não foi lida, isso está dito.

### 1. As fontes

| Fonte | Quem | O que ensina | Lido? |
|---|---|---|---|
| **ABNT NBR 15220-3:2005**, Zoneamento bioclimático brasileiro e diretrizes para habitações unifamiliares de interesse social | ABNT; texto publicado pelo [LabEEE/UFSC](https://labeee.ufsc.br/sites/default/files/publicacoes/15220_3.pdf) | Divide o Brasil em 8 zonas e diz, para cada uma, o tamanho das aberturas, o sombreamento, a parede, a cobertura e a estratégia de conforto | Sim, o texto inteiro |
| **Nota técnica do LabEEE sobre a NBR 15575** (Sorgato, Marinoski, Melo, **Roberto Lamberts**) | LabEEE/UFSC, o laboratório de eficiência energética mais citado do país | Faixa de abertura para ventilação que dá melhor desempenho; o código municipal prevalece quando pede mais | Sim, as partes de abertura e sombreamento ([PDF](https://labeee.ufsc.br/sites/default/files/publicacoes/notas_tecnicas/NT_15575_FINAL.pdf)) |
| **ABNT NBR 15575-1, Anexo G** (informativo), Dimensões mínimas e organização funcional, lido pelo estudo de caso de habitação social em Porto Velho (RO) | Estudo publicado na Blucher Proceedings | Os móveis mínimos de cada cômodo e as folgas de circulação | Sim, o estudo ([PDF](https://proceedings.blucher.com.br/download-pdf/aplicabilidade-da-nbr-15575-habitao-de-interesse-social-quanto-funcionalidade-e-acessibilidade-das-reas-privativas-habitacionais-estudo-de-caso-porto-velho-ro-22617)). A norma original não foi lida |
| **João Filgueiras Lima, o Lelé** (1932–2014), arquiteto dos hospitais da Rede Sarah | Artigo "João Filgueiras Lima, Lelé: o conforto ambiental como o principal…", Revista Jatobá (UFG), 2022, com falas do próprio Lelé | Luz e ventilação naturais, a "grande sombra", o colchão de ar sob o telhado, vegetação e água | Sim ([PDF](https://revistas.ufg.br/revjat/article/download/74780/39353)) |
| **Eficiência Energética na Arquitetura**, Lamberts, Dutra e Pereira, 3ª ed., Eletrobras/Procel, 2014 | O livro-texto brasileiro de conforto e eficiência | Base teórica de tudo acima | **Não lido.** Download gratuito no [LabEEE](https://labeee.ufsc.br/sites/default/files/apostilas/eficiencia_energetica_na_arquitetura.pdf). Próxima leitura |
| **História da casa brasileira**, Carlos Lemos, Contexto, 1989 | Historiador da arquitetura (USP) | A tradição da casa brasileira: varanda, beiral, quintal | **Não lido.** Citado em várias teses; próxima leitura |

### 2. NBR 15220-3: o clima manda na janela

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

### 3. NBR 15575-1, Anexo G: o que tem que caber em cada cômodo

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
2. **Banheiro: atenção.** O estudo cita largura mínima de 1,10 m fora o box. Nossos banheiros de 1,20 m de eixo dão cerca de **1,08 m livres** com a parede de 12 cm do modelo. São 2 cm abaixo. Com bloco de 9 cm mais reboco a parede real fica perto de 14 cm, e aí a diferença aumenta. **Item aberto para o arquiteto registrado:** decidir se os banheiros passam a ter pelo menos 1,10 m livres. Hoje 18 das 24 casas têm um banheiro abaixo disso (C03 a C07, E01, E02, E04, E05, E07, F02 a F05, S04, S05, S07 e S09; conta de 22/11/2026 com as medidas livres de `plantas/dados/*.json`). A C01 saiu da lista no redesenho de 22/11/2026: o banheiro dela passa de 1,50 m.
3. A cozinha linear tem de deixar **0,85 m livres** na frente da bancada. Numa cozinha de 1,80 m de largura, com bancada de 0,60 m, sobram cerca de 1,08 m livres, o que cumpre.
4. O motor 3D (`ferramentas/planta3d.py`) já põe esses móveis. O sofá passou a ter 3 tamanhos (2,10, 1,80 e 1,50 m); o mínimo do Anexo G é 1,20 m.

### 4. Lelé: luz, sombra e ar antes de máquina

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

### 5. O que o Arquiteto passa a fazer

1. **Antes de afirmar qualquer coisa sobre conforto** ("casa fresca", "ventilação cruzada"), conferir na planta: janelas em paredes opostas, tamanho efetivo da abertura, sombreamento. Sem isso, a frase não vai para o público.
2. **Quando o comprador disser a cidade**, achar a zona no Anexo A da NBR 15220-3 e dizer o que o arquiteto da obra pode ajustar: tamanho da janela, beiral, forro e telhado.
3. **Ao criar ou mudar uma planta**, conferir os móveis do Anexo G com as folgas (quarto de casal com 2,40 m livres, 0,85 m na frente da pia).
4. **Nunca citar uma norma como lei.** A NBR 15220-3 é orientativa, o Anexo G da NBR 15575 é informativo e o código de obras da cidade é o que obriga.

### 6. Próximas leituras

- Lamberts, Dutra e Pereira, *Eficiência Energética na Arquitetura*, 3ª ed. ([PDF gratuito](https://labeee.ufsc.br/sites/default/files/apostilas/eficiencia_energetica_na_arquitetura.pdf)).
- Carlos Lemos, *História da casa brasileira* (Contexto, 1989).
- Joana Perén Montero, *Ventilação e iluminação naturais na obra de João Filgueiras Lima, Lelé* (tese, USP, 2006) ([registro](https://repositorio.usp.br/item/001577631)).
- O texto oficial da NBR 15575-1 (Anexo G) e da NBR 9050, para conferir os números acima na fonte original.

<!-- era: ebook/referencias/ARQUITETO.md -->
## Apostila 2 do Arquiteto: como arquiteto de verdade arma uma planta

> Pedido do dono (22/11/2026): "faça o Arquiteto estudar mais, o último layout não fazia sentido; mande ele procurar os sites que arquitetos de verdade usam no trabalho". Leitura obrigatória do agente [`arquiteto`](../../.claude/agents/arquiteto.md) antes de criar ou mudar planta, junto com a [apostila 1](ARQUITETO.md) (clima e móveis) e as [regras](ARQUITETO.md).
>
> A apostila 1 ensinou **medida**. Esta ensina **arranjo**: como os cômodos se ligam. Só entrou aqui o que foi lido ou visto na fonte em 22/11/2026. Onde a fonte não foi lida, isso está dito.

### 1. O que está errado hoje (diagnóstico)

As 24 plantas passam no validador, mas o validador só confere medida, janela e alcance. Ele não sabe se o arranjo faz sentido. Olhando as 24 prévias lado a lado:

| Problema | Onde | Por que não faz sentido |
|---|---|---|
| **Todas as casas saem da mesma fôrma** | `_compacta`, `_familia` e `_estreita` em [`projetos.py`](../plantas/projetos.py): C01, C04 a C07, E04, F01 a F04 eram a mesma casa esticada (diagnóstico de 22/11/2026; a C01 já foi redesenhada e saiu dessa fôrma) | Sala e cozinha na frente, uma faixa de corredor de fora a fora, quartos em fila atrás. O comprador que folheia vê uma planta só, 24 vezes |
| **Corredor que atravessa a casa inteira** | Compactas e família: 10% a 14% da área | A casa de referência do governo da Bahia (seção 3) tem 3 quartos e **zero** corredor. Numa casa de 55 m², 5 m² de corredor é meio quarto jogado fora |
| **Para ir do quarto ao banheiro, a pessoa sai da casa** | Toda a série E, menos a E04 (E01 a E03, E05 a E07): todo cômodo abre para o corredor lateral coberto | De noite, com chuva ou com criança pequena, isso não funciona. O validador marca "circulação 0%" porque o corredor é externo, e conta isso como vantagem |
| **Porta da rua abre em cima do sofá** | Quase todas | Quem entra cruza a sala na diagonal. O estudo da UFRGS (seção 4) mostra que linha de passagem cortando a sala é causa de insatisfação com o tamanho dela |
| **Sem lugar para a mesa** | Compactas: cozinha de 6 a 7 m² em corredor, sala só com sofá | A prefeitura de São Paulo exige mesa com tantas cadeiras quantos são os leitos (seção 2). Casa de 2 quartos é mesa para 4 |
| **Jantar fechado entre paredes, longe do fogão** | F02 | Sala de jantar separada é coisa de casa grande. Em casa popular a mesa fica na cozinha ou entre a cozinha e a sala |
| **Serviço espremido dentro da cozinha** | Compactas: tira de 4 m² com porta para a frente da casa | Nas casas de referência o tanque fica **nos fundos, do lado de fora, coberto**, com saída pela cozinha |
| **Sem varanda de entrada** | Maioria | A casa brasileira popular entra por uma varanda coberta. É a "grande sombra" do Lelé (apostila 1) e é o que o comprador reconhece como casa |

### 2. Prefeitura de São Paulo: Diretrizes de Projeto de HIS (SEHAB, abril de 2021)

Documento que a Secretaria de Habitação entrega aos escritórios contratados ([PDF](https://legislacao.prefeitura.sp.gov.br/leis/portaria-secretaria-municipal-de-habitacao-sehab-37-de-3-de-maio-de-2021/anexo/65301a9c1411920c1295e6d7/DiretrizesProjeto_Publicação_2021.pdf), Portaria SEHAB 37/2021). Lido o capítulo 3, "Unidade habitacional". É diretriz para obra da prefeitura de São Paulo, não lei para o resto do país.

- **3.1, item 1:** atenção especial à largura de cozinha, de área de serviço, de box e de corredor.
- **3.1, item 2:** o layout é definido com os móveis e os eletrodomésticos **desenhados**, nas medidas da NBR 15575.
- **3.1, item 3:** "conforme o número de leitos da unidade habitacional deve-se prever o mesmo número de mobiliários (ex. 4 leitos = mesa com 4 cadeiras = sala para 4 pessoas)".
- **3.1, item 4:** toda unidade deve ser adaptável para pessoa com deficiência (Lei 13.146/2015).
- **3.2, item 5:** "é proibido que seja necessário atravessar a área do boxe para acessar a bacia sanitária ou o lavatório".
- **3.2, item 10:** banheiro sempre com iluminação e ventilação.
- **3.4, item 4:** "tanques não devem ser confinados; devem dispor de espaços para a movimentação das pessoas no ato de lavar roupas".
- **3.5:** janela de dormitório com veneziana integrada; portas e janelas em medida padrão de mercado.

### 3. Governo da Bahia: projeto de referência de casa térrea (CAR, maio de 2024)

Projeto completo, assinado por arquiteto com registro no CAU, para o Minha Casa Minha Vida Rural: [pranchas da casa de 3 quartos](https://www.ba.gov.br/car/sites/site-car/files/2025-08/TODOS%20AS%20PLANTAS.pdf) e [memorial da casa de 2 quartos](https://www.ba.gov.br/car/sites/site-car/files/2025-08/MEMORIAL%20DESCRITIVO%20CASA%202%20QUARTOS.pdf). Vista a planta baixa (prancha ARQ 01/10) e lido o começo do memorial.

**Casa de 3 quartos: 64,82 m² construídos, 53,41 m² úteis, 10,04 x 7,06 m por fora.**

| Cômodo | Área | Como se chega |
|---|---|---|
| Varanda coberta | 5,47 m² | Da rua. Fica encaixada no meio da fachada, entre os dois quartos da frente |
| Sala | 14,66 m² (3,80 m de largura) | Pela varanda. Fica **no centro da casa** |
| Quartos 1 e 2 | 8,00 m² cada | Porta direto para a sala, um de cada lado |
| Quarto 3 | 5,47 m² | Porta direto para a sala |
| Sanitário adaptável | 5,47 m² | Porta direto para a sala, do lado oposto ao quarto 3 |
| Cozinha | 7,22 m² | Nos fundos, aberta para a sala por um vão de 1,40 m |
| Serviço | 6,06 m² | Fora da casa, coberto pelo beiral, com saída pela cozinha; tanque e máquina encostados na parede do banheiro |

**Casa de 2 quartos (memorial):** 51,34 m² construídos, 40,01 m² úteis. Quartos de 8,76 e 8,32 m², sala de estar e jantar de 13,34 m², sanitário adaptável de 4,52 m², cozinha de 5,07 m², serviço coberto de 2,13 m², varanda coberta de 4,90 m². Já vem com o estudo de ampliação: mais um quarto, e a casa vai a 48,71 m² úteis.

**O que essa planta ensina:**
1. **Corredor zero.** A sala é o centro e distribui. Toda a área paga vira cômodo.
2. **A varanda é a entrada**, e fica encaixada no volume da casa, sem aumentar o telhado.
3. **Cozinha nos fundos, aberta para a sala**, com a mesa no meio do caminho. Quem cozinha vê a sala e o quintal.
4. **Serviço do lado de fora, coberto**, colado no banheiro e na cozinha: uma parede hidráulica só.
5. **Banheiro grande (5,47 m²)**, porque já nasce adaptável. O nosso tem 2,5 m².
6. **A ampliação vem desenhada.**
7. **O preço disso:** as portas dos quartos e do banheiro dão para a sala. Privacidade menor em troca de área. É uma escolha, e a ficha da casa tem que dizer.

### 4. UFRGS: o que os moradores fazem com a planta depois (Reis e Lay, 2002)

"Tipos arquitetônicos e dimensões dos espaços da habitação social", Antônio Tarcísio Reis e Maria Cristina Lay, revista Ambiente Construído ([PDF](https://seer.ufrgs.br/index.php/ambienteconstruido/article/download/3441/1855/11807)). Levantamento de 374 moradias em 12 conjuntos da região de Porto Alegre, comparando o projeto original com a casa ocupada. Lidos o resumo e as seções de número de peças, áreas e sala.

- As casas térreas cresceram muito depois de ocupadas: a área construída aumentou cerca de 144% num conjunto e 153% em outro.
- O crescimento é **principalmente no setor de serviço, depois no social**: o morador acrescenta área de serviço, garagem, segundo banheiro e mais uma sala ou um jantar.
- O número de quartos quase não passa de 3; o que cresce é o tamanho do quarto de casal.
- Insatisfação com a sala aparece quando há **duas linhas de circulação atravessando a sala**. Os autores indicam sala de estar (ou estar e jantar) em torno de **10 m² para 3 pessoas** como mínimo.

**Para nós:** a ampliação que o comprador vai fazer é serviço, garagem e mais sala, antes de mais quarto. A planta precisa deixar o lugar disso livre no lote e dizer onde é.

### 5. Os sites que arquiteto usa (para as próximas leituras)

| Site | Para que o arquiteto usa | Lido? |
|---|---|---|
| Diretrizes de órgãos de habitação (SEHAB-SP, CAR-BA) | Regras e projetos de referência de casa popular | **Sim** (seções 2 e 3) |
| Revista Ambiente Construído (UFRGS/ANTAC) | Pesquisa sobre como a casa é usada depois de pronta | **Sim**, um artigo (seção 4) |
| [CDHU, Manual Técnico de Projetos](https://www.cdhu.sp.gov.br/documents/20143/37009/manual-de-projetos.pdf/31dc7a0a-f50c-cbf1-7ede-928708994547) | O manual de projeto de habitação mais usado em São Paulo | **Não.** O site estava em manutenção e devolveu a página inicial |
| [ArchDaily Brasil](https://www.archdaily.com.br/br/tag/habitacao-social), tag habitação social | Projetos construídos com planta, corte e texto do autor | **Não.** As plantas são imagem; só confirmei que as Casas Populares Paudalho (NEBR Arquitetura, 58 m², 2021) estão [publicadas lá](https://www.archdaily.com/971192/paudalho-popular-houses-nebr-arquitetura) |
| concursosdeprojeto.org | Pranchas dos premiados em concursos (CODHAB-DF e CDHU tiveram categoria de casa térrea) | **Não** |
| Vitruvius (Projetos e Arquitextos) | Crítica e projetos comentados | **Não** |
| CAU/BR, página de ATHIS | Assistência técnica para habitação popular (Lei 11.888/2008) | **Não** |
| Neufert, *Arte de projetar em arquitetura*; Panero e Zelnik, *Dimensionamento humano* | Os livros de medida que todo escritório tem | **Não** (livros pagos) |

### 6. O método, a partir de agora

Antes de escrever uma planta em `projetos.py`, o Arquiteto faz, nesta ordem:

1. **Parte de uma referência real.** Diz de qual projeto publicado a casa parte (órgão, concurso ou escritório) e o que mudou. Planta sem referência não entra.
2. **Desenha o caminho do dia:** rua → entrada → sala → cozinha → quintal; quarto → banheiro de madrugada; compras → cozinha; roupa suja → tanque → varal. Nenhum desses caminhos pode sair da casa, cruzar um quarto ou cortar a sala na diagonal.
3. **Tenta primeiro sem corredor.** Corredor só entra quando a privacidade pede (3 quartos ou suíte) e fica curto: um hall, não uma faixa de fora a fora.
4. **Põe a mesa.** Tantas cadeiras quantos são os leitos, desenhada, encostada na cozinha.
5. **Serviço nos fundos**, coberto, com saída pela cozinha e espaço para a pessoa ficar de pé no tanque.
6. **Entrada por varanda ou por um canto da sala**, nunca em cima do sofá.
7. **Banheiro:** ninguém atravessa o box para chegar ao vaso ou à pia; chega-se a ele por dentro de casa.
8. **Ampliação desenhada:** onde entram serviço maior, garagem e o cômodo a mais.
9. **Cada casa é uma casa.** Duas plantas do e-book não podem ser a mesma fôrma com outra medida. Se forem, uma delas sai.
10. **Só então** roda o validador. Passar no validador é o mínimo, não a prova de que a planta é boa.

### 7. O que falta decidir e fazer

- **Refazer as plantas** com este método (decisão do dono: quais e quando). Sugestão de ordem: série E (banheiro por fora), depois as compactas (corredor e mesa), depois a F02.
- **Ensinar o validador** a apontar: banheiro ou quarto que só se alcança por fora, corredor acima de 6% em casa de até 60 m², falta de mesa, duas casas com o mesmo arranjo.
- **Ler** o manual da CDHU, as pranchas de concurso e 5 projetos do ArchDaily com a planta aberta.

<!-- era: ebook/referencias/ARQUITETO.md -->
## Pesquisa: como é a casa popular brasileira e os grandes passos para construir

> Pedido do dono (22/11/2026): "procure coisas relevantes para o projeto, como layouts de casas no Brasil e os grandes passos necessários para construir a casa". Parte da pasta E-book ([`../EBOOK.md`](../EBOOK.md)). Continua a [apostila 2 do Arquiteto](ARQUITETO.md).
>
> Busca feita em 22/11/2026 (busca na web comum, sem ferramenta paga). Cada número traz a fonte. Onde a fonte é blog comercial e não documento oficial, isso está dito. **Nada daqui vai ao público sem passar pelo Redator e pelo Revisor de risco.**

### 1. O layout mínimo que o governo federal exige (fonte oficial)

**Portaria MCID 725/2023**, versão compilada com alterações até março de 2026 ([PDF](https://www.gov.br/cidades/pt-br/acesso-a-informacao/institucional/base-juridica/portarias/2023/Port.MCIDn725_2023COMPILADA.pdf)), Anexo de especificações da unidade habitacional, item 2, "Programa de necessidades". É a regra das casas do Minha Casa Minha Vida (faixa subsidiada). **Não é lei para a casa particular**, mas é o padrão de casa popular mais atual do país, e foi escrita por quem aprova milhares de plantas.

| Item | O que a portaria pede |
|---|---|
| Área útil mínima da casa | **40 m²**, sem contar as paredes |
| Pé-direito | 2,55 m (2,30 m no banheiro) |
| Programa mínimo | Sala + quarto de casal + quarto para duas pessoas + cozinha + área de serviço + banheiro |
| Área de cada cômodo | Não tem mínimo: quem manda é o **móvel que tem de caber** |
| Quarto de casal | Cama 1,40 x 1,90, mesa de cabeceira 0,50 x 0,50, guarda-roupa 1,60 x 0,50; 0,50 m de passagem |
| Quarto para duas pessoas | 2 camas de **0,90** x 1,90, guarda-roupa 1,50 x 0,50; **0,80 m entre as camas** |
| Cozinha | **Largura mínima de 1,80 m**; pia 1,20 x 0,50, fogão, geladeira 0,70 x 0,70 |
| Sala de estar e refeições | **Largura mínima de 2,40 m**; sofá com **tantos assentos quantos são os leitos**, **mesa para 4** e estante de TV |
| Banheiro | **Largura mínima de 1,50 m**; lavatório, vaso e box de 0,90 x 0,95; giro de cadeira de rodas de 1,50 m |
| Área de serviço | Tanque e máquina de lavar, com acesso de frente ao tanque |
| Acessibilidade | 1,20 m livres na frente das portas; a casa é adaptável sem mexer em parede |
| Portas | Vão de 0,80 x 2,10 m em todas. **Em casa, pelo menos duas portas de acesso: a da sala e a de serviço, na cozinha ou na área de serviço** |
| Janelas | Dormitório com veneziana; nas zonas bioclimáticas 5 e 6, sombreamento na abertura da sala |
| Norte e Nordeste | Ganchos de rede nos dormitórios |

#### As nossas 24 plantas contra essa régua

Conta feita sobre os dados das plantas (`ebook/plantas/dados/`), descontando 12 cm de parede do lado menor de cada cômodo. É aproximação: o número exato é do validador.

| Régua federal | Casas nossas abaixo dela |
|---|---|
| Banheiro com 1,50 m de largura | **21 de 24** têm ao menos um banheiro abaixo. A maioria tem perto de 1,08 m. Só C01, E03 e S03 passam (conta refeita em 22/11/2026, depois do redesenho da C01, com as medidas livres de `plantas/dados/*.json`) |
| Cozinha com 1,80 m de largura | 3: C04, C05 e S04 (perto de 1,68 m) |
| Quarto para duas camas (0,90 + 0,80 + 0,90 = 2,60 m) | 6: E02, F03, F04, F05, S07 e S09 (perto de 2,48 m) |
| Sala com 2,40 m de largura | Nenhuma |
| Mesa para 4 na sala ou na cozinha | Não medido; nas compactas não cabe (ver a apostila 2) |
| Porta de serviço além da porta da sala | Não medido |

**Leitura:** o banheiro é o ponto mais fraco das nossas plantas. O item que já estava aberto ("banheiros abaixo de 1,10 m": hoje 18 casas, depois do redesenho da C01) é maior do que parecia: a régua federal atual é 1,50 m.

### 2. Como é a casa popular que arquiteto projeta

- **Casa de referência do governo da Bahia** (CAR, 2024): sala no centro, sem corredor, varanda de entrada, cozinha nos fundos aberta para a sala, serviço coberto do lado de fora. Detalhes na [apostila 2](ARQUITETO.md), seção 3.
- **Casas Populares Paudalho**, NEBR Arquitetura (PE, 2021): 58 m², em lotes de 8 x 20 m, obra de 120 dias com mão de obra local, segundo a [Dwell](https://www.dwell.com/home/paudalho-popular-houses-ca1b6f36) e o [ArchDaily](https://www.archdaily.com/971192/paudalho-popular-houses-nebr-arquitetura). A planta não foi lida (é imagem).
- **O que os moradores mudam depois** (UFRGS, 374 moradias): ampliam primeiro serviço, garagem e sala. Apostila 2, seção 4.

**O que o mercado de plantas prontas oferece** (anúncios e blogs, sem número de venda): títulos pela medida do lote ("casa térrea 8x20", "terreno 12x25"); 3 quartos com 1 suíte e sala integrada à cozinha como o arranjo mais anunciado; em lote de 10 x 20, casas de 100 a 120 m² ([Coohom](https://www.coohom.com/article/planta-de-casa-em-lote-10x20-como-planejar-um-projeto-funcional), [Planner 5D](https://planner5d.com/blog/pt/plantas-de-casas-com-3-quartos/)). **Não achei pesquisa** que diga qual planta ou qual tamanho de lote é o mais comum no Brasil; quem disser isso está chutando.

### 3. Os grandes passos para construir a casa

A ordem abaixo junta o que as fontes repetem. Prazo, taxa e documento mudam por cidade.

#### Antes da obra (papel)

| # | Passo | O que é | Quem faz |
|---|---|---|---|
| 1 | Conferir o lote | Matrícula no cartório, medidas reais, o que a prefeitura deixa construir ali (recuos, altura, quanto do lote pode ocupar) | Dono, com a prefeitura |
| 2 | Escolher a planta | A casa que cabe no lote, na família e no bolso | **É aqui que o e-book entra** |
| 3 | Sondagem do solo | Diz que fundação o terreno pede | Empresa de sondagem, a pedido do engenheiro |
| 4 | Projetos | Arquitetônico para a prefeitura, estrutural, elétrico e hidráulico, com responsável técnico (ART ou RRT) | Arquiteto ou engenheiro |
| 5 | Orçamento e cronograma | Quanto custa cada etapa e em que ordem comprar | Engenheiro, arquiteto ou orçamentista |
| 6 | Alvará de construção | A licença da prefeitura para começar | Prefeitura, com o projeto aprovado |

#### A obra

| # | Etapa | Parte do custo* |
|---|---|---|
| 7 | Serviços preliminares: limpeza, água e luz provisórias, marcação da casa no terreno | 4% |
| 8 | Fundação e impermeabilização do baldrame | 6% |
| 9 | Estrutura e alvenaria: pilares, vigas, paredes, laje | 15% |
| 10 | Cobertura: madeiramento e telhas | 6% |
| 11 | Instalações hidráulicas e de esgoto | 8% |
| 12 | Instalações elétricas | 7% |
| 13 | Esquadrias: portas e janelas | 4% |
| 14 | Revestimentos e acabamentos: reboco, piso, azulejo, louças | **30%** |
| 15 | Pintura | 6% |
| 16 | Complementos: muro, calçada, grades | 4% |

\* Percentuais do guia da [OrçaFascio](https://www.orcafascio.com/papodeengenheiro/inteligencia-do-inicio-ao-fim-conheca-as-etapas-de-uma-construcao-civil) para "residência de padrão médio" (o guia põe ainda 6% em projeto, 1% em orçamento, 2% em instalações complementares e 1% em limpeza). **É blog de empresa de software, não tabela oficial**, e outros portais dão faixas diferentes (acabamento de 35% a 50%). A ordem das etapas bate com o guia do [QuintoAndar](https://www.quintoandar.com.br/guias/?p=2469759). Para valor em reais, a fonte certa é o CUB do Sinduscon do estado ou o SINAPI.

#### Depois da obra (papel)

| # | Passo | O que é |
|---|---|---|
| 17 | Habite-se | A prefeitura vistoria e certifica que a casa pode ser ocupada |
| 18 | Averbação | Levar o habite-se ao cartório para a matrícula passar a dizer "casa", e não só "lote". Sem isso o imóvel fica irregular no papel e é difícil financiar ou vender ([QuintoAndar](https://www.quintoandar.com.br/guias/?p=2467042)) |

O e-book já tem a página "Do e-book até a chave na mão" com 7 passos resumidos (página 60, `gerador/livro.py`). Esta lista é mais completa e traz a parte do custo de cada etapa.

### 4. Um dado de mercado para o anúncio (com cuidado)

Pesquisa **CAU/BR-Datafolha de 2015**: dos brasileiros economicamente ativos que já construíram ou reformaram (54%), **85,4% fizeram a obra sem arquiteto nem engenheiro**; o motivo mais citado é achar caro ([Gazeta do Povo](https://www.gazetadopovo.com.br/imoveis/maioria-das-obras-e-feita-sem-acompanhamento-tecnico-brrq8cjo6sdxlhrzc8xvvq8rk), [AECweb](https://www.aecweb.com.br/revista/noticias/o-caubr-e-o-datafolha-realizaram-pesquisa/12302)). O dado é de 2015 e veio de reportagem, não do relatório original. Serve para mostrar o tamanho do público; **não** serve para dizer que dá para construir sem profissional.

### 5. O que dá para fazer com isso (para o dono decidir)

1. **Redesenho das plantas com a régua federal:** banheiro de 1,50 m, cozinha de 1,80 m, mesa para 4, porta de serviço. Entra no mesmo redesenho da apostila 2.
2. **Página nova no e-book, "Da planta à chave: os 18 passos"**, com a parte do custo de cada etapa. Ajuda quem constrói por etapas a saber o que vem depois e quanto guardar.
3. **Série de posts e reels "passo da obra"**: um passo por vídeo, cada um terminando na planta. Dá 18 temas.
4. **Gancho de anúncio** com a régua do governo ("o governo exige banheiro de 1,50 m; o da sua planta tem quanto?"), só depois de as nossas plantas cumprirem.
5. **Validador:** acrescentar as larguras da portaria como aviso.

### 6. O que não foi achado ou lido

- Pesquisa sobre a planta mais procurada e o lote mais comum no Brasil: não existe nas buscas feitas.
- Cartilha oficial de etapas de obra do CAU, do CREA ou da ABCP: não achada. Há o guia do programa federal Reforma Casa Brasil ([PDF](https://www.gov.br/cidades/pt-br/acesso-a-informacao/acoes-e-programas/habitacao/reforma-casa-brasil/arquivos/guia_famlia_beneficiria_final.pdf)), baixado e ainda não lido.
- Manual da CDHU, concursosdeprojeto.org e plantas do ArchDaily: continuam na fila (apostila 2, seção 5).
