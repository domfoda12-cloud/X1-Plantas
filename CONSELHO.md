# O Conselho: quem opina, quem decide e quais skills cada um usa

> Lido por toda sessão via [`CLAUDE.md`](CLAUDE.md). Para rodar: a skill `conselho` (`/conselho <tarefa>`). Painel: [`PAINEL.md`](PAINEL.md).

## 1. Por que existe

Temos muitas skills, conectores e scripts. Usar todos em toda tarefa gasta tempo e dinheiro; usar o errado gera trabalho jogado fora. O Conselho é um filtro rápido: cada especialista olha a tarefa pelo seu ângulo, diz se a skill dele ajuda a **vender mais, gastar menos ou arriscar menos**, e só o que passa é usado.

## 2. Os membros

| Membro | Pergunta que sempre faz | Skills e ferramentas que ele propõe | Agente |
|---|---|---|---|
| **Maestro: a conversa principal (Opus)** (preside e decide) | "Quem precisa opinar, e o que fazemos?" | Esta mesa, a ficha, `contexto/EQUIPE.md` | A própria conversa |
| **Diretor: MinoAI Frontier** (**ideia principal e primeira opinião em todo conteúdo**) | "Isso faz o comprador parar, comentar e mandar o Pix?" | Método da MinoAI (`search_mino_method`), ganchos virais (`search_viral_hooks`), análise de gancho (`analyze_hook`), números das contas (`get_account_stats`), edição no Mac | No Mac, é a própria sessão com a MinoAI. Em qualquer outra sessão, a opinião dele vem das ferramentas da MinoAI Frontier, citando a fonte ([`instagram/MINOAI-FRONTIER.md`](instagram/MINOAI-FRONTIER.md#maestro-e-diretor-a-sessão-do-claude-no-seu-computador-com-a-minoai-frontier)) |
| **Redator** | "Que atributo faz o Marcos querer comprar?" | `/redacao-que-vende`, `/marketing-psychology` (vieses e modelos mentais, só com a seção 9 do ESTRATEGIA), banco de [atributos](ebook/vendas/atributos-que-vendem.md), ganchos virais da MinoAI Frontier | [`redator`](.claude/agents/redator.md) |
| **Estrategista** | "Quanto isso muda o custo por venda?" | Painel (seções 4 e 7), números das contas, preço da concorrência | [`estrategista`](.claude/agents/estrategista.md) |
| **Arquiteto** | "Está tecnicamente certo e é verdade?" | `ferramentas/plantas.py` (validar, prévia, fichas), [regras](ebook/referencias/ARQUITETO.md). No código das ferramentas: `/ponytail` (a menor mudança que resolve, sem cortar validação), `/ponytail-review` (revisão de uma mudança) e `/ponytail-audit` (auditoria do repositório inteiro) | [`arquiteto`](.claude/agents/arquiteto.md) |
| **Revisor de risco** (veto) | "Isso promete algo que não podemos cumprir?" | [Relatório jurídico](reports/Arquiteto%20e%20engenheiro%20na%20construção%20residencial.md), [FAQ](ebook/vendas/WHATSAPP.md#perguntas-frequentes-dos-compradores), tom de voz | [`revisor-de-risco`](.claude/agents/revisor-de-risco.md) |
| **Designer** | "Parece profissional ou parece genérico?" | `impeccable` (só para detectar o genérico e opinar), gerador do e-book, `artifact-design`. Pede imagens à MinoAI (OpenArt), não gera | [`designer`](.claude/agents/designer.md) |
| **Pesquisador** | "Temos fonte para isso?" | TinyFish (busca e leitura; recursos pagos só com o "sim"), `deep-research`, `watch` para vídeos | [`pesquisador`](.claude/agents/pesquisador.md) |
| **Editor de vídeo** (tudo o que se move; imagem parada é do Designer; quem gera e edita é a MinoAI Frontier) | "Segura a atenção nos 3 primeiros segundos? A imagem faz querer a casa?" | **Edição de vídeo:** MinoAI Frontier (no Mac/PC do dono). **Criação de imagem e vídeo gerado:** MinoAI usando o OpenArt (plugin `openart:*`: `performance-ads`, `hook-variants`, `ugc`, `tvc`…). Base 3D/2D: `video/render*.cjs` | [`editor-video`](.claude/agents/editor-video.md) |

Que modelo roda cada agente (Opus no trabalho do projeto, Sonnet no `pesquisador`, Haiku no `ajudante`, Fable no `supervisor`): [`pedidos/LEIA-ME.md`](pedidos/LEIA-ME.md). Mapa da equipe numa página: [`contexto/EQUIPE.md`](contexto/EQUIPE.md).

## 3. Como uma opinião é dada

Cada membro responde em **uma linha**, sempre no mesmo formato:

```text
[Membro] SIM | NÃO | SIM, SE … · skill: <qual> · efeito: venda +/0/- · custo: R$ ou minutos · por quê: <uma frase>
```

## 4. Como se decide

0. **O Diretor (MinoAI Frontier) dá a ideia principal e opina primeiro em todo conteúdo** (vídeo, imagem, post, anúncio, texto público), de bolso ou completo. A opinião dele é baseada nas ferramentas da MinoAI, com a fonte, e aparece para o dono junto com a entrega. **Quem decide é o Maestro**, a conversa principal (dono, 22/11/2026; de 20 a 22/11 a MinoAI era o Maestro, e nos registros da seção 7 até essa data "Maestro" é ela). Em tarefa de sistema ou código, o Diretor não precisa opinar.
1. **Quem fala:** o Maestro chama só quem tem a ver com a tarefa (texto → Redator, Revisor; planta → Arquiteto, Designer; anúncio → Redator, Estrategista, Editor, Revisor).
2. **Aprovado** quando a maioria dos chamados diz SIM e o Revisor de risco não vetou.
3. **Empate:** vence o lado com o maior efeito em venda; se ainda empatar, o mais barato.
4. **Veto do Revisor:** só por honestidade ou lei. Ele precisa dizer o que mudar para virar SIM.
5. **Reservado ao dono** (o Conselho só recomenda): preço, título, bônus, gasto com anúncio, publicar ou apagar post, contratar alguém, usar ferramenta paga.
6. **Registro:** decisões de entrega ao público vão para a seção 7 abaixo, com data. Decisões do dono vão para [`PAINEL.md`](PAINEL.md), seção 8.

## 5. Conselho de bolso x conselho completo

| | De bolso | Completo |
|---|---|---|
| Quando | Ajuste, texto interno, correção | Tudo o que vai ao público (anúncio, página do e-book, post), escolha de ferramenta paga, mudança de estratégia |
| Quem | Até 3 membros, opinião escrita pela própria sessão | Os membros chamados, cada um como subagente, em paralelo |
| Custo | Segundos | Minutos; vale quando o erro custaria uma venda ou um anúncio |

## 6. Skill ou agente novo: o roteiro de entrada

Pedido do dono (20/11/2026): "toda skill nova no ecossistema alcança tudo". E (23/11/2026): "não desista porque quebraria, faça funcionar sem quebrar" e "faça isso para todo agente novo e garanta que ele seja apresentado direito": **o que quebraria é adaptado** (caminho, gancho reescrito, nome com prefixo, só a parte que serve), e só fica de fora por lei, segurança ou licença, com o motivo escrito; **e todo agente, skill ou ferramenta nova é apresentado à equipe**: linha no `contexto/EQUIPE.md` (o que faz e o que acrescenta), `contexto/<nome>.md` se for agente, seção "Neste projeto" se for skill, aviso no `contexto/QUADRO.md` para todos, e o inventário. Vale para skill do projeto (`.claude/skills/`), agente (`.claude/agents/`), plugin e conector. Nada é usado antes de passar por estes passos:

1. **Ler o que ela roda e a licença inteira.** Ganchos, acesso à rede, dados que saem do projeto, arquivos fora da pasta, e cláusula que restrinja quem pode usar. **Nada se baixa, instala ou roda antes do passo 2** (o cass foi vetado em 22/11: leitura cautelosa nossa, não parecer jurídico, da cláusula que proíbe hospedar e executar para a Anthropic e a OpenAI ou em sistema automático delas; ficha `2151`). O Revisor de risco confere e pode vetar uma parte (foi o que aconteceu com os ganchos do Ponytail).
2. **Conselho de bolso** decide se entra; o Maestro decide, ouvindo o Diretor primeiro se a skill toca conteúdo.
3. **Registrar** na tabela de membros (seção 2: quem usa e quando) e no registro de decisões (seção 7).
4. **Ensinar o projeto.** O arquivo do agente leva só regra fixa do papel; fato que muda (quais casas têm foto, o que está em aberto) fica só no `contexto/<agente>.md`, num lugar só (teste da equipe, 22/11/2026). Toda skill do projeto ganha a seção `## Neste projeto (X1-Plantas)` no `SKILL.md`; todo agente lê `CLAUDE.md`, o `contexto/QUADRO.md` e o seu `contexto/<agente>.md` (não o histórico inteiro); o resumo de passagem em `contexto/entregas/` é um só por tarefa, escrito por quem a conduziu (`CLAUDE.md`). A seção diz o que ler antes, o idioma, as regras que não mudam, onde ela entra no fluxo e que ela nunca corta os avisos legais. Plugin e conector, que ficam fora do repositório, recebem o mesmo texto na mensagem do primeiro uso.
5. **Rodada de alcance.** Rodar a skill uma vez sobre o que já existe onde ela se aplica (exemplo: auditoria no código já escrito, Redator nos textos já publicados). O resultado vai para o `CONTEXTO.md`, e o que precisar de "sim" vai para "Em aberto".
6. **Inventário:** todo nome entra em [`ECOSSISTEMA.md`](ECOSSISTEMA.md) com status (integrado, liberado não usado, ferramenta do Claude Code). Plugin e conector que abrem sessão ou agente próprio recebem o texto de entrada de lá.
7. **Conferência automática.** O `python3 ferramentas/checar.py` dá erro se alguma skill de `.claude/skills/` não tiver a seção "Neste projeto" ou não estiver citada aqui, ou se algum agente de `.claude/agents/` não estiver citado aqui.

## 6b. Ficha do pedido e ciclo de reconferência (regra do dono, 22/11/2026)

Nasceu de um erro: um agente recebeu "área segura para Reels e TikTok" num pedido, e o dono nunca tinha dito onde o vídeo ia passar. Vale para **todo agente e toda sessão**.

1. **Uma ficha por entrega, em `pedidos/`** (entrega longa ganha também uma seção "Pedido do dono" no documento da peça), com três partes: o que o dono pediu, o que foi suposto sem ele dizer, e o que foi pedido a cada agente e o que voltou. Modelo: [`video/ANUNCIO-LOCUCAO.md`](video/ANUNCIO-LOCUCAO.md).
2. **Todo pedido a agente leva a ficha inteira** e separa pedido do dono de suposição.
3. **Reconferência antes de cada etapa** (fechar plano, gerar, montar, entregar): reler os pedidos um por um; nenhuma suposição em aberto decide a etapa; recado novo do dono entra na ficha antes de entrar no plano.
4. **No fim de cada etapa**, quem conduz diz ao dono o que foi reconferido e o que ficou em aberto.

## 7. Registro de decisões do Conselho

| Data | Tarefa | Votos | Decisão | Resultado medido |
|---|---|---|---|---|
| 20/11/2026 | Criar o Conselho e o Redator | Maestro SIM, Estrategista SIM (menos retrabalho), Revisor SIM, SE o veto valer para todo texto público | Criado | A medir: tempo até a primeira peça aprovada |
| 20/11/2026 | Adicionar o Ponytail (skills de código) | Maestro: neutro (é código, não toca venda nem vídeo; o método da MinoAI não fala de ferramenta de código). Estrategista SIM (menos código e retrabalho nas ferramentas). Revisor SIM, só as skills: os ganchos do plugin gravam fora do projeto e podem mandar dados para um webhook | Entraram só as 3 skills em `.claude/skills/` (ponytail, ponytail-review, ponytail-audit), sem ganchos | A medir: erros achados pelo `checar.py` depois de cada mudança de código |
| 21/11/2026 | Vídeo principal E07 com OpenArt, trilha original de 128 BPM e logo | Maestro SIM, SE (1º segundo contido); Editor SIM, SE; Arquiteto SIM, SE (textos e rede); Revisor SIM, SE (selos, lote junto do "Cabe", sem marcas); Designer SIM, SE (sem ciano, papel real) | Aprovado com condições ([plano](video/PRINCIPAL-E07.md), seção 7) | A medir: tempo médio assistido e % que chega ao drop (7,5 s) |
| 22/11/2026 | Selo "Imagem ilustrativa" nos vídeos | Revisor exigia; **o dono tirou a condição** | Sai o selo; o aviso legal fica pequeno, num canto, parado. Registrado em `video/CLAUDE.md` e `contexto/revisor-de-risco.md` | A medir: nenhuma reclamação de "achei que a casa existia" no WhatsApp |
| 22/11/2026 | Adicionar a skill `make-pdf` (gstack) | Conselho de bolso. Maestro: neutro (não toca gancho nem vídeo). Designer SIM para documentos em markdown, não para o e-book (que tem gerador próprio). Revisor SIM só sem o preâmbulo: ele liga telemetria, sincroniza memória da sessão com um repositório e escreve no `CLAUDE.md`. Decisão: skill registrada sem o preâmbulo; instalar o binário do gstack espera o "sim" do dono |
| 22/11/2026 | Divisão do trabalho por modelo e agente `ajudante` (pedido do dono) | Conselho de bolso. Maestro: neutro (não toca gancho nem vídeo). Estrategista SIM (baixa o custo sem tirar qualidade do que vai ao público). Revisor SIM, SE o `ajudante` (Haiku) não tocar nada público nem dado pessoal em arquivo. Decisão: Fable interpreta e confere; Opus executa o trabalho do projeto; Sonnet pesquisa a fundo (`pesquisador`); Haiku faz a tarefa simples e pessoal do dono (`ajudante`). Regras em `pedidos/LEIA-ME.md` |
| 22/11/2026 | Opus na conversa principal; agente `supervisor` (Fable) para socorro e auditoria (pedido do dono) | Conselho de bolso. Maestro: neutro (não toca gancho nem vídeo). Estrategista SIM (o modelo mais forte só onde há erro ou dúvida). Revisor SIM, SE a auditoria procurar promessa sem lastro e suposição tomada como decisão. Decisão: `.claude/settings.json` com `model: opus`; `supervisor` só aponta, quem fez corrige; auditoria a cada 3 fichas, registrada em `pedidos/AUDITORIAS.md` |
| 22/11/2026 | Integrar o cass (busca nas conversas dos agentes), pedido do dono | Estrategista SIM, SE (não misturar no caderno; medir no Mac); Revisor SE (depende da licença) | **Vetado:** a licença proíbe uso e hospedagem para a Anthropic ou quem age por ela, e esta operação é feita por agentes Claude. O dono pode usá-lo à mão no Mac dele | Nenhum: não entra |
| 23/11/2026 | Adicionar a skill `marketing-psychology` (Corey Haines, MIT), pedido do dono | Revisor SIM, SE (aviso MIT; seção "Neste projeto" com a seção 9 do ESTRATEGIA; nada de escassez, preço cheio ou prova social falsos) | Entrou em `.claude/skills/marketing-psychology/`, para o Redator e o Estrategista | A medir: textos do Redator que passam no Revisor de primeira |
| 23/11/2026 | Integrar o everything-claude-code (affaan-m, MIT), pedido do dono (ficha `0209`) | Conselho completo no workflow wkfowrx4b: 5 leitores, Revisor e conferência de compatibilidade por grupo. Revisor SIM, SE (nada que rode `npx` ou baixe pacote; nenhum gancho que bloqueie ou grave fora do projeto; pyright fora; segredo mostrado só como arquivo:linha; LGPD em log e lição; licença MIT citada). Fable SIM, SE (22 correções, que valem sobre o plano) | Entra adaptado, em pedaços, na branch `sistema/everything-claude-code`. Pedaço A (só texto) feito: licença em `.claude/LICENCA-everything-claude-code.txt` e linhas nos contextos, nas skills `ponytail` e `ponytail-review` e no `ECOSSISTEMA.md` (seção 6). Ganchos só com o "sim" do dono; a entrada na main também | A medir: erros pegos pelo `checar.py` antes do commit |
