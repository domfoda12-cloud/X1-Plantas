# Design dos concorrentes: 14 páginas e 1 PDF de amostra, vistos por dentro

> Pedido do dono, 23/11/2026: "VER o design dos e-books e catálogos de planta dos concorrentes, para depois fazermos um que deixe todos de boca aberta". Passo 1 da pesquisa em dois passos (`pedidos/LEIA-ME.md`): **só descrevo o que vi; quem decide o que fazer com isso é o Designer/Maestro**. Nada daqui é copiado para o nosso e-book; é só referência.
>
> **Como foi feito (23/11/2026):** Playwright (Chromium), largura 1280, escala 2, só o topo da página, até 3.000 px de altura (imagem de 2560 x 6000). Só páginas públicas, sem login, nada pago. As capturas estão em `ebook/plantas/rascunhos/concorrentes/` (pasta ignorada pelo git).
> Fonte das 12 primeiras páginas: [`ANUNCIOS.md`](ANUNCIOS.md) (linhas citadas em cada item). Cores e letras de cada página foram lidas do próprio código da página (valor real), não "no olho", salvo onde digo "no olho".

## O que NÃO consegui e por quê (leia antes)

- **Nenhum e-book de catálogo tem miolo público.** Procurei PDF de amostra grátis: achei só (a) uma planta de 1 página do DF Projetos (item 15) e (b) o e-book grátis "100 plantas para casas térreas e sobrados" da 123Projetei, **cuja entrega é por link nos stories**; as cópias soltas dele estão no Scribd e no pdfcoffee. O pdfcoffee bloqueou a leitura (`bot_blocked`; não contornei) e o Scribd é cópia sem o autor, então **não baixei**. Por isso **não vi nenhum miolo de e-book de plantas**: o que existe aqui é loja, página de venda e a planta em PDF.
- **Monte Sua Casa dá 2 projetos completos por R$ 0,00**, mas só "concluindo o pedido pelo site" (carrinho; provavelmente pede cadastro). Não fiz, por causa do "sem login". Seria a melhor amostra de miolo para você ver; **depende do dono autorizar** (ou fazer ele mesmo pelo link: `https://montesuacasa.com.br/categoria-produto/projetos-gratis/`).
- **Hotmart mostrou "$14.00" e "$9.00"** nas capturas 11, 12 e 13. É o preço convertido para dólar porque o navegador da nuvem não está no Brasil; **não é o preço em reais** e eu não o uso. (O `ANUNCIOS.md` diz R$ 69 para o item 12, tirado do texto da página; não conferi de novo.)
- As capturas pegam **cookies, faixas de anúncio e o botão do WhatsApp por cima** em algumas páginas (03, 04, 07, 11, 12, 13, 14). Quando cobre algo importante, eu digo.
- A captura vai só até 3.000 px: o rodapé e o resto das páginas longas (02, 04, 05, 08) **não foram vistos**.
- Só abri a **página inicial** ou **uma página de casa** de cada loja; não vi o carrinho, o e-mail pós-compra nem o que o comprador recebe depois de pagar (**não conferi**).

## As 15 peças, uma por uma

Nota "dá vontade de comprar" = minha leitura de design, de 0 a 5 (hipótese de quem olha, não dado de venda).

### 01. Só Projetos, página inicial · nota 4
- **Link:** <https://soprojetos.com.br> · **Captura:** `ebook/plantas/rascunhos/concorrentes/01-soprojetos-home.png` · ANUNCIOS linha 1
- **O que mostra:** faixa de Black Friday; título "Plantas de casas para construir, adaptadas ao seu terreno"; **caixa branca "Qual planta combina com o seu terreno?"** com botões de lote (5x25, 6x25, 7x20 … 12x30), quartos (2, 3, 4), térrea ou sobrado, e botão laranja "Ver as 153 plantas"; 3 renders de fachada grandes ("Em destaque agora": código, quartos, m², terreno); faixa "36 anos, 5.143 projetos, Registro no CAU, Aprovado na sua prefeitura ou devolvemos 100%"; grade de cartões "DESTAQUE" com render 3D.
- **Cores:** verde-floresta escuro de fundo (`#1B3B2F` nos títulos, verde `#0B5E35`/`#1F5130`), laranja nos botões e no destaque, fundo branco e verde-claro `#F0F7F2` nas faixas. **Letras:** sem serifa (declarada: Lucida Grande; no meu computador caiu numa sans do sistema); legenda dos cartões em serifa (parece Georgia). Título 34 px, branco.
- **Bonito:** a primeira tela **já pergunta o tamanho do lote**, com botões grandes e fáceis de apertar; renders bem iluminados, ao entardecer, com gente na varanda (dão vida); hierarquia clara (um título, uma caixa, um botão laranja). É a página mais bem acabada das 14.
- **Fraco:** a Black Friday em cima e o selo de "Aprovado ou devolvemos" brigam pela atenção; as marcas d'água "soprojetos" dentro dos renders; depois da caixa de lote vira grade igual à de qualquer loja; **as plantas (os desenhos) nem aparecem na primeira tela**: vende a fachada.
- **Para nós:** ele já faz "comece pelo lote". A diferença nossa não pode ser só o filtro; tem de ser o **porquê** (a página dele não explica recuo nem por que aquele lote).

### 02. Só Projetos, página da casa Cód. 65 · nota 3
- **Link:** <https://soprojetos.com.br/projetos-de-casas/Popular-Tipo-2-4-Quartos-Cod-65> · **Captura:** `…/02-soprojetos-cod65.png` · ANUNCIOS linha 2
- **O que mostra:** 1 render grande (anoitecer) + planta humanizada pequena + 2ª foto ("5 imagens"); barra de dados com ícones (terreno mínimo 11 x 20 m, 61 m², 4 quartos, 1 banheiro, sem garagem); **caixa de compra** com botão verde "Ver preço agora" (o preço **só aparece depois do clique**), garantia, WhatsApp; seção "O que você recebe" em lista de texto; **tabela comparando Projeto-Modelo x Projeto Adaptado** (7 linhas: o que é, quem adapta, RRT, garantia, o que chega, prazo, para quem é bom) e 2 perguntas "Responda e veja qual combina com você".
- **Cores/letras:** verde `#1F5130` nos títulos, botão verde `#40C36B`/verde-escuro, texto cinza `#333`; sans de 14 px. Barra de menu em degradê verde-água.
- **Bonito:** a **tabela comparativa** e as 2 perguntas ajudam a decidir; barra de dados limpa; a caixa de compra gruda ao lado da imagem.
- **Fraco:** **a planta é minúscula** (um recorte pequeno ao lado do render); o render é antigo, de baixa resolução, com cara de SketchUp (o contraste com a home é grande); **um anúncio de terceiros (doaudio) ocupa o topo da página**; o miolo é uma coluna de texto cinza; ícones de lista sem cor; preço escondido.
- **Para nós:** tem lote mínimo de verdade (11 x 20 m), só que num ícone de 10 px.

### 03. Planta Pronta, página inicial · nota 2
- **Link:** <https://www.plantapronta.com.br/> · **Captura:** `…/03-plantapronta-home.png` · ANUNCIOS linha 3
- **O que mostra:** logo laranja/cinza, selos PagSeguro e "Protegido"; menu em barra preta; **foto de um casal sentado no chão com móveis desenhados à mão** (rabiscos) e a lista "Suporte técnico gratuito, Garantia de aprovação, Entrega imediata…"; filtro por pavimento, lote (5x20 … 20x40), dormitórios, suítes e área; grade de cartões "by Arquelux" com render + ícones (lote, quartos, banheiros, vagas).
- **Cores/letras:** fundo cinza `#EEEEEE`, faixa preta, laranja `#FF9300`, texto cinza `#666`; Arial 13 px (Open Sans nos títulos).
- **Bonito:** a foto do casal com desenho à mão é simpática e humana (a única home com pessoas de verdade no topo); filtro de lote completo.
- **Fraco:** parece site de 2012: moldura cinza, abas pretas, selos de pagamento grandes, **aviso de cookies e balão do WhatsApp cobrindo os cartões**; texto cinza claro sobre cinza; os cartões são casas de alto padrão (15x35), **não o lote de quem constrói por etapas**.

### 04. Planta Pronta, casa 161A · nota 3
- **Link:** <https://plantapronta.com.br/projeto/161A/planta-de-casa-moderna-com-4-quartos> · **Captura:** `…/04-plantapronta-161A.png` · ANUNCIOS linha 4
- **O que mostra:** render grande de fachada + faixa de miniaturas; "Vantagens" com 6 itens e tique verde; **planta humanizada grande, colorida, com cotas em vermelho e o lote 12 x 30 m inteiro** (casa, garagem, jardim, recuos), botão "Inverter Planta" (espelhar); **3 caixas de preço lado a lado**: Personalizado R$ 2.290 (20 dias), Pronto **R$ 1.145 (desc. 50%)**, e o pacote "Estratégia: Construa Barato + Projeto 161A" **R$ 449** com selo "MAIS VENDIDO"; bloco "Quem fez esse projeto".
- **Cores/letras:** laranja `#FF9300` nos botões e no menu, verde-maçã nos botões "Contratar", azul nos preços; títulos em Open Sans (cinza `#666`), fundo cinza e preto.
- **Bonito:** **a planta humanizada grande, mostrando o lote inteiro com a casa dentro, é a melhor imagem de planta das 14** (mostra jardim, garagem, medidas do terreno); "Inverter Planta" é útil e raro; **3 preços lado a lado com um destacado como "mais vendido"** é uma boa prática de venda.
- **Fraco:** o resto é a mesma moldura antiga; banner "Veja ideias de como construir mais barato" com foto de homem de terno no meio da página de venda; **"desc. 50%" sem mostrar o preço cheio** (o R$ 2.290 é outro produto, o personalizado).
- **Achado novo para preço:** R$ 1.145 (pronto) e R$ 2.290 (personalizado) em uma loja que, no `ANUNCIOS.md`, não mostrava preço na home. Registrado no caderno.

### 05. Projeto Pronto, página inicial · nota 2
- **Link:** <https://projetopronto.com> · **Captura:** `…/05-projetopronto-home.png` · ANUNCIOS linha 5
- **O que mostra:** carrossel de foto/render **enorme** de casa moderna (tela cheia), título "PROJETO PRONTO — PORTFÓLIO DE PROJETOS PRONTOS PARA CONSTRUIR", grade de 3 colunas com render + nome + **"ARQUITETÔNICO: R$ 500,00 / em 10x de R$ 50,00 sem juros"** + botão "saiba mais" (preços R$ 500 a R$ 720 nas casas que vi).
- **Cores/letras:** branco, preto `#232323`, nenhum acento de cor (verde só no parcelamento); **Jost** (geométrica, limpa), caixa-alta nos títulos.
- **Bonito:** o carrossel de foto grande é impactante; a página é limpa e leve; preço em destaque, sem esconder.
- **Fraco:** o cartão tem **título sobreposto ao rótulo "ARQUITETÔNICO:"** (texto em cima de texto, vi em vários cartões); botões cinza quase invisíveis (`#7A7A7A` em `#FAFAFA`); marca d'água grande do logotipo em cima dos renders; nenhuma planta aparece na página; "pronto para construir" no título.

### 06. Archshop, lista de plantas · nota 3
- **Link:** <https://archshop.com.br/plantas-de-casas> · **Captura:** `…/06-archshop-plantas.png` · ANUNCIOS linha 6
- **O que mostra:** faixa de Black Friday preta com balões e "40% de desconto"; **painel de filtros** (térrea/sobrado, quartos, suítes, área, tipo do terreno plano/aclive/declive, **frente de 5 m … 30 m**, "Principais terrenos" 5x25, 10x20, 12x30…); cartões com render, selo "40% OFF", **ficha (terreno, m² do projeto, quartos, banheiros)**, curtidas, **preço do projeto** (R$ 594, R$ 714, R$ 894 … R$ 2.160), botão do WhatsApp em cada cartão.
- **Cores/letras:** branco, cinza-ardósia, laranja em degradê nos botões ("Mais recentes", "Black Friday"), vermelho em "Limpar filtros"; **Roboto Flex**; cantos bem arredondados.
- **Bonito:** é a **mais moderna e organizada** das lojas; o filtro por **tipo de terreno (plano/aclive/declive)** é raro e útil; tem **preço e curtidas** no cartão; cantos suaves; **nomes de casa em vez de código** (Cairo, Nebraska, Idaho).
- **Fraco:** a faixa Black Friday preta e dourada fica enorme e **destoa** do resto (parece outra marca); a primeira tela é só filtro, sem ver uma casa; os renders parecem todos "da mesma máquina" (cinza, vidro, carro); **"40% OFF" em todos os cartões** vira ruído.

### 07. Aquiprojetos, casa H03B · nota 1
- **Link:** <https://aquiprojetos.com/planta-pronta-de-casa-terrea-h03b-0925.html> · **Captura:** `…/07-aquiprojetos-H03B.png` · ANUNCIOS linha 7
- **O que mostra:** render com **marca d'água grande "aquiprojetos.com" escrita em cima**; ficha em quadro de linhas (frente 9, fundos 25, quartos, suítes, banheiros, vagas); preço R$ 107,80 riscado e **R$ 98,00**; **5 "pacotes"** (Pacote 1: planta baixa em PDF R$ 98; Pacote 2 R$ 198; Pacote 3 **R$ 1.290**; Pacote 4 **R$ 1.990**) descritos em **parágrafo corrido, com checkboxes**; coluna "Projetos similares" com preços "78,00*".
- **Cores/letras:** bordô `#831D1C`, botão de compra verde, fundo cinza-escuro `#343333` nas laterais; Open Sans 13 px.
- **Bonito:** a **tabela de quem faz cada etapa** (licenciamento e obra com técnico local) é honesta; nada mais.
- **Fraco:** **a página mais poluída**: aviso de cookies sobre a imagem, janela "Gerado pelo Gemini" em cima da lista, caixa de aceite no topo, ícones sociais soltos, "Descobrir mais" com links de palavra-chave que não ajudam; pacotes são um **muro de texto em itálico** com ✓ e termos como "Anteprojeto [MODELO]", "Alocação de Sapatas", "Cintamento de Base"; preço riscado com asterisco.

### 08. Arquiteto Bruno Machado, Casa de Campo P06 (Hotmart) · nota 3
- **Link:** <https://arquitetobrunomachado.com.br/casa-de-campo-p06-220m%C2%B2> · **Captura:** `…/08-brunomachado-P06.png` · ANUNCIOS linha 9
- **O que mostra:** logo manuscrito branco em faixa escura; foto/render em carrossel; título em preto pesado; lista de cômodos; **"10x R$ 67,00 ou R$ 670,00 à vista"** + botão laranja **COMPRAR**; **vídeo do YouTube** com o render; **planta baixa grande, mobiliada, com cotas, dentro do terreno**; faixa preta **"Exemplo de arquivos enviados"** com **6 pranchas reais em miniatura** (layout com perspectivas, planta executiva, elétrica, cobertura, cortes e fachada, fundação e hidráulica); "Como funciona?".
- **Cores/letras:** faixa grafite `#2A2A25`, laranja forte no botão, bege-taupe nos títulos ("Como funciona?"), preto pesado; **Montserrat** em negrito nos títulos; logo em letra manuscrita.
- **Bonito:** **é a única das 14 que mostra as pranchas de verdade que o comprador recebe**, em miniatura, antes de pagar. A planta é grande e legível. O render de fim de tarde (telhado, pedra, madeira) é o mais "arquitetura de revista" das lojas.
- **Fraco:** a lista de cômodos e o preço ficam numa coluna com **muito branco vazio embaixo** (a imagem é pequena); a planta é um recorte de software com cor chapada; miniaturas pequenas demais para ler.
- **Para nós:** o formato "exemplo de arquivos enviados" é o único modo de ver o produto por dentro; ninguém faz isso com **capa e miolo de livro**.

### 09. Monte Sua Casa, casa térrea 111,02 m² · nota 3
- **Link:** <https://montesuacasa.com.br/produto/111-02m2-casa-terrea-moderna-com-5-quartos-e-garagem-dupla> · **Captura:** `…/09-montesuacasa-111m2.png` · ANUNCIOS linha 10
- **O que mostra:** **tema todo preto com dourado**; galeria (1 render noturno grande + **15 miniaturas**: noites, vista aérea, interiores, **planta, implantação**); **R$ 555,00**; "Projeto pronto • Entrega em até 24h • Compra segura"; botão dourado "COMPRAR PROJETO PRONTO" e **botão verde "ESTE PROJETO SERVE NO MEU TERRENO?"** (WhatsApp); **grade de 12 caixinhas de dados** (área, dormitórios, suítes, banheiros, pavimentos, tipo, estilo de fachada, tipo de terreno, **largura e comprimento do terreno 15,10 x 23,30**, piscina, garagem); caixa "Quer ajuda para encontrar o projeto certo?"; seções de texto "Implantação e adaptações", "Quanto custa construir?", "Compare outras opções".
- **Cores/letras:** fundo preto `#000`, cartões `#111`, **dourado `#D29E55`**, verde WhatsApp `#25D366`; títulos Montserrat 20–25 px em branco, texto Inter/Montserrat cinza-claro `#D5D5D5`.
- **Bonito:** **único com identidade própria forte** (luxo discreto); os renders **noturnos acesos** ficam lindos no fundo preto; a **grade de dados em caixinhas** é a melhor ficha técnica das 14; a pergunta "este projeto serve no meu terreno?" é o gancho certo.
- **Fraco:** a **galeria quebrou na captura** (faixas cinzas, "tela" vazia embaixo); texto longo cinza sobre preto cansa a leitura; a sensação é de casa de **alto padrão (piscina, 5 quartos)**, não de quem constrói com pedreiro por etapas; o texto é de SEO (parágrafos repetidos).

### 10. Cabana Lar, página inicial · nota 3
- **Link:** <https://cabanalarbaixocusto.com.br> · **Captura:** `…/10-cabanalar-home.png` · ANUNCIOS linha 12
- **O que mostra:** título enorme "Moradias compactas, acessíveis e conscientes."; selos em pílulas ("Construção consciente", "Espaços bem aproveitados"); **imagem de casinha 4 x 4 ao pôr do sol** com legenda; faixa verde com 3 promessas; seção "Nossa essência" com arco; mais abaixo **3 cartões de projeto** (4x4 com mezanino, 4x5, taipa de mão) com **"ESTIMATIVA DE MATERIAIS R$ 10.000 a R$ 15.000 … Mão de obra não inclusa"** e botão; faixa "Preços claros / Sem promessas impossíveis / Construção responsável".
- **Cores/letras:** verde-musgo `#1F3D2C`/`#315B43`, **terracota/marrom** nos rótulos, **creme** `#FAF9F4` de fundo; **Georgia em negrito, 64 px** nos títulos, Arial no texto.
- **Bonito:** **a mais coerente e "de marca" das 14** depois da Monte Sua Casa: paleta terrosa, serifa grande, muito ar, tom humano; os avisos honestos ("Sem promessas impossíveis", "Mão de obra não inclusa") entram no próprio layout, não no rodapé.
- **Fraco:** as casas são **imagens de inspiração geradas (têm legenda "Representação ilustrativa")**, de outro público (20 m²); um cartão mostra uma **imagem com texto minúsculo ilegível dentro**; botões iguais; página longa e parada.
- **Para nós:** prova que dá para mostrar aviso honesto com cara bonita.

### 11. Hotmart, "500 plantas baixas de casas" · nota 1
- **Link:** <https://hotmart.com/pt-br/marketplace/produtos/500-plantas-baixas-de-casas-para-voce-se-inspirar-na-sua-construcao-bonus/B87641576R> · **Captura:** `…/11-hotmart-500plantas.png` · ANUNCIOS linha 13
- **O que mostra:** cabeçalho Hotmart; título; **uma miniatura 3D isométrica de 175 px** (planta cortada, móveis, madeira); 3 linhas de texto; abas "Vantagens/Detalhes"; foto vazia do autor; "Outros produtos" com **caixa-cinza de imagem faltando**. Botão verde "Ir para o carrinho"; "Garantia de 7 dias".
- **Cores/letras:** padrão Hotmart: branco, laranja `#EF4E23`, botão verde `#009D43`; **Nunito Sans**.
- **Bonito:** a miniatura isométrica é a única imagem "de produto" de planta que dá vontade de olhar de perto (corte 3D, móveis vistos de cima).
- **Fraco:** **a página não mostra o produto**: nenhuma planta, nenhuma página do e-book, só uma miniatura e três linhas; o aviso de cookies cobre o texto; "foto do autor" vazia.

### 12. Hotmart, "Minha Casa do Zero" · nota 2
- **Link:** <https://hotmart.com/pt-br/marketplace/produtos/minhacasadozero/S80999854U> · **Captura:** `…/12-hotmart-minhacasadozero.png` · ANUNCIOS linha 18
- **O que mostra:** capa de curso (homem de capacete e boné, madeira de telhado, título em letra condensada branca), texto "Já imaginou construir sua própria casa, mesmo sem ser pedreiro ou engenheiro?", **vídeo de aula com legenda "Colunas e vigas convencionais"**, "Vantagens".
- **Cores/letras:** Nunito Sans; capa em laranja-pôr-do-sol, marrom e branco.
- **Bonito:** a **capa tem pessoa e rosto** (única das 14 com isso na capa); o vídeo mostra obra real (andaime, pilar).
- **Fraco:** frase central cai na linha vermelha (dispensa profissional, ANUNCIOS linha 18); capa genérica de "curso"; vídeo com qualidade de celular e marca d'água do site.

### 13. Hotmart, "Projetos de Casas Populares" · nota 1
- **Link:** <https://hotmart.com/pt-br/marketplace/produtos/projetos-de-casas-populares/D12111407D> · **Captura:** `…/13-hotmart-casaspopulares.png` · ANUNCIOS linha 16
- **O que mostra:** **logo circular** (anel cinza e amarelo, silhueta de casa) como capa; texto sobre PDF e DWG; **vídeo escuro de fachada 3D com carro popular** (sem planta); "10 projetos pelo preço de um"; bônus (memorial, planilha de orçamento, contrato).
- **Cores/letras:** Hotmart padrão; logo preto/amarelo/cinza.
- **Bonito:** o bônus de **contrato de empreitada e memorial descritivo** é uma ideia útil.
- **Fraco:** capa = logotipo (nada do produto); render escuro com lente e marca d'água; zero planta à vista.

### 14. Plantas de Casas (plantasdecasas.com), Cód. 100 · nota 2,5
- **Link:** <https://plantasdecasas.com/projetos/casa-terrea-2-quartos-1-suite> · **Captura:** `…/14-plantasdecasas-cod100.png` · ANUNCIOS linha 11
- **O que mostra:** logo com 3 casinhas; faixa laranja de menu; render grande + 2 miniaturas; **R$ 730,00** com selos de cartão/bancos; **opcionais com preço** (hidro-sanitário R$ 340, elétrico R$ 340; lista de materiais e estrutural "sob consulta"); botão verde "Comprar Projeto"; **ícones de dados** (10x20 m, térrea, 94,77 m², 3, 2, 1); texto da casa; **"Planta Humanizada"** grande e colorida com **áreas por cômodo (A: 9,55 m²)**; e, mais abaixo, **o desenho "Medidas mínimas do terreno: 10 x 20 m" com a casa dentro do lote e as cotas** (5,00 m de frente, 1,60 m dos lados, 1,90 m de fundo).
- **Cores/letras:** laranja `#EE8A0F` (no olho), verde `#4CAE4C` no botão, fundo `#F5F5F5`; **Lato** nos títulos, **Roboto** no texto; ícones pretos.
- **Bonito:** **a única que mostra o encaixe da casa no lote com cotas** (planta de implantação colorida com "FRENTE" em seta); **área de cada cômodo escrita dentro da planta**; os opcionais com preço separado deixam claro o que se paga.
- **Fraco:** aparência de 2010 (laranja chapado, ícones pretos, selos de banco); aviso de anúncio sobre a página; o desenho do lote vem **no fim da página**, e nada explica por que 1,60 m ou 5,00 m; "Descobrir mais" (anúncio) no meio.
- **Corrige o `ANUNCIOS.md`** ("ninguém mostra por que cabe"): aqui **há** um desenho de lote com recuos. O que ninguém faz é explicar a regra (ver abaixo). Registrado no caderno.

### 15. DF Projetos, amostra em PDF (1 página) · nota 1
- **Link:** <https://dfprojetos.arq.br/planta-de-casa-terrea-compacta-com-layout-funcional-e-integracao-de-ambientes> (o botão leva a um PDF no Google Drive, público, sem login) · **Captura:** `ebook/plantas/rascunhos/concorrentes/15-dfprojetos-amostra-pdf-p1.png`; o PDF original está em `ebook/plantas/rascunhos/concorrentes-pdf/df.pdf` (193 KB, 1 página, A4, gerado em 15/01/2026 por "Microsoft Print to PDF" de um arquivo de CAD)
- **O que mostra:** **uma planta térrea em preto e branco de CAD**, escala 1:75, cotas em vermelho, nomes dos cômodos em negrito, área de cada um (A = 9,78 m²), lote 10,00 x 18,08 m com a casa e o recuo, moldura de folha e número "1 / Pav. Terreo".
- **Cores/letras:** branco, preto, vermelho nas cotas; fonte padrão de CAD (sem serifa, quase técnica).
- **Bonito:** é **honesta e legível para pedreiro**: tudo cotado, lote e recuos desenhados.
- **Fraco:** **nenhum design**: sem título, sem legenda, sem cor, sem como ler; nome do arquivo cheio de caminho de computador ("C:\Users\…") nos metadados; sem aviso legal.
- **Para nós:** serve de **espelho do pior caso** que o comprador já viu quando baixou "uma planta de graça" por aí.

## Resumo em uma tabela

| # | Quem | Mostra capa de livro? | Mostra a planta? | Mostra 3D/foto? | Mostra o lote com a casa? | Aviso honesto à vista? | Nota |
|---|---|---|---|---|---|---|---|
| 01 | Só Projetos (home) | não | não (só fachada) | render de fachada | filtro por lote | não (tem selo de aprovação) | 4 |
| 02 | Só Projetos (Cód. 65) | não | pequena | render + foto | só ícone "terreno mín." | em parte (tabela Modelo x Adaptado) | 3 |
| 03 | Planta Pronta (home) | não | não | render | filtro por lote | não | 2 |
| 04 | Planta Pronta (161A) | não | **grande, colorida, com lote** | render + miniaturas | **sim (12x30)** | não | 3 |
| 05 | Projeto Pronto | não | não | render/foto grande | não | não | 2 |
| 06 | Archshop | não | não (na lista) | render | filtro por lote | não | 3 |
| 07 | Aquiprojetos | não | só descrita em texto | render com marca d'água | não | tabela de quem faz a obra | 1 |
| 08 | Bruno Machado | **só as pranchas (miniatura)** | grande, mobiliada | render + vídeo | dentro do terreno | **sim (no texto)** | 3 |
| 09 | Monte Sua Casa | não | só em miniatura | render noturno + interiores | **ficha 15,1 x 23,3** | no texto | 3 |
| 10 | Cabana Lar | não | não | imagem gerada | não | **sim (no layout)** | 3 |
| 11 | Hotmart 500 plantas | miniatura 3D | não | miniatura 3D | não | não | 1 |
| 12 | Hotmart Minha Casa do Zero | capa de curso | não | vídeo de obra | não | não (diz o contrário) | 2 |
| 13 | Hotmart Casas Populares | logo | não | vídeo escuro | não | não | 1 |
| 14 | Plantas de Casas | não | grande, com áreas | render | **sim, com cotas** | não | 2,5 |
| 15 | DF Projetos (PDF) | não | sim (CAD) | não | **sim** | não | 1 |

## Os 5 pontos em que todos são iguais (onde dá para ser diferente)

1. **A imagem principal é um render de fachada de céu azul**, grama verde, carro na garagem e palmeira, igual de uma loja para outra (01, 03, 05, 06, 07, 09, 14; só 08 e 09 saem do azul-diurno com cena de fim de tarde). Dá para ser diferente com **uma imagem que explica** (a casa dentro do lote, em desenho, ou a casa em construção) em vez de mais um render de revista.
2. **A planta aparece como "desenho colorido de móveis vistos de cima"**, mostrado sozinho, sem dizer **como ler**: nenhuma legenda de cor, nenhuma seta de por onde se entra, nenhum "comece pela sala". Dá para ser diferente guiando o olho do comprador por dentro da planta (e em linguagem de pedreiro).
3. **A decisão é uma grade de cartões iguais**: render + ícones de lote, m², quartos, banheiros, vagas (01, 03, 05, 06, 07, 14). O comprador compara sozinho, 150 vezes. Dá para ser diferente **escolhendo por ele**: a casa que cabe no lote dele, uma por vez, com o motivo.
4. **A confiança vem de selo genérico**, não de prova: PagSeguro e "Compra segura" (03, 07, 14), "36 anos / 5.143 projetos" (01), "Aprovado ou devolvemos" (01, 02, 03), faixa de **Black Friday** (01, 06), WhatsApp flutuante em todas, aviso de cookies por cima. Dá para ser diferente com prova visível (a lista de conferências que a planta passou, o número de cada cômodo calculado), no lugar do selo.
5. **A página é de "loja", não de produto**: título, preço e botão no canto; "O que você recebe" em **lista de texto** (02, 07, 11, 12, 13). **Só a 08 mostra as folhas reais**, e nenhuma mostra o produto como **um livro com capa e páginas abertas**. Dá para ser diferente com a capa e o miolo à vista, antes do pagamento.

## As 3 coisas que nenhum faz (dentre as 15 que vi)

> "Nenhum faz" = **não vi em 15 peças**, sem Biblioteca da Meta nem miolos de e-book; é hipótese, não fato de mercado.

1. **Um livro de verdade à vista**: capa, folha de rosto e 2 páginas do miolo abertas em mockup. Os e-books do Hotmart (11, 12, 13) usam miniatura, capa de curso ou logo; as lojas mostram o site, não o produto.
2. **A casa desenhada no lote do comprador, com cada recuo explicado em uma frase**: a 14 e a 15 desenham um lote fixo com cotas; a 04 mostra o 12 x 30; a 01 e a 06 perguntam o lote. **Nenhuma desenha o lote que o comprador digitou e diz "aqui sobra X m para a rua, por causa do recuo"**, nem diz o porquê.
3. **A obra em etapas, em desenho**: nenhuma peça mostra "o que você faz primeiro este ano" (fundação, paredes, cobertura) ou "o que levar ao seu pedreiro e ao seu engenheiro" como imagem. A 12 vende vídeo de obra; as lojas vendem a casa pronta. (Lembrete: "ampliar depois" só vale se houver ampliação desenhada; `ESTRATEGIA.md`, seção 9.)

Fora das três, mas também ninguém tem: **uma identidade visual própria e reconhecível em todas as telas**: as 14 usam tema pronto ou o painel do Hotmart; só 09 (preto e dourado) e 10 (verde-musgo, terracota e creme, serifa grande) têm uma cara.

## O que cada papel pode tirar daqui (sem decidir por ele)

- **Designer:** o espaço em branco é o ponto fraco geral: todos são densos ou vazios sem critério. Nenhuma peça mostra **hierarquia de leitura de livro** (capa → sumário → casa → planta).
- **Estrategista:** o preço por casa aparece nas lojas (R$ 98 a R$ 2.290; ver 04, 05, 06, 07, 14); o do e-book não. **Não é âncora oficial**: preço de concorrente só vale com fonte e data (`MERCADO.md`, seção 4).
- **Revisor de risco:** "Garantia de aprovação" em 01, 03 e "Aprovado" seguem na home (linha vermelha). "Estimativa de custo" aparece no 10 com aviso; é para ele decidir se é aceitável.

## Reconferência dos pedidos (ficha)

1. **Escolher 8 a 12 concorrentes que mostram o produto por dentro, só público e sem login:** escolhi 14 páginas de 13 concorrentes diferentes (Só Projetos e Planta Pronta entram 2 vezes; Hotmart são 3 vendedores), mais 1 PDF de amostra; passei do teto de 12 de propósito, para cobrir Hotmart e a amostra em PDF. Hotmart: não achei página interna do produto no Hotmart (mostra só a vitrine). **Cumpri, com a ressalva do miolo.**
2. **Capturas com Playwright (2x, 1280, até 3000 px) em `ebook/plantas/rascunhos/concorrentes/NN-nome.png`:** cumpri (14 capturas + a imagem do PDF). **PDF para pasta nova e vazia e as 2 primeiras páginas:** o PDF do DF Projetos tem **1 página**, então só uma imagem; pasta `concorrentes-pdf/`. **Não cumpri** para e-book com miolo (não havia público).
3. **Escrever o `DESIGN-CONCORRENTES.md` com link, o que mostra, cores e letras, bonito, fraco, nota; no fim, 5 iguais e 3 que ninguém faz:** cumpri.
4. **Não copiar nada para o nosso e-book; caderno com `pesquisa.py nova`:** não copiei imagem alguma para fora de `rascunhos/`; 4 achados no caderno (concorrentes). Sem commit.
- **Em aberto:** (a) o dono autoriza ou faz o pedido do projeto grátis da Monte Sua Casa para vermos um miolo completo; (b) a captura não cobre o rodapé nem o que chega depois da compra; (c) Hotmart em dólar na captura.
