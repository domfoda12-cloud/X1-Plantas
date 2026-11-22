# Contexto do projeto: tudo o que o dono pediu, e o que cada pedido quer dizer

> **Resumo que todo mundo lê.** Cada pedido do dono tem um motivo e continua valendo até ele dizer o contrário. O histórico completo, pedido por pedido, está em [`CONTEXTO-HISTORICO.md`](CONTEXTO-HISTORICO.md): abra só se precisar de um detalhe antigo. Antes de trabalhar, todos leem o [quadro](contexto/QUADRO.md) e o seu arquivo em [`contexto/`](contexto/). Regra em [`CLAUDE.md`](CLAUDE.md).

## O que nunca muda

| O dono disse | O que isso quer dizer |
|---|---|
| "O objetivo é a alegria do consumidor, e a alegria dele me mandar o Pix" | Toda entrega é julgada por duas coisas: o comprador fica feliz com o que recebe? Ele paga? |
| "Pensa como um marketeiro, público brasileiro" | Português do Brasil, R$, Pix, WhatsApp, quem constrói com pedreiro por etapas. Ver [persona](ebook/referencias/persona-e-mercado.md) |
| "Sempre do ponto de vista de um arquiteto profissional" | Toda planta passa pelo validador e explica o porquê de cada decisão; as plantas não são de arquiteto, são de referência ([jurídico](reports/RESUMO.md)) |
| "Não tem landing page" | Venda por anúncio (Facebook e Instagram) → comentário → WhatsApp. O parceiro cuida do funil, o dono cuida do material e do anúncio |
| "Mantenha todo o contexto, tudo o que eu faço significa algo" | Este arquivo. Nada do que foi pedido se perde entre conversas |
| "Quero a opinião da MinoAI sempre, ele é o maestro" | Toda entrega traz a opinião do Maestro, tirada das ferramentas da MinoAI Frontier, com a fonte |
| "Falo muito de eficiência, mas a prioridade é sempre a maior qualidade" | Peça final sempre na melhor configuração; economia só em rascunho e teste ([`CLAUDE.md`](CLAUDE.md)) |
| "Foque em uma coisa por vez, não misture tudo ao mesmo tempo" | Uma frente por vez, do começo ao fim, antes de abrir outra. Ordem atual: e-book → animações → vídeo |
| "Ótimo ao máximo, TUDO" | Fazer completo e bem feito, sem atalho que prejudique a qualidade |
| "Quando eu paro para acrescentar informação, junte tudo" | Recados no meio do trabalho entram todos na mesma entrega |
| "Antes de qualquer vídeo ou gasto no OpenArt, me dê o resumo da produção e as instruções que segue; confirmo os dois" | Nada é montado nem gasto sem as duas confirmações do dono ([`video/CLAUDE.md`](video/CLAUDE.md)) |
| "Continue trabalhando sem pedir permissão" (para tarefas internas) | Avançar sozinho no que é interno; decisões de dinheiro, título, preço e publicação continuam com o dono |

## Em aberto (esperando o dono)

- **E-book (para publicar):** preencher em `ebook/config.json` o título, o preço, os bônus, o WhatsApp do parceiro e, se quiser, `promessa_atualizacao` (prometer as próximas casas de graça é oferta que obriga). Decidir se lança com 12 ou 24 plantas (o PDF tem 24), o preço e a garantia: R$ 67 e 7 dias são só recomendação ([`ESTRATEGIA.md`](ESTRATEGIA.md), seção 7).
- **Arranjo das plantas (22/11):** o dono reprovou o layout. O Arquiteto estudou projetos reais (prefeitura de SP, governo da Bahia, UFRGS) e tem método novo ([apostila 2](ebook/referencias/arquiteto-sites-de-profissionais.md)). Falta o dono dizer quais casas refazer e quando; sugestão: série E, depois compactas, depois F02. Mexe no e-book, que estava fechado no rascunho 1. A [pesquisa de 22/11](ebook/referencias/pesquisa-layouts-e-etapas-da-obra.md) traz a régua federal (22 casas com banheiro estreito, contagem de antes da C01 nova) e 5 ideias para o dono escolher (seção 5).
- **Arquiteto registrado:** revisar as 24 plantas, começando pelas apertadas (E02, E03, suítes da E01, E05 e E07); decidir os banheiros abaixo de 1,10 m livres (18 casas, contagem de 22/11) e a nota de clima por zona bioclimática.
- **Calculadora do parceiro:** compartilhar a página com ele (menu Share). Os dados agora saem do validador; a página publicada precisa ser republicada.
- **OpenArt: só com o "sim" do dono a cada uso (22/11);** saldo em [`ORCAMENTO.md`](ORCAMENTO.md). O selo "Imagem ilustrativa" saiu dos vídeos (dono, 22/11) e continua em imagem parada. **Vídeo realista:** o dono filma com o celular em alguns dias; o Editor manda a lista de planos. Até lá o vídeo usa planta, 3D próprio (ilustração) e páginas do e-book.
- **Vídeos guardados (22/11):** assistir ao convite (`video/saida/convite/`, passeio pela F03, o último feito) e ao principal de 21/11 (`video/saida/principal/`); os outros foram apagados para refazer do zero. Dizer o que é "pagar por mais" e se libera o OpenArt para a versão realista.
- **Vídeo (aberto pelo dono em 21/11):** refazer do zero pelo plano de `contexto/dono/RETROSPECTIVA.md`; criar o Instagram e configurar a MinoAI Frontier no Mac.
- **Skill `make-pdf`:** em teste; o binário fica fora do repositório (`~/.cache/gstack`) e some quando a máquina é trocada ([`ECOSSISTEMA.md`](ECOSSISTEMA.md)).
- **Imagens 2D dos posts** estão desatualizadas para C03, E04, F02, F05, S03 e S09, e a C01 redesenhada: refazer quando a frente de animação abrir.
- Informar quanto resta do limite semanal (Configurações → Uso) para fechar o [orçamento](ORCAMENTO.md) em números.
- Atualizar o relatório jurídico com Caixa e Confea (pedido antes, sem resposta).

## Ferramentas: o que cada uma é (e o que não é)

- **Skills do Ponytail** (`/ponytail`, `/ponytail-review`, `/ponytail-audit`): só para o código das ferramentas. O texto que vai ao público é do Redator e do Revisor.
- **AgentScope** (ideias, não instalado) e **product-demo-agent-toolkit** (vídeo de página web; a proteção automática bloqueou: o dono libera com o modo "Accept edits"; não contorne): [`ECOSSISTEMA.md`](ECOSSISTEMA.md), seção 6.
- **Onde roda:** esta sessão roda na nuvem da Anthropic; servidor próprio não economiza token. O que economiza é ler pouco (o seu `contexto/<papel>.md` e o último resumo em `contexto/entregas/`) e usar o modelo certo para cada pedido ([`pedidos/LEIA-ME.md`](pedidos/LEIA-ME.md)).

## Mapa: onde está cada coisa

| Quero saber… | Abra |
|---|---|
| As regras que não mudam, o objetivo e o jeito de trabalhar | [`CLAUDE.md`](CLAUDE.md) |
| O que o dono acabou de pedir; onde está cada documento | [`contexto/QUADRO.md`](contexto/QUADRO.md), [`INDICE.md`](INDICE.md) |
| Como um pedido do dono vira trabalho, e qual modelo faz | [`pedidos/LEIA-ME.md`](pedidos/LEIA-ME.md) |
| Tudo o que o dono já pediu, pedido por pedido | [`CONTEXTO-HISTORICO.md`](CONTEXTO-HISTORICO.md) |
| Quem decide o quê (Conselho, Maestro, vetos) e como uma skill nova entra | [`CONSELHO.md`](CONSELHO.md), [`MAESTRO.md`](MAESTRO.md) |
| Tudo o que a operação pode usar (skills, plugins, conectores) e o prompt de cada um | [`ECOSSISTEMA.md`](ECOSSISTEMA.md) |
| O que cada agente precisa saber agora | [`contexto/`](contexto/) (um arquivo por papel, inclusive o Maestro) |
| O que a última tarefa deixou pronto e pendente | [`contexto/entregas/`](contexto/entregas/) |
| Estratégia, preço, funil, o que não prometer | [`ESTRATEGIA.md`](ESTRATEGIA.md) (seção 9: honestidade) |
| Custo por venda e números | [`PAINEL.md`](PAINEL.md), [`ORCAMENTO.md`](ORCAMENTO.md) |
| E-book: plano, gerador, 24 plantas, regras do arquiteto | [`ebook/EBOOK.md`](ebook/EBOOK.md), `ebook/plantas/`, `ebook/referencias/` |
| Animações 3D e OpenArt | [`animacoes-3d/ANIMACOES-3D.md`](animacoes-3d/ANIMACOES-3D.md), [`animacoes-3d/OPENART-MINOAI.md`](animacoes-3d/OPENART-MINOAI.md) |
| Vídeo e referência de edição | [`video/VIDEO.md`](video/VIDEO.md), [`video/REFERENCIA-CONDOR.md`](video/REFERENCIA-CONDOR.md) |
| Instagram e a edição pela MinoAI Frontier | [`instagram/INSTAGRAM.md`](instagram/INSTAGRAM.md), [`instagram/MINOAI-FRONTIER.md`](instagram/MINOAI-FRONTIER.md) |

## Passagem entre tarefas

Quando uma tarefa termina, quem fez escreve um resumo curto em [`contexto/entregas/`](contexto/entregas/) (modelo em `MODELO.md`). Quem pega a tarefa seguinte lê o resumo, não a conversa. O mais recente é o ponto de partida.
