# Ecossistema: tudo o que a operação pode usar, e se já alcançou o projeto

> Pedido do dono (20/11/2026): "toda skill nova alcança tudo" e "confira se todos, não só o Ponytail, passaram pelas instruções iniciais". O roteiro de entrada está no [`CONSELHO.md`](CONSELHO.md), seção 6. Aqui fica o inventário: o que existe, quem usa, o que faz por fora do projeto e em que pé está.
>
> **Status:**
> - **Integrado:** passou pelo roteiro e já foi usado com o contexto do projeto.
> - **Liberado, não usado:** pode entrar, mas passa pelo roteiro (passos 1 a 5) antes do primeiro uso.
> - **Ferramenta do Claude Code:** infraestrutura, não é membro do Conselho e não precisa do roteiro.

## 1. Como as instruções chegam a cada um

| Quem | Como recebe as regras do projeto |
|---|---|
| **Qualquer modelo** (Fable, Opus, Sonnet, Haiku) na sessão principal | Automático: o Claude Code carrega o `CLAUDE.md` em toda sessão, seja qual for o modelo escolhido no `/model` |
| **Skill do projeto** (`.claude/skills/`) | Seção "Neste projeto (X1-Plantas)" no próprio `SKILL.md`. O `checar.py` confere |
| **Agente do projeto** (`.claude/agents/`) | Linha "Alcance o projeto": manda ler `CLAUDE.md` e o seu `contexto/<agente>.md`. O `checar.py` confere, e confere também o tamanho |
| **Plugin e conector** (ficam fora do repositório) | Rodam dentro da sessão, que já tem o `CLAUDE.md`. Quando um deles abre um agente ou uma sessão própria, essa sessão nova não leva o contexto: na mensagem de abertura vai o **texto de entrada** da seção 5 |

## 2. Do projeto (no repositório)

| Nome | Tipo | Status |
|---|---|---|
| `conselho`, `redacao-que-vende`, `ponytail`, `ponytail-review`, `ponytail-audit` | Skills | Integrado: seção "Neste projeto" em cada uma |
| `arquiteto`, `designer`, `editor-video`, `estrategista`, `pesquisador`, `redator`, `revisor-de-risco` | Agentes | Integrado: cada um manda ler `CLAUDE.md` e `CONTEXTO.md` |

## 3. Conectores (serviços externos)

| Conector | Status | Quem usa | O que faz por fora | Alcance |
|---|---|---|---|---|
| **MinoAI Frontier** | Integrado | Maestro, Editor de vídeo | Lê as redes conectadas; a edição roda no Mac do dono | Feito: método, ganchos e `analyze_hook` usados (`instagram/MINOAI-FRONTIER.md`, `video/REFERENCIA-CONDOR.md`) |
| **OpenArt** | Integrado | MinoAI (imagens e vídeos) | Gasta créditos; manda as imagens de referência para o OpenArt | Feito: `animacoes-3d/OPENART-MINOAI.md`; orçamento em `ORCAMENTO.md` |
| **TinyFish** | Integrado | Pesquisador | Busca e leitura grátis; dataset e deep research são **pagos** (só com o "sim" do dono) | Feito: pesquisas de mercado, referências, normas |
| **Google Drive / Google Docs** | Liberado, não usado | (a decidir) | Lê e escreve arquivos na conta Google do dono | Pendente. Antes do primeiro uso, o Revisor confere o que sai |
| **Claude Docs** | Liberado, não usado | (a decidir: roteiros para o parceiro?) | Documentos compartilháveis no claude.ai | Pendente |
| **Graphify** | Liberado, não usado | Arquiteto (código) | Grafo de código de repositórios indexados | Pendente; só serve se este repositório for indexado |
| **claude-code-remote** | Ferramenta do Claude Code | Sessão | Ambiente, sessões e tarefas agendadas | Não se aplica |

## 4. Skills de plugin e do Claude Code

| Skill | Status | Quem usa | Observação |
|---|---|---|---|
| `openart:*` (ad-variation, hook-variants, performance-ads, pgc, product-listing-video, talking-head, tvc, ugc) | Integrado (pelo OpenArt) | MinoAI | Gastam créditos: conselho completo antes de usar |
| `watch:watch` | Integrado | Pesquisador | Usado no CONDOR; o YouTube bloqueia download na nuvem |
| `impeccable` | Integrado | Designer | Só para detectar o que parece genérico, sem refazer o projeto (decisão do dono) |
| `artifact-design`, `artifact-diagramming`, `artifact-capabilities` | Integrado | Designer | Páginas publicadas (prévia do e-book, calculadora, leitor do rascunho) |
| `anthropic-skills:deep-research` | Integrado | Pesquisador | Abre agentes: mandar o texto de entrada da seção 5 |
| `claude-api` | Integrado | Consulta | Referência de modelos e preços (resposta de 20/11) |
| `loop` | Integrado | Sessão | Já usado nos ciclos de melhoria |
| `ponytail`, `ponytail-review`, `ponytail-audit` | Integrado (skill do projeto) | Arquiteto (código) | Auditoria de 20/11 foi a rodada de alcance |
| `code-review`, `simplify`, `security-review` | Liberado, não usado | Arquiteto (código) | Fazem o mesmo papel do Ponytail. Antes de usar, o Conselho decide qual dos dois fica, para não ter duas regras de código |
| `dataviz` | Liberado, não usado | Estrategista (painel) | Para gráficos do painel de custo por venda |
| `anthropic-skills:pdf`, `docx`, `pptx`, `xlsx`, `docs`, `google-workspace` | Liberado, não usado | (a decidir) | O PDF do e-book já sai do nosso gerador; estas servem para material avulso |
| `run`, `init`, `update-config`, `keybindings-help`, `fewer-permission-prompts`, `plugin-authoring`, `session-start-hook`, `skill-creator`, `built-in-browser`, `chrome-browser`, `computer-use`, `morning`, `import-memory`, `setup-writing-style` | Ferramenta do Claude Code | Sessão | Não são membros do Conselho. `computer-use` e os navegadores precisam do computador do dono |

## 5. Texto de entrada (para plugin, conector ou agente que abre sessão própria)

Cole no começo da mensagem de abertura:

```text
Projeto X1-Plantas: e-book brasileiro de plantas de casas térreas, vendido por Instagram e Facebook com funil no WhatsApp. Público: quem tem o lote e vai construir com pedreiro, classe C, 25 a 50 anos.
Antes de tudo, leia CLAUDE.md (regras que não mudam) e CONTEXTO.md (o resumo: o que nunca muda e o que está em aberto). Responda em português do Brasil, com palavras simples.
Regras: qualidade antes de economia; uma coisa por vez (e-book → animações → vídeo); nunca dizer ou dar a entender que a planta dispensa pedreiro, engenheiro ou arquiteto; nunca prometer aprovação, prazo ou custo de obra; só relatar números que uma ferramenta devolveu; imagem gerada leva "Imagem ilustrativa"; ferramenta paga só com o "sim" do dono.
```

### Prompt específico de cada um (vai junto com o texto base acima)

| Quem | Prompt específico |
|---|---|
| **MinoAI Frontier** | Você é o Maestro: opine primeiro no que é da sua área (conteúdo, vídeo, anúncio, Instagram, imagem), citando a fonte; você não comanda o resto do projeto (`search_mino_method`, `search_viral_hooks`). Edição só no Mac do dono. Referência de edição: `video/REFERENCIA-CONDOR.md`. O público tem de 25 a 50 anos: nada de hiperedição com corte a cada 0,75 s, e sempre texto no primeiro quadro. Nunca estime métrica de rede social |
| **OpenArt** (e as skills `openart:*`) | Sempre imagem a partir de uma imagem nossa (planta, vista da rua ou 3D), nunca uma casa inventada. Primeiro o rascunho em 1k baixa, depois o final em 4K extra-alta a partir do rascunho aprovado. Parede de divisa sem janela. Toda imagem leva "Imagem ilustrativa". No máximo 4 imagens em paralelo. Os créditos seguem o `ORCAMENTO.md`, e o Conselho aprova antes de gastar |
| **TinyFish** | Busca e leitura são grátis; dataset e deep research são pagos e só rodam com o "sim" do dono. Fonte primária brasileira primeiro. Diga quando um site bloqueou |
| **`watch`** | Na nuvem, o YouTube bloqueia o download. Para Reels e TikTok use o `analyze_hook` da MinoAI; para YouTube, peça o Mac do dono ou os minutos que importam |
| **`impeccable`** | Só detecte o que parece genérico e opine; não refaça. Identidade: azul `#0B4FA8`, amarelo `#FFC857`, Bricolage Grotesque e Inter |
| **`artifact-*`** | Página privada, na identidade do projeto, com os dados tirados do validador, nunca colados à mão. Nada que se passe por marca real |
| **`deep-research`** | Abre agentes: mande o texto base. Fonte brasileira primeiro. Use só quando a pergunta pede várias fontes, porque gasta muitos tokens |
| **`claude-api`** | Só consulta de modelos e preços. O projeto não chama a API |
| **`loop`** | Uma tarefa por volta. Cada volta termina com `checar.py`, uma linha no `CONTEXTO.md` e commit |
| **Google Drive e Google Docs** | Antes do primeiro uso, o Revisor lista o que vai sair do projeto. Nunca subir dados pessoais de comprador. Só os arquivos que o dono pedir |
| **Claude Docs** | Para documentos que o parceiro edita (roteiro do WhatsApp, perguntas frequentes). O texto passa pelo Revisor |
| **Graphify** | Só para entender o código, e só se o repositório estiver indexado. O resultado é conferido com o `checar.py` |
| **`code-review`, `simplify`, `security-review`** | Não use junto com o Ponytail: o Conselho escolhe um dos dois para o código |
| **`dataviz`** | Gráficos do painel só com números que uma ferramenta devolveu |
| **`pdf`, `docx`, `pptx`, `xlsx`** | O e-book sai do `livro.py` e nunca é editado à mão. Use só para material avulso que o dono pedir |

## 6. Frameworks de agentes de fora

| Nome | Status | O que é, e o que aproveitamos |
|---|---|---|
| **product-demo-agent-toolkit** ([chapter-dev-pty-ltd/product-demo-agent-toolkit](https://github.com/chapter-dev-pty-ltd/product-demo-agent-toolkit), MIT, versão 0.2.1, Node 22.18 ou mais) | **Aguarda o "sim" do dono para instalar** (a proteção automática do Claude Code bloqueou a instalação e a cópia das skills em 20/11) | Grava vídeo de demonstração de **página web** com Playwright: cursor que se move como uma mão, digitação no ritmo de uma pessoa, espera até a página carregar sem tempo morto, roteiro escrito depois de explorar a página, locução sincronizada com cada clique, 1080p a 60 quadros, 22 fundos, molduras, sons de clique e um estúdio de edição no navegador. Duas skills: `product-demo` (filmar) e `product-demo-review` (revisar o vídeo). **Uso no X1-Plantas:** filmar a calculadora do parceiro ("digite o seu lote e veja as casas que cabem") e o leitor do e-book folheando as páginas, como B-roll e anúncio. É da frente de **vídeo** (a última). **Cuidados do Revisor:** a locução usa o ElevenLabs, com chave paga (só com o "sim" do dono); a música "lofi" foi feita no ElevenLabs Music, e a licença para anúncio não foi conferida (não usar em anúncio pago); os sons são CC0 e os fundos são MIT ou Apache-2.0. O `setup` instala as skills na pasta global de todos os agentes do computador: preferir `product-demo-agent-toolkit skills .claude/skills`, que fica só no projeto |
| **AgentScope 2.0** ([agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope), Apache-2.0, Python 3.11 ou mais) | Liberado, não usado: só ideias | Framework para **construir** agentes em Python que chamam modelos pela API (cobrada por token, à parte da assinatura). Não roda o Claude Code. Li o README e a lista de módulos; **não instalei nem rodei**. Ideias que já usamos ou passamos a usar: compactação automática do contexto e descarte de resultado de ferramenta grande (nosso resumo de passagem e o `CONTEXTO-HISTORICO.md`), escolha do modelo por resposta (nossa regra de Opus para decidir e Sonnet para o rotineiro), equipe com líder que delega (o Conselho) e procedimentos padrão em etapas (o roteiro de entrada). Só valeria instalar se um dia houvesse um agente próprio, por exemplo o que responde no WhatsApp |

## 7. Como manter este inventário

- **Apareceu um nome novo** na lista de skills, plugins ou conectores da sessão: ele entra aqui como "Liberado, não usado" e passa pelo roteiro antes do primeiro uso.
- **Usou pela primeira vez:** passa a "Integrado", com a evidência (o arquivo ou a linha do `CONTEXTO.md`).
- O `checar.py` confere que toda skill e todo agente **do projeto** aparecem aqui e no `CONSELHO.md`. Plugin e conector não estão no repositório, então são conferidos à mão, no começo de cada sessão nova: o primeiro passo é comparar a lista da sessão com esta página.
