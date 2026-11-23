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
| 1.4 | P | Medir o Graphify antes e depois | Maestro | **Feito** (22/11): 2.013 → 1.781 círculos, 2.231 → 2.012 ligações (medido no commit 1af9f47; no 2bb0773, 1.846 e 2.038: uns 8% menos, porque cada documento novo de sistema sobe o número). Metade só cortando conteúdo repetido: vai para a fase 2 |
| 1.5 | P | Auditoria das fichas fechadas | `supervisor` (Fable) | **Feito** (22/11): auditoria 3, 0 alta, 13 médias, 8 baixas; corrigidas, lista em `AUDITORIAS.md` |

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
| 3.1 | G | E07 redesenhada: quartos fora de fila, mantendo **se possível** 72 m², 3 quartos, 1 suíte, 2 banheiros e lote de 8 m (ficha `1616`) | `arquiteto` (Opus) | passa no validador; prévia mobiliada; E07 do e-book intacta |
| 3.2 | P | Conferir a proposta | Maestro | validador, prévia aberta e olhada |
| 3.3 | Dono | Aprova a E07 e diz quais casas refazer e em que ordem (sugestão: série E, compactas, F02) | dono | resposta na ficha |
| 3.4 | G | Refazer as casas, **uma por vez**, na ordem dele | `arquiteto`; Maestro confere cada uma | validador + prévia + "sim" do dono por casa |
| 3.5 | P | Cada casa aprovada: imagem 3D, páginas e ficha refeitas | `designer` (com o Diretor) | `checar.py`, páginas sem estouro |
| 3.6 | P | Cada casa aprovada: textos da casa | `redator`; `arquiteto` confere os números; `revisor-de-risco` no Fable | texto com atributo e número da ficha; SIM do Revisor |
| 3.6b | Dono | Arquiteto registrado revisa as plantas antes de vender, começando pelas apertadas (E02, E03, suítes da E01, E05, E07) | dono contrata | parecer na ficha |
| 3.7 | Dono | Título, preço, garantia, bônus, 12 ou 24 casas, WhatsApp do parceiro | dono | `ebook/config.json` preenchido |
| 3.8 | G | PDF final na melhor qualidade | Maestro; Revisor (Fable) lê inteiro | PDF sem campo pendente; `checar.py` sem aviso |

## Fase 4 · Animações e imagens (abre só quando a fase 3 fechar)

*Objetivo: a imagem faz o comprador querer a casa e é verdadeira com a planta.*

| # | Tipo | Tarefa | Quem | Pronto quando |
|---|---|---|---|---|
| 4.1 | G | Imagens 2D e 3D dos posts com as plantas novas | `designer` (ideia do Diretor) | batem com a planta; Arquiteto confere |
| 4.2 | G | Carrossel de cada casa | `designer` + `redator` + `arquiteto` + `revisor-de-risco` (Fable) | peça pronta; "sim" do dono para publicar |
| 4.3 | Dono | Fotos realistas no OpenArt (gasta crédito) | dono | "sim" com resumo e custo |

## Fase 5 · Vídeo

*Objetivo: segurar os 3 primeiros segundos e levar ao comentário e ao WhatsApp.*

| # | Tipo | Tarefa | Quem | Pronto quando |
|---|---|---|---|---|
| 5.1 | P | Lista de planos para o dono filmar com o celular | `editor-video` (ideia do Diretor) | lista curta, plano por plano |
| 5.2 | G | Anúncio com a voz do dono, com a casa nova | `editor-video` + `redator` + `arquiteto` + `revisor-de-risco` (Fable) | resumo e custo aprovados antes; vídeo aprovado depois |
| 5.3 | G | Convite e principal refeitos | `editor-video` | idem |
| 5.4 | Dono | Criar o Instagram; MinoAI no PC (Windows); PLANTA ou LOTE | dono | feito por ele |
| 5.5 | G | Meme recriado e POV do caramelo (ficha `2055-video-reel`, plano vetado pelo time e pelo Fable) | `editor-video` e equipe | ver a ficha |

A lista de planos para o dono filmar (5.1) pode sair antes, se ele quiser filmar logo: pergunta a ele.

## Fase 6 · Vender e medir (o objetivo é o Pix)

*Objetivo: cada real de anúncio volta como venda; o custo por venda cai.*

| # | Tipo | Tarefa | Quem | Pronto quando |
|---|---|---|---|---|
| 6.1 | G | Funil refeito com as casas novas: planta grátis, tabela do WhatsApp, calculadora do parceiro (republicada) | `redator` + `estrategista` + `arquiteto`; `revisor-de-risco` (Fable) | parceiro com o material novo |
| 6.2 | P | Relatório jurídico atualizado com Caixa e Confea | `pesquisador` acha; `revisor-de-risco` conclui | relatório em `reports/` |
| 6.3 | Dono | Verba do primeiro anúncio e do teste A/B | dono | valor e prazo |
| 6.4 | G | Primeiro anúncio no ar e medido: custo por contato, conversão do parceiro, custo por venda | `estrategista` | números no `PAINEL.md`, seção 4, só os que a ferramenta devolveu |

## Tempo livre: deixar a equipe mais inteligente (dono, 22/11/2026)

*Quando não há tarefa concreta (a fila espera o dono, ou nada aberto dá para fazer), o Maestro **alterna** (dono, 22/11/2026: "uma mistura"): uma tarefa da equipe (L), depois uma do projeto (M), e assim por diante. Uma por vez, até 6 chamadas de agente, nada pago, nada publicado. No fim, conta ao dono o que melhorou, com número quando houver. Melhoria do projeto que muda planta, texto público ou preço vira **proposta** para o dono, não mudança.*

| # | Tarefa | O que deixa mais inteligente | Pronto quando |
|---|---|---|---|
| L1 | Cada agente confirma que vê as suas ferramentas (web, MinoAI, caderno); vale já, não espera a próxima conversa | sem isso, os outros passos não valem | uma linha por agente na ficha `2041-tempo-livre` |
| L2 | Lições: cada erro de auditoria e cada correção do dono vira uma linha em "Lições" do `contexto/<papel>.md` e, se der, uma conferência no `checar.py` | errar menos: o agente lembra do erro de ontem | lições em dia com `AUDITORIAS.md` |
| L3 | Teste da equipe com o pedido da próxima fase (ex.: "refaça a E07"), 3 ou 4 agentes; corrigir o que sair confuso | entender melhor | contradições achadas e corrigidas |
| L4 | Afiar o método de um papel por vez: o `pesquisador` busca a melhor prática (com fonte, no caderno), o papel propõe, o Maestro decide; em conteúdo, o Diretor (MinoAI) opina primeiro | saber mais | uma regra nova no agente, com fonte |
| L5 | Cortar conteúdo repetido entre documentos (tarefa 2.5b), uma pasta por vez | ler menos | números de antes e depois |
| L6 | Medir o gasto: tokens por chamada de cada agente (o aviso de cada agente traz o número) e o que encarece | gastar menos | tabela na ficha; a lista de ferramentas mais cara revista |

**Do projeto (M)**

| # | Tarefa | O que melhora | Pronto quando |
|---|---|---|---|
| M1 | `plantas.py validar` nas 24: a casa com mais avisos ganha proposta do `arquiteto` | a casa que o comprador recebe | proposta na ficha; o dono decide |
| M2 | `/ponytail-audit` no código das ferramentas (só relatório) | menos erro e menos código | achados por gravidade; os altos viram ficha |
| M3 | `revisor-de-risco` relê os textos que já estão prontos para o público (`contexto/dono/TEXTOS-DESATUALIZADOS.md`, posts, WhatsApp) | menos risco | promessas sem lastro listadas, com a correção |
| M4 | `redator` e `estrategista` conferem o funil (anúncio, comentário, WhatsApp) contra as decisões mais novas | mais venda | o que está velho, com a proposta |
| M5 | `designer` olha as páginas do PDF de rascunho (`livro.py --previa`) em busca do que parece genérico | o comprador confia no que vê | páginas apontadas, com o porquê |
| M6 | Conferir o `PAINEL.md`: todo número tem fonte e data | decisões com número certo | número sem fonte apontado |

## Sempre, em toda fase

- Antes de cada tarefa: a ficha diz o objetivo e o que cada agente acrescenta; o "Agora" do quadro é atualizado.
- Erro achado vira regra ou conferência no `checar.py` (`pedidos/LEIA-ME.md`, "Consertar de vez").
- Antes da web: `python3 ferramentas/pesquisa.py buscar`.
- Depois de cada tarefa: `checar.py`, painel, resumo de passagem, **marcar "Feito" aqui**, commit e push na `main`.
