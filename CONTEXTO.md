# Contexto do projeto: tudo o que o dono pediu, e o que cada pedido quer dizer

> **Resumo que todo mundo lê.** Cada pedido do dono tem um motivo e continua valendo até ele dizer o contrário. O histórico completo, pedido por pedido, está em [`CONTEXTO-HISTORICO.md`](CONTEXTO-HISTORICO.md): abra só se precisar de um detalhe antigo. Cada agente lê também o seu arquivo em [`contexto/`](contexto/). Regra em [`CLAUDE.md`](CLAUDE.md).

## O que nunca muda

| O dono disse | O que isso quer dizer |
|---|---|
| "O objetivo é a alegria do consumidor, e a alegria dele me mandar o Pix" | Toda entrega é julgada por duas coisas: o comprador fica feliz com o que recebe? Ele paga? |
| "Pensa como um marketeiro, público brasileiro" | Português do Brasil, R$, Pix, WhatsApp, quem constrói com pedreiro por etapas. Ver [persona](ebook/referencias/persona-e-mercado.md) |
| "Sempre do ponto de vista de um arquiteto profissional" | Toda planta passa pelo validador e explica o porquê de cada decisão |
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

- **E-book (para publicar):** preencher em `ebook/config.json` o título, o preço, os bônus, o WhatsApp do parceiro e, se quiser, `promessa_atualizacao` (prometer as próximas casas de graça é oferta que obriga). Decidir se lança com 12 ou 24 plantas.
- **Arquiteto registrado:** revisar as 24 plantas, começando pelas apertadas (E02, E03, suítes da E01, E05 e E07); decidir os banheiros abaixo de 1,10 m livres (19 casas) e a nota de clima por zona bioclimática.
- **Calculadora do parceiro:** compartilhar a página com ele (menu Share). Os dados agora saem do validador; a página publicada precisa ser republicada.
- **Toolkit de vídeo de demonstração:** a proteção automática bloqueou a instalação. Trocar o modo para "Accept edits" ou rodar `npx product-demo-agent-toolkit skills .claude/skills`.
- **Vídeo realista sem OpenArt (pedido em 21/11):** o motor próprio só chega a ilustração 3D. O dono escolhe o caminho: filmagem real dele, vídeo de banco gratuito, Blender (precisa liberar a instalação) ou recarregar o OpenArt.
- **Vídeo principal e prévia do WhatsApp (feitos em 21/11):** assistir aos dois (`video/saida/principal/` e `video/saida/previa-whatsapp/`) e dizer o que muda; escolher a palavra da chamada (PLANTA ou LOTE); pôr a música licenciada na edição da MinoAI Frontier, no Mac. **OpenArt liberado de novo** (dono recarregou, plano Pro, 21/11 à noite). Vídeo principal novo da E07 em `video/plano-principal-e07.md`: versão 2 pronta e aprovada pelo Revisor; **anúncio do e-book com locução (25 s):** o dono tirou o selo "Imagem ilustrativa" e mandou refazer a planta da E07 (os 3 quartos em fila são erro para ele). Esperando ele aprovar a planta nova e o plano do vídeo (`contexto/entregas/ULTIMO.md`); confirmar se o tio existe e se "volto em algumas semanas" é literal; escolher o logo em `marca/logo/`.
- **Vídeo (última frente):** os 5 anúncios e os reels 1 e 6 usam o 3D antigo da C01, refazer; assistir ao CONDOR XIII no Mac ou mandar 3 a 5 momentos com o minuto; gravar o apresentador, criar o Instagram e configurar a MinoAI Frontier no Mac; testar PLANTA contra LOTE como palavra do comentário.
- **Imagens 2D dos posts** estão desatualizadas para C03, E04, F02, F05, S03 e S09: refazer quando a frente de animação abrir.
- Informar quanto resta do limite semanal (Configurações → Uso) para fechar o orçamento em números.
- Atualizar o relatório jurídico com Caixa e Confea (pedido antes, sem resposta).

## Ferramentas: o que cada uma é (e o que não é)

- **Skills do Ponytail** (`/ponytail`, `/ponytail-review`, `/ponytail-audit`): só para o código das ferramentas. O texto que vai ao público é do Redator e do Revisor.
- **AgentScope:** não é skill do Claude Code. É uma biblioteca em Python para construir agentes próprios num servidor, pagos por token na API. Não foi instalado; só as ideias dele entraram (Conselho, roteiro, modelo por tarefa). Pode servir um dia para um agente de WhatsApp num servidor do dono.
- **product-demo-agent-toolkit:** grava vídeo de **página web** (calculadora do parceiro, leitor do e-book) com cursor humano, roteiro e locução. É da frente de vídeo. **Não instalado:** a proteção automática do Claude Code bloqueia pacote de terceiros que traz skills para o agente. Não contorne; o dono libera trocando o modo da sessão para "Accept edits" ou instalando ele mesmo.
- **Onde roda:** esta sessão roda na nuvem da Anthropic; servidor próprio não economiza token. O que economiza é ler pouco (o seu `contexto/<papel>.md` e o último resumo em `contexto/entregas/`) e usar o modelo certo (Opus para decidir e revisar, Sonnet para o rotineiro, Fable para o que é muito difícil).

## Mapa: onde está cada coisa

| Quero saber… | Abra |
|---|---|
| As regras que não mudam, o objetivo e o jeito de trabalhar | [`CLAUDE.md`](CLAUDE.md) |
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

Nada foi apagado do histórico: o `CONTEXTO.md` antigo está inteiro em `CONTEXTO-HISTORICO.md` e no git.

## Passagem entre tarefas

Quando uma tarefa termina, quem fez escreve um resumo curto em [`contexto/entregas/`](contexto/entregas/) (modelo em `MODELO.md`). Quem pega a tarefa seguinte lê o resumo, não a conversa. O mais recente é o ponto de partida.
