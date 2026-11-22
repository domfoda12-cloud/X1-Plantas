# Ecossistema: tudo o que a operação pode usar, e se já alcançou o projeto

> Pedido do dono (20/11/2026): "toda skill nova alcança tudo" e "confira se todos, não só o Ponytail, passaram pelas instruções iniciais". O roteiro de entrada está no [`CONSELHO.md`](CONSELHO.md), seção 6. Aqui fica o inventário: o que existe, quem usa, o que faz por fora do projeto e em que pé está.
>
> **Status:**
> - **Integrado:** passou pelo roteiro e já foi usado com o contexto do projeto.
> - **Liberado, não usado:** pode entrar, mas passa pelo roteiro (passos 1 a 5) antes do primeiro uso.
> - **Em teste:** registrado, mas ainda sem a rodada de alcance; não serve para peça final.
> - **Ferramenta do Claude Code:** infraestrutura, não é membro do Conselho e não precisa do roteiro.
>
> **Uma linha por ferramenta, com um status só.** Mudou o status: troque na linha, não acrescente outra.

## 1. Como as instruções chegam a cada um

| Quem | Como recebe as regras do projeto |
|---|---|
| **Qualquer modelo** (Fable, Opus, Sonnet, Haiku) na sessão principal | Automático: o Claude Code carrega o `CLAUDE.md` em toda sessão, seja qual for o modelo escolhido no `/model` |
| **Skill do projeto** (`.claude/skills/`) | Seção "Neste projeto (X1-Plantas)" no próprio `SKILL.md`. O `checar.py` confere |
| **Agente do projeto** (`.claude/agents/`) | Linha "Alcance o projeto": o `CLAUDE.md` já chega carregado; lê `contexto/QUADRO.md` e o seu `contexto/<agente>.md`. O `checar.py` confere o contexto e o tamanho. O modelo de cada um está na seção 2 |
| **Plugin e conector** (ficam fora do repositório) | Rodam dentro da sessão, que já tem o `CLAUDE.md`. Quando um deles abre um agente ou uma sessão própria, essa sessão nova não leva o contexto: na mensagem de abertura vai o **texto de entrada** da seção 5 |

## 2. Do projeto (no repositório)

| Nome | Tipo | Status |
|---|---|---|
| `conselho`, `redacao-que-vende`, `ponytail`, `ponytail-review`, `ponytail-audit` | Skills | Integrado: seção "Neste projeto" em cada uma. As do Ponytail são do Arquiteto, só para código; a auditoria de 20/11 foi a rodada de alcance |
| `make-pdf` (do gstack) | Skill | **Em teste.** Registrada sem o preâmbulo (telemetria, sincronização de memória, mudanças no `CLAUDE.md`). O binário é compilado **fora do repositório**, em `~/.cache/gstack`, e some quando a máquina é trocada. Serve para documento em markdown (guia do parceiro, relatório jurídico); não para o e-book, que sai do `livro.py` |
| `arquiteto`, `designer`, `editor-video`, `estrategista`, `redator`, `revisor-de-risco` | Agentes, **Opus** | Integrado: lê `CLAUDE.md`, `contexto/QUADRO.md` e o seu `contexto/<papel>.md` |
| `pesquisador` | Agente, **Sonnet** | Integrado: passo 1 da pesquisa (busca e lê as fontes); um agente no Opus confere e conclui |
| Ambiente de nuvem "x1-plantas" | Ambiente pessoal | Criado em 22/11: o script de preparação instala o motor 3D (`npm install` em `video/`) em toda conversa nova. Rede limitada: fontes do Google, OpenArt e instaladores de pacote. Para usar, escolher "x1-plantas" no menu de ambiente |
| `supervisor` | Agente, **Fable** | Integrado em 22/11: socorro quando o Opus (conversa principal) trava ou erra, e auditoria a cada 3 fichas fechadas (`pedidos/AUDITORIAS.md`). Só aponta; quem fez corrige |
| `ajudante` | Agente, **Haiku** | Integrado em 22/11: tarefa simples e pessoal do dono, não dos agentes. Não toca o público nem arquivo do projeto |

Quem faz cada tipo de pedido, e com qual modelo: [`pedidos/LEIA-ME.md`](pedidos/LEIA-ME.md). A conversa principal interpreta e confere; os agentes executam.

## 2b. Que skill e ferramenta está ligada a cada agente

Pedido do dono (22/11/2026): ver com clareza o que cada agente usa. Todos usam o caderno de pesquisa (`ferramentas/pesquisa.py`), menos o `ajudante` (é pessoal); o Revisor lê o caderno e devolve o achado novo para o Maestro registrar (não roda comando).

| Quem (modelo) | Skills e ferramentas | Só com o "sim" do dono |
|---|---|---|
| **Maestro**, a conversa principal (Opus) | `conselho`, `ponytail`, `ponytail-review`, `ponytail-audit`, `artifact-*`, `dataviz`, `make-pdf`, `loop`, Graphify, `pedido.py`, `checar.py` | publicar, gastar, contratar |
| **Diretor**, MinoAI Frontier | `search_mino_method`, `search_viral_hooks`, `analyze_hook`, `get_account_stats`, kit e estilo de edição | OpenArt, `publish_post` |
| `redator` (Opus) | `redacao-que-vende`, ganchos da MinoAI | |
| `estrategista` (Opus) | painel, `dataviz`, números da MinoAI, busca TinyFish | anúncio, TinyFish pago |
| `arquiteto` (Opus) | `plantas.py`, `planta3d.py`, `imagens3d.py`, Graphify, `ponytail`, web | |
| `designer` (Opus) | Diretor MinoAI, `impeccable` (só detectar), `artifact-design`, `make-pdf`, `livro.py` | imagem no OpenArt |
| `editor-video` (Opus) | Diretor MinoAI, `watch`, `video/render*.cjs`, `montar.py` | `openart:*` (`performance-ads`, `hook-variants`, `ugc`, `tvc`, `talking-head`...) |
| `pesquisador` (Sonnet) | busca e leitura do TinyFish, web, `deep-research`, `watch`, `analyze_hook` | TinyFish dataset e deep research |
| `revisor-de-risco` (Opus; Fable na peça final) | leitura do projeto e da web | |
| `supervisor` (Fable) | `checar.py`, `pedido.py`, leitura de tudo | |
| `ajudante` (Haiku) | busca rápida na web, só para o dono | nada pago |

## 3. Conectores (serviços externos)

| Conector | Status | Quem usa | O que faz por fora | Alcance |
|---|---|---|---|---|
| **MinoAI Frontier** | Integrado | Diretor do conteúdo; usada pelo Designer e pelo Editor de vídeo | Lê as redes conectadas; a edição roda no Mac do dono | Feito: método, ganchos e `analyze_hook` usados (`instagram/MINOAI-FRONTIER.md` (seção "Editor: MinoAI Frontier"), `video/REFERENCIAS.md` (seção "Referência de edição: CONDOR XIII (Payton Talbott)")) |
| **OpenArt** | Integrado | MinoAI (imagens e vídeos) | Gasta créditos; manda as imagens de referência para o OpenArt | Plano Pro, 21.137 créditos em 22/11/2026. **Cada uso pede o "sim" do dono**, com resumo e custo antes. Guia: `animacoes-3d/OPENART-MINOAI.md`; saldo: `ORCAMENTO.md` |
| **TinyFish** | Integrado | Pesquisador | Busca e leitura grátis; dataset e deep research são **pagos** (só com o "sim" do dono) | Feito: pesquisas de mercado, referências, normas |
| **Google Drive / Google Docs** | Liberado, não usado | (a decidir) | Lê e escreve arquivos na conta Google do dono | Pendente. Antes do primeiro uso, o Revisor confere o que sai |
| **Claude Docs** | Liberado, não usado | (a decidir: roteiros para o parceiro?) | Documentos compartilháveis no claude.ai | Pendente |
| **Graphify** | Integrado | Arquiteto (código) | Grafo de código; indexa a `main` a cada push | Feito em 22/11 (1.877 itens). É mapa, não etapa obrigatória: ler e buscar arquivos direto continua valendo |
| **claude-code-remote** | Ferramenta do Claude Code | Sessão | Ambiente, sessões e tarefas agendadas | Não se aplica |

## 4. Skills de plugin e do Claude Code

| Skill | Status | Quem usa | Observação |
|---|---|---|---|
| `openart:*` (ad-variation, hook-variants, performance-ads, pgc, product-listing-video, talking-head, tvc, ugc) | Integrado (pelo OpenArt) | MinoAI | Gastam créditos: conselho completo e o "sim" do dono a cada uso |
| `watch:watch` | Integrado | Pesquisador | Usado no CONDOR; o YouTube bloqueia download na nuvem |
| `impeccable` | Integrado | Designer | Só para detectar o que parece genérico, sem refazer o projeto (decisão do dono) |
| `artifact-design`, `artifact-diagramming`, `artifact-capabilities` | Integrado | Designer | Páginas publicadas (prévia do e-book, calculadora, leitor do rascunho) |
| `anthropic-skills:deep-research` | Integrado | Pesquisador | Abre agentes: mandar o texto de entrada da seção 5 |
| `claude-api` | Integrado | Consulta | Referência de modelos e preços (resposta de 20/11) |
| `loop` | Integrado | Sessão | Já usado nos ciclos de melhoria |
| `code-review`, `simplify`, `security-review` | Liberado, não usado | Arquiteto (código) | Fazem o mesmo papel do Ponytail. Antes de usar, o Conselho decide qual dos dois fica, para não ter duas regras de código |
| `dataviz` | Liberado, não usado | Estrategista (painel) | Para gráficos do painel de custo por venda |
| `anthropic-skills:pdf`, `docx`, `pptx`, `xlsx`, `docs`, `google-workspace` | Liberado, não usado | (a decidir) | O PDF do e-book já sai do nosso gerador; estas servem para material avulso |
| `run`, `init`, `update-config`, `keybindings-help`, `fewer-permission-prompts`, `plugin-authoring`, `session-start-hook`, `skill-creator`, `built-in-browser`, `chrome-browser`, `computer-use`, `morning`, `import-memory`, `setup-writing-style` | Ferramenta do Claude Code | Sessão | Não são membros do Conselho. `computer-use` e os navegadores precisam do computador do dono |

## 5. Texto de entrada (para plugin, conector ou agente que abre sessão própria)

Cole no começo da mensagem de abertura:

```text
Projeto X1-Plantas: e-book brasileiro de plantas de casas térreas, vendido por Instagram e Facebook com funil no WhatsApp. Público: quem tem o lote e vai construir com pedreiro, classe C, 25 a 50 anos.
Antes de tudo, leia CLAUDE.md (regras que não mudam), contexto/QUADRO.md (o que o dono acabou de pedir) e CONTEXTO.md (o que nunca muda e o que está em aberto). Responda em português do Brasil, com palavras simples.
Regras: qualidade antes de economia; uma coisa por vez (e-book → animações → vídeo); nunca dizer ou dar a entender que a planta dispensa pedreiro, engenheiro ou arquiteto; nunca prometer aprovação, prazo ou custo de obra; só relatar números que uma ferramenta devolveu; imagem parada gerada leva "Imagem ilustrativa" (nos vídeos o selo saiu por ordem do dono; o aviso "Planta de referência…" continua); ferramenta paga e cada uso do OpenArt só com o "sim" do dono.
```

### Prompt específico de cada um (vai junto com o texto base acima)

| Quem | Prompt específico |
|---|---|
| **MinoAI Frontier** | Você é o Diretor: dê a ideia principal de todo conteúdo e opine primeiro nele, citando a fonte; quem decide é o Maestro (a conversa principal) (`search_mino_method`, `search_viral_hooks`). Edição só no Mac do dono. Referência de edição: `video/REFERENCIAS.md` (seção "Referência de edição: CONDOR XIII (Payton Talbott)"). O público tem de 25 a 50 anos: nada de hiperedição com corte a cada 0,75 s, e sempre texto no primeiro quadro. Nunca estime métrica de rede social |
| **OpenArt** (e as skills `openart:*`) | Sempre imagem a partir de uma imagem nossa (planta, vista da rua ou 3D), nunca uma casa inventada. Primeiro o rascunho em 1k baixa, depois o final em 4K extra-alta a partir do rascunho aprovado. Parede de divisa sem janela. Imagem parada leva "Imagem ilustrativa"; vídeo não leva o selo (ordem do dono, 22/11), mas leva o aviso "Planta de referência…". No máximo 4 imagens em paralelo. Cada uso pede o "sim" do dono, com resumo e custo antes |
| **TinyFish** | Busca e leitura são grátis; dataset e deep research são pagos e só rodam com o "sim" do dono. Fonte primária brasileira primeiro. Diga quando um site bloqueou |
| **`watch`** | Na nuvem, o YouTube bloqueia o download. Para Reels e TikTok use o `analyze_hook` da MinoAI; para YouTube, peça o Mac do dono ou os minutos que importam |
| **`impeccable`** | Só detecte o que parece genérico e opine; não refaça. Identidade: azul `#0B4FA8`, amarelo `#FFC857`, Bricolage Grotesque e Inter |
| **`artifact-*`** | Página privada, na identidade do projeto, com os dados tirados do validador, nunca colados à mão. Nada que se passe por marca real |
| **`deep-research`** | Abre agentes: mande o texto base. Fonte brasileira primeiro. Use só quando a pergunta pede várias fontes, porque gasta muitos tokens |
| **`claude-api`** | Só consulta de modelos e preços. O projeto não chama a API |
| **`loop`** | Uma tarefa por volta. Cada volta termina com `checar.py`, uma linha no `CONTEXTO.md` e commit |
| **Google Drive e Google Docs** | Antes do primeiro uso, o Revisor lista o que vai sair do projeto. Nunca subir dados pessoais de comprador. Só os arquivos que o dono pedir |
| **Claude Docs** | Para documentos que o parceiro edita (roteiro do WhatsApp, perguntas frequentes). O texto passa pelo Revisor |
| **Graphify** | Mapa para entender o código, não etapa obrigatória. Confira se o `commitSha` do resultado é o `HEAD`; se não for, leia o arquivo. O resultado é conferido com o `checar.py` |
| **`code-review`, `simplify`, `security-review`** | Não use junto com o Ponytail: o Conselho escolhe um dos dois para o código |
| **`dataviz`** | Gráficos do painel só com números que uma ferramenta devolveu |
| **`pdf`, `docx`, `pptx`, `xlsx`** | O e-book sai do `livro.py` e nunca é editado à mão. Use só para material avulso que o dono pedir |

## 6. Frameworks de agentes de fora

| Nome | Status | O que é, e o que aproveitamos |
|---|---|---|
| **product-demo-agent-toolkit** ([chapter-dev-pty-ltd/product-demo-agent-toolkit](https://github.com/chapter-dev-pty-ltd/product-demo-agent-toolkit), MIT, versão 0.2.1, Node 22.18 ou mais) | **Aguarda o "sim" do dono para instalar** (a proteção automática do Claude Code bloqueou a instalação e a cópia das skills em 20/11) | Grava vídeo de demonstração de **página web** com Playwright: cursor que se move como uma mão, digitação no ritmo de uma pessoa, espera até a página carregar sem tempo morto, roteiro escrito depois de explorar a página, locução sincronizada com cada clique, 1080p a 60 quadros, 22 fundos, molduras, sons de clique e um estúdio de edição no navegador. Duas skills: `product-demo` (filmar) e `product-demo-review` (revisar o vídeo). **Uso no X1-Plantas:** filmar a calculadora do parceiro ("digite o seu lote e veja as casas que cabem") e o leitor do e-book folheando as páginas, como B-roll e anúncio. É da frente de **vídeo** (a última). **Cuidados do Revisor:** a locução usa o ElevenLabs, com chave paga (só com o "sim" do dono); a música "lofi" foi feita no ElevenLabs Music, e a licença para anúncio não foi conferida (não usar em anúncio pago); os sons são CC0 e os fundos são MIT ou Apache-2.0. O `setup` instala as skills na pasta global de todos os agentes do computador: preferir `product-demo-agent-toolkit skills .claude/skills`, que fica só no projeto |
| **AgentScope 2.0** ([agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope), Apache-2.0, Python 3.11 ou mais) | Liberado, não usado: só ideias | Framework para **construir** agentes em Python que chamam modelos pela API (cobrada por token, à parte da assinatura). Não roda o Claude Code. Li o README e a lista de módulos; **não instalei nem rodei**. Ideias que já usamos ou passamos a usar: compactação automática do contexto e descarte de resultado de ferramenta grande (nosso resumo de passagem e o `CONTEXTO-HISTORICO.md`), escolha do modelo por resposta (nossa regra de Opus para decidir e Sonnet para o rotineiro), equipe com líder que delega (o Conselho) e procedimentos padrão em etapas (o roteiro de entrada). Só valeria instalar se um dia houvesse um agente próprio, por exemplo o que responde no WhatsApp |

**Vetado:** **cass** (Coding Agent Session Search, de Jeffrey Emanuel), 22/11/2026: a licença (MIT com adendo) nega direitos à Anthropic e à OpenAI e a quem age por elas, e proíbe hospedar ou executar para elas; os agentes do projeto são Claude. O dono pode usá-lo à mão no Mac dele. Ficha `2151-integrar-o-cass`.

## 7. Como manter este inventário

- **Apareceu um nome novo** na lista de skills, plugins ou conectores da sessão: ele entra aqui como "Liberado, não usado" e passa pelo roteiro antes do primeiro uso.
- **Usou pela primeira vez:** passa a "Integrado", com a evidência (o arquivo ou a linha do `CONTEXTO.md`).
- O `checar.py` confere que toda skill e todo agente **do projeto** aparecem aqui e no `CONSELHO.md`. Plugin e conector não estão no repositório, então são conferidos à mão, no começo de cada sessão nova: o primeiro passo é comparar a lista da sessão com esta página.
