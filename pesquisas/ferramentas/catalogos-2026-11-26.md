# Catálogos de terceiros: o que vale olhar (26/11/2026)

Passo 1 da pesquisa (Pesquisador, Sonnet). Falta a conferência do Opus. **Nada foi instalado, conectado ou rodado.** Só se leu: README bruto das três listas e a documentação oficial dos itens abaixo. Data das leituras: 26/11/2026.

Legenda de certeza: **C** = confirmado no texto oficial lido; **S** = só a linha da lista (ou README do próprio projeto), não conferi na fonte; **H** = hipótese minha. A = e-book de plantas; B = Instagram de IA ("matemática do mundo real").

As três listas são, elas mesmas, só catálogos: licença MIT para `public-apis` e `awesome-mcp-servers` (C, arquivos LICENSE lidos em raw.githubusercontent.com); `free-for-dev` não tem arquivo LICENSE na `main` nem na `master` (C, 404). Estar na lista **não** é aval: qualquer um abre pull request com o próprio serviço (vi anúncios dentro da lista do MCP).

Regra do projeto que vale para tudo abaixo: antes do primeiro uso, o roteiro de entrada do `CONSELHO.md` (seção 6): licença lida, o que roda, veto.

---

## 1. public-apis/public-apis  (https://github.com/public-apis/public-apis , raw README 26/11/2026)

A lista diz de cada API só: chave (`apiKey`/`OAuth`/não), HTTPS, CORS. Não diz licença dos dados nem limite. Tudo abaixo é **chamada de leitura (GET) a uma API pública**: o que enviamos é só a consulta.

| # | Item | O que faria por nós | Custo / limite | Licença | Risco |
|---|---|---|---|---|---|
| 1 | **IBGE (servicodados.ibge.gov.br/api)** https://servicodados.ibge.gov.br/api/docs | B: dados reais para as contas (população, municípios, nomes, séries SIDRA via "Agregados", "Pesquisas", "Países"); A: municípios (Localidades) e notícias/calendário IBGE. Famílias vistas na página: Agregados, Localidades, Malhas, Nomes, Notícias, Países, Pesquisas, Calendário, CNAE (C, TinyFish 26/11) | Sem chave (lista: `No`); limite não declarado na página que li | Dados IBGE: licença/termos **não conferi** (a página bloqueou o WebFetch com 403; li pelo TinyFish só o índice) | Baixo (órgão oficial, só GET). Citar a fonte e a data em toda peça; checar o termo de uso antes de publicar número |
| 2 | **Banco Central, Dados Abertos / SGS** https://dadosabertos.bcb.gov.br/ | B: Selic, IPCA, dólar (PTAX) para reels de juros compostos, inflação, "quanto vale R$ 100 de 2015 hoje"; A: contexto de financiamento. Fonte primária brasileira | Sem chave. **Limite confirmado:** desde 26/03/2025, séries diárias em JSON/CSV exigem filtro de datas e consulta por período limitada a **10 anos**, senão dá erro (C, página da série Selic) | Página não declara licença (C: não declara) | Baixo. Nunca prometer custo/prazo de obra com taxa (regra do projeto) |
| 3 | **BrasilAPI** https://brasilapi.com.br/ | A e B: CEP, feriados nacionais, taxas (juros e índices oficiais), câmbio, municípios IBGE, bancos, CPTEC (clima). B: calendário de postagem sem postar em feriado ruim; A: CEP → município do lote | Sem chave. **Sem SLA, projeto "experimental/beta"; pede uso "de natureza de uma pessoa real" e não fazer crawling automatizado** (C, README) | **MIT** (C, LICENSE lido) | Médio-baixo: serviço de voluntários pode cair ou mudar; guardar resposta em cache local e ter a fonte oficial como reserva. CEP digitado por comprador vai a terceiro (dado pessoal, LGPD): só se o fluxo precisar |
| 4 | **ViaCEP** https://viacep.com.br | A: reserva do CEP (lista: sem chave, HTTPS) | Sem chave (S); limite não conferi | Não conferi | Mesmo risco do CEP acima. Só como reserva da BrasilAPI |
| 5 | **USGS Earthquake Hazards** https://earthquake.usgs.gov/fdsnws/event/1/ | B: terremotos reais com magnitude (escala logarítmica: cada ponto de magnitude é cerca de 32 vezes a energia) = reel "matemática do mundo real" com dado vivo e som (grave proporcional à energia) | Sem chave (S); limite não conferi | Dados USGS: não conferi (H: domínio público dos EUA) | Baixo. Citar USGS e data |
| 6 | **INPE Queimadas** https://terrabrasilis.dpi.inpe.br/queimadas/portal/ | B: focos de calor por estado/dia, dado brasileiro oficial para conta de proporção/taxa | Sem chave (S) | Não conferi | Baixo; conteúdo sensível (queimadas): enquadrar sem alarmismo |
| 7 | **Mercado Pago** https://www.mercadopago.com.br/developers/es/reference | A: cobrança Pix automática com confirmação (o fluxo de hoje é Pix manual no WhatsApp) | `apiKey` (S). **Taxa por venda: não conferi** | Proprietário (API) | **Dinheiro e contratação: decisão do dono.** Conta com CPF/CNPJ, dados de comprador vão ao Mercado Pago. Não é para agora |
| 8 | **Freesound** https://freesound.org/docs/api/ | B (só se um dia precisar de som gravado; hoje o som é sintetizado por nós, melhor) | `apiKey` (S) | **Licença por som** (CC0, CC-BY, CC-BY-NC): exige conferir um a um | Baixo; só entra o CC0 |

**Não escolhidos de propósito:** MathJS e CodeCogs (fazemos conta e fórmula localmente, sem enviar nada a terceiro); ferramentas de cripto, jogos, anime e clima de outros países; a seção "MCP Servers" da lista (são serviços hospedados de terceiros, ver item 3 da seção 3).

---

## 2. ripienaar/free-for-dev  (https://github.com/ripienaar/free-for-dev , raw README da `master`, 26/11/2026)

Lista de **planos grátis de serviços** (não de código). Cada linha traz o limite do plano **no dia em que alguém a escreveu**; planos mudam. Não tem seção de áudio, TTS nem Pix (C: busquei "audio, music, speech, sound, voice, pix, brazil": nenhum serviço próprio para isso).

| # | Item | O que faria por nós | Custo / limite | Licença | Risco |
|---|---|---|---|---|---|
| 1 | **Cloudflare R2** https://developers.cloudflare.com/r2/ | A: guardar o PDF entregue ao comprador (link). O `ebook/saida/ebook.pdf` tem 4,9 MB. B: guardar os MP4 com **URL pública**, que a Graph API exige (ver seção 4) | **Confirmado no site oficial:** 10 GB-mês, 1 milhão de operações de escrita e 10 milhões de leitura por mês, **saída de dados grátis** (só armazenamento "Standard") (C, developers.cloudflare.com/r2/pricing) | Serviço proprietário | Precisa de conta (cartão: **não conferi**). Link público de PDF pago = alguém repassa; entrega com link assinado exige um Worker. ToS e LGPD: dados do comprador não devem ir junto |
| 2 | **Cloudflare Pages + Workers** https://developers.cloudflare.com/pages/ | A: página de venda estática e redirecionador do link do WhatsApp; Worker para link de download com validade | Pages: **25 MiB por arquivo**, 20.000 arquivos, 500 builds/mês no plano grátis (C, página de limites). Workers: 100 mil requisições/dia (S, lista) | Proprietário | Mesma conta do item 1. O PDF atual cabe (4,9 MB) |
| 3 | **Fontes: Google Fonts, Fontshare, Bunny Fonts** https://fonts.google.com/ , https://www.fontshare.com/ , https://fonts.bunny.net | A e B: fonte para o manual de identidade (D50) e para os reels. B: Press Start 2P já confirmada OFL (outra pesquisa, `ferramentas-gratis-animacao.md`) | Grátis, uso comercial (lista: Fontshare "100% free for personal and commercial use" = S) | OFL por família no Google Fonts; **Fontshare: conferir a licença de cada fonte antes de usar** | Baixo. Baixar o arquivo e embutir (não carregar de CDN em runtime: não manda dado do comprador ao Google). Conferir acentos do português |
| 4 | **Backend de formulário** (Formsubmit.co, Formspree, Backforms) https://formsubmit.co , https://formspree.io , https://backforms.com | A: formulário "diga o tamanho do lote" antes de abrir o WhatsApp, para o funil. Lista: Formsubmit "sem cadastro"; Formspree 50 envios/mês/formulário; Backforms 300/mês com alerta no WhatsApp (traz a própria chave) | 50 a 300 envios/mês (S, lista) | Proprietários | **LGPD**: nome e telefone do comprador vão a empresa fora do Brasil. O funil de hoje é o WhatsApp direto, sem formulário: só vale se o teste mostrar ganho. Decisão do Estrategista e do Revisor |
| 5 | **Cloudinary** https://cloudinary.com/ | B: hospedagem de imagem/vídeo com URL pública para a Graph API publicar; A: miniaturas | 25 créditos/mês (1 crédito = 1.000 transformações ou 1 GB de armazenamento ou 1 GB de banda) (S, lista) | Proprietário | Conta; redundante com o R2 (item 1). Só se o R2 não servir |
| 6 | **Make (automação)** https://www.make.com | A/B: ligar "pedido pago" a mensagem, planilha etc. sem escrever código | 1.000 operações/mês, intervalo mínimo de 15 min (S, lista) | Proprietário | Guarda tokens de contas (Instagram, Google): **veto forte** enquanto não houver necessidade comprovada; o que fazemos hoje cabe em script nosso |
| 7 | **Rizamo** https://rizamo.com | B: agenda e publica no Instagram por REST/MCP, "grátis para 2 contas, posts ilimitados" (S, linha da lista) | Grátis 2 contas (S) | Proprietário | **Veto forte**: terceiro guarda o token da nossa conta e o MCP acessa as nossas ferramentas. A API oficial (seção 4) faz o mesmo sem intermediário |
| 8 | **Orshot / Metashot / PDFBolt** (imagem e PDF por API) | **Não recomendo**: já geramos PDF e imagens localmente com mais qualidade e sem enviar nada para fora | 100 a 500 por mês (S) | Proprietários | Listado só para registrar que foi visto e dispensado |

---

## 3. punkpeye/awesome-mcp-servers  (https://github.com/punkpeye/awesome-mcp-servers , raw README, 26/11/2026)

A lista tem milhares de servidores. Cada um é **código de terceiro que roda na nossa máquina (ou serviço que recebe nossas chamadas) com acesso às nossas ferramentas**. Regra geral: **para dado público, é mais seguro chamar a API oficial direto de um script nosso do que instalar um MCP** (menos código de estranho). Ícones da lista: 🏠 = roda local, ☁️ = chama serviço na nuvem.

| # | Item | O que faria por nós | Custo | Licença | Risco |
|---|---|---|---|---|---|
| 1 | **SidneyBissoli/bcb-br-mcp** https://github.com/SidneyBissoli/bcb-br-mcp | B: Selic, IPCA, PTAX, expectativas Focus por pergunta em português. Embrulha o item 2 da seção 1 | Grátis; roda via npm | **MIT** (C, LICENSE) | Médio: código npm de terceiro. Equivale a chamar a API do BCB direto; preferir o script nosso |
| 2 | **SidneyBissoli/ibge-br-mcp** https://github.com/SidneyBissoli/ibge-br-mcp | B: tabelas SIDRA, censo, projeções, malhas do IBGE | Grátis | **MIT** (C) | Médio (mesmo do anterior) |
| 3 | **alanpcf/brasil-data-mcp** https://github.com/alanpcf/brasil-data-mcp | A: CEP, feriados, bancos, CNPJ pela BrasilAPI | Grátis | **MIT** (C) | Médio. CNPJ e CEP vão para a BrasilAPI |
| 4 | **ChanMeng666/archlang** https://github.com/ChanMeng666/archlang | A: planta "como código" (`.arch` → SVG/DXF/PDF), lê de volta cômodos, áreas e adjacências; **serve como segunda conferência de áreas das nossas plantas**, não substitui `plantas.py validar` | Grátis; local via `npx` | **MIT** (C) | Médio. **Vetar a versão hospedada** (`mcp.archlang.uk`, o README oferece): nossos desenhos iriam para fora. Só a local, e só depois de ler o código |
| 5 | **Kentucky-ai/opentakeoff** https://github.com/Kentucky-ai/opentakeoff | A: medir áreas e perímetros em PDF de planta (conferir o que o e-book diz de m²) | Grátis; local | **AGPL-3.0** (C, LICENSE) | Licença forte: usar só como programa separado, nunca copiar código para o nosso. Cabe ao Revisor |
| 6 | **mberg/kokoro-tts-mcp** https://github.com/mberg/kokoro-tts-mcp (+ modelo https://huggingface.co/hexgrad/Kokoro-82M) | B: **voz em português do Brasil, local, grátis**, para narrar. O modelo Kokoro-82M é Apache (C, página oficial) e a lista de vozes traz **pt-BR: pf_dora (feminina), pm_alex e pm_santa (masculinas)** (C, VOICES.md). O README do MCP está configurado para `af_heart`/`en-us` e para subir MP3 em S3 da Amazon (C): para nós, desligar o S3 | Grátis; baixa pesos ONNX (tamanho: não conferi) | MCP **Apache-2.0** (C); pesos Apache | Médio: o pacote usa AWS se ligar `S3_ENABLED`. Qualidade da voz pt-BR **não ouvida**. Alternativa já pesquisada: Piper (outra nota). Ouvir 3 amostras antes de decidir |
| 7 | **mikusnuz/meta-mcp** https://github.com/mikusnuz/meta-mcp | B: publica reels, carrossel e stories, agenda, lê métricas e comentários **pela Graph API oficial**; o README diz que suporta o rótulo "AI info" (S, README) | Grátis | **MIT** (C) | **VETO FORTE.** Guarda o token da nossa conta Instagram, 66 ferramentas incluindo DM e comentários, escreve e apaga. Melhor: ler a seção 4 e fazer 3 chamadas da API oficial num script curto nosso |
| 8 | **Regenerating-World/pix-mcp** https://github.com/Regenerating-World/pix-mcp | A: gera QR Code e "copia e cola" Pix com vários provedores (Efí, Cielo) | Grátis (o código); provedores cobram | **MIT** (C) | **VETO FORTE**: pagamento, chaves de provedor, dinheiro. O QR estático do Pix não precisa disso: o Banco Central publica o manual do BR Code (PDF de 13 páginas, C, baixado e aberto: `bcb.gov.br/content/estabilidadefinanceira/spb_docs/ManualBRCode.pdf`) e o código é um texto com CRC que se gera localmente em Python (H: a conferir) |

**Servidores que vi e não escolhi:** `adaptlypost`, `postsider`, `posteverywhere`, `publora`, `taisly`, `upload-post`, `PlanVortex` e dezenas de outros "publicadores" (são SaaS que guardam o token: mesmo veto do item 7); `tokportal` (contas gerenciadas por humanos de terceiro: incompatível com "100% IA" e arriscado); `HasData/instagram-mcp` e `SocialAPIsHub` (raspagem de Instagram: ToS e risco); `Transcript Dock` (envia link de Reels/YouTube a terceiro; para Reels já temos o `analyze_hook`). Playwright e busca na web já temos (navegador e TinyFish).

---

## 4. Meta Graph API (Instagram) por API oficial: o que ela exige (fonte primária, lida 26/11/2026)

Fontes: https://developers.facebook.com/docs/instagram-platform/content-publishing e https://developers.facebook.com/docs/instagram-platform/overview (C).

- **Tipo de conta:** só conta **profissional** (Business ou Creator). Pessoal não consta (C).
- **Publicar Reels é possível:** contêiner com `media_type=REELS` e `video_url` (C). A própria página não lista formatos/codecs de vídeo (C: não declara); imagem só JPEG.
- **Vídeo precisa estar numa URL pública** no momento da tentativa (a Meta baixa o arquivo); há também envio "resumível" de arquivo local ou por `file_url` (C). Daí a utilidade do R2 (seção 2, item 1).
- **Permissões:** com Instagram Login, `instagram_business_basic` + `instagram_business_content_publish`; com Facebook Login, `instagram_basic` + `instagram_content_publish` + `pages_read_engagement` (C). Se a Página exigir "Page Publishing Authorization", não publica sem concluir (C).
- **Acesso:** Standard Access é o padrão e serve a "pessoas com função no app" e testes; **Advanced Access exige App Review e Business Verification e só é preciso se o app servir contas que não são suas**. Para **só a nossa conta**, "Standard Access é tudo o que o app precisa" (C, página overview). A página de publicação não descreve App Review (C), então **não está provado** que dispensa revisão na prática: provar com um teste real.
- **Limite:** a página traz dois números sem reconciliar: **100 posts por API em 24 h** (seção de limite) e **50** (seção de carrossel); consultar `GET /<IG_ID>/content_publishing_limit` (C). Para nós, 1 a 2 por dia, folga enorme.
- **Não suporta:** tags de compra e filtros (C). A página não menciona música/áudio da biblioteca do Instagram (C: não menciona): como o nosso som já vai **dentro** do MP4, não depende disso.
- **Rótulo de IA:** a página que li não trata do rótulo. O README do `meta-mcp` diz que a API aceita a marcação "AI info" (S): **conferir na documentação do endpoint antes de usar**, e marcar, por honestidade e pelo veto do Revisor.
- **Não conferi:** o passo a passo de criar o app e o token de longa duração (renovação a cada 60 dias, H), e se criar app exige a conta pessoal do dono ou alguma verificação de identidade.

---

## 5. Os 5 de maior uso, em ordem

1. **API de dados do Banco Central (SGS) + IBGE, chamadas direto de script nosso** (seção 1, itens 1 e 2): fonte primária brasileira, sem chave, sem instalar nada de terceiro. Alimenta as contas reais dos reels (B) e dá fonte citável. Atenção ao limite de 10 anos por consulta.
2. **Graph API oficial do Instagram, chamada por script nosso, sem MCP intermediário** (seção 4): resolve "agendar/publicar" na conta de IA (B). Exige conta profissional e URL pública do vídeo. Usar o `meta-mcp` só como referência de leitura, **vetado para instalar**.
3. **Cloudflare R2 (e Pages)** (seção 2, itens 1 e 2): onde guardar o PDF (A) e os MP4 com URL pública (B), com números oficiais confirmados e o PDF atual cabendo. Falta: ver se pede cartão e como entregar com link que expira.
4. **BrasilAPI** (seção 1, item 3, MIT): feriados (calendário de postagem), CEP e taxas num lugar só, com reserva ViaCEP. Cuidado: sem SLA, usar com cache.
5. **Kokoro-82M (Apache) com voz pt-BR** (seção 3, item 6): única opção grátis nova que apareceu para a **voz** (B). Falta ouvir pf_dora, pm_alex e pm_santa e comparar com o Piper antes de qualquer decisão; sem o S3.

Menções: ArchLang (conferir áreas das plantas, A) e USGS (reel de terremoto, B) são boas, mas dependem de ver o código/licença e de o dono querer.

## 6. O que NÃO confirmei

IBGE: termo de uso e limite (a página deu 403 ao WebFetch). Licença dos dados do BCB, USGS e INPE. Limite e licença do ViaCEP. Se o Cloudflare pede cartão. Taxa do Mercado Pago. Quantos MB os pesos ONNX do Kokoro têm e como soa o pt-BR. O rótulo "AI info" na documentação oficial da Graph API. Se a publicação só na nossa conta dispensa App Review na prática. Nenhuma lista foi lida inteira: busquei por seção e por palavra (o README do MCP tem cerca de 5.400 linhas e quase 5.000 links).
