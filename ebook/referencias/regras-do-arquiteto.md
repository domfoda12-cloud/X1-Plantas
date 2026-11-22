# Regras de projeto: como o arquiteto decide cada planta

> Parte da pasta E-book ([`../EBOOK.md`](../EBOOK.md)). As regras estão em código em [`../../ferramentas/plantas.py`](../../ferramentas/plantas.py): cada planta só vira `dados` se passar pelo validador (`python3 ferramentas/plantas.py validar`).
>
> **São regras de referência.** Recuo, taxa de ocupação, iluminação e áreas mínimas mudam por cidade e por zona bioclimática (NBR 15220). Elas não substituem o código de obras local nem um projeto assinado por arquiteto ou engenheiro. Um arquiteto registrado deve revisar as 24 plantas e este texto antes da venda.

## 1. Dimensões (medidas **por dentro** das paredes)

Desde o rascunho 1, as medidas da casa são **por fora** e cada cômodo perde a parede por dentro: parede externa de 15 cm inteira, metade da interna de 12 cm (`PAREDE_EXT` e `PAREDE_INT` em `ferramentas/plantas.py`). Os mínimos abaixo (`MINIMOS_UTIL`) são de área e lado **livres**. Abaixo do limite de conforto (`CONFORTO_UTIL`), a casa passa com aviso para o engenheiro conferir a mobília.

| Cômodo | Mínimo livre (erro abaixo disso) | Conforto (aviso abaixo disso) | Origem |
|---|---|---|---|
| Sala | 8 m², lado 2,30 m | 9 m², lado 2,50 m | NBR 15575 Anexo G: sofá de 2 lugares 1,20 x 0,70 e estante |
| Quarto de casal | 7 m², lado 2,30 m | 8 m², lado **2,40 m** | Cama 1,40 + 0,50 + 0,50 de passagem (Anexo G) |
| Quarto | 6 m², lado 2,00 m | | Cama 0,80 x 1,90, guarda-roupa 1,50 x 0,50 |
| Cozinha | 4 m², lado 1,50 m | | 0,85 m livres na frente de pia, fogão e geladeira (Anexo G) |
| Banheiro | 1,8 m², lado 1,00 m | (estudo cita 1,10 m fora o box: ver a [apostila](arquiteto-fontes-brasileiras.md), seção 3) | Vaso 0,60 x 0,60, lavatório |
| Serviço | 1,5 m², lado 0,95 m | | Tanque 0,52 x 0,53 e máquina 0,60 x 0,65 |
| Circulação | 0,80 m livres; **no máximo 14%** da área | | Corredor não pode virar a casa |
| Casa acessível (S03) | Banheiro e circulação com **1,50 m livres** | | Giro de cadeira de rodas (NBR 9050); o resto da norma é do engenheiro |
| Pé-direito | 2,50 m em cômodo de permanência | | COE-SP; verificar no município |

## 2. Luz e ventilação

- Janela de **1/6 do piso** em sala, quarto e escritório; **1/8** em cozinha, serviço e banheiro (valores típicos de códigos de obras).
- Janela só em parede que dá para fora **e** que não seja a divisa. A parede da esquerda das plantas é divisa (sem janela), salvo as que declaram recuo dos dois lados.
- Banheiro sem janela só com exaustão mecânica (aparece como aviso, e nenhuma das 24 depende disso).
- **O clima manda na janela** (NBR 15220-3, orientativa): abertura **efetiva** de ventilação de 15% a 25% do piso nas zonas 1 a 6, pequena (10% a 15%) na zona 7 e grande (mais de 40%) na zona 8 (Rio, Salvador, Recife, Fortaleza, Manaus, Belém). Nossa janela de 1/6 do piso, de correr, dá perto de 8% de abertura efetiva: o arquiteto da obra aumenta a janela, usa veneziana e beiral onde o clima pede. Detalhes na [apostila](arquiteto-fontes-brasileiras.md), seção 2.

## 3. Circulação e privacidade

- **Todo cômodo é alcançável a partir da entrada.**
- **Quarto e banheiro social nunca ficam no caminho de outro quarto.** A suíte só se alcança pelo quarto.
- A circulação vem **depois** da zona social: sala e cozinha na frente, corredor no meio, quartos nos fundos.
- Banheiro social não abre direto para a cozinha.

## 4. Áreas molhadas juntas

Cozinha, serviço e banheiros ficam **encostados**, para uma prumada só (o encanamento mais barato). Quando um banheiro fica longe do núcleo molhado, o validador avisa. Hoje é o caso da suíte de E07, F03, F04 e S09, que a gente aceita porque a suíte pede privacidade, e do banheiro da C01 (redesenhada em 22/11/2026), que não encosta em cozinha, serviço nem outro banheiro e pede prumada própria. Nos dois casos custa mais tubulação: a ficha manda perguntar ao engenheiro quanto.

## 5. Vãos e estrutura

Cômodos de permanência com lado acima de 4,5 m pedem conferência de laje e vigas. O validador anota isso. A grade estrutural e o cálculo são do engenheiro.

## 6. O lote

Lote mínimo = largura da casa + recuos, e fundo = profundidade + recuo de frente + recuo de fundos. Usamos **frente 3 m, fundos 1,5 m, lateral direita 1,5 m e esquerda 0** (parede na divisa) salvo na casa estreita, que recua dos dois lados. O lote nunca pode ter menos de 5 m de frente (Lei 6.766/1979, art. 4º, II).

## 7. Orientação do sol (hemisfério sul)

Não existe orientação perfeita. O validador compara as quatro orientações da frente da casa e indica a melhor para as janelas daquela planta, assim:

- **Quarto:** sol da manhã (leste) é bom; sol da tarde (oeste) esquenta.
- **Sala:** norte tem sol durante boa parte do ano; leste é agradável pela manhã.
- **Cozinha:** sul e leste, sem sol forte.
- **Serviço:** oeste, para secar a roupa.

É um critério simplificado. Cada região tem sua zona bioclimática (NBR 15220) e cada terreno tem as suas sombras; o arquiteto da obra decide. O e-book mostra a recomendação e o **porquê**.

## 8. O que o validador confere (24 plantas, 0 erros)

Geometria sem sobreposição nem vão solto · dimensões mínimas · janelas (proporção e posição) · alcance a partir da entrada · circulação até 14% · privacidade · núcleo molhado · lote mínimo · orientação.
Rodar: `python3 ferramentas/plantas.py validar`. Desenhar: `python3 ferramentas/plantas.py previa`. Exportar JSON: `python3 ferramentas/plantas.py exportar`.

## 9. O que o validador NÃO faz

Não calcula estrutura, instalações, conforto térmico detalhado, taxa de ocupação nem coeficiente de aproveitamento do município. Não confere acessibilidade além do giro de 1,50 m da S03, nem a NBR 9050 inteira. Não mede ainda a ventilação cruzada (janelas em paredes opostas) nem a abertura efetiva por zona bioclimática. E não sabe o recuo da sua cidade.

## Fontes

Apostila com as fontes brasileiras lidas (NBR 15220-3, nota técnica do LabEEE/UFSC, Anexo G da NBR 15575, Lelé): [`arquiteto-fontes-brasileiras.md`](arquiteto-fontes-brasileiras.md). IBGE (Censo 2022); Lei 6.766/1979; Portaria MCID 725/2023; COE São Paulo 2017 e NBR 15575 (dimensões, pelo resumo de um arquiteto); Gelker Ribeiro, arquiteto, sobre orientação solar; NBR 15220 (zonas bioclimáticas). Confira os textos oficiais antes de afirmar em anúncio.
