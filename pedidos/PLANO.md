# Plano de trabalho: o que a equipe faz, em que ordem, e para quê

> Pedido do dono (22/11/2026): "sempre dê um objetivo à equipe; um plano passo a passo, separado em tarefas grandes e pequenas, entre os agentes". Quem mantém: o Maestro (a conversa principal). Toda tarefa daqui vira ou já é ficha em `pedidos/`; ao terminar uma, marque **feito** e atualize o "Agora" do [quadro](../contexto/QUADRO.md). Os papéis estão em [`contexto/EQUIPE.md`](../contexto/EQUIPE.md).

## O objetivo da equipe

**O comprador acha a casa que cabe no lote dele, entende por quê e se sente seguro para construir, e por isso manda o Pix.** Toda tarefa abaixo diz que parte desse objetivo ela move. O número que manda: o custo por venda ([`PAINEL.md`](../PAINEL.md), seção 4).

**G** = tarefa grande (vários agentes ou várias horas; precisa de ficha com plano). **P** = tarefa pequena (um agente, um arquivo ou uma conferência). **Dono** = só ele decide; o resto continua enquanto ele não responde.

## Fase 1 · Organizar a base (ficha `1529-organizar-os-arquivos`)

*Objetivo: cada agente acha o que precisa lendo pouco, para gastar menos token em toda tarefa daqui para frente.*

| # | Tipo | Tarefa | Quem | Pronto quando |
|---|---|---|---|---|
| 1.1 | G | Juntar documentos lidos juntos | Maestro | **Feito** (22/11): 138 → 100 documentos, 0 link quebrado |
| 1.2 | P | Código repetido | Maestro | **Feito** (22/11): medido; 12 a 24 linhas nos `render-*.cjs` e uma linha de caminho por programa. Juntar acrescentaria mais código do que tira: fica como está |
| 1.3 | P | Cada `contexto/<papel>.md` aponta no máximo 3 resumos | Maestro | **Feito** (22/11): 5 contextos cortados; o `checar.py` agora confere |
| 1.4 | P | Medir o Graphify antes e depois | Maestro | **Feito** (22/11): 2.013 → 1.781 círculos, 2.231 → 2.012 ligações (cerca de 10% menos). Metade só cortando conteúdo repetido: vai para a fase 2 |
| 1.5 | P | Auditoria das fichas fechadas | `supervisor` (Fable) | quando fechar a 3ª ficha desde a última (agora: 2); erro alto corrigido antes de seguir |

## Fase 2 · O plano mestre da equipe (ficha `1944-plano-mestre`)

*Objetivo: a equipe mostra que entendeu o projeto sozinha, e o sistema passa a se melhorar sem o dono pedir.*

| # | Tipo | Tarefa | Quem | Pronto quando |
|---|---|---|---|---|
| 2.1 | P | Enquadrar: objetivo, o que ler na `main`, liberdade total de pensamento | Maestro | pedido aberto escrito na ficha |
| 2.2 | G | Rodada 1: cada papel propõe o plano que acha óbvio | `estrategista`, `arquiteto`, `redator`, `designer`, `editor-video` (com o Diretor), `revisor-de-risco` | 6 propostas na ficha |
| 2.3 | G | Rodada 2: cada um lê as outras e critica | os mesmos 6 | críticas na ficha |
| 2.4 | P | Juntar num plano só e conferir contra o contexto | Maestro; `supervisor` confere | este arquivo atualizado com o que mudou |
| 2.5 | Dono | O plano bate com o que ele quer? | dono | "sim" ou correção |
| 2.5b | G | Cortar o conteúdo repetido entre documentos (o que reduz o Graphify pela metade) | os agentes de cada pasta, no Opus; Maestro confere | nada perdido; números de antes e depois |
| 2.6 | P | Rotina de melhoria: a cada 3 fichas fechadas, até 6 chamadas | Maestro | regra em `pedidos/LEIA-ME.md` |

## Fase 3 · E-book: as casas refeitas (frente atual)

*Objetivo: cada casa faz sentido para quem vai morar (arranjo antes da medida), e o comprador confia no que vê.*

| # | Tipo | Tarefa | Quem | Pronto quando |
|---|---|---|---|---|
| 3.1 | G | E07 redesenhada: quartos fora de fila, 72 m², 3 quartos, 1 suíte, lote 8 m (ficha `1616`) | `arquiteto` (Opus) | passa no validador; prévia mobiliada; E07 do e-book intacta |
| 3.2 | P | Conferir a proposta | Maestro | validador, prévia aberta e olhada |
| 3.3 | Dono | Aprova a E07 e diz quais casas refazer e em que ordem (sugestão: série E, compactas, F02) | dono | resposta na ficha |
| 3.4 | G | Refazer as casas, **uma por vez**, na ordem dele | `arquiteto`; Maestro confere cada uma | validador + prévia + "sim" do dono por casa |
| 3.5 | P | Cada casa aprovada: imagem 3D, páginas e ficha refeitas | `designer` (com o Diretor) | `checar.py`, páginas sem estouro |
| 3.6 | P | Cada casa aprovada: textos da casa | `redator`; `revisor-de-risco` no Fable | texto com atributo e número da ficha; SIM do Revisor |
| 3.7 | Dono | Título, preço, garantia, bônus, 12 ou 24 casas, WhatsApp do parceiro | dono | `ebook/config.json` preenchido |
| 3.8 | G | PDF final na melhor qualidade | Maestro; Revisor (Fable) lê inteiro | PDF sem campo pendente; `checar.py` sem aviso |

## Fase 4 · Animações e imagens (abre só quando a fase 3 fechar)

*Objetivo: a imagem faz o comprador querer a casa e é verdadeira com a planta.*

| # | Tipo | Tarefa | Quem | Pronto quando |
|---|---|---|---|---|
| 4.1 | G | Imagens 2D e 3D dos posts com as plantas novas | `designer` (ideia do Diretor) | batem com a planta; Arquiteto confere |
| 4.2 | G | Carrossel de cada casa | `designer` + `redator` + `revisor-de-risco` (Fable) | peça pronta; "sim" do dono para publicar |
| 4.3 | Dono | Fotos realistas no OpenArt (gasta crédito) | dono | "sim" com resumo e custo |

## Fase 5 · Vídeo

*Objetivo: segurar os 3 primeiros segundos e levar ao comentário e ao WhatsApp.*

| # | Tipo | Tarefa | Quem | Pronto quando |
|---|---|---|---|---|
| 5.1 | P | Lista de planos para o dono filmar com o celular | `editor-video` (ideia do Diretor) | lista curta, plano por plano |
| 5.2 | G | Anúncio com a voz do dono, com a casa nova | `editor-video` + `redator` + `revisor-de-risco` (Fable) | resumo e custo aprovados antes; vídeo aprovado depois |
| 5.3 | G | Convite e principal refeitos | `editor-video` | idem |
| 5.4 | Dono | Criar o Instagram; MinoAI no Mac; PLANTA ou LOTE | dono | feito por ele |

## Sempre, em toda fase

- Antes de cada tarefa: a ficha diz o objetivo e o que cada agente acrescenta; o "Agora" do quadro é atualizado.
- Erro achado vira regra ou conferência no `checar.py` (`pedidos/LEIA-ME.md`, "Consertar de vez").
- Antes da web: `python3 ferramentas/pesquisa.py buscar`.
- Depois de cada tarefa: `checar.py`, painel, resumo de passagem, commit e push na `main`.
