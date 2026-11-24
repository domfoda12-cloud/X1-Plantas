# Como mobiliar as 3 casas do lançamento (conteúdo técnico)

> **Medidas conferidas em 24/11/2026, segunda conferência**, cômodo por cômodo, pela face de dentro da parede, contra `ebook/plantas/dados/<ID>.json`, `video/src/plantas/<ID>.js` (móveis, portas e janelas do desenho 3D) e `python3 ferramentas/plantas.py validar` (C01, E03 e F01: zero erros). Mudou desde 23/11: a sala e a cozinha da C01, a copa da E03, o quarto 2, a sala, a cozinha e o serviço da F01. **Mudou de novo em 24/11, à tarde** (conserto dos achados da seção 5): os dois quartos, o serviço e o banheiro da C01, o banheiro da E03, o quarto casal e o banheiro da F01; a parede de fora do 3D agora fica onde o validador põe (15 cm para dentro). **Segunda conferência (24/11, noite):** o desenho passou a usar os móveis de loja desta lista: guarda-roupa de 4 portas (1,61 x 0,46) e de 6 portas (2,00 x 0,47) nos quartos da E03 e da F01 (eram 0,60 de fundo), tanque e máquina da Portaria (0,52 x 0,53 e 0,60 x 0,65) no serviço da E03 e da F01; na F01, o guarda-roupa do quarto 3 foi para a parede do corredor.
> **Pedido do dono (23/11, comentário no quadro; `decisoes-do-dono-2026-11-23.md`, linha 85), palavra por palavra:** "quero algo mais como detalhes de como a casa pode ser mobiliada ou ideias de construções, coisas assim". Troca a ideia do "raio-X da casa".
> **Autor:** Arquiteto, 23/11/2026 (medidas refeitas em 24/11). **É conteúdo técnico, não texto final:** o Designer faz a página e o Redator escreve; nada vai ao público sem o Revisor de risco.
> **Casas:** C01 Casa Compacta (51 m², com hall), E03 Casa Fita (56 m², 2 quartos), F01 Casa Família Compacta (71 m², 3 quartos). Dados oficiais de `ebook/plantas/dados/<ID>.json` (validação de 24/11: zero erros), portas e janelas do `ferramentas/planta3d.py` (mesma geometria da prévia).
> **Suposições (o dono não disse):** que vira uma página por casa no e-book (pode ser só a amostra grátis); que o comprador compra móvel pronto de loja, não planejado. Com móvel planejado a conta muda: refazer.

## Como ler as contas

- **Medidas dos cômodos por dentro das paredes** (as do validador: parede externa de 15 cm, interna de 12 cm). Medidas dos móveis: a lista do fim (seção 4), com a fonte. **Onde a conta descreve o arranjo do desenho 3D**, os móveis são os do desenho (por exemplo, bancada de pia e fogão de 0,62 de fundo e geladeira de 0,72 x 0,70); nas outras ideias, os de loja da seção 4.
- **"Passagem"** é o vão livre entre dois móveis, ou entre o móvel e a parede, em cm. A régua: **50 cm** ao lado da cama e na frente do guarda-roupa (Portaria MCID 725 e Anexo G da NBR 15575, que é informativo); **85 cm** na frente de pia, fogão e geladeira (Anexo G); **80 cm** entre duas camas de solteiro (Portaria MCID 725; o Anexo G aceita 60); **75 cm** da borda da mesa para a cadeira (Anexo G). A Portaria vale para o Minha Casa Minha Vida, não obriga casa particular: aqui é régua de conforto.
- O raio da folha da porta (80 cm nas internas, 90 na da rua) conta como lugar ocupado: nenhum móvel abaixo entra nele.
- **Régua federal, de uma vez:** as 3 casas passam na sala (2,40 m de largura), na cozinha (1,80 m), no banheiro (1,50 m) e no quarto para duas pessoas (2 camas de 0,90 com 80 cm entre elas: C01 quarto da frente, E03 quarto da frente, F01 quartos 2 e 3).

---

## 1. C01 · Casa Compacta (6,50 x 8,50 m, 51 m², 2 quartos; cabe num lote de 8 x 15 m)

A parede da esquerda (varanda, sala e serviço) fica na divisa, sem janela.

| Cômodo (por dentro) | O que cabe, com a passagem que sobra | O que não cabe |
|---|---|---|
| **Quarto casal** 2,94 x 3,19 m | Cama de casal padrão (**1,38 x 1,88**, a do desenho) com a cabeceira na parede da cozinha e **2 criados** (o do lado da porta fica 2 cm fora do giro da folha); **guarda-roupa de 6 portas** (2,00 x 0,47) na parede do hall, logo depois da porta: **80 cm livres** na frente dele até a lateral da cama. No pé da cama: **1,06 m** até a parede da direita. Do lado da janela: **54 cm** | Queen (1,58 x 1,98): do lado da janela sobram 34 cm (a régua pede 50). Não recomendo. Guarda-roupa na parede da direita, de frente para o pé da cama: com a cama de 1,88, sobram 59 cm na frente do de 6 portas e 60 cm na do de 4 portas (0,46): no limite |
| **Quarto** (da frente) 2,85 x 3,09 m | **Duas camas de solteiro** (0,90 x 1,90) com a cabeceira na parede da rua, uma encostada em cada parede: **1,05 m entre elas** (a Portaria pede 80) e um criado no meio, junto da cabeceira; **guarda-roupa de 4 portas** (1,61 x 0,46) na parede do hall, no canto do lado da janela, fora do giro da porta: **73 cm** até o pé das camas. Ou cama de casal (1,40 + 50 + 50 = 2,40 m ≤ 2,85) | Guarda-roupa de 6 portas (2,00 m): a parede livre tem 2,05 m; só encostado no batente, sem folga |
| **Sala e jantar** 3,14 x 3,99 m | **Sofá de 2 lugares** (o do desenho: 1,40 x 0,88) na parede da divisa, depois do giro da porta; **rack de TV** (1,60) na parede do quarto, a **1,86 m** do sofá; **mesa de 4 lugares** (1,20 x 0,80) no fundo, junto da passagem da cozinha: as cadeiras ficam com **46 cm** do lado da parede do serviço e **51 cm** do lado do braço do sofá. Da ponta da mesa até a parede do quarto: **1,81 m livres**, o caminho da cozinha e do hall | **75 cm para puxar a cadeira:** não cabem. Do braço do sofá à parede do serviço são 1,78 m, e mesa com cadeira dos dois lados pede 2,30. As 4 cadeiras entram, mas a pessoa senta e levanta de lado, apertada. O que cabe sem aperto: **banco sem encosto** encostado na parede do serviço e a mesa encostada no banco (as 2 cadeiras do lado do sofá ficam com 58 cm). Sofá de 3 lugares (2,00): chega à borda da mesa e tira as 2 cadeiras desse lado |
| **Cozinha** 1,83 x 2,95 m | Tudo numa parede só (a do quarto casal), 2,95 m: **geladeira** (0,72 x 0,70) na ponta da sala, depois a **bancada de pia e fogão** (1,80 x 0,62), e ainda sobram 30 cm até a parede do fundo. Livre na frente: **113 cm** da geladeira e **121 cm** da bancada | Mesa: não cabe; ela fica na sala. Geladeira na parede da esquerda (a do serviço): sobram 51 cm entre ela e a bancada |
| **Serviço** 1,19 x 2,89 m | **Tanque** (0,52 x 0,53) **e máquina** (0,60 x 0,65), as medidas da Portaria, lado a lado na parede da divisa, entre os giros das duas portas: a folha da porta da cozinha passa a **3 cm** do tanque e a da porta de fora a **21 cm** da máquina. Na frente: **66 cm** do tanque e **54 cm** da máquina | Armário fundo ou secadora ao lado: o cômodo tem só 1,19 de largura. Tanque no canto da porta da cozinha: a folha bate nele |
| **Banheiro** 1,84 x 1,68 m | Box de **0,95 x 0,90** (a Portaria pede 0,90 x 0,95) no canto da frente, do lado da janela; **vaso na parede da janela**, entre o box e o fundo (19 cm de cada lado); **pia no fundo**, ao lado da porta: a folha aberta passa a 2 cm dela. Entre a pia e a frente do vaso, 52 cm. Ninguém atravessa o box para chegar ao vaso ou à pia | Vaso no fundo, de frente para o box: ficaria a 13 cm do vidro |
| **Hall** 1,04 x 1,68 m | Só passagem: abre para 2 quartos e o banheiro | Qualquer móvel |
| **Varanda** 3,35 x 1,20 m | Fechada na divisa; a porta da sala fica na ponta da esquerda. Cadeiras encostadas na janela da sala, fora da porta | — |

**Um arranjo na sala, só mexendo nos móveis (proposta conferida e não aplicada, 24/11):** girar a mesa (lado comprido de frente para a TV), de 0,90 a 1,70 m da divisa, logo depois do braço do sofá: as 4 cadeiras ganham os 75 cm (2 do lado da divisa, 2 do lado do hall) e sobram 84 cm até a abertura do hall.
O preço, medido no desenho: atrás da mesa ficam 54 cm, e a entrada da cozinha passa a uns **69 cm** com alguém sentado do lado do hall (81 com as cadeiras encostadas), na diagonal entre a cadeira e a quina da geladeira. Abaixo dos 80 cm de passagem: a mesa fica como está.

**Três ideias de arrumação**
1. **A mesa entre o fogão e o sofá.** A mesa de 4 fica no fundo da sala, colada na passagem da cozinha: o prato vai do fogão à mesa em poucos passos, e o sofá fica na parede da divisa, olhando a TV. As cadeiras ficam com 46 e 51 cm: para sentar sem aperto, um banco sem encosto do lado da parede.
2. **A cozinha numa parede só.** Geladeira na ponta da sala, pia e fogão depois, em linha na parede do quarto (2,57 m de 2,95): a janela do fundo fica livre para a luz e sobram 121 cm na frente da bancada (113 na frente da geladeira).
3. **O quarto da frente para dois.** Duas camas de solteiro, uma em cada parede, com 1,05 m entre elas e um criado no meio; guarda-roupa de 4 portas na parede do hall, fora do giro da porta, com 73 cm livres na frente: quarto de duas crianças sem tirar a passagem.

**Três ideias de construção (o engenheiro decide)**
1. **Tomada onde o móvel vai.** Leve este arranjo ao eletricista antes do reboco: tomada e antena atrás do rack, tomadas dos dois lados da cama de casal, tomada da geladeira e da bancada na parede do quarto casal. Onde passa cada fio é ele quem decide.
2. **O cano do banheiro é só dele.** O banheiro não encosta na cozinha nem no serviço (aviso do validador): tem cano próprio descendo. Pergunte ao engenheiro, antes do piso, por onde ele passa e quanto isso pesa.
3. **A água do telhado na divisa.** A varanda, a sala e o serviço encostam no vizinho, e a chuva não pode cair no terreno dele (Código Civil, art. 1.300). Telhado para dentro ou calha: o engenheiro escolhe.

**Ampliação:** esta planta **não prevê** cômodo a mais, nem espera de laje. Aumentar a casa é projeto novo, do arquiteto ou do engenheiro.

---

## 2. E03 · Casa Fita (3,50 x 16,10 m, 56 m², 2 quartos; cabe num lote de 5 x 25 m)

A sala, a cozinha e os dois quartos têm **3,20 m livres** de largura (o serviço e o banheiro, 2,19 m, lado a lado com o hall). A parede da esquerda é a divisa de ponta a ponta, sem janela (Código Civil, art. 1.301); as janelas da sala, da cozinha, do serviço e do banheiro e as duas portas de fora dão para o recuo de 1,50 m da direita; os quartos têm janela na frente e no fundo.

| Cômodo (por dentro) | O que cabe, com a passagem que sobra | O que não cabe |
|---|---|---|
| **Quarto casal** (fundos) 3,20 x 2,99 m | Cama de casal com a cabeceira na parede do recuo e **2 criados**; **guarda-roupa de 6 portas** (2,00 m) na parede da divisa, depois do giro da porta: **83 cm** até o pé da cama; **79 e 80 cm** dos dois lados da cama. **Queen (1,58 x 1,98) cabe**: 75 cm no pé, 70 cm de cada lado | — |
| **Quarto** (da frente) 3,20 x 2,89 m | No desenho: cama de solteiro na divisa, escrivaninha embaixo da janela e **guarda-roupa de 4 portas** na parede do recuo, no canto da sala. **Duas camas de solteiro cabem, mas não no lugar da escrivaninha** (ali a 2ª cama fica a 34 cm da 1ª, por causa da frente do guarda-roupa): cabem com a cabeceira na parede do recuo, **80 cm entre elas** (a Portaria pede 80) e um criado no meio, e o guarda-roupa vai para a parede da divisa, no canto da janela, com **84 cm** livres na frente. Ou **cama de casal** com a cabeceira na divisa, 1 criado do lado da janela, 50 cm de passagem desse lado e guarda-roupa de 4 portas na parede do recuo, a 84 cm do pé | Com casal, o criado do lado da porta: cai no giro dela. Duas camas com a cabeceira na divisa: a de trás cai no giro da porta |
| **Sala** 3,20 x 3,54 m | **Sofá de 3 lugares** (o do desenho: 2,10 x 0,88) embaixo da janela, depois do giro da porta da rua; **rack de TV** na parede da divisa, a **1,92 m** do sofá | Mesa de centro grande: o caminho da porta até a cozinha passa entre o sofá e a TV |
| **Cozinha e copa** 3,20 x 3,14 m | **Bancada de pia e fogão** (1,80 x 0,62) embaixo da janela; **geladeira** na parede da divisa e, ao lado dela, a **mesa de 4** (1,20 x 0,80), com 2 cadeiras do lado da divisa. Entre a mesa e a bancada: **132 cm** sem ninguém, **87 cm** com as cadeiras encostadas, uns **57 cm** com alguém sentado. Da mesa à passagem do hall: 104 cm. Na frente da geladeira: 188 cm | As 2 cadeiras do lado da divisa ficam com 46 cm: apertadas. Mesa de 6 lugares: a passagem do hall cai para 64 cm |
| **Serviço** 2,19 x 1,18 m | **Máquina e tanque** na parede do fundo, ao lado do giro da porta (o trecho livre tem 1,20 m; os dois pedem 1,12). Na frente: **53 cm** da máquina e **65 cm** do tanque | Porta para o quintal: o serviço não tem (a 2ª porta de fora é a da cozinha) |
| **Banheiro** 2,19 x 1,58 m | Box na ponta do recuo, de parede a parede (1,58 x 0,90, maior que os 0,90 x 0,95 da Portaria), vaso e pia na parede do serviço; a porta (no hall) passa a 2 cm da quina da pia e a 16 cm do vaso | — |
| **Hall** 0,89 x 2,94 m | Só passagem (89 cm), até o banheiro e o quarto casal | Armário ou estante: tira a passagem |

**Três ideias de arrumação**
1. **A parede da divisa guarda.** Ela é a única sem janela nem porta, de ponta a ponta: rack ou estante na sala, geladeira e mesa na copa, guarda-roupa de 6 portas no quarto do fundo. O que fica na outra parede é a janela.
2. **Banco corrido na divisa, na copa.** Trocar as 2 cadeiras do lado da parede (que ficam com 46 cm) por um banco encostado, de uns 40 cm de fundo: a mesa de 4 continua, chega 6 cm mais perto da parede, e a passagem até a pia fica em 93 cm com as cadeiras do outro lado encostadas.
3. **Cama na parede cega.** No quarto da frente, a cama de casal com a cabeceira na divisa fica longe da janela e da rua; a janela da frente fica livre, sem guarda-roupa na frente.

**Três ideias de construção (o engenheiro decide)**
1. **Os canos num trecho só.** O banheiro encosta no serviço e o serviço encosta na cozinha: a água e o esgoto correm juntos, com menos parede para abrir. O traçado final é do engenheiro.
2. **A divisa sem janela e sem goteira.** Não abra basculante na parede da divisa por conta própria: o vizinho pode tapar quando construir (Código Civil, art. 1.302). E a chuva do telhado não pode cair no terreno dele (art. 1.300): telhado para o recuo ou calha, o engenheiro escolhe.
3. **O recuo lateral é a rua de dentro.** As portas da sala e da cozinha abrem para os 1,50 m da direita: a calçada lateral com caimento para longe da parede leva a água embora. Medida e material, o engenheiro define.

**Ampliação:** esta planta **não prevê** cômodo a mais, nem espera de laje. Aumentar a casa é projeto novo, do arquiteto ou do engenheiro.

---

## 3. F01 · Casa Família Compacta (8,50 x 8,30 m, 71 m², 3 quartos; cabe num lote de 10 x 15 m)

A parede da esquerda (sala e quarto casal) fica na divisa, sem janela. Os 3 quartos ficam nos fundos, com janela para o fundo do lote.

| Cômodo (por dentro) | O que cabe, com a passagem que sobra | O que não cabe |
|---|---|---|
| **Quarto casal** 2,62 x 3,29 m | Cama de casal com a cabeceira na parede da divisa e **2 criados** (o do lado da porta fica 3 cm fora do giro da folha); **guarda-roupa de 4 portas** (1,61 m) na parede do corredor, depois do giro da porta: **82 cm** até a lateral da cama. No pé da cama: **72 cm** até a parede. Queen: cabe no limite (64 cm no pé; com os dois criados de 45 cm, sobram 7 cm) | **Guarda-roupa de 6 portas** (2,00 m): a parede do corredor tem 1,72 m livres; na parede da direita, sobram 25 cm até o pé da cama. **Não cabe** |
| **Quarto 2** (do meio) 2,71 x 3,29 m | **Duas camas de solteiro** com a cabeceira na parede da janela, **91 cm entre elas** (cabe um criado no meio); **guarda-roupa de 4 portas** na parede do corredor: **93 cm** até o pé das camas | Guarda-roupa de 6 portas: parede livre de 1,72 m |
| **Quarto 3** 2,62 x 3,29 m | No desenho: cama de solteiro na parede da direita, escrivaninha no canto da esquerda, embaixo da janela, e **guarda-roupa de 4 portas** (1,61 m) na parede do corredor, depois da porta (sobram 1,77 m de parede), com **93 cm** até o pé da cama. **Cabem duas camas de solteiro no lugar da escrivaninha:** 0,90 + 0,82 + 0,90 = 2,62 m, **82 cm entre elas** (a Portaria pede 80), com o criado no meio; o guarda-roupa fica onde está, com os mesmos 93 cm na frente | Guarda-roupa de 6 portas. As cabeceiras ficam embaixo da janela (peitoril de 1,00 m): funciona, mas a janela fica atrás da cama |
| **Sala e jantar** 4,45 x 3,55 m | **Rack de TV** na parede da divisa, depois do giro da porta da rua; **sofá de 3 lugares** (o do desenho: 2,10 x 0,88) de frente para ela, a **1,45 m**, de costas para a mesa; **mesa de 4** (1,20 x 0,80) junto da cozinha, com **130 cm** de um lado e **145 cm** do outro para as cadeiras. Entre o encosto do sofá e a cabeceira da mesa (que fica sem cadeira): **42 cm**; da ponta do sofá ao corredor: **70 cm** | Mesa de 6 lugares (1,60 m): encosta no sofá; só cabe avançando 30 cm para dentro da cozinha (sobram 1,12 m até a bancada) |
| **Cozinha** 2,04 x 3,49 m | Na parede do banheiro e do serviço (2,59 m depois da porta do serviço): **fogão, pia e geladeira** em linha. No desenho, bancada de pia e fogão de 1,60 x 0,62 e geladeira de 0,72: sobram 27 cm. Com pia de 1,20, fogão de 0,60 e geladeira de 0,70 de loja (2,50 m), sobram 9 cm. Livre na frente: **142 cm** da bancada (134 da geladeira). Na parede da janela cabe uma **bancada de apoio de até 1,00 m**, do lado da sala, deixando 1,04 m livres até a porta do serviço | Mesa: fica na sala. Bancada em L colada na pia: fecha o caminho da porta do serviço |
| **Serviço** 1,59 x 2,09 m | **Tanque** na parede da frente, no canto da janela, e **máquina** na parede do banheiro, junto da parede da cozinha, fora do giro das duas portas: **62 cm** na frente do tanque até o giro da porta de fora, **54 cm** na frente da máquina até o giro da porta da cozinha (medidas da Portaria: tanque 0,52 x 0,53, máquina 0,60 x 0,65). Tem porta para o recuo lateral | — |
| **Banheiro** 1,59 x 2,38 m | Box de 0,90 x 0,95 no canto da frente, pia na parede da cozinha (canos juntos), vaso no fundo, a 30 cm do giro da porta. (O desenho 3D, que é automático aqui, põe o box de 0,95 x 0,90 no canto da cozinha, o vaso ao lado dele e a pia na parede da janela, a 47 cm do giro) | — |
| **Corredor** 6,49 x 0,98 m | Só passagem (98 cm) | Estante ou armário raso: com 25 a 30 cm de fundo, a passagem cai para 68 a 73 cm, abaixo de 80 |

**Três ideias de arrumação**
1. **Três quartos que servem a 5.** Casal no quarto da divisa e duas camas de solteiro em cada um dos outros dois (80 cm ou mais entre elas), cada quarto com o seu guarda-roupa de 4 portas na parede do corredor.
2. **O sofá separa sem parede.** Na sala de 4,45 m, o sofá de 3 lugares de costas para a mesa divide estar e jantar: a TV fica na parede da divisa e a mesa encostada na cozinha.
3. **Cozinha na parede molhada, com apoio na janela.** Fogão, pia e geladeira em linha na parede que o banheiro e o serviço dividem, e uma bancada de apoio de até 1,00 m embaixo da janela da frente, do lado da sala, sem fechar a porta do serviço.

**Três ideias de construção (o engenheiro decide)**
1. **Os canos num trecho só.** Banheiro, cozinha e serviço dividem a mesma parede: água e esgoto juntos, com menos parede para abrir. O traçado final é do engenheiro.
2. **A sala de 4,60 m pede viga.** O vão da sala e jantar é grande (4,60 m de eixo a eixo, 4,45 livres; nota do validador): laje, viga e pilar são do engenheiro. Não tire nem ponha parede por conta própria.
3. **Tomada onde o móvel vai.** Nos quartos com duas camas embaixo da janela, as tomadas ficam nas paredes do lado das camas, não embaixo da janela; na sala, tomada e antena atrás do rack, na parede da divisa. Quem traça é o eletricista.

**Ampliação:** esta planta **não prevê** cômodo a mais, nem espera de laje. Aumentar a casa é projeto novo, do arquiteto ou do engenheiro.

---

## 4. Medidas de móveis comuns no Brasil (as usadas nas contas)

Registradas no caderno `pesquisas/plantas.md` (Arquiteto, 23/11/2026). As de loja são de **um modelo vendido**, não norma: a ficha do móvel que o comprador escolher manda.

| Móvel | Medida usada (largura x fundo) | Fonte | Grau |
|---|---|---|---|
| Colchão de solteiro | 0,88 x 1,88 (contei a cama com 0,90 x 1,90) | [MadeiraMadeira, guia de colchões](https://www.madeiramadeira.com.br/central-de-dicas/artigos/como-comprar-colchao-pela-internet); Portaria MCID 725 (cama 0,90 x 1,90) | Catálogo + portaria |
| Colchão de casal | 1,38 x 1,88 (contei a cama com 1,40 x 1,90) | Mesmo guia; Portaria MCID 725 e Anexo G (cama 1,40 x 1,90) | Catálogo + portaria |
| Colchão queen | 1,58 x 1,98 | Mesmo guia | Catálogo |
| Criado-mudo | 0,45 x 0,40 | Medida do desenho 3D; o Anexo G usa 0,50 x 0,50 | **Hipótese** |
| Guarda-roupa de 3 portas (solteiro) | 1,15 x 0,53 | [Ficha Vicenzo, MadeiraMadeira](https://www.madeiramadeira.com.br/-976502.html) | Catálogo |
| Guarda-roupa de 4 portas de bater (casal) | 1,61 x 0,46; folha de cerca de 40 cm | [Ficha Madrid, MadeiraMadeira](https://www.madeiramadeira.com.br/guarda-roupa-casal-4-portas-bater-madrid-bege-creme-branco-176379464.html) | Catálogo |
| Guarda-roupa de 6 portas de bater (casal) | 2,00 x 0,47; folha de cerca de 33 cm | [Ficha Roma, MadeiraMadeira](https://www.madeiramadeira.com.br/guarda-roupa-casal-6-portas-3-gavetas-com-espelho-com-pes-roma-espresso-moveis-919941.html) | Catálogo |
| Sofá de 2 lugares | 1,50 x 0,80 | [Ficha Basic, MadeiraMadeira](https://www.madeiramadeira.com.br/-868779.html) (o Anexo G aceita 1,20 x 0,70) | Catálogo |
| Sofá de 3 lugares | 2,00 x 0,88 | [Ficha Dior, MadeiraMadeira](https://www.madeiramadeira.com.br/-802113.html) | Catálogo |
| Rack de TV | 1,60 x 0,40 | Medida do desenho 3D; o Anexo G pede estante de 0,80 x 0,50 | **Hipótese** |
| Mesa de 4 lugares | 1,20 x 0,80, mais 75 cm por cadeira | [Ficha Miami, MadeiraMadeira](https://www.madeiramadeira.com.br/-854599.html); folga do Anexo G | Catálogo + norma informativa |
| Geladeira duplex (300 a 400 L) | 0,60 a 0,65 x 0,65 a 0,70; com a folga (3 a 5 cm dos lados, 5 a 10 atrás), contei 0,70 x 0,75 | [Brastemp, como medir](https://www.brastemp.com.br/experience/tech/tamanho-da-geladeira-como-medir-e-escolher/) | Fabricante |
| Fogão de 4 bocas de piso | 0,47 a 0,56 x 0,58 a 0,69; contei 0,60 com a folga lateral do manual (3 a 10 cm) | [Casa dos Eletrodomésticos, guia](https://www.casadoseletrodomesticos.com.br/qual-e-a-medida-exata-de-um-fogao-4-bocas-mesa-de-vidro-para-planejar-o-espaco-da-cozinha-sem-erro) | Loja |
| Pia (bancada) | 1,20 x 0,50; bancada de obra de 0,60 de fundo | Anexo G (pelo estudo de Porto Velho, na apostila); o fundo de 0,60 é **hipótese** | Norma informativa + hipótese |
| Máquina de lavar e tanque | 0,60 x 0,65 e 0,52 x 0,53 | Anexo G (pelo estudo de Porto Velho); [Portaria MCID 725/2023 compilada](https://www.gov.br/cidades/pt-br/acesso-a-informacao/institucional/base-juridica/portarias/2023/Port.MCIDn725_2023COMPILADA.pdf), Anexo, item 2.I.c.vi (lida em 24/11) | Norma informativa + portaria |
| Box | 0,90 x 0,95 | [Portaria MCID 725/2023 compilada](https://www.gov.br/cidades/pt-br/acesso-a-informacao/institucional/base-juridica/portarias/2023/Port.MCIDn725_2023COMPILADA.pdf), Anexo, item 2.I.c.v, redação da Portaria 335/2026 (lida em 24/11; caderno `pesquisas/normas.md`) | Portaria |
| Passagens | 50 cm (cama, guarda-roupa), 85 cm (pia, fogão, geladeira), 80 cm (entre camas), 75 cm (cadeira) | Portaria MCID 725 e Anexo G, lidos na apostila (`ebook/referencias/ARQUITETO.md`) | Portaria + norma informativa |

**O que o desenho 3D usa, onde é diferente da lista** (`video/src/plantas/<ID>.js`, 24/11, à tarde): sofá de 2 lugares 1,40 x 0,88; sofá de 3 lugares 2,10 x 0,88; bancada de pia e fogão 1,80 x 0,62 (C01, E03) e 1,60 x 0,62 (F01); geladeira 0,72 x 0,70; cadeira da mesa 0,45 para fora do tampo; cama de casal 1,40 x 1,90 (E03, F01; na C01, 1,38 x 1,88); box 0,95 x 0,90 (C01, F01) e 0,90 x 1,58 (E03). **Guarda-roupa, tanque e máquina são os desta lista nas 3 casas** (segunda conferência, 24/11): 4 portas 1,61 x 0,46, 6 portas 2,00 x 0,47, tanque 0,52 x 0,53 e máquina 0,60 x 0,65.

Ressalvas: o texto oficial da NBR 15575 não foi lido (o Anexo G vem pelo estudo de Porto Velho); nenhuma norma ABNT de tamanho de colchão foi achada (é convenção de mercado); o guia de sofá da Sklum (de Portugal) dá 1,40 a 1,80 para o de 2 lugares e 1,80 a 2,20 para o de 3 lugares (só de apoio); o banco corrido de 40 cm de fundo é **hipótese** (não há ficha de loja registrada).

---

## 5. Para a equipe (não vai ao público)

- **Resolvido em 24/11:** a geladeira da C01 saiu da frente da janela da cozinha; agora fica na ponta da sala, com a bancada depois (conferido no `C01.js`).
- **Resolvido em 24/11, à tarde (Arquiteto):** o motor 3D desenha a parede de fora com os 15 cm para dentro, como o validador, e os móveis param na mesma face (`paredes_reais` em `ferramentas/planta3d.py`); a interna tem 12 cm no eixo. C01: duas camas e guarda-roupa com 73 cm na frente no quarto da frente; cama de casal padrão e guarda-roupa de 6 portas com 80 cm na frente no quarto casal; tanque fora do giro da porta da cozinha; box de 0,95 x 0,90. O `checar.py` falha se voltar guarda-roupa com menos de 60 cm na frente ou porta batendo em tanque, pia, vaso, bancada, box ou máquina.
- **Ainda no eixo: a planta 2D do PDF e das prévias** (`ebook/gerador/livro.py`, do Designer) desenha a parede de fora sobre o eixo. Com o móvel na face de verdade, ele aparece 7,5 cm afastado da linha da parede de fora na 2D. Conserto: desenhar a parede pela `P3.paredes_reais` (o mesmo do 3D).
- **C01, sala:** a mesa girada não entrou (a entrada da cozinha ficaria com 69 cm com alguém sentado). As cadeiras continuam com 46 e 51 cm.
- **E03, copa:** no desenho, as cadeiras do lado da divisa ficam com 46 cm (eram 38 até 23/11). A ideia do banco corrido resolve na página; mudar o 3D é decisão do Arquiteto.
- **Segunda conferência (24/11, noite, Arquiteto):** o desenho usava guarda-roupa de 0,60 de fundo (fundo de móvel planejado) e este levantamento, o de loja (0,46 e 0,47). Ficou o de loja nos dois lugares: é o que o comprador compra (fichas da MadeiraMadeira: 0,46 a 0,53) e fica perto dos 0,50 da Portaria MCID 725; os 60 cm livres na frente, que o `checar.py` cobra, dão a folga para um modelo mais fundo (com um de 0,53, as passagens caem 6 a 7 cm e continuam acima de 60). O mesmo para tanque e máquina (Portaria). Se o comprador escolher outro modelo, a ficha dele manda.
- **Rascunhos:** os dados oficiais da E03 e da F01 já têm as medidas dos rascunhos E03R e F01R (3,20 m livres; quartos de 2,62 e 2,71 m). Se a planta mudar de novo, esta conta se refaz.
- **Frases proibidas na página:** "cabe tudo", "casa fresca", "aprovada", "sem engenheiro". Toda ideia de construção termina com quem decide (engenheiro, eletricista).
