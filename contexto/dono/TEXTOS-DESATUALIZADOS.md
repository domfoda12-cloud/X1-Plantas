# O que ainda não bate: pendências depois da limpeza de 22/11/2026

> Em 22/11/2026 quatro agentes leram todos os documentos e acharam cerca de 60 contradições. Três agentes no Opus resolveram as que dependiam só de texto (a regra mais recente do dono vence; texto de venda só promete o que existe; documento superado foi apagado). **Aqui ficou só o que depende do dono, do Revisor de risco ou de refazer imagem e vídeo.** Quem resolver um item apaga a linha.

## Decisões do dono (os textos estão com o campo entre colchetes, esperando)

- **Preço, garantia de 7 dias, bônus, parcelamento, promessa de atualização e título** do e-book: `ebook/vendas/faq-compradores.md`, `sequencia-whatsapp.md`, `respostas-objecoes.md`, `atributos-que-vendem.md`, `ebook/EBOOK.md` seção 5, `video/anuncios/anuncio-facebook.md` (ângulo 6).
- **Lançar com 12 ou 24 plantas:** o PDF tem 24; `ebook/catalogo.md` e `video/roteiro-lancamento.md` deixam o número em aberto.
- **Selo "Imagem ilustrativa":** aplicamos a leitura "saiu dos vídeos, continua em imagem parada (post e e-book)". Falta o dono confirmar.
- **Vídeo:** o que é "pagar por mais" no vídeo-convite; formato 4:5 ou 9:16 do anúncio com locução; qual planta a chamada promete (`video/VIDEO.md`).
- **PDF de 23 MB:** precisa ficar mais leve para mandar no WhatsApp?

## Revisor de risco

- Em 22/11 ele leu os textos de venda e vetou trechos em 5 de 7 arquivos; as frases aceitas foram aplicadas. A foto antiga de fachada da C01 saiu do e-book: a casa usa a vista da rua simplificada até a foto ser refeita (OpenArt, com o "sim" do dono).
- Ainda sem a leitura dele: os textos de cada casa em `ebook/fichas/textos.py` (fora C01 e C03), a calculadora, os posts e os roteiros de vídeo.

## Já revisado em 22/11 (apagar quando conferir que ficou certo)

- `ebook/vendas/material-gratuito.md`: ficha nova da C01.
- `ebook/vendas/sequencia-whatsapp.md`: dias 1 e 3; `ebook/vendas/faq-compradores.md`: "O que vem no e-book?".
- `video/anuncios/anuncio-facebook.md`: ângulo 3, reescrito com a C03 (41 m², "o lugar do 2º quarto desenhado").
- `reports/`: a frase "a separação de quem emite o quê é consistente em todas as fontes".

## Imagem e vídeo que ainda mostram a casa velha (texto já corrigido)

- **C01 antiga:** o mockup `ebook/visual/mockups/casa-c01-celulares.png`, o clipe `video/broll/clipes/c01-3d.mp4`, a pasta `animacoes-3d/plantas/casa-compacta/` e as imagens dos posts em `instagram/posts/imagens/` (os textos dentro de `instagram/posts/gerar-imagens.cjs` também).
- **Roteiros de vídeo** (`video/roteiros/*.json`): `principal.json` diz "55 m² · 2 quartos" (C01 antiga); `principal.json`, `principal-condor.json` e `previa-whatsapp.json` dizem "24 casas no e-book" (o número está em aberto); o `convite.json` põe 8 selos "Ilustração do modelo 3D" (é selo com outro nome). Acertar ao refazer.
- **Vídeos a remontar antes de usar:** `previa-whatsapp` e `principal` usam o clipe da C01 antiga; os quatro roteiros em `video/roteiros/*.json` ainda põem "Ilustração do modelo 3D" ou "Imagem ilustrativa" na tela; `saida/v1` a `v5` são da C01 velha.
- **E07:** está na fila do redesenho (3 quartos em fila); os vídeos `principal-condor` e `principal-e07` são rascunho.

## Para o Revisor e o dono (achados da auditoria de 22/11, sem veredito)

- `ebook/fichas/textos.py`: a E02 é vendida com "2 quartos em fila, como na casa de vila", o mesmo arranjo que o dono reprovou na E07.
- A caixa "Informação da casa" do PDF diz "Conferido medida por medida pelo X1-Plantas": quem conferiu foi o validador, não um profissional.
- A planta grátis diz "Essa foi 1 de 24" com "12 ou 24" ainda em aberto.
- Qual casa a planta grátis oferece para "8 m, quer 3 quartos" enquanto a E07 é redesenhada.

## Ainda não conferido

- `ebook/catalogo.md`: a seção "Ache pelo jeito da família" e os destaques das séries C, F e S não foram conferidos casa por casa contra os dados.
- Contagens de banheiro: 21 de 24 casas com algum banheiro abaixo de 1,50 m e 18 abaixo de 1,10 m (recalculadas em 22/11 pelos dados; mudam quando mais casas forem redesenhadas).
