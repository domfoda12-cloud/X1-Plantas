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
| "Continue trabalhando sem pedir permissão" (para tarefas internas) | Avançar sozinho no que é interno; decisões de dinheiro, título, preço e publicação continuam com o dono |

## Em aberto (esperando o dono)

- Dizer se instalo o toolkit de vídeo de demonstração (filma a calculadora e o leitor do e-book). A proteção automática bloqueou: precisa liberar a permissão ou rodar você mesmo `npx product-demo-agent-toolkit skills .claude/skills` na pasta do projeto.
- Arquiteto registrado decidir: banheiros com pelo menos 1,10 m livres (hoje 19 casas abaixo) e se o e-book ganha uma nota de clima por zona bioclimática (janela maior, veneziana e beiral na zona 8).
- Dizer se aplico as correções da revisão técnica (as 2 primeiras: calculadora do parceiro com dados velhos e promessas vetadas; `checar.py` que não pega página estourada).
- Assistir ao CONDOR XIII quadro a quadro no Mac (o YouTube bloqueia a nuvem), ou mandar 3 a 5 momentos favoritos com o minuto, para completar [`video/REFERENCIA-CONDOR.md`](video/REFERENCIA-CONDOR.md).
- Informar quanto resta do limite semanal (claude.ai, Configurações → Uso) para fechar o orçamento em números.

- Compartilhar a calculadora de lote com o parceiro (menu Share da página) para ele usar no WhatsApp.
- Os 5 vídeos de anúncio (`video/saida/v1` a `v5`) usam o 3D antigo da Casa Compacta: refazer quando o 3D for liberado.

- Testar a palavra do comentário "PLANTA" contra "LOTE" ([`ebook/referencias/concorrentes.md`](ebook/referencias/concorrentes.md)): "PLANTA" também é usada por criadores de jardinagem.

- Decidir se o e-book promete as próximas casas de graça (o texto só aparece se `promessa_atualizacao` for preenchido em `ebook/config.json`, porque oferta escrita obriga).

- Aprovar o plano do e-book (formato A4 de cerca de 60 páginas, capa "Que casa cabe no seu lote?", começar os passos 1 a 6).
- Título, preço, bônus, lançar com 12 ou 24 plantas, contato do parceiro.
- Arquiteto registrado para revisar as 24 plantas (o rascunho 1 já mostra medidas por fora e áreas por dentro; ele confere as casas apertadas que o validador marcou: E02, E03, suítes da E01, E05 e E07).
- Preencher no `ebook/config.json`: título, preço, bônus, WhatsApp do parceiro e, se quiser, `promessa_atualizacao`. São os únicos espaços reservados do rascunho 1 (página 61).
- Depois do rascunho 1: regenerar as imagens 2D dos posts e o 3D das casas que mudaram (C03, E04, F02, S09) quando a frente de animação abrir.
- Gravar o apresentador; criar o Instagram; configurar a MinoAI Frontier no Mac.
- Atualizar o relatório jurídico com Caixa e Confea (pedido antes, sem resposta).
- Reels 1 e 6 usam o vídeo 3D antigo da Casa Compacta: usar o B-roll do e-book ou esperar o 3D novo.

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
