# Skills candidatas para design criativo (passo 1 da pesquisa)

> **Pesquisador, 23/11/2026.** Passo 1: achados com fonte. Quem conclui é o Opus (Designer e Maestro) e o Conselho. **Nada foi baixado, instalado nem executado**; só páginas públicas, nada pago, sem commit. Falta a ficha e o veto do Conselho para qualquer uma entrar (CONSELHO.md, seção 6).
> **Para que serve:** o dono quer um e-book e carrosséis que prendam o olhar, "nada comum". O Designer já tem `artifact-design`, `dataviz`, `impeccable` (só detectar), `make-pdf` e o `livro.py` (ECOSSISTEMA.md). Aqui está o que ainda não temos.
> **Lei da licença:** "licença lida" = abri o texto da licença ou a seção de licença da página do repositório. Onde só li o aviso do README, está escrito.

## As 3 melhores no topo

| # | Skill | Nota "sai do comum" | Por quê, em uma linha | Veto provável |
|---|---|---|---|---|
| 1 | **frontend-design** (Anthropic) | **4** | Obriga a fazer um plano de design (cores, tipos, layout) e **revisá-lo contra o que a IA faz por padrão antes de desenhar**; lista os "vícios" da IA (fundo creme com serifa e terracota, preto com verde ácido, cartões iguais, etiquetas em caixa alta) | Licença Apache 2.0 lida; sem script: só texto. Baixo risco |
| 2 | **pdf-design** (Georgi45) | **4** | Monta PDF **página por página**, sangrado, sem moldura branca e sem página meio vazia; mede cada página e gera uma imagem dela para o agente se revisar. Bate com o nosso HTML para PDF | MIT lida; só 5 estrelas, autor novo; roda scripts Node: ler antes |
| 3 | **canvas-design** (Anthropic) | **4** (para capa e arte de anúncio; 2 para página de texto) | Escreve uma "filosofia visual" e só depois pinta uma peça de **90% imagem e 10% texto**, PDF ou PNG; é o oposto do modelo pronto | Apache 2.0 lida; manda baixar fontes (rede): usar só as fontes que já temos |

**Minha leitura (hipótese, quem decide é o Designer):** 1 e 3 se leem e se aplicam como método, sem instalar nada pesado; 2 vale por copiar a ideia do "medir cada página e olhar a imagem" no `livro.py`.

## Mapa rápido (as 12 lidas)

| Skill | Autor | Licença | Serve para | Nota |
|---|---|---|---|---|
| frontend-design | Anthropic | Apache 2.0 | plano de design e anti-genérico | 4 |
| pdf-design | Georgi45 | MIT (fontes SIL OFL) | e-book/PDF página a página | 4 |
| canvas-design | Anthropic | Apache 2.0 | capa e arte de anúncio | 4 |
| taste-skill | Leonxlnx | MIT | direção de arte com referência e checagem | 3 |
| ui-ux-pro-max | nextlevelbuilder | MIT | paletas e pares de fontes pesquisáveis | 3 |
| diagram-design | cathrynlavery | MIT | infográfico HTML+SVG sem sombra | 3 |
| editorial-svg | vpgits | MIT | ilustração SVG "uma ideia em poucas marcas" | 3 |
| open-carrusel | Hainrixz | MIT | carrossel 1080 por 1350 em PNG | 3 |
| open-design | nexu-io | Apache 2.0 (+ licenças próprias por pasta) | vitrine de 277 skills: só para garimpar ideia | 3 |
| theme-factory | Anthropic | Apache 2.0 (aviso do cabeçalho; arquivo não aberto) | temas de cor e fonte | 2 |
| algorithmic-art | Anthropic | Apache 2.0 (aviso do cabeçalho; arquivo não aberto) | textura e fundo gerados por código | 2 |
| kasiopa-home-plans | Damien Moras | MIT | editor de planta 2D HTML | 2 |

---

## Fichas

### 1. frontend-design
- **Link:** https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md
- **Autor:** Anthropic (repositório `anthropics/skills`, 199,3 mil estrelas na página de 23/11/2026).
- **Licença lida:** `LICENSE.txt` da pasta: Apache 2.0, texto inteiro lido. Permite uso, cópia e obra derivada, com aviso de licença e de mudança se redistribuir.
- **O que faz (trecho lido):** "make deliberate, opinionated choices about palette, typography, and layout that are specific to this brief"; trabalha em duas passadas: 1) plano compacto de 4 a 6 cores com nome, tipos, layout com esboço em ASCII; 2) "review that plan against the brief before building" e refazer o que for o padrão de qualquer página parecida.
- **O que acrescenta ao projeto:** o que o `impeccable` só detecta depois, esta skill faz **antes**: a revisão do plano contra o genérico. Também traz regras de tipografia úteis para o e-book: linhas com menos de 80 caracteres, serifa com entrelinha um pouco maior, evitar destacar uma só palavra do título, evitar rótulo em caixa alta, só numerar o que for sequência. "Gaste a ousadia em um lugar só": um elemento memorável, o resto quieto.
- **Risco:** baixo (só texto). Falta de aderência: foi escrita para site; páginas de livro precisam de adaptação. O `impeccable` nasceu desta skill (README do impeccable: "started from Anthropic's frontend-design skill"), então parte da ideia já está no projeto. **Aviso de versão:** a página da Composio (05/05/2026) diz que a skill proíbe Inter, Roboto, Arial e Space Grotesk; **o SKILL.md que li hoje não tem essa lista**, só diz para não usar as fontes de sempre. A versão mudou; vale o texto lido.
- **Nota "sai do comum": 4.**

### 2. pdf-design
- **Link:** https://github.com/Georgi45/pdf-design
- **Autor:** Georgi (georgi5.com). Página mostra 5 estrelas.
- **Licença lida:** seção "License" do README: "MIT. The bundled fonts are under the SIL Open Font License". Não abri o arquivo LICENSE.
- **O que faz (trecho lido):** "Every page designed as a whole. Full-bleed backgrounds, covers, dividers and closing pages. A4, A4 landscape or 16:9"; texto em vetor com fonte embutida; seis temas (`poster`, `gallery`, `ledger`, `archive`, `product`, `stage`), cada um com margens, escala de letra, cantos e filetes próprios; um script de impressão mede cada página (conteúdo cortado, texto sobre o rodapé, página meio vazia, fonte faltando) e gera um PNG de cada folha. A página do Skills Directory dá nota de segurança A (100/100) em 24/09/2026: fonte secundária.
- **O que acrescenta:** é o mesmo caminho do nosso e-book (HTML para PDF), com **conferência automática por página**. Mesmo sem instalar, a ideia de "medir e olhar a imagem de cada página" cabe no `checar.py`/`livro.py`.
- **Risco:** autor novo e pouco usado; roda script Node (`print.mjs`) e provavelmente um navegador sem tela (**não confirmei qual**); pode brigar com o `livro.py`. Os temas prontos podem parecer "de modelo": usar o método, não o tema.
- **Nota "sai do comum": 4** (pela conferência de página e pelo sangrado total; os temas, 2).

### 3. canvas-design
- **Link:** https://github.com/anthropics/skills/blob/main/skills/canvas-design/SKILL.md
- **Autor:** Anthropic. **Licença lida:** `LICENSE.txt` da pasta, Apache 2.0, texto inteiro e apêndice ("Copyright 2026 Anthropic, PBC").
- **O que faz:** em dois passos, escreve um manifesto de movimento visual (4 a 6 parágrafos, nome de 1 a 2 palavras, como "Concrete Poetry") e depois pinta uma peça de "90% design visual, 10% texto", em PDF ou PNG, com opção de várias páginas "como um livro de mesa". Manda manter tudo dentro da margem, nada sobreposto.
- **O que acrescenta:** um jeito de chegar a uma **capa e peças de anúncio com identidade própria**, em vez de modelo; a regra "texto mínimo, imagem manda" combina com capa de e-book e com o primeiro quadro do carrossel.
- **Risco:** mandado para arte, não para texto de venda: não serve para página com planta e tabela. Manda "baixar as fontes que precisar" (rede e licença de fonte): só usar fonte com licença livre, ou as nossas. O trecho "citação sutil do tema" pode gerar peça abstrata demais para o comprador de classe C; o Redator e o Revisor conferem.
- **Nota "sai do comum": 4** para capa e anúncio.

### 4. taste-skill (design-taste-frontend)
- **Link:** https://github.com/Leonxlnx/taste-skill
- **Autor:** Leonxlnx (Leon Lin). 120,5 mil estrelas na página.
- **Licença lida:** arquivo `LICENSE` bruto: MIT, "Copyright (c) 2026 Leonxlnx".
- **O que faz:** "art direction, reference images and a browser check instead of generic AI pages"; página única por pedido, copy simples, "um sistema", "um momento marcante", com um verificador e uma "porta de saída" (`gate.mjs`) que não deixa terminar enquanto houver falha corrigível.
- **O que acrescenta:** o hábito de **partir de referência de verdade** e de conferir no navegador; a trava de fim.
- **Risco:** feita para site de empresa; exige Node 22+ e Chrome; usa fotos reais "de arquivos abertos" com crédito (rede); o README tem patrocinadores e um aviso sobre moedas de cripto que usam o nome do autor (ruído, sem relação). Seria camada pesada sobre o que já temos.
- **Nota "sai do comum": 3.**

### 5. ui-ux-pro-max
- **Link:** https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- **Autor:** nextlevelbuilder. **Licença lida:** README: "This project is licensed under the MIT License" (arquivo LICENSE não aberto).
- **O que faz:** gera um "sistema de design" (padrão de página, estilo, paleta, tipos, efeitos, o que evitar) a partir de uma busca em tabelas locais (script Python `search.py`). Os números (192 paletas, 74 pares de fontes, 80 estilos) vêm do blog de Bartosz Gaca de 29/06/2026 (**fonte secundária**; o README que li fala em fontes Google aprovadas e 8 exclusões por falta de licença confirmada).
- **O que acrescenta:** banco de paletas e **pares de fontes com licença conferida**; útil para o Designer escolher tipo que não seja o de sempre (hoje: Bricolage Grotesque e Inter).
- **Risco:** foco em tela e em pilhas de programação, quase nada de impresso; roda Python e baixa dados; muito material para pouco uso. O blog avisa que 36,82% de 3.984 skills públicas que a Snyk examinou tinham ao menos uma falha de segurança (fonte secundária): ler os scripts antes.
- **Nota "sai do comum": 3** (as tabelas dão repertório, mas tendem à média).

### 6. diagram-design
- **Link:** https://github.com/cathrynlavery/diagram-design
- **Autor:** Cathryn Lavery (LittleMight). 70,3 mil estrelas. **Licença lida:** página do repositório mostra "MIT license"; arquivo não aberto.
- **O que faz:** desenha diagramas como um arquivo HTML+SVG, "51 diagram types. No shadows. No Mermaid slop", e pode "pegar" paleta e fontes de um site.
- **O que acrescenta:** infográficos do e-book (fases da obra, o que o pedreiro faz primeiro, quadro de decisão) com acabamento editorial, sem sombra, que o `dataviz` e o `artifact-diagramming` não cobrem do mesmo jeito.
- **Risco:** o PRIVACY.md lista o que vai pela rede (**não li**); a função de "importar a marca de um site" busca páginas: usar só com o nosso site. Diagrama técnico de planta não é a função.
- **Nota "sai do comum": 3.**

### 7. editorial-svg
- **Link:** https://github.com/vpgits/claude-editorial-svg
- **Autor:** vpgits (não oficial; o README diz "not affiliated with Anthropic"). 0 estrelas.
- **Licença lida:** README: MIT, "see LICENSE" (arquivo não aberto).
- **O que faz:** ilustração SVG pequena e esparsa: "a tiny visual argument made from 3-8 vector marks"; pede primeiro achar o argumento ("o que são as menos marcas que deixam a ideia óbvia") e só depois desenha, com um conjunto fixo de formas (bolha, gesto, seta, nó, painel, mão, cursor, grupo). Saída em `.svg` gerado de um `.ts` que fica no repositório.
- **O que acrescenta:** o método "metáfora do mecanismo, não o desenho do substantivo" (exemplo da tabela do autor: trocar "robôs ao notebook" por "corrente de repasse que enfraquece"); serve para ilustrar a ideia de cada capítulo.
- **Risco:** o estilo imita a "casa" visual da Anthropic: **não usar o estilo**, só o método, ou o e-book fica parecido com blog de tecnologia. Projeto sem uso. A tecnologia pede TypeScript (não confirmei como roda).
- **Nota "sai do comum": 3** (método 4, estilo 2).

### 8. open-carrusel
- **Link:** https://github.com/Hainrixz/open-carrusel
- **Autor:** Hainrixz (tododeia). 528 estrelas. **Licença lida:** README: "MIT — do anything you want with it" e `LICENSE` na lista de arquivos.
- **O que faz:** aplicativo local em que se conversa com o Claude; ele cria slides HTML/CSS e tira capturas em PNG no tamanho exato do Instagram.
- **O que acrescenta:** fluxo de carrossel pronto: mas **o que a gente quer é o jeito de pensar o slide**, e isso o Designer já faz com HTML.
- **Risco:** é um aplicativo inteiro (Next.js), baixa cerca de 300 MB de Chromium na primeira vez (dito no README); pesado e duplica o que a nossa geração já faz. Só vale como leitura do `CLAUDE.md` e do prompt de sistema do repositório, para pegar ideias.
- **Nota "sai do comum": 3.**

### 9. open-design (nexu-io)
- **Link:** https://github.com/nexu-io/open-design e https://opendesigner.io/skills
- **Autor:** nexu-io. 109,1 mil estrelas. **Licença lida:** README: Apache 2.0, "Bundled skills and templates with their own LICENSE files retain those licenses" (por exemplo MIT para `guizang-ppt` e `html-ppt`).
- **O que faz:** "277 droppable SKILL.md bundles" com amostra viva (apresentações, protótipos, carrosséis sociais, "magazine spreads"); cada pasta tem um `SKILL.md` e um `example.html`.
- **O que acrescenta:** **vitrine para garimpar referência de carrossel e de página de revista**, sem instalar nada: abrir a lista de amostras e anotar o que chama atenção.
- **Risco:** espaço de trabalho pago com planos e créditos (o README anuncia preços); cada pasta tem licença própria (conferir uma a uma); há skill de "clonar site" (`web-clone`): **vetada de saída**, copiar página alheia fere direito autoral. Só olhar.
- **Nota "sai do comum": 3** (como fonte de referência, 4).

### 10. theme-factory
- **Link:** https://github.com/anthropics/skills/blob/main/skills/theme-factory/SKILL.md
- **Autor:** Anthropic. **Licença:** o cabeçalho diz "Complete terms in LICENSE.txt"; **abri só o `LICENSE.txt` de frontend-design e canvas-design (Apache 2.0)**, o desta pasta não abri.
- **O que faz:** 10 temas prontos de cor e fonte (Ocean Depths, Sunset Boulevard, Botanical Garden...) e cria um tema novo sob medida; escrita para apresentação.
- **O que acrescenta:** pouco. Já temos identidade (azul `#0B4FA8`, amarelo `#FFC857`).
- **Risco:** baixo. Temas prontos geram o comum.
- **Nota "sai do comum": 2.**

### 11. algorithmic-art
- **Link:** https://github.com/anthropics/skills/blob/main/skills/algorithmic-art/SKILL.md
- **Autor:** Anthropic. **Licença:** mesmo caso do theme-factory (cabeçalho; arquivo não aberto).
- **O que faz:** arte generativa com p5.js e semente fixa: o mesmo número de semente repete a mesma imagem; página HTML com controles.
- **O que acrescenta:** **textura de fundo única por capítulo** (linhas de campo, curvas de nível, hachuras) que lembre topografia de lote; semente fixa deixa refazer sem mudar.
- **Risco:** o modelo de página obriga a marca da Anthropic (cores, Poppins e Lora, fundo degradê) e a biblioteca p5.js vem de CDN (rede); só usar a ideia da semente e do fundo, não o modelo. Textura demais cansa o olho.
- **Nota "sai do comum": 2.**

### 12. kasiopa-home-plans
- **Link:** https://github.com/kasiopajg/kasiopa-home-plans
- **Autor:** Damien Moras (kasiopa.com). 5 estrelas. **Licença lida:** README: "MIT, see LICENSE" (arquivo não aberto).
- **O que faz:** transforma descrição, foto ou croqui de uma casa em planta 2D com rede elétrica, hidráulica, TI etc., entregue como um único arquivo HTML editável, com camadas e exportação para SVG, PNG e CSV; normas da França (NF C 15-100), Espanha (REBT), Reino Unido (BS 7671) ou IEC 60364.
- **O que acrescenta:** ideia de **camadas por especialidade na planta** (casa, elétrica, hidráulica) como brinde ou bônus; não é "planta humanizada" (sem mobília bonita, sem cor).
- **Risco:** as normas não são as brasileiras (NBR 5410 etc.); jamais usar saída dela como projeto: contraria a regra de não prometer aprovação nem dispensar profissional. Só para inspirar.
- **Nota "sai do comum": 2.**

---

## Lidas e **descartadas**

| Skill | Por quê |
|---|---|
| **brand-guidelines** (Anthropic) | Aplica as cores e as fontes **da Anthropic** (`#d97757`, Poppins, Lora). Não é nossa marca. Só serve de exemplo de como escrever um guia de marca. Nota 0 |
| **instagram-carousel** (AdityaDutta02, `carousel-skill`) | **Não achei licença** (o arquivo LICENSE deu 404 e a página não mostra). Usa o sistema "Wolf Media" e um bloco de marca de terceiros (`figr.design`); caminho fixo de Mac. Sem licença, não entra. Nota 1 |
| **carousel-generator-skill** (nopefallacy) | MIT lida, mas entrega comandos para colar no ChatGPT Image 2 (serviço de fora do nosso fluxo, OpenArt). Vale ler o método de "ganchos" e o "perigo do slide 3" só como ideia, que o Redator e o Diretor já cobrem. Nota 2 |
| **awesome-claude-design** (VoltAgent) | MIT; 68 arquivos `DESIGN.md` "inspirados em padrões públicos" de sites conhecidos, avisando que não são oficiais. Copiar a cara de marca alheia dá problema e não "sai do comum". Nota 1 |

## O que ainda precisa de decisão (nada disso eu fiz)

1. **Qual das 3 do topo o Designer quer testar primeiro?** Sugestão minha (hipótese): ler `frontend-design` como regra de método no `contexto/designer.md`, sem instalar; depois decidir sobre `pdf-design` com o Conselho.
2. **Instalar ou só ler?** Para as skills só de texto (frontend-design, canvas-design) o risco é baixo; para as que rodam script (pdf-design, ui-ux-pro-max, taste-skill, open-carrusel) é preciso ler os scripts antes (custo do Opus) e passar pelo Conselho.
3. **Quem confere a licença em arquivo:** li o texto só de `frontend-design` e `canvas-design`; as outras eu vi no README ou na página do repositório. O Revisor de risco deve abrir o `LICENSE` de cada uma que for entrar.

## O que não consegui confirmar

- A API do GitHub não estava liberada para esta sessão: **não tenho data do último commit nem contagem oficial de cada repositório**, só o que a página mostrou (estrelas na data de hoje).
- Não abri o `LICENSE` de pdf-design, ui-ux-pro-max, diagram-design, editorial-svg, kasiopa e open-carrusel (só a menção no README/página); nem as pastas de theme-factory, brand-guidelines e algorithmic-art.
- Não li os scripts de nenhuma (pdf-design, taste-skill, ui-ux-pro-max): **a segurança delas é desconhecida**, exceto a nota A da página do Skills Directory para pdf-design (fonte secundária).
- Não procurei skill de **vendas** nesta rodada (só design, como pedido).
- A frase "frontend-design proíbe Inter etc." é de blog (Composio, 05/05/2026) e **não confere** com o SKILL.md lido hoje.
- Estrelas e instalações são números das páginas na data da leitura; não são prova de qualidade nem de segurança.

## Fontes lidas (todas em 23/11/2026)

- https://github.com/anthropics/skills (README, página principal) e os SKILL.md brutos de frontend-design, canvas-design, theme-factory, brand-guidelines, algorithmic-art; LICENSE.txt de frontend-design e canvas-design.
- https://github.com/Leonxlnx/taste-skill e o LICENSE bruto.
- https://github.com/nextlevelbuilder/ui-ux-pro-max-skill; https://bartoszgaca.pl/en/news/claude-skills-ui-ux-design-complete-guide/ (29/06/2026, secundária).
- https://github.com/Georgi45/pdf-design; https://www.skillsdirectory.com/skills/georgi45-pdf-design (secundária).
- https://github.com/cathrynlavery/diagram-design; https://github.com/vpgits/claude-editorial-svg; https://github.com/kasiopajg/kasiopa-home-plans.
- https://github.com/Hainrixz/open-carrusel; https://github.com/nexu-io/open-design; https://opendesigner.io/skills.
- https://github.com/AdityaDutta02/carousel-skill; https://github.com/nopefallacy/carousel-generator-skill; https://github.com/VoltAgent/awesome-claude-design; https://github.com/pbakaus/impeccable (Apache 2.0, "started from Anthropic's frontend-design skill").
- https://composio.dev/content/top-design-skills (05/05/2026, secundária).

## Reconferência da ficha (tarefa recebida)

| Pedido | Cumprido? |
|---|---|
| Procurar skills de design criativo (SKILL.md, plugins, GitHub, skills oficiais da Anthropic) | Sim: 12 lidas, 4 descartadas |
| 8 a 12 candidatas com nome, link, autor, licença lida, o que faz, o que acrescenta, risco, nota | Sim; licença **lida por inteiro em 2**, só em README ou página nas outras (dito em cada ficha) |
| As 3 melhores no topo | Sim |
| Nada baixado, instalado ou executado; só páginas públicas; sem commit | Sim |
| Só número que uma página devolveu | Sim (estrelas e contagens com a fonte) |
| Terminar com "O que aprendi" | Sim, na resposta |
| Cobrir skills de vendas | Não: a tarefa era design; fica em aberto |
