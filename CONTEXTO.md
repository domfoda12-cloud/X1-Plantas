# Contexto do projeto: tudo o que o dono pediu, e o que cada pedido quer dizer

> **Leia antes de qualquer tarefa.** Cada pedido do dono tem um motivo e continua valendo até ele dizer o contrário. Toda sessão (nuvem, Mac, MinoAI Frontier) acrescenta aqui, no fim, cada pedido novo com a data e o que ele quer dizer na prática. Regra em [`CLAUDE.md`](CLAUDE.md).

## O que nunca muda

| O dono disse | O que isso quer dizer |
|---|---|
| "O objetivo é a alegria do consumidor, e a alegria dele me mandar o Pix" | Toda entrega é julgada por duas coisas: o comprador fica feliz com o que recebe? Ele paga? |
| "Pensa como um marketeiro, público brasileiro" | Português do Brasil, R$, Pix, WhatsApp, quem constrói com pedreiro por etapas. Ver [persona](ebook/referencias/persona-e-mercado.md) |
| "Sempre do ponto de vista de um arquiteto profissional" | Toda planta passa pelo validador e explica o porquê de cada decisão |
| "Não tem landing page" | Venda por anúncio (Facebook e Instagram) → comentário → WhatsApp. O parceiro cuida do funil, o dono cuida do material e do anúncio |
| "Mantenha todo o contexto, tudo o que eu faço significa algo" | Este arquivo. Nada do que foi pedido se perde entre conversas |
| "Quero a opinião da MinoAI sempre, ele é o maestro" | Toda entrega traz a opinião do Maestro, tirada das ferramentas da MinoAI Frontier, com a fonte |
| "Ótimo ao máximo, TUDO" | Fazer completo e bem feito, sem atalho que prejudique a qualidade |
| "Continue trabalhando sem pedir permissão" (para tarefas internas) | Avançar sozinho no que é interno; decisões de dinheiro, título, preço e publicação continuam com o dono |

## Linha do tempo dos pedidos

| Quando | Pedido | O que virou |
|---|---|---|
| Início | Vender no X1 "planta de casas", não é campanha de Natal (outra sessão) | Produto: e-book de plantas |
| Início | Adicionar o repositório, tudo em português, Facebook Ads + WhatsApp, Brasil primeiro e talvez fora depois | Repositório `X1-Plantas`, branch `planta-de-casas-anuncio` |
| Início | Sem landing page; dono faz material e anúncio, parceiro faz o funil | [`ebook/vendas/`](ebook/vendas/) com a sequência do WhatsApp |
| Fase de vídeo | Brief criativo; procurar plantas e pensar em animar em 3D; perfil de Instagram de arquitetura | [`video/anuncios/brief-criativo.md`](video/anuncios/brief-criativo.md), [`animacoes-3d/`](animacoes-3d/), [`instagram/plano-perfil.md`](instagram/plano-perfil.md) |
| Fase de vídeo | Seguir o reel de referência; prestar atenção na retenção; o cliente precisa se interessar pelas plantas | Regras de edição em [`instagram/MINOAI-FRONTIER.md`](instagram/MINOAI-FRONTIER.md) e [`instagram/referencias-mino-lee.md`](instagram/referencias-mino-lee.md) |
| Fase de vídeo | Clipes menos travados: blueprint azul ganhando vida; gancho "vou te salvar os R$ 1.000 que um arquiteto te salvaria" | Motor 3D com blueprint que ganha vida; 5 versões de gancho em `video/saida/` |
| Fase de vídeo | Narrador sempre falando, sem pausa, sempre um visual prendendo a atenção | Regra de roteiro em [`video/VIDEO.md`](video/VIDEO.md) |
| Fase de vídeo | Referências do perfil minolee.mp4 e de 3 reels; juntar tudo de valioso ao editor | [`instagram/referencias-mino-lee.md`](instagram/referencias-mino-lee.md) |
| Fase de vídeo | Não precisa verificar preço de arquiteto | Fora das pesquisas |
| Organização | Dezenas de plantas num e-book com grande variação; pastas Vídeo, Animações 3D, Instagram, E-book e um painel que controla tudo | [`PAINEL.md`](PAINEL.md), [`ebook/catalogo.md`](ebook/catalogo.md) com 35 plantas em 3 lançamentos |
| Organização | Não só revisar, melhorar o conteúdo; um chat por frente | Chats na nuvem por frente (branches `frente-*`) |
| Organização | MinoAI Frontier como editor e depois como maestro | [`MAESTRO.md`](MAESTRO.md) |
| Organização | Roteiro "volto pro Brasil com casas na mala" | [`video/roteiro-lancamento.md`](video/roteiro-lancamento.md) |
| Ferramentas | Skills para o e-book (Impeccable só para opinar sobre o genérico; Karpathy); ferramenta de pesquisa melhor (TinyFish), por meios brasileiros e sites oficiais | Pesquisa jurídica em [`reports/`](reports/); TinyFish no Pesquisador |
| 19–20/11/2026 | Analisar os 5 catálogos de porcelanato; linguagem que convence; visual melhor; animações; pelo menos 20 plantas como um arquiteto; pesquisa de público com uma persona alinhada ao arquiteto; como as casas são de verdade no Brasil | 24 plantas validadas ([`ebook/plantas/PLANTAS.md`](ebook/plantas/PLANTAS.md)), [persona "Marcos"](ebook/referencias/persona-e-mercado.md), [regras do arquiteto](ebook/referencias/regras-do-arquiteto.md), [análise dos catálogos](ebook/referencias/analise-catalogos-porcelanato.md), [linguagem e animação](ebook/referencias/linguagem-visual-e-animacao.md) |
| 20/11/2026 | Um redator que sempre pensa em bons atributos, com o objetivo no dinheiro | Agente [`redator`](.claude/agents/redator.md), skill `/redacao-que-vende`, [banco de atributos](ebook/vendas/atributos-que-vendem.md) |
| 20/11/2026 | Um ecossistema de skills que se entendem, dão opinião e só usam a skill quando concordam | [Conselho](CONSELHO.md), skill `/conselho`, 7 agentes em `.claude/agents/` |
| 20/11/2026 | Depois disso, começar o e-book; exemplo de skills juntas: MinoAI + OpenArt para imagens e animações | [Fluxo OpenArt + MinoAI](animacoes-3d/OPENART-MINOAI.md) (OpenArt sem conector; usado no navegador ou por API com chave) |
| 20/11/2026 | Segurar as animações 3D, deixar por último | Motor preparado para as 24, render parado; passo 9 do plano |
| 20/11/2026 | Primeiro o roteiro passo a passo e como o e-book vai ficar; "visualize it" | [`ebook/PLANO-EBOOK.md`](ebook/PLANO-EBOOK.md) e a prévia visual (página privada no claude.ai, fonte em [`ebook/visual/plano-visual.html`](ebook/visual/plano-visual.html)) |
| 20/11/2026 | O objetivo é a alegria do consumidor, que vira Pix | Primeira regra do [`CLAUDE.md`](CLAUDE.md) e do Redator |
| 20/11/2026 | Manter todo o contexto | Este arquivo |
| 20/11/2026 | "Quero que pareça mais inovador" | Prévia nova: capa fita métrica, vitrine pelo lote, casa desenhada no lote com recuos e bússola, ficha "Informação da casa" no formato da tabela nutricional, orelhas por largura de lote, e-book vivo por QR |
| 20/11/2026 | "A edição de vídeo é responsabilidade e a criação de imagem será o Mino usando o OpenArt" | MinoAI Frontier dona da edição de vídeo e da criação de imagem, com o plugin OpenArt (falta autorizar a conta). [`MAESTRO.md`](MAESTRO.md), [`CONSELHO.md`](CONSELHO.md), [fluxo](animacoes-3d/OPENART-MINOAI.md) |
| 20/11/2026 | "A MinoAI está fazendo algo aqui? Ele é o maestro. Quero a opinião dele sempre" | MinoAI Frontier opina em toda tarefa, primeiro, com as ferramentas dele e a fonte ([`CONSELHO.md`](CONSELHO.md), regra 0). Primeira opinião registrada na prévia do e-book |

| 20/11/2026 | "Economizar o máximo do OpenArt, mas enfeitado; pode começar, mas não use o primeiro modelo" | Plano de economia em [`animacoes-3d/OPENART-MINOAI.md`](animacoes-3d/OPENART-MINOAI.md): modelo de imagem em vez do padrão de vídeo, rascunho antes, uma imagem para vários formatos, teto de 6. OpenArt ainda sem autorização |
| 20/11/2026 | "Prepare tudo o que precisa ser preparado, e dale. EFICIÊNCIA" | E-book gerado: [`ebook/saida/ebook.pdf`](ebook/saida/ebook.pdf) (61 páginas) e a planta grátis C01 com a página-ímã; 3 mockups grátis em `ebook/visual/mockups/` |

## Em aberto (esperando o dono)

- Autorizar a conta do OpenArt nos conectores do claude.ai e dizer quanto crédito pode gastar.

- Aprovar o plano do e-book (formato A4 de cerca de 60 páginas, capa "Que casa cabe no seu lote?", começar os passos 1 a 6).
- Título, preço, bônus, lançar com 12 ou 24 plantas, contato do parceiro.
- Arquiteto registrado para revisar as 24 plantas.
- Gravar o apresentador; criar o Instagram; configurar a MinoAI Frontier no Mac.
- Atualizar o relatório jurídico com Caixa e Confea (pedido antes, sem resposta).
- Juntar as branches `frente-instagram` e `frente-video` (a `frente-ebook` já foi aproveitada).
