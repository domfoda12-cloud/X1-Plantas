# Quadro de avisos: o que o dono acabou de pedir

> **Todo agente e toda conversa lê este quadro antes de trabalhar** (regra do dono, 22/11/2026: "depois de cada pedido, SEMPRE informe todo mundo do que está acontecendo, crie um contexto a partir disso e alimente todos"). Quem atende o pedido escreve aqui, no topo, e apaga o mais antigo: ficam os 5 últimos. O histórico inteiro está em [`CONTEXTO-HISTORICO.md`](../CONTEXTO-HISTORICO.md).

## 22/11 · Índice, resumos por pasta e os prompts do dono

- **O dono pediu:** separar os documentos em categorias, ligar cada agente às suas pastas e criar resumos baratos; incluir os prompts dele.
- **Todos:** comece pelo [`INDICE.md`](../INDICE.md) e pelo `RESUMO.md` da pasta; documento inteiro só se precisar. Documento novo: `python3 ferramentas/resumos.py`.
- **Todos:** os prompts do dono, palavra por palavra, estão em `contexto/dono/PROMPTS.md`; acrescente cada pedido novo no fim.
- **Todos:** há cerca de 60 contradições entre documentos em `contexto/dono/TEXTOS-DESATUALIZADOS.md`. Vale a regra mais recente; quem corrigir apaga a linha.
- **Redator e Revisor:** o FAQ e a sequência do WhatsApp prometem 3D, animação e garantia que ainda não estão confirmados.

## 22/11 · A `main` é a única branch; arquivos comprimidos

- **O dono pediu:** destravar o projeto: juntar tudo, comprimir, manter arrumado e ver o sistema no Graphify.
- **Todos:** o projeto inteiro está na `main`. **Trabalhe e envie na `main`** (`git pull --rebase` antes); a `planta-de-casas-anuncio` acabou. Mudança de sistema: branch `sistema/<assunto>` com pull request.
- **Todos (regra do dono):** analise todo dado e código que recebe, lê ou cria; confira o número contra a fonte antes de repassar.
- **Todos:** leia e busque arquivos direto; o Graphify é mapa, não etapa obrigatória. Arquivo fica junto do que tem a mesma função.
- **Designer e Editor de vídeo:** as fotos do OpenArt agora são `.jpg` (`ebook/visual/openart/`); vídeos reencodados; tours da C06 em `video/saida/tour-c06/`.

## 22/11 · Skill `make-pdf` e conversa própria do Editor

- **O dono pediu:** adicionar a skill `make-pdf` (gstack) e ter o Editor como conversa de verdade.
- **Todos:** `make-pdf` está registrada sem o preâmbulo (telemetria), mas **não funciona**: instalar o gstack espera o "sim" do dono. Não é para o e-book.
- **Editor de vídeo:** há outra conversa na mesma branch: `git pull --rebase` antes de enviar.

## 22/11 · C01 redesenhada; OpenArt só com permissão

- **O dono pediu:** refazer por enquanto só 1 planta do vídeo e usar o OpenArt: "eu NÃO proibi, apenas necessita permissão".
- **O que mudou:** **C01** nova: varanda de entrada, sala e jantar, cozinha nos fundos, hall curto (circulação 4%), banheiro de 1,69 m livres, serviço com porta para o quintal; 50 m². Dados, 3D, PDF, planta grátis e calculadora regenerados.
- **OpenArt (todos):** não é proibido; **cada uso pede o "sim" do dono**, com resumo e custo antes. Conta: 21.137 créditos.
- **Editor de vídeo:** clipes e imagens antigos da C01 mostram a casa velha; use `ebook/visual/3d/C01.jpg`. A E07 do escaneamento continua com o arranjo antigo.
- **Redator e Revisor:** gancho e "para quem é" da C01 mudaram (`ebook/fichas/textos.py`): revisar. `instagram/posts/POSTS.md` ainda diz 55 m².
- **Designer:** imagem 2D da C01 desatualizada; a sala ainda não desenha a mesa.
