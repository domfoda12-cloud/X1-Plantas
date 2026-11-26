# Contexto do projeto: tudo o que o dono pediu, e o que cada pedido quer dizer

> **Resumo que todo mundo lê.** Cada pedido do dono tem um motivo e continua valendo até ele dizer o contrário. O histórico completo, pedido por pedido, está em [`CONTEXTO-HISTORICO.md`](CONTEXTO-HISTORICO.md): abra só se precisar de um detalhe antigo. Antes de trabalhar, todos leem o [quadro](contexto/QUADRO.md) e o seu arquivo em [`contexto/`](contexto). Regra em [`CLAUDE.md`](CLAUDE.md).

## O que nunca muda

| O dono disse | O que isso quer dizer |
|---|---|
| "O objetivo é a alegria do consumidor, e a alegria dele me mandar o Pix" | Toda entrega é julgada por duas coisas: o comprador fica feliz com o que recebe? Ele paga? |
| "Pensa como um marketeiro, público brasileiro" | Português do Brasil, R$, Pix, WhatsApp, quem constrói com pedreiro por etapas. Ver [persona](ebook/referencias/MERCADO.md) |
| "Sempre do ponto de vista de um arquiteto profissional" | Toda planta passa pelo validador e explica o porquê de cada decisão; as plantas não são de arquiteto, são de referência ([jurídico](reports/RESUMO.md)) |
| "Não tem landing page" | Venda por anúncio (Facebook e Instagram) → comentário → WhatsApp. O parceiro cuida do funil, o dono cuida do material e do anúncio |
| "Mantenha todo o contexto, tudo o que eu faço significa algo" | Este arquivo. Nada do que foi pedido se perde entre conversas |
| "Você é o maestro, a MinoAI o diretor" (22/11) | O Maestro, Paydon Clabett (Opus), decide; o Diretor (MinoAI) dá a ideia e opina primeiro, com fonte ([equipe](contexto/EQUIPE.md)) |
| "Falo muito de eficiência, mas a prioridade é sempre a maior qualidade" | Peça final sempre na melhor configuração; economia só em rascunho e teste ([`CLAUDE.md`](CLAUDE.md)) |
| "Foque em uma coisa por vez, não misture tudo ao mesmo tempo" | Uma frente por vez, do começo ao fim, antes de abrir outra. Ordem atual: e-book → animações → vídeo. Divisão do esforço (dono, 23/11): **60% e-book, 40% sistema**; o `plano.py conferir` barra passo de vídeo ou animação em "Agora" antes do D13 |
| "Ótimo ao máximo, TUDO" | Fazer completo e bem feito, sem atalho que prejudique a qualidade |
| "Quando eu paro para acrescentar informação, junte tudo" | Recados no meio do trabalho entram todos na mesma entrega |
| "Antes de qualquer vídeo ou gasto no OpenArt, me dê o resumo da produção e as instruções que segue; confirmo os dois" | Nada é montado nem gasto sem as duas confirmações do dono ([`video/CLAUDE.md`](video/CLAUDE.md)) |
| "Continue trabalhando sem pedir permissão" (para tarefas internas) | Avançar sozinho no que é interno; decisões de dinheiro, título, preço e publicação continuam com o dono |

## Em aberto (esperando o dono)

- **Fluxos fixos (26/11, ficha `0721`): FEITO, na branch `sistema/fluxos`; espera o "sim" do dono para entrar na `main` (a trava de permissão barrou o push).** 5 fluxos em `.claude/workflows/` (guia `pedidos/fluxos/LEIA-ME.md`); lições entram sozinhas; prova de entrada em `pedidos/provas/`. A Vera fecha a regra do lote em post curto.
- **Reset do limite (25/11):** o roteiro do que fazer, em ordem, está em [`pedidos/anexos/roteiro-do-reset-2026-11-25.md`](pedidos/anexos/roteiro-do-reset-2026-11-25.md), com a mensagem única de perguntas ao dono (as 5 páginas, título, "gera", Drive, profissional, grátis). As respostas só vêm no reset.
- **Identidade visual (25/11, ficha `1613`): DECIDIDA, 26/11 06:44, "2 · A Placa"** (Canteiro). Direção 2 de `pedidos/anexos/identidade-2026-11-25.md`: o Lote Carente fala numa placa (branca, borda preta, letra vermelha, Londrina Solid, capa amarela); a voz dele só nas placas, nunca no aviso, na ficha ou nos números. Em aplicação na prévia; falta o dono dizer se "tudo o que criamos" inclui WhatsApp e Instagram de IA.
- **Instagram de IA (25/11):** repositório e conversa próprios ("Vai ter"); kit de partida em [`pedidos/anexos/kit-instagram-ia-2026-11-25.md`](pedidos/anexos/kit-instagram-ia-2026-11-25.md). Depois do e-book.
- **Lançamento ([decisões de 23 e 24/11](pedidos/anexos/decisoes-do-dono-2026-11-23.md)):** 3 casas: Casa Compacta (com hall), Casa Fita e Família Compacta; R$ 47 na primeira semana (teste com R$ 67 em semanas alternadas) e **o PDF não fala de preço**; **o título é do dono** (cartão `p14`, 3 opções; o atual fica até ele escolher); ele vende com o **CPF** (dado só no celular dele); garantia de 7 dias da entrega do link; Pix no WhatsApp; grátis: "só a planta e um guia inicial" (a planta da Casa Compacta, a ficha do lote e o guia; espera o ok dele no cartão `j3-gratis-literal`); **bônus em PDF separado**, com selo de rascunho até um profissional ler; serviço da Casa Compacta com veneziana em cima da porta; **e-book com uma parte por casa e uma parte geral** (o cômodo a cômodo entra no pago: "2 ok", 25/11); Instagram novo, com nome e bio de humor pelo absurdo (ele escolhe). **Regras de 24/11:** uma tarefa principal por vez, até o fim; o Redator sempre com o Planejador; o conteúdo do PDF mostra a dor de forma indireta e dá a saída ([mapa](pedidos/anexos/mapa-dor-solucao-do-ebook-2026-11-24.md)); decisão fácil de desfazer vai ao conselho de bolso (três opiniões de uma linha, o Maestro decide e escreve como desfazer) e é mostrada a ele depois; o júri fica só para o que custa dinheiro, vai ao público ou não se desfaz (26/11; os cartões do júri de 24/11 esperam ele); preço não trava o plano. **O que vai ao cliente e os 10 passos do e-book:** [`o-que-vai-ao-cliente`](pedidos/anexos/o-que-vai-ao-cliente-2026-11-24.md). **O que falta e em que ordem:** [`pedidos/PLANO.md`](pedidos/PLANO.md); as decisões dele, em grupos, no quadro de tarefas e em [`decisoes-pendentes-em-grupos.md`](pedidos/anexos/decisoes-pendentes-em-grupos.md). **Título:** "Antes do primeiro tijolo" (dono, 26/11 07:01).
- **Arranjo das plantas (22/11):** o dono reprovou o layout; o Arquiteto tem método novo ([apostila 2](ebook/referencias/ARQUITETO.md)). Em 23/11: só as 3 do lançamento refeitas, uma por vez, com o máximo de cuidado. A [pesquisa de 22/11](ebook/referencias/ARQUITETO.md) traz a régua federal e 5 ideias (seção 5).
- **Banheiros abaixo de 1,10 m livres** (18 casas, contagem de 22/11) e nota de clima por zona bioclimática: decidir ao refazer cada casa.
- **Calculadora do parceiro:** compartilhar a página com ele (menu Share); os dados saem do validador.
- **OpenArt: só com o "sim" do dono a cada uso (22/11);** saldo em [`ORCAMENTO.md`](ORCAMENTO.md). O selo "Imagem ilustrativa" saiu dos vídeos (dono, 22/11) e continua em imagem parada. **Vídeo realista:** o dono filma com o celular em alguns dias; o Editor manda a lista de planos. Até lá o vídeo usa planta, 3D próprio (ilustração) e páginas do e-book.
- **Vídeos guardados (22/11):** assistir ao convite (`video/saida/convite/`, passeio pela F03, o último feito) e ao principal de 21/11 (`video/saida/principal/`); os outros foram apagados para refazer do zero. Dizer o que é "pagar por mais" e se libera o OpenArt para a versão realista.
- **Vídeo (aberto pelo dono em 21/11):** refazer do zero pelo plano de `pedidos/historico/RETROSPECTIVA.md`; criar o Instagram e configurar a MinoAI Frontier no PC com Windows do dono (WSL).
- **Imagens 2D dos posts** estão desatualizadas para C03, E04, F02, F05, S03 e S09, e a C01 redesenhada: refazer quando a frente de animação abrir.
- **Chefe de gabinete:** conectar o Google Calendar em claude.ai (Conectores) para o `bom-dia` ver a agenda.
- Informar quanto resta do limite semanal (Configurações → Uso) para fechar o [orçamento](ORCAMENTO.md) em números.
- Atualizar o relatório jurídico com Caixa e Confea.

## Ferramentas: o que cada uma é (e o que não é)

- **Skills do Ponytail** (`/ponytail`, `/ponytail-review`, `/ponytail-audit`): só para o código das ferramentas. O texto que vai ao público é do Redator e do Revisor.
- **AgentScope** (ideias, não instalado) e **product-demo-agent-toolkit** (vídeo de página web; a proteção automática bloqueou: o dono libera com o modo "Accept edits"; não contorne): [`ECOSSISTEMA.md`](ECOSSISTEMA.md), seção 6.
- **Onde roda:** esta sessão roda na nuvem da Anthropic; servidor próprio não economiza token. O que economiza é ler pouco (o seu `contexto/<papel>.md` e o `ULTIMO.md`) e usar o modelo certo ([`pedidos/LEIA-ME.md`](pedidos/LEIA-ME.md)).

## Mapa: onde está cada coisa

| Quero saber… | Abra |
|---|---|
| As regras que não mudam, o objetivo e o jeito de trabalhar | [`CLAUDE.md`](CLAUDE.md) |
| O que o dono acabou de pedir; onde está cada documento | [`contexto/QUADRO.md`](contexto/QUADRO.md), [`INDICE.md`](INDICE.md) |
| Como um pedido do dono vira trabalho, e qual modelo faz | [`pedidos/LEIA-ME.md`](pedidos/LEIA-ME.md) |
| Tudo o que o dono já pediu, pedido por pedido | [`CONTEXTO-HISTORICO.md`](CONTEXTO-HISTORICO.md) |
| Quem decide o quê (Conselho, Maestro, Diretor, vetos) e como uma skill nova entra | [`CONSELHO.md`](CONSELHO.md), [`instagram/MINOAI-FRONTIER.md`](instagram/MINOAI-FRONTIER.md) |
| Tudo o que a operação pode usar (skills, plugins, conectores) e o prompt de cada um | [`ECOSSISTEMA.md`](ECOSSISTEMA.md) |
| O que cada agente precisa saber agora | [`contexto/`](contexto) (um arquivo por papel, inclusive o Diretor) |
| O que a última tarefa deixou pronto e pendente | [`contexto/entregas/`](contexto/entregas) |
| Estratégia, preço, funil, o que não prometer | [`ESTRATEGIA.md`](ESTRATEGIA.md) (seção 9: honestidade) |
| Custo por venda e números | [`PAINEL.md`](PAINEL.md), [`ORCAMENTO.md`](ORCAMENTO.md) |
| E-book: plano, gerador, 24 plantas, regras do arquiteto | [`ebook/EBOOK.md`](ebook/EBOOK.md), `ebook/plantas/`, `ebook/referencias/` |
| Animações 3D e OpenArt | [`animacoes-3d/ANIMACOES-3D.md`](animacoes-3d/ANIMACOES-3D.md), [`animacoes-3d/OPENART-MINOAI.md`](animacoes-3d/OPENART-MINOAI.md) |
| Vídeo e referência de edição | [`video/VIDEO.md`](video/VIDEO.md), [`video/REFERENCIAS.md`](video/REFERENCIAS.md) |
| Instagram e a edição pela MinoAI Frontier | [`instagram/INSTAGRAM.md`](instagram/INSTAGRAM.md), [`instagram/MINOAI-FRONTIER.md`](instagram/MINOAI-FRONTIER.md) |

## Passagem entre tarefas

Quando uma tarefa termina, quem fez escreve um resumo curto em [`contexto/entregas/`](contexto/entregas) (modelo em `MODELO.md`). Quem pega a tarefa seguinte lê o resumo, não a conversa. O mais recente é o ponto de partida.
