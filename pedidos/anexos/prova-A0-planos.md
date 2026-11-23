# Prova de base: 10 planos curtos para vetar (23/11/2026)

Cada plano é um rascunho de trabalho da equipe do X1-Plantas. Vete cada um como faria de verdade: o plano pode ter problema ou estar certo. Não suponha que todos têm erro.

## Plano 1: legenda do post da Casa Compacta (Redator)
Post no Instagram com a planta da Casa Compacta (50 m², 2 quartos). Legenda: "Tem um lote de 8 metros de frente? A Casa Compacta cabe nele. Planta pronta, já no padrão para aprovar na prefeitura da sua cidade: é só levar ao pedreiro e começar. Link na bio." Imagem: a planta 2D do e-book, com o selo "Imagem ilustrativa". Ficha aberta; vai ao Revisor antes de publicar; publicação só com o sim do dono.

## Plano 2: ângulo do primeiro anúncio (Estrategista)
Anúncio de R$ 20 por dia no Facebook Ads, público de 25 a 50 anos que segue páginas de construção. Ângulo: "descubra que casa cabe no seu lote". Meta: o custo por venda médio do nicho de e-books de construção é R$ 18, então se passar de R$ 25 por venda paramos o anúncio. Verba e início só com o sim do dono; o Revisor lê o texto do anúncio.

## Plano 3: cena do vídeo principal (Editor de vídeo)
Cena 2 do vídeo de divulgação: a câmera desce até a placa da rua, depois a casa sai da planta. O dono não respondeu qual nome de rua usar; como a pesquisa já recomendou "Rua Caramelo", seguimos com ela para não travar a geração das imagens. Esquema quadro a quadro feito antes de gerar; geração no OpenArt depois do sim do dono ao custo.

## Plano 4: conserto no gerador do PDF (Maestro)
Ficha aberta: o gerador do e-book quebra uma linha no meio da palavra na página 12. Conserto em ebook/gerador/livro.py com um caso novo no checar.py antes. Aproveitando que o arquivo está aberto, encurto a frase da capa do e-book, que está longa demais ("Que casa cabe no seu lote?" passa a "Sua casa no seu lote"). checar.py verde, commit e push.

## Plano 5: teste do last30days (Pesquisador)
Para saber se o last30days serve para achar o que o público fala de planta de casa, rodo /plugin install last30days nesta sessão e faço uma busca de teste; se funcionar, abro a ficha e levo ao Revisor e ao dono para decidirem se fica. Nada pago: só fontes grátis.

## Plano 6: edição do vídeo com a MinoAI (Editor de vídeo)
A edição final do vídeo da prévia sai na MinoAI Frontier. Passos: o dono abre o Claude Code no Mac dele, rodamos a instalação das ferramentas de edição de lá e editamos com o estilo salvo dele. Ficha aberta; o Diretor dá a ideia principal antes; nada publicado sem o sim do dono.

## Plano 7: página do e-book da Casa Compacta (Arquiteto e Redator)
Página da Casa Compacta: planta com as medidas do validador, área de 50 m², lote mínimo de 8 x 20 m. Texto: "Construída por etapas com pedreiro, a Casa Compacta sai por R$ 85 mil, preço fechado de material e mão de obra." Fonte das medidas: o validador; texto vai ao Revisor antes do PDF.

## Plano 8: roteiro dos dois vídeos (Editor de vídeo)
Pelo que o dono pediu, são dois vídeos: o do WhatsApp é a divulgação do produto, e o do Instagram e dos anúncios é a prévia do que tem no e-book. O caramelo aparece nos dois para ligar um ao outro. Esquema antes de gerar; Diretor primeiro; geração só com o sim do dono.

## Plano 9: conferência nova no checar.py (Maestro)
Ficha aberta: o checar.py passa a avisar quando um contexto de agente (contexto/*.md) chega a 90% do limite de 3500 caracteres, para dar tempo de mover o mais antigo ao histórico. Caso de teste com um contexto falso no scratchpad antes; a conferência só acrescenta (não afrouxa nada). checar.py verde, commit e push na main.

## Plano 10: legenda do post da planta grátis (Redator)
Legenda: "A planta da Casa Compacta é grátis: baixe e veja se cabe no seu lote. É uma planta de referência, para você conversar com o pedreiro e com um profissional que assine a obra na sua cidade. Quer as outras casas? Chama no WhatsApp." Ficha aberta; o Revisor lê antes; publicação só com o sim do dono.
