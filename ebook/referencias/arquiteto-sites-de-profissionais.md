# Apostila 2 do Arquiteto: como arquiteto de verdade arma uma planta

> Pedido do dono (22/11/2026): "faça o Arquiteto estudar mais, o último layout não fazia sentido; mande ele procurar os sites que arquitetos de verdade usam no trabalho". Leitura obrigatória do agente [`arquiteto`](../../.claude/agents/arquiteto.md) antes de criar ou mudar planta, junto com a [apostila 1](arquiteto-fontes-brasileiras.md) (clima e móveis) e as [regras](regras-do-arquiteto.md).
>
> A apostila 1 ensinou **medida**. Esta ensina **arranjo**: como os cômodos se ligam. Só entrou aqui o que foi lido ou visto na fonte em 22/11/2026. Onde a fonte não foi lida, isso está dito.

## 1. O que está errado hoje (diagnóstico)

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

## 2. Prefeitura de São Paulo: Diretrizes de Projeto de HIS (SEHAB, abril de 2021)

Documento que a Secretaria de Habitação entrega aos escritórios contratados ([PDF](https://legislacao.prefeitura.sp.gov.br/leis/portaria-secretaria-municipal-de-habitacao-sehab-37-de-3-de-maio-de-2021/anexo/65301a9c1411920c1295e6d7/DiretrizesProjeto_Publicação_2021.pdf), Portaria SEHAB 37/2021). Lido o capítulo 3, "Unidade habitacional". É diretriz para obra da prefeitura de São Paulo, não lei para o resto do país.

- **3.1, item 1:** atenção especial à largura de cozinha, de área de serviço, de box e de corredor.
- **3.1, item 2:** o layout é definido com os móveis e os eletrodomésticos **desenhados**, nas medidas da NBR 15575.
- **3.1, item 3:** "conforme o número de leitos da unidade habitacional deve-se prever o mesmo número de mobiliários (ex. 4 leitos = mesa com 4 cadeiras = sala para 4 pessoas)".
- **3.1, item 4:** toda unidade deve ser adaptável para pessoa com deficiência (Lei 13.146/2015).
- **3.2, item 5:** "é proibido que seja necessário atravessar a área do boxe para acessar a bacia sanitária ou o lavatório".
- **3.2, item 10:** banheiro sempre com iluminação e ventilação.
- **3.4, item 4:** "tanques não devem ser confinados; devem dispor de espaços para a movimentação das pessoas no ato de lavar roupas".
- **3.5:** janela de dormitório com veneziana integrada; portas e janelas em medida padrão de mercado.

## 3. Governo da Bahia: projeto de referência de casa térrea (CAR, maio de 2024)

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

## 4. UFRGS: o que os moradores fazem com a planta depois (Reis e Lay, 2002)

"Tipos arquitetônicos e dimensões dos espaços da habitação social", Antônio Tarcísio Reis e Maria Cristina Lay, revista Ambiente Construído ([PDF](https://seer.ufrgs.br/index.php/ambienteconstruido/article/download/3441/1855/11807)). Levantamento de 374 moradias em 12 conjuntos da região de Porto Alegre, comparando o projeto original com a casa ocupada. Lidos o resumo e as seções de número de peças, áreas e sala.

- As casas térreas cresceram muito depois de ocupadas: a área construída aumentou cerca de 144% num conjunto e 153% em outro.
- O crescimento é **principalmente no setor de serviço, depois no social**: o morador acrescenta área de serviço, garagem, segundo banheiro e mais uma sala ou um jantar.
- O número de quartos quase não passa de 3; o que cresce é o tamanho do quarto de casal.
- Insatisfação com a sala aparece quando há **duas linhas de circulação atravessando a sala**. Os autores indicam sala de estar (ou estar e jantar) em torno de **10 m² para 3 pessoas** como mínimo.

**Para nós:** a ampliação que o comprador vai fazer é serviço, garagem e mais sala, antes de mais quarto. A planta precisa deixar o lugar disso livre no lote e dizer onde é.

## 5. Os sites que arquiteto usa (para as próximas leituras)

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

## 6. O método, a partir de agora

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

## 7. O que falta decidir e fazer

- **Refazer as plantas** com este método (decisão do dono: quais e quando). Sugestão de ordem: série E (banheiro por fora), depois as compactas (corredor e mesa), depois a F02.
- **Ensinar o validador** a apontar: banheiro ou quarto que só se alcança por fora, corredor acima de 6% em casa de até 60 m², falta de mesa, duas casas com o mesmo arranjo.
- **Ler** o manual da CDHU, as pranchas de concurso e 5 projetos do ArchDaily com a planta aberta.
