# Regras de projeto: como o arquiteto decide cada planta

> Parte da pasta E-book ([`../EBOOK.md`](../EBOOK.md)). As regras estão em código em [`../../ferramentas/plantas.py`](../../ferramentas/plantas.py): cada planta só vira `dados` se passar pelo validador (`python3 ferramentas/plantas.py validar`).
>
> **São regras de referência.** Recuo, taxa de ocupação, iluminação e áreas mínimas mudam por cidade e por zona bioclimática (NBR 15220). Elas não substituem o código de obras local nem um projeto assinado por arquiteto ou engenheiro. Um arquiteto registrado deve revisar as 24 plantas e este texto antes da venda.

## 1. Dimensões

| Cômodo | Mínimo que usamos | Origem |
|---|---|---|
| Sala | 10 m², lado 2,6 m | Acima do mínimo legal (NBR 15575 pede lado de 2,40 m; COE-SP, 5 m²) |
| Quarto de casal | 8,5 m², lado 2,6 m | Cama 1,40 x 1,90 m com 0,50 m de circulação ao redor (NBR 15575) |
| Quarto | 7 m², lado 2,4 m | Mesma lógica, cama de solteiro |
| Cozinha | 4,5 m², lado 1,7 m | Cabe o círculo de 1,50 m e 0,85 m livres na frente de pia e fogão |
| Banheiro | 2,4 m², lado 1,2 m (1,5 m na casa acessível) | Cabe o círculo de 0,90 m; acessível pede giro de 1,50 m |
| Serviço | 2 m², lado 1,2 m | Tanque e máquina |
| Circulação | 0,90 m, 1,20 m na casa acessível; **no máximo 14%** da área | Corredor não pode virar a casa |
| Pé-direito | 2,50 m em cômodo de permanência | COE-SP; verificar no município |

## 2. Luz e ventilação

- Janela de **1/6 do piso** em sala, quarto e escritório; **1/8** em cozinha, serviço e banheiro (valores típicos de códigos de obras).
- Janela só em parede que dá para fora **e** que não seja a divisa. A parede da esquerda das plantas é divisa (sem janela), salvo as que declaram recuo dos dois lados.
- Banheiro sem janela só com exaustão mecânica (aparece como aviso, e nenhuma das 24 depende disso).

## 3. Circulação e privacidade

- **Todo cômodo é alcançável a partir da entrada.**
- **Quarto e banheiro social nunca ficam no caminho de outro quarto.** A suíte só se alcança pelo quarto.
- A circulação vem **depois** da zona social: sala e cozinha na frente, corredor no meio, quartos nos fundos.
- Banheiro social não abre direto para a cozinha.

## 4. Áreas molhadas juntas

Cozinha, serviço e banheiros ficam **encostados**, para uma prumada só (o encanamento mais barato). Quando a suíte fica longe do núcleo molhado, o validador avisa; hoje é o caso de E07, F03, F04 e S09, e a gente aceita porque a suíte pede privacidade (custa um pouco mais de tubulação).

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

Não calcula estrutura, instalações, conforto térmico detalhado, taxa de ocupação nem coeficiente de aproveitamento do município, não confere acessibilidade além do que está na seção 1 (a S03 segue 1,20 m e giro de 1,50 m, não a NBR 9050 inteira) e não sabe o recuo da sua cidade.

## Fontes

IBGE (Censo 2022); Lei 6.766/1979; Portaria MCID 725/2023; COE São Paulo 2017 e NBR 15575 (dimensões, pelo resumo de um arquiteto); Gelker Ribeiro, arquiteto, sobre orientação solar; NBR 15220 (zonas bioclimáticas). Confira os textos oficiais antes de afirmar em anúncio.
