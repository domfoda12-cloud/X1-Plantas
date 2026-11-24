# Cômodo a cômodo: o próximo passo depois da planta (C01, E03, F01)

**Revisto pelo Revisor de risco em 24/11/2026: trocas aplicadas** (veredito em [`veto-comodo-a-comodo-2026-11-24.md`](veto-comodo-a-comodo-2026-11-24.md)). **Reconferência do Revisor aplicada (Arquiteto, 24/11):** sem distância da tomada ao box, fonte da contagem em cada "o mínimo é", corredor, marcas só na nota de fonte e números da Portaria conferidos no PDF.

**As 5 ideias para abrir a página** (escolhidas pelo Revisor de risco, as mais seguras e úteis):
1. Testar o encanamento antes de fechar a parede e um registro por cômodo (banheiro da C01).
2. Marcar a obra com trena: janela a 1,5 m da divisa (recuo lateral da C01).
3. O que não fazer depois em cada casa (seção 4, página 3).
4. Carro ou quintal: decidir antes de marcar (frente do lote das 3 casas).
5. Caixas de tomada que não ficam costas com costas, e tomada nas duas paredes de cabeceira (sala, cozinha e quarto casal da C01; quarto da frente da E03).

> **Pedido do dono (24/11/2026, ficha `pedidos/2026-11/2026-11-24-1119-casas-comodo-a-comodo-...`), palavra por palavra:** "continue trabalhando nas casas, podem estar desenhadas corretas mas qual o próximo passo? Planejar cada quarto, ideias do que fazer em lugares da casa etc". Continua dois pedidos de 23/11: "detalhes de como a casa pode ser mobiliada ou ideias de construções" e, para o quarto com parede na divisa, "uma solução criativa para o que pode ser feito ou acontecer naquele quarto/área".
> **Autor:** Arquiteto, 24/11/2026. **É conteúdo técnico, não texto final:** o Redator escreve, o Designer desenha, o Revisor de risco confere antes de ir ao público.
> **De onde vêm os números:** medidas livres de `python3 ferramentas/plantas.py validar` (C01, E03, F01: zero erros, 24/11); portas, janelas e móveis do desenho de `ferramentas/planta3d.py` (`construir`, a mesma geometria da prévia); passagens dos móveis da conta já conferida em [`como-mobiliar-as-3-casas.md`](como-mobiliar-as-3-casas.md) (citada como "anexo de mobiliar"). Lote e recuos: `validacao.metricas` de `ebook/plantas/dados/<ID>.json` (recuo de referência: frente 3,0 m, fundo 1,5 m, direita 1,5 m, esquerda na divisa).
> **Fontes de fora** (abertas e registradas no caderno `pesquisas/`, menos as marcadas "pela apostila, não conferido na fonte"): NBR 5410:2004, contagem de tomadas (item 9.5.2.2.1), por duas fontes secundárias que concordam: slides de Projeto Residencial da [UDESC](https://www.udesc.br/arquivos/udesc/id_cpmenu/9731/projeto_residencial_1_v8_26_SPR1_17854413765872_9731.pdf) (agosto de 2026, pp. 16 e 17) e [Engenharia 360](https://engenharia360.com/quantas-tomadas-deve-ter-em-cada-comodo/) (atualizado em julho de 2026); revisão da NBR 5410 em consulta nacional pela [O Setor Elétrico](https://www.osetoreletrico.com.br/?p=165060) (agosto de 2025); alturas e interruptor paralelo pelo manual Elektro/Pirelli de 2003, revisado pelo secretário da comissão da norma ([parte 1](https://www.coe.ufrj.br/~kleber/INST_ELET_RES_PARTE_01.pdf), pp. 13 a 16; [parte 2](https://www.coe.ufrj.br/~kleber/INST_ELET_RES_PARTE_02.pdf), pp. 75 e 111); DR pela [UDESC](https://udesc.br/arquivos/udesc/id_cpmenu/9731/choque_eletrico_SPR1_10_24_1729019218554_9731.pdf); Código Civil, arts. 1.300 a 1.302 ([Planalto](https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm)); Portaria MCID 725 ([PDF](https://www.gov.br/cidades/pt-br/acesso-a-informacao/institucional/base-juridica/portarias/2023/Port.MCIDn725_2023COMPILADA.pdf), aberta em 24/11, anexo, item 2: pé-direito de 2,55 e 2,30 m, porta de 0,80 x 2,10, 0,80 m entre as camas, ganchos de rede a 1,70 a 1,90 m do piso e de 2,90 a 3,30 m entre si, veneziana no dormitório); [Guia da Família Beneficiária](https://www.gov.br/cidades/pt-br/acesso-a-informacao/acoes-e-programas/habitacao/reforma-casa-brasil/arquivos/guia_famlia_beneficiria_final.pdf) (MCID); ficha técnica de tubo da [Tigre](https://tigresite.s3.amazonaws.com/2025/10/FT_Aquatherm_2025-Rev-Final.pdf) (citada no corpo como "ficha do fabricante"); faixa de rede de 2,50 a 3,30 m pelo [guia QuintoAndar](https://www.quintoandar.com.br/guias/?p=393400) (citado no corpo como "guia de rede"); pé-direito de 2,50 m em São Paulo, **pela apostila, não conferido na fonte** (busca de 24/11 não achou o trecho; caderno, hipótese); medida de carro e de moto (nota no fim); a pesquisa da UFRGS sobre a sala, **pela apostila 2 (seção 4), não conferido na fonte**.
> **Suposições (o dono não disse):** que isto vira páginas do e-book e posts (a lista do fim é recomendação); que o comprador compra móvel de loja; que a casa é de alvenaria comum (tijolo ou bloco de vedação, com pilar e viga). **Se a casa for de alvenaria estrutural, parede não se corta depois:** nicho, rasgo de cano e de fio só onde o projeto previu. Quem diz qual é a do comprador é o engenheiro.

## Como ler

- **Medida livre** é por dentro das paredes (parede de fora 15 cm, de dentro 12 cm). **Passagem** é o vão entre móvel e móvel ou parede, em cm.
- **Tomadas: a conta mínima da NBR 5410:2004** (item 9.5.2.2.1), conferida em duas fontes secundárias que concordam (slides da UDESC de agosto de 2026, p. 17, e Engenharia 360, atualizado em julho de 2026); o texto da norma, que é pago, não foi lido. Sala e quarto: um ponto de tomada a cada 5 m de perímetro, ou fração. Cozinha, copa e **área de serviço**: um ponto a cada 3,5 m de perímetro, ou fração, e **duas tomadas em cima da bancada da pia** (no mesmo ponto ou em pontos separados). Varanda: um ponto. Banheiro: um ponto junto da pia. Outros cômodos: até 2,25 m², um ponto (dentro ou a até 0,80 m da porta); de 2,25 a 6 m², um ponto dentro; acima de 6 m², um a cada 5 m de perímetro. Um ponto pode ter mais de uma tomada. Luz: um ponto no teto por cômodo, com interruptor na parede (UDESC, p. 16). O manual de 2003 da nota de fonte avisa que o mínimo costuma ser pouco: mais tomadas evitam o benjamim. A conta abaixo usa o perímetro da medida livre do validador. **É o mínimo pelas fontes, não o projeto: quem faz o projeto elétrico é o eletricista, e ele confere na norma vigente** (há revisão da NBR 5410 em consulta nacional, pela O Setor Elétrico, 2025).
- **Tomada do banheiro e o box:** a tomada da pia vai **do lado mais longe do box; a distância, o eletricista confere.** A regra do banheiro na norma de 2004 (item 9.1) não foi lida aqui, e a revisão em consulta mexe justamente na tomada perto do box: por isso este documento não dá número de distância.
- **Alturas de tomada** só como exemplo do mesmo manual (parte 2, p. 111, pé-direito de 2,80 m): tomada baixa a 0,30 m, interruptor e tomada média a 1,30 m, saída alta a 2,20 m. Não é regra: o eletricista decide.
- **Pé-direito:** o desenho 3D usa 2,80 m. Nas casas do Minha Casa Minha Vida, a Portaria MCID 725 usa 2,55 m (2,30 no banheiro) e porta de 0,80 x 2,10 m; ela não obriga a sua casa: quem diz é o código de obras da sua cidade e o projeto (a apostila cita 2,50 m para São Paulo: pela apostila, não conferido na fonte). Por isso o espaço em cima da porta fica entre uns 40 e 70 cm: depende do pé-direito da sua obra.
- **Ampliação, de uma vez:** nenhuma das 3 plantas tem cômodo a mais desenhado nem laje preparada para subir. Em cada casa abaixo digo onde o lote tem chão sobrando e por que isso **não** vira cômodo sem projeto novo do arquiteto ou do engenheiro.
- **O sol no lote:** o validador diz para onde a rua fica melhor (C01 e E03: rua ao norte; F01: rua ao sul). A frente e o fundo são certos; **não uso o lado direito ou esquerdo para dizer sol**, porque não conferi a convenção de lado do validador contra o desenho (seção "Para a equipe").

---

## 1. C01 · Casa Compacta (6,50 x 8,50 m, 51 m², 2 quartos; lote de 8 x 15 m, mínimo 8 x 13)

> **Planta de referência; o projeto legal é assinado por profissional habilitado.** Se a casa for de alvenaria estrutural, parede não se corta depois: nicho, rasgo de cano e de fio só onde o projeto previu. Quem diz qual é a sua é o engenheiro.

O que esta casa tem de próprio: o **hall de 1,7 m²** no meio de tudo (a circulação é 4% da casa, a menor das três), a **varanda** na frente da sala e o banheiro **entre os dois quartos**, com o guarda-roupa de cada quarto encostado nele.

### Sala e jantar · 3,14 x 3,99 m livres (12,5 m²)
- **Cabe** (anexo de mobiliar): sofá de 2 lugares na divisa, rack na parede do quarto da frente a 1,86 m do sofá, mesa de 4 no fundo, colada na passagem da cozinha. As cadeiras ficam com 46 e 51 cm (a referência do Anexo G da NBR 15575 sugere 75): banco sem encosto do lado da parede do serviço resolve.
- **Ideias:**
  1. **Trocar a TV de parede.** Hoje o rack fica na parede do quarto da frente, atrás da cama de uma criança. Dá para inverter: **rack de até 1,50 m na divisa**, começando 5 cm depois da folha aberta da porta e terminando 7 cm antes da cadeira da mesa; **sofá de 2 lugares (1,40) na parede do quarto**, que tem 1,95 m livres antes da abertura do hall. A distância TV e sofá continua 1,86 m, a janela fica livre. O som da TV vai para a divisa, e o sofá, que não faz barulho, encosta no quarto. Rack de 1,60 não cabe nesse lugar; sofá de 3 lugares (2,00) também não.
  2. **Dois pontos de luz no teto, decididos antes da laje ou do forro:** um no meio do estar e outro em cima da mesa, a **73 cm da parede da divisa e a 87 cm da parede do serviço** (o centro da mesa no desenho). A luz do meio da sala, sozinha, cai no tapete e deixa a mesa na sombra.
  3. **Interruptor do lado da maçaneta:** no desenho, a folha da porta abre contra a divisa, e sobram **20 cm de parede entre a porta e a janela**. O interruptor vai nessa faixa, não atrás da porta, onde a folha aberta encosta; o eletricista confere se a caixa cabe com o batente e o marco.
- **Tomadas:** perímetro de 14,3 m: o mínimo é **3 pontos** (um a cada 5 m). Sugestão de lugar: atrás da TV (com antena), um do lado do sofá e um na divisa junto da mesa (celular, ventilador). Pela NBR 5410:2004, segundo UDESC (2026) e Engenharia 360; o eletricista confere na norma vigente.
- **Cuidado:** caixa de tomada e de antena da TV **costas com costas** com a tomada da cama do outro lado da parede de 12 cm. Esta planta, do jeito que está, põe a TV atrás da cama do quarto da frente: a ideia 1 evita.
- **Pergunte:** ao eletricista, se a caixa da TV pode ficar na divisa e por onde desce o fio da antena; ao engenheiro, onde passa a viga do teto antes de marcar o ponto da mesa.

### Cozinha · 1,83 x 2,95 m livres (5,4 m²)
- **Cabe** (anexo de mobiliar): geladeira na ponta da sala e bancada de pia e fogão (1,80) em linha na parede do quarto casal, com **121 cm** livres na frente; sobram 30 cm até a parede do fundo. A janela (0,90 m, peitoril de 1,10 no desenho) fica **na parede do fundo**, não em cima da pia.
- **Ideias:**
  1. **Bancada de apoio embaixo da janela do fundo, em L com a principal:** a parede do fundo tem 1,21 m entre a parede do serviço e a frente da bancada. Uma bancada de uns 40 cm de fundo ali (medida de hipótese, sem ficha de loja) dá lugar ao micro-ondas e ao liquidificador sem tirar a passagem: ninguém precisa passar além dela. O peitoril de 1,10 m do desenho fica acima do tampo; a altura do tampo, o pedreiro confere.
  2. **Ponto alto acima do fogão** para depurador ou exaustor, deixado antes do reboco, mesmo que o aparelho venha depois; a altura e o circuito, o eletricista confere.
- **Tomadas:** perímetro de 9,6 m: o mínimo é **3 pontos** (um a cada 3,5 m), com **duas tomadas em cima da bancada da pia**, longe da cuba. Sugestão: o terceiro ponto na bancada de apoio e a geladeira à parte. O lugar de cada um, o eletricista confere. Pela NBR 5410:2004, segundo UDESC (2026) e Engenharia 360; o eletricista confere na norma vigente.
- **Cuidado:** a parede da pia é **a mesma da cabeceira da cama de casal**, do outro lado (12 cm). Cano de esgoto da pia, louça batendo e as tomadas da bancada ficam atrás da cabeça de quem dorme. **Esta planta não evita.** O que dá para fazer na obra: não deixar as caixas de tomada da bancada e da cabeceira costas com costas, e pedir ao engenheiro o melhor lugar para o cano descer.
- **Pergunte:** ao engenheiro, onde fica o botijão de gás e por onde passa a mangueira ou o tubo; ao encanador, se a pia (na parede do quarto) e o tanque (na divisa) descem em canos separados e quanto isso pesa.

### Serviço · 1,19 x 2,89 m livres (3,4 m²)
- **Cabe** (anexo de mobiliar): tanque e máquina lado a lado na divisa, entre os giros das duas portas; **66 cm** na frente do tanque, **54 cm** na frente da máquina.
- **Ventilação: veneziana em cima da porta de fora** (decisão do dono, 24/11: "manter a porta e pôr veneziana em cima"; aplicada no D1). A parede do fundo tem 1,19 m livres e só comporta a porta de fora (0,90); a janela de 0,70 que caía em cima dela saiu. No lugar, uma **veneziana de 0,90 x 0,50 m no vão da porta, de 2,10 a 2,60 m do piso** (sobram 20 cm de verga até o teto de 2,80 do desenho 3D; com pé-direito menor, a veneziana fica mais baixa, e quem decide é o projeto). **Conta:** 0,45 m² de vão para 3,4 m² de piso livre dá 13%; a referência do projeto é 1/8 (12,5%, 0,43 m²). Só passa contando o vão inteiro: as aletas tiram parte do ar e quase toda a luz, e a luz do dia passa a vir da porta aberta e da cozinha. **O engenheiro confere a ventilação e a luz do serviço** (é o aviso do validador, no "Atenção" da página da casa). Na planta, a veneziana aparece tracejada (fica acima do corte); na imagem 3D, cortada a 1,1 m, não aparece.
- **Ideias:**
  1. **Prateleira em cima da máquina, na divisa**, acima da tampa aberta, para sabão e balde. Não na parede do fundo: em cima da porta fica a veneziana.
  2. **Varal de teto para dia de chuva**, preso na laje ou no forro (o profissional confere a fixação); o varal de sol fica no fundo do lote, a um passo da porta.
- **Tomadas:** perímetro de 8,2 m: o mínimo é **3 pontos** (área de serviço entra na regra da cozinha, um a cada 3,5 m). O da máquina em lugar seco, longe do respingo do tanque. O lugar de cada um, o eletricista confere. Pela NBR 5410:2004, segundo UDESC (2026) e Engenharia 360; o eletricista confere na norma vigente.
- **Cuidado:** tanque encostado no canto da porta, com a folha batendo nele. Esta planta evita (a folha passa a 3 cm).
- **Pergunte:** ao eletricista, se a máquina tem circuito próprio e se o circuito do serviço tem DR (a NBR 5410 pede DR em área de serviço, cozinha, banheiro e área externa, pelo material da UDESC); ao pedreiro, onde ficam o ralo e a saída de água da máquina.

### Quarto casal · 2,94 x 3,19 m livres (9,4 m²)
- **Cabe** (anexo de mobiliar): cama de casal padrão (1,38 x 1,88) com a cabeceira na parede da cozinha, 2 criados, guarda-roupa de 6 portas (2,00) na parede do hall e do banheiro, com **80 cm** livres na frente; **1,06 m** no pé da cama. Queen não (34 cm do lado da janela).
- **Ideias:**
  1. **Tomada e interruptor nos dois lados da cabeceira**, deslocados das caixas da bancada da cozinha (mesma parede, ver a cozinha).
  2. **Espera de ar-condicionado antes do reboco:** tomada alta e caminho do dreno na parede da janela, que dá para o fundo do lote (a condensadora fica no fundo, não no recuo do vizinho). O circuito é o eletricista que define.
- **Tomadas:** perímetro de 12,3 m: o mínimo é **3 pontos** (um a cada 5 m). Pela NBR 5410:2004, segundo UDESC (2026) e Engenharia 360; o eletricista confere na norma vigente.
- **Cuidado:** guarda-roupa encostado em parede molhada. Aqui ele encosta na parede do banheiro, do lado da pia e do vaso (não do box); a impermeabilização dessa parede, o pedreiro confere.
- **Pergunte:** ao pedreiro, se a parede do banheiro leva impermeabilização do lado de dentro do banheiro até onde respinga.

### Quarto (da frente) · 2,85 x 3,09 m livres (8,8 m²)
- **Cabe** (anexo de mobiliar): duas camas de solteiro com a cabeceira na parede da rua, **1,05 m** entre elas (nas casas do Minha Casa Minha Vida, a Portaria MCID 725 usa 80; ela não obriga a sua casa: quem diz é o código de obras da sua cidade e o projeto), criado no meio, guarda-roupa de 4 portas na parede do hall com **73 cm** na frente; ou cama de casal. A janela não dá para a rua: dá para o recuo da direita.
- **Ideias:**
  1. **Três tomadas baixas na parede da rua, que não tem janela:** uma no meio, no criado das duas camas, e uma perto de cada ponta, para quando o quarto das crianças virar quarto de casal. O quarto muda de arranjo sem extensão no chão.
  2. **Ganchos de rede**, se você é do Norte ou do Nordeste (nas casas do Minha Casa Minha Vida dessas regiões, a Portaria MCID 725 usa ganchos de rede nos dormitórios, a 1,70 a 1,90 m do chão e de 2,90 a 3,30 m um do outro; ela não obriga a sua casa: quem diz é o código de obras da sua cidade e o projeto). Das paredes de 2,85 e 3,09 m livres, a de 3,09 m fica dentro dessa faixa; a de 2,85 m fica abaixo (um guia de rede da nota de fonte aceita a partir de 2,50 m). Parede oca não segura: o profissional confere a parede e a bucha.
- **Tomadas:** perímetro de 11,9 m: o mínimo é **3 pontos** (um a cada 5 m). Pela NBR 5410:2004, segundo UDESC (2026) e Engenharia 360; o eletricista confere na norma vigente.
- **Cuidado:** guarda-roupa na parede do box. **Esta planta não evita:** o guarda-roupa de 4 portas fica na parede que o quarto divide com o banheiro, e os 95 cm da direita dele ficam atrás do box. Não há outra parede onde ele caiba (a da sala tem 1,19 m livres depois da cama). O cuidado é na obra: a parede do box bem impermeabilizada e o móvel com um vão atrás para o ar passar (quanto, a ficha do móvel e o pedreiro dizem).
- **Pergunte:** ao pedreiro, até onde sobe a impermeabilização da parede do box que encosta neste quarto.

### Banheiro · 1,84 x 1,68 m livres (3,1 m²)
- **Cabe** (anexo de mobiliar): box de 0,95 x 0,90 no canto da janela, vaso na parede da janela, pia no fundo, ao lado da porta. Ninguém atravessa o box.
- **Ideias:**
  1. **Tomada da pia do lado mais longe do box; a distância, o eletricista confere.** No desenho, é o lado do hall, que também fica longe da água do vaso (seção "Como ler").
  2. **Prateleira de canto no box, não nicho:** a parede do box que dá para o quarto da frente tem 12 cm, e do outro lado está o guarda-roupa. Nicho ali deixa pouca parede entre a água e o móvel. Nicho só se o pedreiro garantir a espessura e a impermeabilização.
- **Cuidado:** fechar a parede antes de testar o cano. A ficha do fabricante do tubo (nota de fonte) manda fechar "após o teste de estanqueidade".
- **Pergunte:** ao encanador, se este banheiro, que tem cano só dele (aviso do validador), terá registro próprio (o guia do MCID recomenda registro por cômodo, para fechar a água num vazamento), e quando é o teste antes do reboco.

### Hall · 1,04 x 1,68 m livres (1,7 m²)
- **Cabe:** nada. Ele abre para os 2 quartos e o banheiro, e é por isso que a casa não tem corredor.
- **Ideias:**
  1. **Maleiro em cima do hall inteiro.** As três portas têm 2,10 m; acima delas sobra de uns 40 a 70 cm até o teto, conforme o pé-direito (seção "Como ler"). Um tampo fechado sobre o hall dá um armário de 1,04 x 1,68 m para mala, cobertor e caixa de Natal, sem tirar piso de ninguém. Quem apoia o tampo (marceneiro ou pedreiro) e quanto peso aguenta, o profissional confere. A luz do teto do hall fica embaixo do tampo; o eletricista confere.
  2. **Luz baixa para a madrugada:** do quarto casal ao banheiro é um passo pelo hall. Uma luz de balizamento perto do chão evita acender a luz do teto de noite.
- **Tomadas:** cômodo de até 2,25 m²: o mínimo é **1 ponto**, dentro do hall ou a até 0,80 m da passagem. O interruptor do hall vai numa das duas faixas de **44 cm** que sobram ao lado da porta do banheiro (são as únicas paredes do hall sem porta). Pela NBR 5410:2004, segundo UDESC (2026) e Engenharia 360; o eletricista confere na norma vigente.
- **Cuidado:** corredor comprido e escuro. Esta planta evita: o hall tem 1,68 m.
- **Pergunte:** ao eletricista, se o quadro de luz pode ficar no hall, no meio da casa, ou onde ele recomenda.

### Varanda · 3,35 x 1,20 m (4,0 m², coberta e aberta na frente)
- **Cabe:** cadeiras encostadas na janela da sala, fora da porta (anexo de mobiliar). Entre a parede da divisa e a parede do quarto ficam **3,20 m** (3,35 no eixo menos os 15 cm da parede da divisa).
- **Ideias:**
  1. **Rede, só de pôr e tirar.** Os 3,20 m estão dentro da faixa da Portaria MCID 725 (2,90 a 3,30 m entre os ganchos). Mas a porta da sala fica na ponta da divisa e o caminho da rua passa pela varanda: **rede armada fecha a entrada**. Ganchos sim, rede guardada quando não estiver em uso. Rede de um gancho só, no canto do quarto, longe da porta, pede apoio no teto: o engenheiro confere a viga ou a laje.
  2. **Uma tomada e um ponto de luz na varanda** (a NBR 5410:2004 pede um ponto de tomada na varanda, pelas fontes do "Como ler"); o interruptor da luz da varanda fica dentro da sala, ao lado da porta.
- **Cuidado: fechar a varanda para aumentar a sala.** Nesta casa, a **única janela da sala dá para a varanda**: fechada, a sala fica sem janela para fora. A lateral da divisa já é fechada (Código Civil, art. 1.301; o engenheiro confirma).
- **Pergunte:** ao engenheiro, para que lado cai a água do telhado da varanda (o telhado não pode despejar água diretamente no vizinho, art. 1.300).

### Frente do lote · 3,0 x 8,0 m (recuo de referência)
- **O que cabe:** moto, sim (uma moto pequena mede uns 2,0 x 0,75 m). **Carro, não:** não cabe carro de frente para a rua no recuo de referência de 3,0 m; um carro popular pequeno mede uns 3,6 m; o tamanho da vaga é o código de obras que diz. (Fonte das medidas: nota no fim.)
- **Ideias:**
  1. **Carro ou quintal: decida antes de marcar a obra.** No lote de 8 x 15, sobram 3,5 m no fundo. Se a casa for 2,0 m para trás, a frente fica com **5,0 m** e o fundo com **1,5 m**, o mínimo do Código Civil para janela (art. 1.301), para as janelas da cozinha e do quarto casal e a veneziana do serviço; o código de obras pode pedir mais. O código de obras da cidade diz o recuo de frente e o tamanho da vaga; o engenheiro marca.
  2. **Horta na frente, se a rua ficar ao norte** (a melhor posição para esta casa, pelo validador): aí é a frente que pega sol, e o fundo fica do lado da sombra da casa.
- **Cuidado:** fazer o muro e o portão antes de saber onde ficam o medidor de luz e o hidrômetro.
- **Pergunte:** à prefeitura ou ao engenheiro, o recuo de frente da sua cidade (pode ser maior que os 3,0 m de referência); à concessionária, onde vai o padrão de entrada.

### Recuo lateral (direita) · 1,5 x 8,5 m
- **O que tem:** a janela do quarto da frente e a do banheiro, e o caminho da frente até o fundo.
- **Ideias:** calçada com caimento para longe da parede e uma torneira na saída para o fundo (medida e material, o engenheiro define).
- **Cuidado: marcar a casa 10 cm mais perto do vizinho.** As janelas desta lateral precisam ficar a 1,5 m da divisa (art. 1.301): se o recuo encolher na obra, a janela fica em desacordo com o Código Civil, e o vizinho pode pedir para fechar em até ano e dia (art. 1.302). Confira a marcação com trena antes da fundação.
- **Pergunte:** ao engenheiro, se o recuo de 1,5 m é medido até a face de fora da parede.

### Fundo do lote · 3,5 x 8,0 m no lote de 8 x 15 (1,5 m no lote mínimo)
- **O que tem:** a porta do serviço, com a veneziana em cima, e as janelas da cozinha e do quarto casal.
- **Ideias:** varal de sol a um passo da porta do serviço; torneira e ralo junto da porta (o lugar, a saída da água e o caimento, o encanador confere).
- **Onde a casa cresce:** aqui tem chão (2,0 m além do recuo mínimo), mas **duas janelas e a veneziana do serviço dependem dele**. Cômodo no fundo tapa a luz da cozinha e do quarto casal e o ar do serviço: só com projeto novo.
- **Cuidado:** cobrir o fundo inteiro com telha para o varal. Cobertura leve, só na frente da porta do serviço, e o engenheiro confere se não tira a luz da janela da cozinha.

---

## 2. E03 · Casa Fita (3,50 x 16,10 m, 56 m², 2 quartos; lote de 5 x 25 m, mínimo 5 x 20,6)

> **Planta de referência; o projeto legal é assinado por profissional habilitado.** Se a casa for de alvenaria estrutural, parede não se corta depois: nicho, rasgo de cano e de fio só onde o projeto previu. Quem diz qual é a sua é o engenheiro.

O que esta casa tem de próprio: **a divisa de ponta a ponta à esquerda, sem janela**, e **o recuo de 1,5 m à direita como a rua de dentro**: as duas portas de fora e as janelas da sala, da cozinha, do serviço e do banheiro dão para ele. Um quarto em cada ponta.

### Quarto (da frente) · 3,20 x 2,89 m livres (9,2 m²)
- **Cabe** (anexo de mobiliar): no desenho, cama de solteiro na divisa, escrivaninha embaixo da janela da rua e guarda-roupa de 4 portas na parede do recuo. Também cabem duas camas (cabeceira na parede do recuo, 80 cm entre elas) ou cama de casal (cabeceira na divisa).
- **Ideias:**
  1. **Tomadas nas duas paredes de cabeceira**, a da divisa e a do recuo: o quarto troca de solteiro para duas camas ou para casal sem extensão no chão.
  2. **Canto de estudo na janela da rua:** a tomada da escrivaninha vai nos **70 cm de parede** entre a janela e a parede do recuo, na altura do tampo ou baixa.
  3. **Veneziana na janela** (nas casas do Minha Casa Minha Vida, a Portaria MCID 725 usa veneziana no dormitório; ela não obriga a sua casa: quem diz é o código de obras da sua cidade e o projeto): é o único quarto virado para a rua, a 3 m da calçada.
- **Tomadas:** perímetro de 12,2 m: o mínimo é **3 pontos** (um a cada 5 m). Pela NBR 5410:2004, segundo UDESC (2026) e Engenharia 360; o eletricista confere na norma vigente.
- **Cuidado: nicho na parede da divisa.** A parede de 15 cm que separa do vizinho é a que mais se quer usar (a cabeceira encosta nela), e é a que não se quebra: prateleira de cabeceira, sim; nicho, só se o engenheiro aprovar.
- **Pergunte:** ao engenheiro, se a parede da divisa é estrutural e se leva impermeabilização no pé (o guia do MCID trata da umidade que sobe do solo; o quintal do vizinho fica do outro lado).

### Sala · 3,20 x 3,54 m livres (11,3 m²)
- **Cabe** (anexo de mobiliar): sofá de 3 lugares embaixo da janela, rack na divisa, **1,92 m** entre os dois. A porta da rua fica na parede do recuo, na ponta do quarto.
- **Ideias:**
  1. **Sem mesa de centro grande:** o caminho da porta até a cozinha passa entre o sofá e a TV. Os 1,92 m são o corredor da casa.
  2. **TV e antena na divisa**: atrás do rack não tem quarto, tem o vizinho.
  3. **Interruptor nos 43 cm** entre o fim da porta aberta e a janela, acima do encosto do sofá.
- **Tomadas:** perímetro de 13,5 m: o mínimo é **3 pontos** (um a cada 5 m). Pela NBR 5410:2004, segundo UDESC (2026) e Engenharia 360; o eletricista confere na norma vigente.
- **Cuidado:** a porta do quarto da frente abre direto na sala: quem está no sofá vê dentro. Esta planta não evita; a porta fica no canto da divisa, e o que se vê é a cama (no desenho, o pé da cama de solteiro).
- **Pergunte:** ao eletricista, onde fica o quadro de luz (a sala é o primeiro cômodo depois da porta).

### Cozinha e copa · 3,20 x 3,14 m livres (10,0 m²)
- **Cabe** (anexo de mobiliar): bancada de pia e fogão (1,80) **inteira embaixo da janela** do recuo, geladeira e mesa de 4 na divisa; 132 cm entre a mesa e a bancada sem ninguém sentado.
- **Ideias:**
  1. **Armário aéreo na divisa, por cima da mesa e da geladeira.** É a única parede da cozinha sem janela nem porta (3 m).
  2. **Banco corrido na divisa** no lugar das 2 cadeiras apertadas (anexo de mobiliar).
- **Tomadas:** perímetro de 12,7 m: o mínimo é **4 pontos** (um a cada 3,5 m), com **duas tomadas em cima da bancada da pia**. **O ponto delicado desta cozinha:** a janela (1,70 m) cobre a parede da bancada inteira. As duas tomadas da bancada não têm parede: ou ficam na faixa estreita entre o tampo e o peitoril (1,10 m no desenho), ou nas pontas (**22,5 cm** de parede entre o vão da janela e o vão da porta de fora, pelos dados do desenho, antes de batente e marco; quase nada do lado da sala); o eletricista confere se a caixa cabe com o batente e o marco. Micro-ondas e filtro vão para a divisa, perto da geladeira. A torneira da pia é de bancada, porque a parede é janela; o encanador confere. Pela NBR 5410:2004, segundo UDESC (2026) e Engenharia 360; o eletricista confere na norma vigente.
- **Cuidado:** pôr a pia embaixo da janela e só descobrir na hora do acabamento que não sobrou parede para tomada e torneira. Esta planta tem a luz certa na pia e pede esse cuidado.
- **Pergunte:** ao eletricista, se a faixa entre o tampo e o peitoril comporta tomada; ao engenheiro, onde fica o botijão e se a porta de fora, a um passo do fogão, muda alguma coisa.

### Serviço · 2,19 x 1,18 m livres (2,6 m²)
- **Cabe** (anexo de mobiliar): máquina e tanque na parede do banheiro; 53 e 65 cm na frente. Não tem porta para fora (aviso de referência do validador): a roupa sai pela porta da cozinha, a uns 2 m.
- **Ideias:**
  1. **Os canos num trecho só:** o tanque encosta no banheiro, e o banheiro no hall. Deixe as esperas de água e esgoto da máquina antes do reboco; a altura e o lugar, o encanador confere.
  2. **Varal de teto retrátil** para dia de chuva (o profissional confere a fixação).
- **Tomadas:** perímetro de 6,7 m: o mínimo é **2 pontos** (área de serviço entra na regra da cozinha, um a cada 3,5 m). O da máquina longe do tanque. O lugar de cada um, o eletricista confere. Pela NBR 5410:2004, segundo UDESC (2026) e Engenharia 360; o eletricista confere na norma vigente.
- **Cuidado:** porta do serviço batendo na máquina. Esta planta evita: os dois ficam ao lado do giro.
- **Pergunte:** ao eletricista, o DR do circuito do serviço.

### Banheiro · 2,19 x 1,58 m livres (3,5 m²)
- **Cabe** (anexo de mobiliar): box de 0,90 x 1,58 de parede a parede, na ponta do recuo; vaso e pia na parede do serviço. A janela fica **inteira dentro do box**.
- **Ideias:**
  1. **A tomada da pia do lado do hall, o mais longe do box; a distância, o eletricista confere.** No desenho, do lado do hall ela fica a mais de 1 m do box; do lado do vaso, bem mais perto (seção "Como ler").
  2. **Nicho do box, se houver, na parede do serviço, e só onde não passar cano:** do outro lado está o tanque (área molhada), não o quarto. A parede de 12 cm e a impermeabilização, o pedreiro confere.
- **Cuidado:** janela de madeira dentro do box. Aqui a janela pega água do chuveiro: o material da janela é conversa com o pedreiro.
- **Pergunte:** ao encanador, o teste do encanamento antes de fechar a parede (ficha do fabricante, nota de fonte) e o registro do banheiro.

### Hall · 0,89 x 2,94 m livres (2,6 m²)
- **Cabe:** nada (89 cm de passagem). Estante ou armário tira a passagem.
- **Ideias:**
  1. **Maleiro em cima do hall**, como na C01: 0,89 x 2,94 m acima das portas, de 40 a 70 cm de altura conforme o pé-direito. A luz do teto do hall fica embaixo do tampo; o eletricista confere.
  2. **Luz com interruptor nas duas pontas** (interruptores paralelos, manual de 2003 da nota de fonte): acende na copa e apaga na porta do quarto casal.
- **Tomadas:** cômodo de 2,25 a 6 m²: o mínimo é **1 ponto**, dentro do hall. Pela NBR 5410:2004, segundo UDESC (2026) e Engenharia 360; o eletricista confere na norma vigente.
- **Cuidado:** guardar coisa no corredor estreito. A parede da divisa do hall (2,9 m, sem porta) convida: aqui só ganchos e quadros.
- **Pergunte:** ao engenheiro, se a caixa d'água vai em cima do hall e do banheiro (é o meio das áreas molhadas) e se o maleiro atrapalha o acesso a ela.

### Quarto casal (fundos) · 3,20 x 2,99 m livres (9,6 m²)
- **Cabe** (anexo de mobiliar): cama de casal com a cabeceira na parede do recuo e 2 criados, guarda-roupa de 6 portas na divisa, **83 cm** até o pé da cama. **Queen cabe** (75 cm no pé, 70 de cada lado).
- **Ideias:**
  1. **Interruptor paralelo na cabeceira:** a porta fica no canto oposto ao da cama, junto da divisa. Apagar a luz deitado pede um segundo interruptor no criado.
  2. **Espera de ar-condicionado** na parede do fundo (janela para o quintal), antes do reboco; o circuito, o eletricista define, e o caminho do dreno, o encanador confere.
- **Tomadas:** perímetro de 12,4 m: o mínimo é **3 pontos** (um a cada 5 m). Pela NBR 5410:2004, segundo UDESC (2026) e Engenharia 360; o eletricista confere na norma vigente.
- **Cuidado:** guarda-roupa encostado em parede úmida. Aqui ele vai na divisa, não no banheiro (a parede do banheiro não tem móvel encostado): a umidade a olhar é a do pé da parede da divisa.
- **Pergunte:** ao pedreiro, como fica o pé da parede da divisa por fora, se o vizinho ainda não construiu.

### Frente do lote · 3,0 x 5,0 m
- **O que cabe:** moto, sim (uns 2,0 x 0,75 m). Carro, não: não cabe carro de frente para a rua no recuo de referência de 3,0 m; um carro popular pequeno mede uns 3,6 m; o tamanho da vaga é o código de obras que diz.
- **Ideias:**
  1. **Carro ou quintal:** no lote de 5 x 25, sobram 5,9 m no fundo. Pondo a casa 2,0 m para trás, a frente fica com **5,0 m** e o fundo com 3,9 m (dá para ir até 4,4 m). O carro fica na frente da janela do quarto da frente. O código de obras e o engenheiro decidem.
  2. **Portão de pedestre na direita, alinhado com o recuo:** o caminho da rua à porta da sala é reto (uns 6 m da rua até a porta).
  3. **Horta na frente, se a rua ficar ao norte** (a melhor para esta casa, pelo validador).
- **Pergunte:** o recuo de frente da sua cidade e onde vai o padrão de luz.

### Recuo lateral (direita) · 1,5 x 16,1 m: a rua de dentro
- **O que tem:** a porta da sala, a porta da cozinha e as janelas da sala, da cozinha, do serviço e do banheiro. É o único caminho até o fundo.
- **Ideias:**
  1. **Luz de fora na porta da sala**, com interruptor dentro: a porta fica a uns 6 m da rua, dentro do recuo.
  2. **Vasos encostados no muro do vizinho**, não na parede da casa (o guia do MCID trata da umidade que sobe do solo para a parede). O varal **não** mora aqui: entre a porta da cozinha e a janela do serviço sobram uns 60 cm de parede.
- **Cuidado, o maior desta casa: cobrir o recuo com telhado.** Aqui o telhado tira boa parte da luz de **quatro cômodos** (todas as janelas de sala, cozinha, serviço e banheiro dão para ele), e o código de obras da sua cidade diz se janela para área coberta ainda conta como ventilação. E as janelas precisam ficar a 1,5 m do vizinho (art. 1.301): mais perto, ficam em desacordo com o Código Civil, e o vizinho pode pedir para fechar em até ano e dia (art. 1.302). Marque a obra com trena.
- **Pergunte:** ao engenheiro, a calçada com caimento para longe da parede e o lado da água do telhado (art. 1.300).

### Fundo do lote · 5,9 x 5,0 m no lote de 5 x 25 (1,5 m no lote mínimo)
- **O que tem:** só a janela do quarto casal. Chega-se pelo recuo, uns 7 m depois da porta da cozinha.
- **Ideias:** varal e horta aqui, onde a roupa não passa na frente de janela de cômodo. Com a rua ao norte, o fundo fica ao sul, do lado da sombra da casa: olhe no seu lote onde o sol bate antes de plantar.
- **Onde a casa cresce:** tem chão (4,4 m além do recuo mínimo), mas **a janela do fundo é a única do quarto casal**. Cômodo aqui pede outra janela para o quarto: projeto novo.

---

## 3. F01 · Família Compacta (8,50 x 8,30 m, 71 m², 3 quartos; lote de 10 x 15 m, mínimo 10 x 12,8)

> **Planta de referência; o projeto legal é assinado por profissional habilitado.** Se a casa for de alvenaria estrutural, parede não se corta depois: nicho, rasgo de cano e de fio só onde o projeto previu. Quem diz qual é a sua é o engenheiro.

O que esta casa tem de próprio: **os 3 quartos lado a lado nos fundos**, a sala de 4,45 m (vão de 4,60 m: o validador manda o engenheiro conferir laje e viga), a cozinha aberta para a sala, e o **serviço na frente**, com porta para o recuo.

### Sala e jantar · 4,45 x 3,55 m livres (15,8 m²)
- **Cabe** (anexo de mobiliar): rack na divisa, sofá de 3 lugares solto no meio, de costas para a mesa, mesa de 4 junto da cozinha.
- **Ideias:**
  1. **A tomada do sofá vai embaixo da janela da frente**, na ponta dele: o sofá não encosta em parede (a janela tem peitoril de 1,00 m no desenho; tomada baixa passa embaixo). A altura da caixa com o peitoril, o eletricista confere.
  2. **Ponto de luz em cima da mesa:** a **3,75 m da divisa e 1,70 m da parede da frente** (centro da mesa no desenho), marcado **depois** que o engenheiro disser onde passa a viga do vão de 4,60 m.
  3. **Interruptor nos 62 cm** entre a porta da rua e a janela.
- **Tomadas:** perímetro de 16,0 m: o mínimo é **4 pontos** (um a cada 5 m). Pela NBR 5410:2004, segundo UDESC (2026) e Engenharia 360; o eletricista confere na norma vigente.
- **Cuidado:** sala atravessada por dois caminhos (a pesquisa da UFRGS liga isso à insatisfação do morador). **Esta planta não evita de todo:** quem entra e vai para os quartos passa entre a TV e o sofá (1,45 m), e o corredor corre no fundo da sala. O que ajuda: sem mesa de centro e sem tapete solto no caminho.
- **Pergunte:** ao engenheiro, a viga do vão e a verga e contraverga da janela de 2,40 m (o guia do MCID liga a trinca no canto da janela à falta de contraverga).

### Cozinha · 2,04 x 3,49 m livres (7,1 m²)
- **Cabe** (anexo de mobiliar): fogão, pia e geladeira em linha na parede do banheiro e do serviço (2,59 m depois da porta do serviço), **142 cm** livres na frente; bancada de apoio de até 1,00 m embaixo da janela.
- **Ideias:**
  1. **Armário aéreo de ponta a ponta na parede molhada:** ao contrário da E03, a parede da pia **não tem janela**. Cabem o aéreo e as tomadas da bancada; o encanador mostra por onde passam os canos antes de furar.
  2. **Despensa rasa na parede do corredor:** com a geladeira na ponta do corredor (suposição de arranjo), sobram uns 1,30 m de parede entre a quina da sala e a geladeira, num canto sem passagem.
  3. **Ponto do depurador acima do fogão:** a cozinha abre para a sala nos 3,5 m de lado, sem parede; sem exaustão, o cheiro de fritura vai para o sofá.
- **Tomadas:** perímetro de 11,1 m: o mínimo é **4 pontos** (um a cada 3,5 m), com **duas tomadas em cima da bancada da pia**. Pela NBR 5410:2004, segundo UDESC (2026) e Engenharia 360; o eletricista confere na norma vigente.
- **Cuidado:** bancada em L fechando o caminho da porta do serviço (anexo de mobiliar). A bancada de apoio fica do lado da sala.
- **Pergunte:** ao encanador, os canos de pia, banheiro e serviço num trecho só (é a parede comum dos três).

### Serviço · 1,59 x 2,09 m livres (3,3 m²)
- **Cabe** (anexo de mobiliar): tanque na parede da frente, no canto da janela; máquina na parede do banheiro. **É passagem:** porta da cozinha de um lado, porta para o recuo do outro.
- **Ideias:**
  1. **A faixa entre o tanque e a máquina (uns 91 cm) é o caminho da cozinha ao quintal:** cesto de roupa e balde vão em prateleira em cima da máquina, não no chão.
  2. **Torneira e ralo do lado de fora da porta do serviço**, no recuo (o lugar, a saída da água e o caimento, o encanador confere).
- **Tomadas:** perímetro de 7,4 m: o mínimo é **3 pontos** (área de serviço entra na regra da cozinha, um a cada 3,5 m), um deles para a máquina. O lugar de cada um, o eletricista confere. Pela NBR 5410:2004, segundo UDESC (2026) e Engenharia 360; o eletricista confere na norma vigente.
- **Cuidado:** torneira do tanque na parede da janela. Aqui o tanque encosta na parede da frente; a janela fica do lado.
- **Pergunte:** ao eletricista, o DR; ao engenheiro, onde fica o botijão (o serviço é o cômodo com porta para fora).

### Banheiro · 1,59 x 2,38 m livres (3,8 m²)
- **Cabe** (anexo de mobiliar): box de 0,90 x 0,95 no canto da frente, pia na parede da cozinha (canos juntos), vaso no fundo. **Aviso:** os dados da F01 não trazem os móveis do banheiro; o desenho 3D arruma sozinho e põe outro arranjo. As ideias abaixo seguem o arranjo do anexo.
- **Ideias:**
  1. **Tomada ao lado da pia, do lado mais longe do box; a distância, o eletricista confere.**
  2. **Registro próprio** e teste do encanamento antes do reboco (guia do MCID; ficha do fabricante, nota de fonte).
- **Cuidado:** vaso encostado na parede do quarto. Aqui o vaso fica na parede do quarto 3, onde está o guarda-roupa dele (ver o quarto 3).
- **Pergunte:** ao pedreiro, a impermeabilização da parede do fundo do banheiro.

### Corredor · 6,49 x 0,98 m livres (6,4 m²)
- **Cabe:** só passagem (98 cm). Estante rasa derruba a passagem para 68 a 73 cm (anexo de mobiliar). **Ele é aberto para a sala** em 4,6 m: na prática, é o fundo da sala até a cozinha, e fecha só nos últimos 2 m, até a porta do banheiro.
- **Ideias:**
  1. **Interruptores paralelos** (manual de 2003 da nota de fonte): acende na sala, apaga perto do banheiro.
  2. **Luz baixa perto do chão no trecho fechado**, para o caminho do quarto ao banheiro de madrugada.
- **Tomadas:** cômodo acima de 6 m², perímetro de 14,9 m: pela conta de um a cada 5 m, dariam 3 pontos (pela NBR 5410:2004, segundo UDESC (2026) e Engenharia 360; o eletricista confere na norma vigente). Como ele é aberto para a sala, pergunte ao eletricista se o corredor conta à parte.
- **Cuidado:** corredor como depósito. Aqui não cabe nem estante rasa.

### Quarto casal · 2,62 x 3,29 m livres (8,6 m²)
- **Cabe** (anexo de mobiliar): cama de casal com a cabeceira na divisa, 2 criados, guarda-roupa de **4 portas** (o de 6 não cabe) na parede do corredor; **72 cm** no pé da cama.
- **Ideias:**
  1. **Guardar para cima:** como o guarda-roupa de 6 portas não cabe, um maleiro acima do de 4 portas, até o teto, compensa.
  2. **Nada no pé da cama:** os 72 cm são a passagem; cômoda ali não cabe.
- **Tomadas:** perímetro de 11,8 m: o mínimo é **3 pontos** (um a cada 5 m); sugestão: nos dois lados da cabeceira, na divisa. Pela NBR 5410:2004, segundo UDESC (2026) e Engenharia 360; o eletricista confere na norma vigente.
- **Cuidado:** comprar queen e descobrir na entrega. Aqui ela cabe só no limite (64 cm no pé, 7 cm sobrando com os criados).
- **Pergunte:** ao pedreiro, a impermeabilização do pé da parede da divisa.

### Quarto 2 (do meio) · 2,71 x 3,29 m livres (8,9 m²)
- **Cabe** (anexo de mobiliar): duas camas de solteiro com a cabeceira na parede da janela, **91 cm** entre elas, guarda-roupa de 4 portas na parede do corredor, **93 cm** até o pé das camas.
- **Ideias:**
  1. **Uma tomada na parede de cada cama**, perto da cabeceira, não embaixo da janela (anexo de mobiliar), e sem ficar costas com costas com a do quarto vizinho.
  2. **Veneziana** (nas casas do Minha Casa Minha Vida, a Portaria MCID 725 usa veneziana no dormitório; ela não obriga a sua casa: quem diz é o código de obras da sua cidade e o projeto): as cabeceiras ficam embaixo da janela.
- **Tomadas:** perímetro de 12,0 m: o mínimo é **3 pontos** (um a cada 5 m). Pela NBR 5410:2004, segundo UDESC (2026) e Engenharia 360; o eletricista confere na norma vigente.
- **Cuidado:** cama embaixo da janela sem veneziana: luz no rosto.

### Quarto 3 · 2,62 x 3,29 m livres (8,6 m²)
- **Cabe** (anexo de mobiliar): cama de solteiro na parede da direita, escrivaninha no canto, embaixo da janela, guarda-roupa de 4 portas na parede do corredor, **93 cm** até o pé da cama; ou duas camas (82 cm entre elas) no lugar da escrivaninha.
- **Ideias:**
  1. **Canto de estudo no canto da escrivaninha:** tomada baixa e ponto de internet na parede da esquerda, ao lado da mesa (a do quarto 2: deslocada da tomada da cama de lá).
  2. **Quarto de hóspede ou escritório:** as tomadas da escrivaninha e as das duas camas servem às três funções.
- **Tomadas:** perímetro de 11,8 m: o mínimo é **3 pontos** (um a cada 5 m). Pela NBR 5410:2004, segundo UDESC (2026) e Engenharia 360; o eletricista confere na norma vigente.
- **Cuidado: guarda-roupa encostado no banheiro.** **Esta planta não evita:** a "parede do corredor" deste quarto, onde o guarda-roupa fica, é, nesse trecho, a parede do fundo do banheiro (a do vaso, no arranjo do anexo). O cuidado é o mesmo da C01: impermeabilização do lado do banheiro e vão atrás do móvel.
- **Pergunte:** ao pedreiro, a impermeabilização dessa parede pelo lado do banheiro.

### Frente do lote · 3,0 x 10,0 m
- **O que cabe:** moto, sim (uns 2,0 x 0,75 m). Carro, não: não cabe carro de frente para a rua no recuo de referência de 3,0 m; um carro popular pequeno mede uns 3,6 m; o tamanho da vaga é o código de obras que diz.
- **Ideias:**
  1. **Carro ou quintal:** no lote de 10 x 15, sobram 3,7 m no fundo. Com a casa até 2,2 m para trás, a frente fica com **5,2 m** e o fundo com **1,5 m**, o mínimo do Código Civil para janela (art. 1.301), para as janelas dos 3 quartos; o código de obras pode pedir mais. O quintal some. Decida antes da marcação, com o código de obras e o engenheiro.
  2. **Portão de pedestre na esquerda**, na direção da porta da sala, que fica no canto da divisa.
- **Pergunte:** o recuo de frente da cidade e o lugar do padrão de luz.

### Recuo lateral (direita) · 1,5 x 8,3 m
- **O que tem:** a porta do serviço, a janela do serviço e a do banheiro; é o caminho da frente ao quintal do fundo (uns 6,5 m da porta do serviço).
- **Ideias:** calçada com caimento e luz de fora na porta do serviço.
- **Cuidado:** cobrir o recuo tira boa parte da luz da única janela do serviço e da do banheiro, e o código de obras da sua cidade diz se janela para área coberta ainda conta como ventilação.

### Fundo do lote · 3,7 x 10,0 m no lote de 10 x 15 (1,5 m no lote mínimo)
- **O que tem:** as janelas dos 3 quartos.
- **Ideias:** **com a rua ao sul (a melhor para esta casa, pelo validador), o fundo fica ao norte**, o lado do sol: é o melhor lugar do lote para varal e horta. Condensadoras de ar dos 3 quartos também saem por aqui.
- **Onde a casa cresce:** **não no fundo:** é a janela dos 3 quartos. Na frente, uma varanda ou um abrigo cobriria as janelas da sala e da cozinha, e o recuo de frente costuma ter regra própria na prefeitura. As duas coisas são projeto novo do arquiteto.

---

## 4. O que disso vira o quê (recomendação; quem decide é o dono)

**Página do e-book** (o Redator escreve, o Designer desenha, o Revisor confere):
1. **"Antes do reboco", uma por casa:** a planta com tomadas, pontos de luz e interruptores marcados no lugar dos móveis (a conta mínima da NBR 5410:2004 pelas fontes do "Como ler" e as ideias acima). É o que o comprador leva ao eletricista, que confere na norma vigente. A da C01 espera o conserto do serviço.
2. **"Carro ou quintal: decida antes de marcar a obra":** as 3 casas, o recuo de referência de 3,0 m contra um carro popular pequeno de uns 3,6 m (o tamanho da vaga é o código de obras que diz), e quanto a casa pode ir para trás em cada lote (2,0, 4,4 e 2,2 m).
3. **"O que não fazer depois", por casa:** C01, não fechar a varanda; E03, não cobrir o recuo; F01, não construir no fundo. Cada um com o porquê tirado da planta.
4. **"Cômodo a cômodo", uma por casa:** este documento enxuto, com os 4 itens por cômodo.

**Post ou vídeo** (o Diretor dá a ideia principal primeiro; o Editor e o Redator fazem):
1. "No recuo de 3 m não cabe carro de frente para a rua": um carro popular pequeno mede uns 3,6 m, e o tamanho da vaga é o código de obras que diz; o que fazer antes da obra.
2. "O maleiro que ninguém vê": o hall da C01 virando armário por cima das portas.
3. "Não cubra o corredor lateral": a E03 com as 4 janelas que dependem dele.
4. "A tomada do banheiro: do lado mais longe do box": o caso da E03 (um lado da pia perto do box, o outro a mais de 1 m). **Sem número de distância:** a distância, o eletricista confere (ver "O que ainda não pode virar página").
5. "Pia embaixo da janela: onde vai a tomada?" (E03).

**O que eu recomendo desenhar** (Arquiteto e Designer, depois do "sim" do dono):
1. **Planta de pontos de cada casa**, saída do mesmo dado da planta (tomada baixa, média e alta, ponto de luz, interruptor simples e paralelo).
2. **Vista de parede:** a bancada da E03 embaixo da janela, com a faixa da tomada; a parede do box da C01 com o guarda-roupa do outro lado.
3. **Corte do hall da C01** com o maleiro em cima das portas, nos dois pés-direitos (2,55 e 2,80 m).
4. **A C01 no lote de 8 x 15 nas duas posições:** a de hoje e a recuada 2 m, com o carro (depois do conserto do serviço: o desenho mostra a casa inteira).
5. **A sala da C01 com a TV na divisa** (ideia 1 da sala), se o Arquiteto e o dono aprovarem mudar o 3D: só vira desenho se o 3D mostrar o mesmo arranjo.

---

## 5. Para a equipe (não vai ao público)

- **C01, serviço, casa do lançamento:** a parede do fundo (1,19 m livres) não comporta a porta de fora (0,90) e a janela (0,70); no desenho a janela cai em cima da porta. O `checar.py` já avisa (`janelas_sobre_portas`), com a nota "até as casas de fora do lançamento serem refeitas", mas a C01 **está** no lançamento. Espera a decisão do dono sobre o conserto; depois, o Arquiteto aplica em `projetos.py`, com o validador e o arrasto de sempre (exportar, 3D, imagem 3D, PDF, calculadora). Não mexi: a tarefa proibia.
- **Convenção de lado e sol, a conferir:** `ORIENTACAO` em `plantas.py` dá esquerda = oeste com a rua ao norte, mas a página do lote no PDF desenha a rua embaixo e a esquerda à esquerda, onde, com a rua ao norte, fica o leste. Pode ser um espelho no cálculo de sol das janelas laterais. Não conferi a fundo; por isso este documento só fala de sol na frente e no fundo.
- **Ampliação desenhada:** as 3 casas não têm (passo 8 do método da apostila 2). Este documento diz onde não dá; desenhar onde dá é trabalho novo, que o dono decide.
- **Frases que não podem ir à página:** "cabe carro", "pode fechar", "pode cobrir", "sem engenheiro"; nem número mínimo de tomadas sem fonte, Portaria do MCMV como regra para a casa do comprador, frequência de erro sem fonte, ou marca e modelo de carro e de moto (lista do veto do Revisor de risco, 24/11/2026). Toda ideia de obra termina com quem decide.

---

## 6. O que ainda não pode virar página

- **O serviço da C01:** espera o conserto da janela em cima da porta (decisão do dono). Nenhuma página, imagem 3D, vista ou planta de pontos que mostre esse cômodo sai antes da planta resolvida em `projetos.py` e do arrasto de sempre.
- **A distância da tomada ao box (página e post 4):** a contagem de tomadas fechou em duas fontes secundárias de 2004 ou mais novas, mas a distância ao box só tem o manual de 2003, anterior à norma vigente. A regra do banheiro na norma de 2004 (item 9.1) não foi lida, e a revisão da NBR 5410 em consulta nacional (O Setor Elétrico, agosto de 2025) mexe na tomada perto do box. Veto mantido do Revisor (24/11): nenhum número de distância vai à página nem ao post 4; os dois dizem "do lado mais longe do box; a distância, o eletricista confere".
- **Divergência da USP, não resolvida:** um material da USP (atrás de login, só visto no resumo da busca, não aberto) fala em uma tomada por bancada de 0,30 m ou mais; as duas fontes abertas, que citam a norma de 2004, falam em duas em cima da bancada da pia. Este documento usa as duas tomadas e diz que o eletricista confere.

**Nota das medidas de carro e de moto:** caderno `pesquisas/plantas.md`, entradas do Arquiteto de 24/11/2026 (carro popular pequeno: AutoPapo, avaliação de 2026, 3.596 mm de comprimento; moto pequena: Carzin, 1.996 x 746 mm). As duas são fontes secundárias; a ficha do fabricante não foi aberta.
