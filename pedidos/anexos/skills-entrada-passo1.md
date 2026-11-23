# Entrada de 6 skills: passo 1 do roteiro (ler o que ela roda)

> **Pesquisador, 23/11/2026.** Passo 1 de `CONSELHO.md`, seção 6. Só leitura de páginas públicas (TinyFish: GitHub raw, blob e a API pública de commits e pastas). **Nada foi baixado, clonado, instalado nem executado; nada pago; sem commit.** O `gh` e o `curl` do shell continuam sem acesso a esses repositórios e **não foram contornados**; o SHA e os tamanhos vêm de páginas públicas da API do GitHub lidas pelo TinyFish (leitura, como o resto). Quem confere e conclui é o Opus; o Revisor de risco tem veto. Os rascunhos "Neste projeto" são **propostas**: nada foi gravado em `.claude/skills/`.
> Origem dos pedidos: o dono aprovou as 3 de venda ("as 3") e as 3 de design ("usa as 3, mas não use o estilo de referência de arte deles, use o nosso próprio"). Listas anteriores: `skills-candidatas-venda.md` e `skills-candidatas-design.md`.
> Certeza de tudo: **confirmado no texto lido** (SHA, tamanhos e licença vêm da API e do arquivo no commit fixado). Onde não li linha a linha, está dito na seção "O que não li".

## Resumo em uma tabela

| Skill | Commit lido | Licença | Roda algo? | Recomendação |
|---|---|---|---|---|
| `meta-click-to-message-ads` | `4883fa97…` (10/11/2026) | MIT, © 2026 InsightfulPipe | Nada local. O texto manda usar o MCP da InsightfulPipe (de fora) | **Reescrever o método** em português, sem o MCP; manter o `LICENSE` MIT na pasta |
| `copy-thief` | `2a9b3a01…` (12/10/2026) | MIT, © 2026 Thales Holleben | Nada. O `form.html` é local e sem rede | **Copiar a pasta** (com `LICENSE`), cortando 8 arquivos e avisando 3 trechos |
| `offers` | `8a0c22d6…` (23/11/2026, 20:41 UTC) | MIT, © 2025 Corey Haines | Nada | **Copiar `SKILL.md` e 6 das 8 referências** (com `LICENSE`), sem `evals/`, `saas-offers.md`, `examples.md` |
| `frontend-design` | `e4bb5d96…` (16/11/2026) | Apache 2.0 (`LICENSE.txt` sem linha de copyright) | Nada | **Copiar a pasta** (2 arquivos) e anotar a mudança (Apache, cláusula 4b) |
| `canvas-design` | `e4bb5d96…` (16/11/2026) | Apache 2.0, "Copyright 2026 Anthropic, PBC" | Nada próprio; o texto manda baixar fontes e gerar PDF/PNG | **Reescrever só o método** em duas passadas, sem a pasta de fontes e sem o estilo |
| `pdf-design` | `a4d54449…` (20/09/2026, v1.2.0) | MIT, © 2026 Georgi Zagoruyko Krivtsov; fontes SIL OFL 1.1 | **Sim:** Node 22+ e Chrome sem tela, escreve PDF e PNG; `brand.mjs` e `fonts.mjs` usam a rede | **Reescrever só o método** (conferência página a página); scripts e temas ficam de fora |

Os SHA inteiros estão em cada ficha. O dono pode abrir qualquer commit em `https://github.com/<dono>/<repositório>/commit/<SHA>`.

---

## 1. meta-click-to-message-ads (Insightful-Pipe/meta-ads-skills)

- **SHA e data:** `4883fa9783b978a31320239f839a618fdb16aff5`, 10/11/2026 20:54 UTC. Mensagem do commit: "Sync skills from insightfulpipe.com", feita por `github-actions[bot]`, **sem assinatura**. O repositório é **reconstruído duas vezes por dia a partir do site insightfulpipe.com** (`.github/workflows/sync.yml`, cron 02:27 e 14:27): o texto muda sem revisão de ninguém. Por isso o SHA fixado manda e **nada de `/plugin marketplace add` nem `npx skills add`** (puxariam a versão do dia).
- **Licença:** `LICENSE` na raiz, MIT, "Copyright (c) 2026 InsightfulPipe" (texto inteiro lido; 1.071 bytes). Exige manter o aviso e o texto da licença em cópias.
- **Arquivos da pasta `skills/meta-click-to-message-ads/`:** `SKILL.md` 22.644 bytes; `HOW_TO_USE.md` 3.661; `expected_output.json` 16.553; `sample_input.json` 49.651. Fora da pasta: `README.md` 9.301 e `.claude-plugin/plugin.json` 756 (lidos; o README diz "adds no hooks, commands or MCP servers, runs no code").
- **O que roda:**
  - Nada local: é só Markdown. Não há script, `package.json`, chave nem instalação.
  - O texto manda usar o **MCP da InsightfulPipe** (`query_data`, `query_contexts`, `execute_action`, `platform="facebook-ads"`) para ler a conta e, só depois de um "sim", criar campanha, conjunto e anúncio **pausados** ou pausar um anúncio. **Esse MCP é de fora: não conectar** (regra do projeto e do roteiro de entrada).
  - Sem o MCP o próprio texto diz que "tudo o mais funciona igual", com texto colado ou planilha exportada.
- **O que serve para nós (5 linhas):**
  1. O **kit de mensagem em 6 partes** para anúncio que abre o WhatsApp: texto e título do anúncio, saudação (até 300 caracteres), **mensagem já preenchida** diferente em cada anúncio (diz de qual anúncio veio a conversa), 3 frases de partida (até 80 caracteres cada) e a primeira resposta humana, mais 2 ou 3 perguntas que dizem se a conversa é qualificada.
  2. **A regra que combina com o nosso painel:** quem decide é o custo por venda; custo por conversa só informa (a skill diz "uma conversa barata que nunca qualifica é o jeito mais comum de perder dinheiro").
  3. **Veredito por anúncio** contra o alvo de custo por venda (escalar, manter, consertar, pausar, cedo demais), com mínimo de 3 vendas antes de condenar; e a regra "mensagem preenchida por anúncio" para o time saber qual anúncio trouxe a conversa, mesmo sem ferramenta de caixa de entrada.
  4. **Resposta fora do horário** que já faz a primeira pergunta; no máximo dois passos automáticos antes de uma pessoa entrar; pergunta de preço, reclamação ou pedido de humano vai direto a uma pessoa.
  5. **Dado de conversa é dado pessoal:** usar só para contar, nunca citar nome, número nem mensagem no relatório (casa com a LGPD no `WHATSAPP.md`).
- **O que NÃO pode entrar:**
  - Todo o caminho do MCP (`query_data`, `execute_action`, os "payloads", `upload_ad_image`, `create_*`, `update_ad`): MCP de fora e ação na conta de anúncio, que é decisão e gasto do dono.
  - A tabela de roteiros por tipo de negócio (clínica, casa de serviço, loja) e a ideia de "uma vaga esta semana" no anúncio: e-book não tem vaga; **urgência só se for verdadeira**.
  - Qualquer alvo de custo por venda **inventado**: o skill manda perguntar; no nosso projeto o alvo é do dono (`PAINEL.md`, seção 4) ou fica "em aberto". Não estimar métrica.
  - As frases "Meta cobra", "janela de 24 horas" e "até 7 dias" como fato nosso: são fonte secundária do autor; conferir na página oficial da Meta antes de citar.
  - Prometer prazo de resposta ("em 5 minutos") antes de o dono dizer **quem responde** e em que número (o chip próprio ainda não existe: `decisoes-do-dono-2026-11-23.md`).
  - Promessa de resultado, depoimento ou desconto na saudação: o skill já proíbe inventar preço, oferta ou frase que o usuário não deu; manter.
- **Recomendação: reescrever só o método**, em português e em um `SKILL.md` curto, porque 60% do texto original é o caminho do MCP, os exemplos são de outro nicho e o repositório muda sozinho. Manter um `LICENSE` MIT na pasta com a linha "método adaptado de InsightfulPipe/meta-ads-skills, commit 4883fa97" (a MIT pede o aviso se houver parte substancial do texto). Copiar a pasta inteira exigiria cortar à mão o MCP e ainda deixaria o inglês.
- **Rascunho da seção (para o `SKILL.md` reescrito):**

```markdown
## Neste projeto (X1-Plantas)

> Origem: método adaptado de github.com/Insightful-Pipe/meta-ads-skills, `skills/meta-click-to-message-ads/SKILL.md` (commit 4883fa97, 10/11/2026), licença MIT, Copyright (c) 2026 InsightfulPipe: o texto da licença está em `LICENSE`, nesta pasta. Reescrita em português, sem o caminho do MCP. Entrou em [data] a pedido do dono, com o veto do Revisor de risco ([resultado]; ficha `pedidos/2026-11/<ficha>`).

- **Leia antes:** `ebook/vendas/WHATSAPP.md` (sequência, regras do funil, resposta a quem comenta PLANTA), `ESTRATEGIA.md` (seção 7: a oferta; seção 9: honestidade), `pedidos/anexos/decisoes-do-dono-2026-11-23.md` (garantia de 7 dias, Pix pelo WhatsApp, número próprio do negócio ainda sem chip) e `PAINEL.md`, seção 4 (custo por venda). Português do Brasil, preços em R$.
- **Só se usa o que roda sem conexão:** o kit de mensagem (6 partes) e a leitura de uma planilha ou exportação **colada à mão** pelo dono. **Nenhum MCP, nenhum painel de anúncios conectado, nenhuma criação ou pausa de anúncio:** o anúncio, o orçamento e o público são do dono.
- **Cobre só o anúncio pago que abre o WhatsApp.** O "Comente PLANTA" e a sequência de mensagens continuam sendo do `WHATSAPP.md`.
- **Todo kit passa pela seção 9 do `ESTRATEGIA.md`:** nada de prazo de obra, custo exato, aprovação na prefeitura ou no banco, nem de dar a entender que a planta dispensa pedreiro, engenheiro ou arquiteto; preço, desconto, vaga ou prazo de oferta só se o dono já decidiu e for verdade; sem depoimento, número de clientes nem "resultado" que nenhuma ferramenta devolveu.
- Não se aplicam aqui: vaga ou "horário disponível" no anúncio; o alvo de custo por venda que o dono não definiu (escreva "em aberto" e não estime); meta de resposta em minutos antes de o dono dizer quem responde e em qual número; os números da janela de conversa da Meta (24 horas, 7 dias) como fato, sem conferir na página oficial; qualquer métrica que nenhuma ferramenta devolveu.
- **Dado de conversa é dado pessoal (LGPD):** use a planilha só para contar; nenhum nome, telefone ou mensagem entra no repositório nem no relatório.
- **Quem usa:** o `estrategista` (plano e veredito por custo por venda), o `redator` (texto do anúncio, saudação e mensagem preenchida) e o `revisor-de-risco` (veto).
- Ela é membro do Conselho (`CONSELHO.md`); o que ela sugerir é opção para o dono, nunca decisão.
- **Prompt de entrada:** antes de planejar um anúncio que abre o WhatsApp, diga qual casa e qual ângulo ele vende (`ebook/vendas/atributos-que-vendem.md`), qual é o alvo de custo por venda **do dono** (ou "em aberto"), quem responde e em qual número; escreva o kit de 6 partes em português simples, com uma mensagem preenchida diferente por anúncio; marque como **opção para o dono** tudo que envolva preço, garantia, orçamento ou público.
```

---

## 2. copy-thief (thalesholleben/copy-thief)

- **SHA e data:** `2a9b3a01a06e836a2c06ba90b2e6162d2ab1a72e`, 12/10/2026 23:42 UTC ("docs: point to the Pack Tráfego and use %USERPROFILE% in the Windows path (#1)").
- **Licença:** `LICENSE`, MIT, "Copyright (c) 2026 Thales Holleben" (inteiro lido; 1.072 bytes).
- **Arquivos (25) e tamanhos em bytes:** `SKILL.md` 7.114; `reference/` 01 6.912, 02 5.559, 03 4.081, 04 4.888, 05 6.014, 06 4.143, 07 4.429, 08 4.671, 09 5.314; `templates/` lp 3.704, advertorial 2.342, vsl 2.306; `checklists/` briefing 1.656, qa-review 2.666; `examples/swipe-file.md` 4.693; `intake/form.html` 10.965; mais `README.md` 3.635, `AGENTS.md` 1.879, `CLAUDE.md` 193, `CONTRIBUTING.md` 1.268, `SECURITY.md` 821, `.github/copilot-instructions.md` 713, `.gitignore` 249, `LICENSE` 1.072. Sem `package.json`, sem script.
- **O que roda:**
  - Nada. O `SKILL.md` só manda ler os arquivos acima.
  - **`intake/form.html` lido inteiro (256 linhas):** é um formulário local; o script só junta as respostas, copia para a área de transferência (`navigator.clipboard`) ou baixa um JSON (`Blob`). **Sem `fetch`, sem `XMLHttpRequest`, sem endereço externo, sem fonte da web.** Nenhum dado sai da página.
  - Nenhuma das referências lidas tem endereço (`http`) nem comando.
  - O `README.md` termina com um link para um **pacote pago do autor** (skills.thalesgomes.com): propaganda, não entra na cópia.
- **O que serve para nós (5 linhas):**
  1. **Diagnóstico antes de escrever:** nível de consciência de quem chega do anúncio e sofisticação do mercado (Schwartz); "a maior causa de página que não converte é desalinhamento de consciência".
  2. **Fluxo que para e pede aprovação** (diagnóstico, estrutura, **parada**, só então o texto): combina com a ficha e com o dono que decide título e preço.
  3. **Congruência anúncio → página** (`reference/07`): a promessa da primeira dobra repete o anúncio; serve também para anúncio → primeira mensagem do WhatsApp.
  4. **Placeholders no lugar de prova** (`[INSERIR DEPOIMENTO REAL]`) e "não fabrica depoimento, número, autoridade nem resultado": é a nossa regra.
  5. **Lista de conferência de anúncio** (`reference/09`): atributo pessoal presumido ("você que está endividado"), garantia de resultado, antes e depois irreal, falsa escassez; em português do Brasil. É resumo do autor das políticas da Meta e do Google (**fonte secundária**): o Revisor confere na política oficial antes de afirmar.
- **O que NÃO pode entrar:**
  - **Empilhar "valor total" com preços inventados por item** (`reference/05` "Value Stack" e `examples/swipe-file.md`, exemplo 2: "valor R$ 3.000… valor total R$ 7.000, hoje R$ 1.497"). Aqui só vale preço cheio **cobrado de fato**; é o mesmo corte da `marketing-psychology`.
  - **"Garantia nomeada" que devolve se a pessoa "não tiver resultado"** (exemplo 3): a nossa garantia é a de 7 dias da entrega do link, decidida pelo dono. Nada de garantia de resultado de obra.
  - Números "específicos" de ganho em prazo (`SKILL.md`, regra 5: "R$ 2.347 em 19 dias"): é exemplo do nicho dele; no nosso caso número só com fonte.
  - Depoimento "da Marina… aplicou em 26 dias" (exemplo 4): é marcado como placeholder, mas **não copiar para texto público**. Ainda não temos depoimento real.
  - "Mecanismo único", "segredo", "resultado dos sonhos" e ancoragem de preço como técnica: só se for verdadeiro e o Revisor aprovar.
  - **Advertorial que pareça notícia ou endosso** (o próprio `reference/07` já proíbe; manter).
  - A regra pessoal do autor "nunca usar travessão ou hífen solto como pontuação": é gosto dele, não é regra do projeto; **sair do `SKILL.md`** (o dono decide se quer a regra).
  - O link do pacote pago, o `.github/`, `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, `SECURITY.md` e o `README.md`: ficam de fora da cópia (o `CLAUDE.md` do autor tem `@AGENTS.md` e poderia puxar instruções nas sessões; **não copiar**).
  - **Pergunta que fica com o dono:** o funil é anúncio, WhatsApp e Pix; ainda não existe página de vendas decidida. Não presumir página; usar a skill para anúncio e primeira mensagem até o dono dizer.
- **Recomendação: copiar a pasta** (já está em português, só texto, MIT) **com os cortes acima**, mais um aviso de uma linha no topo de `reference/05` e do exemplo 2 do `swipe-file.md` ("não usar valor inventado"). Manter o `LICENSE` MIT. Marcar no `SKILL.md` as mudanças feitas.
- **Rascunho da seção:**

```markdown
## Neste projeto (X1-Plantas)

> Origem: github.com/thalesholleben/copy-thief (commit 2a9b3a01, 12/10/2026), licença MIT, Copyright (c) 2026 Thales Holleben: o texto da licença está em `LICENSE`, nesta pasta. Cópia com cortes (sem README, AGENTS, CLAUDE, CONTRIBUTING, SECURITY e `.github/`) e com avisos nos trechos de valor empilhado. Entrou em [data] a pedido do dono, com o veto do Revisor de risco ([resultado]; ficha `pedidos/2026-11/<ficha>`).

- **Leia antes:** `ebook/referencias/MERCADO.md` (persona e mercado), `ESTRATEGIA.md` (seção 7: a oferta; seção 9: honestidade), `ebook/vendas/atributos-que-vendem.md`, `ebook/vendas/WHATSAPP.md` e `pedidos/anexos/decisoes-do-dono-2026-11-23.md` (título, garantia de 7 dias, Pix pelo WhatsApp). Português do Brasil, preços em R$. Nosso funil é anúncio, WhatsApp e Pix: **não presuma página de vendas**; use o diagnóstico e a congruência para o anúncio e para a primeira mensagem, e a estrutura de página só se o dono pedir uma.
- **O briefing usa fatos do projeto:** casas e lotes de `ebook/`, preço **decidido ou "em aberto"**, garantia de 7 dias, prova real (hoje não há depoimento nem número de clientes: use o placeholder `[INSERIR DEPOIMENTO REAL]` e diga que falta).
- **O fluxo para na estrutura e o dono aprova** (diagnóstico, estrutura, parada, copy); título, preço e gasto com anúncio são dele.
- **Todo texto passa pela seção 9 do `ESTRATEGIA.md`:** nunca prometer prazo, custo de obra ou aprovação; nunca dar a entender que a planta dispensa pedreiro, engenheiro ou arquiteto; a planta é de referência e o projeto legal é assinado por profissional habilitado.
- Não se aplicam aqui: "valor total" empilhado com preço que ninguém cobra (`reference/05`, exemplo 2 do `swipe-file`); garantia de resultado ou "devolvo se não tiver resultado"; número de ganho em prazo; o depoimento "da Marina"; mecanismo "único" ou "segredo"; urgência ou vaga que não existe; advertorial que pareça notícia; atributo pessoal presumido no anúncio. A lista de `reference/09` é resumo do autor das políticas da Meta e do Google: o Revisor confere na política oficial antes de qualquer afirmação.
- **Quem usa:** o `redator` (texto, em cima de `redacao-que-vende`), o `estrategista` (diagnóstico e oferta) e o `revisor-de-risco` (veto).
- Ela é membro do Conselho (`CONSELHO.md`); o que ela sugerir é opção para o dono, nunca decisão.
- **Prompt de entrada:** antes do passo 1, preencha o briefing só com fatos do projeto e escreva "em aberto" no que o dono não decidiu (preço, bônus, página); diga o nível de consciência que você atribui ao tráfego e por quê; ao terminar, passe a copy pelo `checklists/qa-review.md` e marque como **opção para o dono** tudo que envolva preço, garantia, prazo de oferta ou prova social.
```

---

## 3. offers (coreyhaines31/marketingskills, pasta `skills/offers/`)

- **SHA e data:** `8a0c22d677e6031e8a5dd4b554b6ce059b753ffe`, 23/11/2026 20:41 UTC, autor Corey Haines. **Commit de hoje: o repositório muda toda hora; fixar este SHA** (a nossa `marketing-psychology` veio da versão 2.0.3 de outro dia).
- **Licença:** `LICENSE` na raiz, MIT, "Copyright (c) 2025 Corey Haines" (inteiro lido). Já temos o mesmo texto em `.claude/skills/marketing-psychology/LICENSE`.
- **Arquivos da pasta (11) e tamanhos em bytes:** `SKILL.md` 9.593 (versão 1.0.6); `references/` value-equation 7.883, offer-anatomy 8.857, guarantee-design 8.173, bonus-stacking 7.758, scarcity-urgency 7.106, offer-formats 10.690, saas-offers 7.869, examples 10.203; `evals/evals.json` 3.190.
- **O que roda:** **nada.** `SKILL.md` lido inteiro: só Markdown, sem `allowed-tools`, sem script. A varredura das 8 referências e do `evals.json` achou **zero endereços e zero comandos** (`npx`, `node`, `curl`, `tools/`). Ele manda ler `.agents/product-marketing.md` **se existir** (aqui não existe; a `marketing-psychology` já foi adaptada para ler `MERCADO.md`). Cita skills irmãs que **não** estão instaladas (`pricing`, `copywriting`, `cro`, `launch`, `paywalls`, `sales-enablement`, `emails`, `ab-testing`). O pacote `marketingskills` tem `tools/` e instalador `npx skills`: **não copiar nada fora de `skills/offers/`**.
- **O que serve para nós (5 linhas):**
  1. **"A oferta é a coisa, não a página":** antes de pedir texto melhor, perguntar se a oferta em si é boa (3 perguntas de diagnóstico).
  2. **Equação de valor** (resultado desejado, chance percebida de dar certo, tempo até o resultado, esforço): achar qual das quatro peças está fraca. Para um e-book de preço baixo, "tempo" e "esforço" são as peças que o nosso material mexe (lote medido, perguntas prontas para o engenheiro).
  3. **Seis partes de uma oferta** (o que se entrega, bônus, garantia, por que agora, nome, preço e forma de pagar); para cada uma, o que é fraco e o que é forte. `offer-formats.md` tem uma ficha de "produto de informação" (guia, modelo, pacote), que é o nosso caso.
  4. **Escassez honesta contra falsa** (`scarcity-urgency.md`): contador que reinicia, "só 3 vagas" em produto digital, urgência que sempre volta; só vale o que tem data ou limite verdadeiro.
  5. **Vocabulário banido** ("revolucionário", "segredo", "tempo limitado" sem limite, "vale R$ X" sem comparável, "100% garantido" sem condições) e **bônus que resolve uma objeção real**, não bônus inflado: ambos casam com o que o Revisor já veta.
- **O que NÃO pode entrar:**
  - A "projeção de ganho" do passo 7 do loop de diagnóstico ("conte com 10 a 40% de ganho relativo por mudança"): é número sem fonte nossa; **não estimar métrica**.
  - **Valor de bônus ou "valor total" sem comparável** (o próprio skill proíbe; manter) e qualquer "de R$ X por R$ Y" sem o preço cheio cobrado de fato. **Atenção ao Revisor:** a decisão do dono de variar R$ 47 e R$ 67 em semanas alternadas **não pode ser apresentada** como "promoção", "preço de lançamento" nem "o preço sobe": são dois preços de teste; como mostrar isso ao comprador é do dono, com o Revisor.
  - Escassez de vaga ou de "lote" para e-book: não há estoque nem turma. "Preço sobe em tal data" só se o dono decidir e se de fato subir (o skill diz: "se não subir, foi mentira").
  - Garantia "em dobro", "devolvo mais R$ 1.000" ou condicional com resultado de obra: a nossa é a de 7 dias da entrega do link, decidida pelo dono (`WHATSAPP.md`, CDC art. 49).
  - `saas-offers.md` e `examples.md` (exemplos em dólar, SaaS, B2B, consultoria, nomes de empresas), `evals/` (testes do autor) e links para skills que não temos.
  - "Acesso vitalício" e "comunidade" como bônus: não prometer o que o dono não decidiu (o que vai de graça ainda está em aberto com o dono; só a Casa Compacta é grátis).
- **Recomendação: copiar `SKILL.md` e 6 referências** (`value-equation`, `offer-anatomy`, `guarantee-design`, `bonus-stacking`, `scarcity-urgency`, `offer-formats`), **sem** `evals/`, `saas-offers.md` e `examples.md`, e **tirar do `SKILL.md`** as duas linhas de `saas-offers`/`examples` e a projeção de 10 a 40%. Segue o precedente da `marketing-psychology` (cópia, `LICENSE` na pasta, seção "Neste projeto"). Reescrever em português seria melhor para o dono ler, mas custa mais e os modelos entendem o inglês; fica como opção.
- **Rascunho da seção:**

```markdown
## Neste projeto (X1-Plantas)

> Origem: github.com/coreyhaines31/marketingskills, `skills/offers/` (versão 1.0.6, commit 8a0c22d6, 23/11/2026), licença MIT, Copyright (c) 2025 Corey Haines: o texto da licença está em `LICENSE`, nesta pasta. Cópia sem `evals/`, `saas-offers.md` e `examples.md`, e sem a projeção de ganho do passo 7. Entrou em [data] a pedido do dono, com o veto do Revisor de risco ([resultado]; ficha `pedidos/2026-11/<ficha>`).

- **Leia antes:** no lugar do `product-marketing.md` citado acima (não existe aqui), leia `ebook/referencias/MERCADO.md` (persona e mercado), `ESTRATEGIA.md` (seção 7: a oferta, que é só recomendação até o dono decidir; seção 9: honestidade) e `pedidos/anexos/decisoes-do-dono-2026-11-23.md` (título "Antes do primeiro tijolo", garantia de 7 dias, só a Casa Compacta é grátis, bônus decididos). Português do Brasil, preços em R$.
- **A skill organiza perguntas e opções; título, preço, garantia, bônus e gasto com anúncio são do dono.** Ela é para a oferta de um e-book de preço baixo (`offer-formats.md`, "produto de informação"); as partes de serviço, mentoria e B2B não se aplicam.
- **Todo modelo desta skill passa pela seção 9 do `ESTRATEGIA.md`:** escassez, prazo, preço cheio, bônus e prova social só se forem verdadeiros e tiverem fonte; nunca prometer custo, prazo ou aprovação de obra, nem dar a entender que a planta dispensa pedreiro, engenheiro ou arquiteto; a planta é de referência e o projeto legal é assinado por profissional habilitado.
- Não se aplicam aqui: vaga, turma ou estoque (e-book não tem); "valor total" ou valor de bônus sem comparável; "de R$ X por R$ Y" sem o preço cheio cobrado de fato (**os preços de R$ 47 e R$ 67 em semanas alternadas são um teste do dono: não os apresente como promoção, lançamento ou aumento sem o Revisor**); garantia de resultado ou "em dobro"; acesso vitalício; projeção de ganho em porcentagem; número de clientes ou depoimento que nenhuma ferramenta devolveu; skills irmãs que não estão instaladas.
- **Quem usa:** o `estrategista` (oferta e ângulo), o `redator` (o texto continua seguindo `.claude/skills/redacao-que-vende/`) e o `revisor-de-risco` (veto).
- Ela é membro do Conselho (`CONSELHO.md`); o que ela sugerir é opção para o dono, nunca decisão.
- **Prompt de entrada:** antes de propor qualquer mudança de oferta, diga qual das quatro peças da equação de valor está mais fraca e em que fato do projeto você se apoia (`atributos-que-vendem.md`, `MERCADO.md`); proponha **uma** mudança por vez; confira cada fato contra a seção 9 do `ESTRATEGIA.md` e marque como **opção para o dono** tudo que envolva preço, garantia, bônus ou prazo de oferta.
```

---

## 4. frontend-design (anthropics/skills, pasta `skills/frontend-design/`)

- **SHA e data:** `e4bb5d960d87126ff3b3a8af1a104b7db67560ba`, 16/11/2026 14:22 UTC. **É o último commit do repositório inteiro** ("Update docx, pptx and xlsx skills…"), não o último que mexeu nesta pasta: não consegui separar pela leitura que fiz. O texto lido é o do arquivo nesse commit.
- **Licença:** `LICENSE.txt` da pasta (10.174 bytes), Apache 2.0, texto padrão inteiro lido. **Não tem linha de copyright nem apêndice preenchido.** Pede: dar cópia da licença a quem receber; **avisar nos arquivos que você mudou** (cláusula 4b); manter os avisos de autoria (4c). Não há arquivo `NOTICE` na pasta.
- **Arquivos:** `SKILL.md` 9.390 bytes e `LICENSE.txt`. Nada mais.
- **O que roda:** nada. `SKILL.md` lido inteiro: só texto; não cita script, arquivo, rede nem fonte baixada. A descrição diz "making choices that don't read as templated defaults".
- **O que serve para nós (5 linhas):**
  1. **Duas passadas:** primeiro um plano curto (4 a 6 cores com nome e valor, tipos e seus papéis, ideia de layout com esboço em texto, princípios); **depois revisar o plano contra o pedido** e refazer o que for o padrão de qualquer página parecida, dizendo o que mudou e por quê. É o que o `impeccable` só detecta depois.
  2. **Uma ousadia só:** deixar um elemento como o memorável e o resto quieto; "tire um acessório antes de sair".
  3. **Regras de tipo que servem ao e-book:** linhas com menos de 80 caracteres, serifa com um pouco mais de entrelinha, não destacar uma só palavra do título, não usar caixa alta em rótulo, só numerar o que é sequência de verdade.
  4. **Partir da matéria do assunto** (material, vocabulário e uso da casa) em vez de modelo; escrever texto de interface pelo ponto de vista de quem usa.
  5. **Lista de "vícios de IA" para evitar** (creme com serifa e terracota; preto com verde ácido; cartões iguais com a mesma sombra; rótulo em caixa alta com ponto no meio): serve como **lista do que não fazer**, não como estilo.
- **O que NÃO pode entrar:**
  - **Qualquer estilo de arte vindo da skill** (o dono: "use o nosso próprio"). A skill, por si, não impõe estilo; a lista de vícios e as cores citadas (`#F4F1EA`, `#D97757`) são exemplos **do que evitar**. `#D97757` é a cor de interação do Claude: não usar em peça nossa. A identidade do projeto é a da `ECOSSISTEMA.md` (azul `#0B4FA8`, amarelo `#FFC857`, Bricolage Grotesque e Inter; o Designer confirma).
  - Movimento, hover, "responsivo até o celular" e foco de teclado são de página na tela; no PDF e na imagem do Instagram não se aplicam.
  - A seção "More on writing in design" **não manda no Redator**: texto de venda segue `redacao-que-vende` e o veto do Revisor.
  - Instalar por plugin ou por `npx`: só copiar a pasta, com o `LICENSE.txt`.
- **Recomendação: copiar a pasta** (2 arquivos), porque é curta e o valor está no texto exato da passada de revisão. Ao acrescentar a seção "Neste projeto", pôr a linha de mudança (Apache 4b).
- **Rascunho da seção:**

```markdown
## Neste projeto (X1-Plantas)

> Origem: github.com/anthropics/skills, `skills/frontend-design/SKILL.md` (commit e4bb5d96, 16/11/2026), licença Apache 2.0: o texto está em `LICENSE.txt`, nesta pasta. **Modificado em [data]:** acrescentada a seção "Neste projeto (X1-Plantas)"; o resto do texto é o original. Entrou em [data] a pedido do dono ("usa as 3, mas não use o estilo de referência de arte deles, use o nosso próprio"), com o veto do Revisor de risco ([resultado]; ficha `pedidos/2026-11/<ficha>`).

- **Leia antes:** `contexto/designer.md`, `ebook/referencias/VISUAL.md` (linguagem visual do projeto) e `ECOSSISTEMA.md` (o `impeccable`, que continua só detectando).
- **O estilo é o nosso, não o de ninguém:** a identidade vem do projeto (azul `#0B4FA8`, amarelo `#FFC857`, Bricolage Grotesque e Inter, planta no estilo 1 nas casas e o 3 na capa e no Instagram). A lista de "vícios" da skill serve **só como lista do que evitar**; `#D97757` e o fundo creme com serifa terracota **não entram**. Mudar identidade (cor, fonte, logo) é **opção para o dono**.
- **Onde se aplica:** capa, páginas do e-book (HTML para PDF pelo `livro.py`), carrosséis e posts. Movimento, hover e "responsivo" são de tela e não se aplicam ao PDF.
- **Não manda no texto:** a seção "More on writing in design" não vale para texto de venda; esse segue `.claude/skills/redacao-que-vende/` e o veto do Revisor de risco.
- **Nada da skill corta os avisos legais** nem dispensa "Não substitui o profissional"; a imagem de uma casa não promete aprovação, prazo ou custo (`ESTRATEGIA.md`, seção 9).
- **Quem usa:** o `designer`.
- Ela é membro do Conselho (`CONSELHO.md`); o que ela sugerir é opção para o dono, nunca decisão.
- **Prompt de entrada:** antes de desenhar, escreva o plano de duas passadas (4 a 6 cores nomeadas, tipos e papéis, layout com esboço, princípios) **partindo da identidade do projeto**; revise o plano contra o pedido e diga o que mudou e por quê; escolha **um** elemento memorável; liste o que mudou na identidade (se algo mudou) para o dono decidir.
```

---

## 5. canvas-design (anthropics/skills, pasta `skills/canvas-design/`)

- **SHA e data:** `e4bb5d960d87126ff3b3a8af1a104b7db67560ba`, 16/11/2026 (o mesmo da ficha 4; mesma ressalva).
- **Licença:** `LICENSE.txt` da pasta (11.345 bytes), Apache 2.0 inteiro, com apêndice "Copyright 2026 Anthropic, PBC." As **fontes** têm uma `*-OFL.txt` cada (SIL Open Font License; cada arquivo lido apenas como nome e tamanho, 4,4 KB; **não abri o texto de nenhuma**).
- **Arquivos:** `SKILL.md` 11.939 bytes; `LICENSE.txt`; pasta `canvas-fonts/` com **81 arquivos** (`.ttf` de 25 a 190 KB e uma `-OFL.txt` por família; soma de 5.530.719 bytes, cerca de 5,3 MB, somando os tamanhos da API), de Arsenal SC a Young Serif. Lista pela API; **não abri nenhum `.ttf`**.
- **O que roda:** nada próprio (sem script). O texto manda: 1) escrever um arquivo `.md` com uma "filosofia visual" de 4 a 6 parágrafos e nome de 1 a 2 palavras; 2) pintar **uma peça de 90% imagem e 10% texto** em PDF ou PNG, "como um livro de mesa" se pedir várias páginas, e dar **uma segunda passada de refino sem acrescentar gráficos**. Manda "usar as fontes de `./canvas-fonts`" e também **"Download and use whatever fonts are needed"** (rede e licença de fonte). Para gerar a peça, o modelo escreve e roda código dele (não vem script).
- **O que serve para nós (5 linhas):**
  1. **Nomear a direção antes de pintar** e só então executar: a filosofia vira o contrato da peça (capa, primeiro quadro do carrossel, arte do anúncio).
  2. **"Texto mínimo, imagem manda"** (90/10): combina com capa de e-book e com o primeiro quadro, que tem de parar o dedo.
  3. **Nada cai da página e nada se sobrepõe:** margens e respiro conferidos, "inegociável".
  4. **Segunda passada de polimento** em vez de acrescentar enfeite ("como tornar o que já está aqui mais coeso?").
  5. **Opção de várias páginas contando uma história**, útil para carrossel (primeira página, páginas irmãs com variações).
- **O que NÃO pode entrar:**
  - **O estilo de referência de arte deles** (dono): a lista de movimentos de exemplo ("Concrete Poetry", "Chromatic Language", "Analog Meditation", "Organic Systems", "Geometric Silence"), as referências a Josef Albers, Le Corbusier, "Polish poster", "Japanese photobook" e o parágrafo de "bíblia científica": "diagrama de uma disciplina imaginária", "marcadores de referência sistemáticos". São estilos e nomes de terceiros e fazem peça abstrata.
  - **A "referência sutil" ("tema como citação que só quem conhece sente")**: para o comprador classe C, 25 a 50 anos, a capa tem de dizer **no primeiro olhar** que casa cabe no lote. O Redator e o Revisor conferem a peça pública.
  - **Baixar fonte da internet e a pasta `canvas-fonts/`:** fontes só as do projeto (ou fonte de licença livre já conferida); a pasta tem cerca de 5,3 MB de arquivos que não usamos.
  - "Obra de museu", "mestre do ofício", "centenas de horas" repetidos como instrução: é enfeite de texto; não ajuda e pode virar promessa de qualidade no anúncio.
  - Ilustração que dê a entender que a casa já existe, está aprovada ou tem custo: o selo do projeto e as regras de `ESTRATEGIA.md` seção 9 continuam.
- **Recomendação: reescrever só o método**, em nosso português, em um `SKILL.md` curto (2 passos, 90/10, margens, segunda passada, várias páginas), **sem a pasta de fontes e sem os exemplos de movimento**, com uma linha "método adaptado de anthropics/skills, `canvas-design` (Apache 2.0)" e o `LICENSE.txt`. Cópia literal traria o estilo que o dono recusou.
- **Rascunho da seção (vai no fim do `SKILL.md` reescrito):**

```markdown
## Neste projeto (X1-Plantas)

> Origem: método adaptado de github.com/anthropics/skills, `skills/canvas-design/SKILL.md` (commit e4bb5d96, 16/11/2026), licença Apache 2.0: o texto está em `LICENSE.txt`, nesta pasta. **Reescrito em português**, sem a pasta `canvas-fonts/`, sem os exemplos de movimento e sem as referências de arte do original. Entrou em [data] a pedido do dono ("usa as 3, mas não use o estilo de referência de arte deles, use o nosso próprio"), com o veto do Revisor de risco ([resultado]; ficha `pedidos/2026-11/<ficha>`).

- **Leia antes:** `contexto/designer.md`, `ebook/referencias/VISUAL.md` e `ECOSSISTEMA.md`. A direção visual é a **do projeto** (azul `#0B4FA8`, amarelo `#FFC857`, Bricolage Grotesque e Inter), não a de um movimento de arte de terceiros.
- **Onde se aplica:** capa, primeira imagem do carrossel e arte de anúncio, onde **imagem manda e texto é pouco**. **Não se aplica** à página com planta, tabela ou preço.
- **A capa tem de dizer "que casa cabe no meu lote" no primeiro olhar:** nada de referência escondida nem peça abstrata. O que ela promete passa pela seção 9 do `ESTRATEGIA.md` e pelo veto do Revisor (nada de prazo, custo, aprovação, nem de dar a entender que a planta dispensa profissional).
- **Fontes: só as do projeto** (ou de licença livre já conferida pelo Designer). Nada de baixar fonte da internet.
- **Quem usa:** o `designer`; o `editor-video` só pega a imagem pronta.
- Ela é membro do Conselho (`CONSELHO.md`); o que ela sugerir é opção para o dono, nunca decisão.
- **Prompt de entrada:** antes de pintar, escreva a direção em 4 a 6 linhas **partindo da identidade do projeto** (nada de "movimento" de terceiros), diga o que a peça tem de mostrar no primeiro olhar e confira margens e sobreposição; na segunda passada, **tire** em vez de acrescentar; marque como **opção para o dono** qualquer mudança de identidade.
```

---

## 6. pdf-design (Georgi45/pdf-design)

- **SHA e data:** `a4d5444997a1912c13927a3bc08e5f133b29ba94`, 20/09/2026 23:37 UTC ("Release 1.2.0: plain description, and ignore the video working folders").
- **Licença:** `LICENSE`, MIT, "Copyright (c) 2026 Georgi Zagoruyko Krivtsov" (1.240 bytes, inteiro lido); a última linha diz que as fontes de `skills/pdf-design/assets/fonts` são **SIL OFL 1.1**, com os textos em `.../fonts/licenses`.
- **Arquivos de `skills/pdf-design/` (bytes):** `SKILL.md` 6.416; `references/` rules 4.290, page-types 5.568, themes 12.029; `assets/base.css` 13.545; `assets/themes/` 6 CSS de 4,5 a 4,9 KB (archive, gallery, ledger, poster, product, stage); `assets/fonts/` 10 famílias em `.woff2` (cerca de 1,0 MB) mais CSS e `licenses/*-OFL.txt`; `scripts/` **print.mjs 25.231, brand.mjs 28.551, fonts.mjs 3.483**. Fora da pasta: `README.md` 6.369, `AGENTS.md` 683, `.claude-plugin/marketplace.json` 587 e `examples/` (PDFs de até 1,1 MB). **Não há `package.json`**: o `print.mjs` diz "No npm: Node 22+ ships fetch and WebSocket".
- **O que roda (é a única das 6 que executa programa):**
  - `print.mjs <documento.html>`: **abre o Chrome, Chromium ou Edge sem tela** (`spawn`, com `--remote-debugging-port` numa porta aleatória entre 9222 e 9921, só no `127.0.0.1`, e `--no-sandbox` se o usuário for root), imprime o HTML em PDF com margem zero, mede cada folha (conteúdo cortado, texto sobre o rodapé, vão maior que 30% da folha, letra menor que 7 pt, fonte que caiu para a do sistema), confere se as fontes foram embutidas e **grava uma imagem PNG de cada folha**. Escreve ao lado do HTML: `<nome>.pdf` e a pasta `<nome>-review/` e **apaga essa pasta a cada rodada** (`rmSync` recursivo). Procura o navegador em caminhos fixos e em `CHROME_PATH`. **Não chama a rede por si** (o `fetch` é para o `127.0.0.1`); **recusa** HTML que ligue ao Google Fonts. Cola no PDF qualquer arquivo local que o HTML cite (imagem, `<!-- include: -->`).
  - `brand.mjs <fonte>`: transforma um `DESIGN.md`, `tokens.json`, CSS, HTML ou **uma URL** em tema. Com URL ele **busca a página e as folhas de estilo pela rede** (`fetch`); com `--fonts` chama o `fonts.mjs`.
  - `fonts.mjs`: **baixa fonte do Google Fonts** (`fonts.googleapis.com`) e a licença OFL de `raw.githubusercontent.com/google/fonts`.
  - Sem chave, sem variável de ambiente secreta, sem telemetria vista. **Exige Node 22+ e navegador:** não conferi se o ambiente do dono (PC com Windows e WSL) ou a nuvem os têm.
- **O que serve para nós (5 linhas):**
  1. **A folha é a unidade:** um plano por folha, **a manchete diz a conclusão** ("Instagram traz gente. O site perde.") e não o assunto; "se não cabe, são duas folhas, cada uma com a sua manchete"; nada de "continua na próxima".
  2. **Nada de página meio vazia nem moldura branca:** o aviso dispara quando há vão maior que 30% da folha; pouco conteúdo vira conteúdo maior (número grande, tabela mais folgada).
  3. **Área segura e mínimo de letra** (7 pt) conferidos por máquina, **e depois um olhar humano em cada PNG** com 5 perguntas (dá para entender só pela manchete? algum vão parece erro? algo cortado ou com pouco contraste? todas as folhas parecem da mesma família? a capa funcionaria como cartaz?).
  4. **"Não encolher a letra para caber; mover para outra folha."**
  5. **Tabela de quanto cabe numa A4** (área útil 178 x 265 mm; manchete de duas linhas 45 mm; linha de tabela 10 a 14 mm): régua simples para o `livro.py` e o Designer.
- **O que NÃO pode entrar:**
  - **Os seis temas e as 10 fontes** (poster, gallery, ledger, archive, product, stage): são estilo de terceiros; o dono quer o nosso. O próprio skill manda **perguntar "você já tem um estilo?"** e transformar o estilo existente em tema: a resposta é "sim, o do projeto".
  - **`brand.mjs` com URL** (busca página alheia pela rede, e o skill foi feito também para "copiar a cara" de um site) e **`fonts.mjs`** (baixa fonte): fora, por regra do projeto. Se um dia ligarmos o `brand.mjs`, só com arquivo local nosso.
  - **Rodar `print.mjs`** (abre navegador e porta local; apaga pasta) **sem a ficha e o veto**: só depois de ler os 3 scripts linha a linha (não li assim, ver abaixo) e do "sim" do Conselho. Hoje o `livro.py` já gera o PDF; o ganho aqui é a **conferência**, que se pode reescrever no nosso `checar.py` sem o navegador novo.
  - A regra "capa 90% imagem e 10% texto, título embaixo à esquerda, um elemento decorativo grande" e "uma só cor de destaque": são gosto do autor; servem de ponto de partida, **não de regra** do e-book, que já tem direção própria.
  - O pacote de `examples/` (PDFs de exemplo de 1,1 MB) e os símbolos que ele proíbe (⚠ ✓ → ●): só valem para as fontes dele.
  - Instalar como plugin (`/plugin marketplace`): só copiar a pasta, se um dia o Conselho aprovar o uso.
- **Recomendação: reescrever só o método** (plano por folha; manchete com conclusão; sem folha vazia; letra mínima; medir e olhar cada folha) como **seção de conferência no `contexto/designer.md` ou como regras novas no `livro.py` e no `checar.py`**; **não copiar** scripts, temas nem fontes. A cópia do `SKILL.md` sozinho não serve: ele depende dos três scripts e dos seis temas.
- **Rascunho da seção** (se o Conselho preferir uma skill própria de "conferência de folha", `SKILL.md` reescrito; senão, vira texto do `designer.md`):

```markdown
## Neste projeto (X1-Plantas)

> Origem: método adaptado de github.com/Georgi45/pdf-design, `skills/pdf-design/SKILL.md` e `references/rules.md` (commit a4d54449, 20/09/2026, versão 1.2.0), licença MIT, Copyright (c) 2026 Georgi Zagoruyko Krivtsov: o texto da licença está em `LICENSE`, nesta pasta. **Só o método**, reescrito em português: os scripts (`print.mjs`, `brand.mjs`, `fonts.mjs`), os seis temas e as fontes **não** foram copiados. Entrou em [data] a pedido do dono ("usa as 3, mas não use o estilo de referência de arte deles, use o nosso próprio"), com o veto do Revisor de risco ([resultado]; ficha `pedidos/2026-11/<ficha>`).

- **Leia antes:** `contexto/designer.md`, `ebook/referencias/VISUAL.md` e o gerador do e-book (`ebook/livro.py`). O estilo do PDF é o **do projeto** (azul `#0B4FA8`, amarelo `#FFC857`, Bricolage Grotesque e Inter); nenhum tema de fora entra.
- **O método:** planejar **uma folha por vez** (tipo, manchete que diz a conclusão, conteúdo, layout) e mostrar o plano ao dono antes de montar; **uma ideia por folha e preenchida**; se não cabe, são **duas folhas**, nunca letra menor; letra mínima de 7 pt e área segura medidas; **olhar cada folha em imagem** com as cinco perguntas (manchete basta? algum vão parece erro? algo cortado ou sem contraste? todas parecem da mesma família? a capa funcionaria sozinha como cartaz?).
- **A conferência é automática onde der:** quem mede é o `ferramentas/checar.py` ou o `livro.py`, não um navegador novo. **Não rodar `print.mjs`, `brand.mjs` nem `fonts.mjs`** (abrem navegador, buscam página e baixam fonte) sem o "sim" do dono e a leitura linha a linha dos scripts.
- **Nada da skill corta os avisos legais:** toda folha de casa mantém "Não substitui o profissional" e a regra de não prometer aprovação, prazo nem custo (`ESTRATEGIA.md`, seção 9).
- **Quem usa:** o `designer`.
- Ela é membro do Conselho (`CONSELHO.md`); o que ela sugerir é opção para o dono, nunca decisão.
- **Prompt de entrada:** antes de montar ou mudar uma folha do e-book, escreva o plano (tipo, manchete-conclusão, o que entra) e diga qual folha sobra ou falta; depois da montagem, abra a imagem de **cada** folha e responda às cinco perguntas por escrito; marque como **opção para o dono** qualquer mudança de identidade (cor, fonte, logo).
```

---

## Riscos transversais (para o Revisor de risco)

1. **Conteúdo que muda sozinho:** o repositório da InsightfulPipe se reconstrói duas vezes por dia e o `marketingskills` teve commit hoje. Só vale o SHA fixado; qualquer atualização é uma nova leitura.
2. **Nenhuma das 6 tem gancho, hook ou MCP próprio.** O único MCP citado é o da InsightfulPipe (de fora, não conectar). A única que executa programa é a `pdf-design`.
3. **Licenças:** quatro MIT (aviso e texto em cópia parcial ou substancial) e duas Apache 2.0 (copiar a licença; **anotar o que mudou**, cláusula 4b; a `frontend-design` não traz copyright próprio no texto). Nenhuma proíbe uso por IA nem uso comercial. **Leitura cautelosa nossa, não parecer jurídico.**
4. **A `copy-thief`, a `offers` e a `meta-click-to-message-ads` ensinam técnicas de empilhar valor, urgência e ancoragem.** Todas têm seção própria que proíbe a versão falsa; as nossas seções "Neste projeto" repetem o corte.

## O que não li (dito de uma vez)

- **meta-click-to-message-ads:** `sample_input.json` (49.651 bytes), `expected_output.json` (16.553) e `scripts/sync_plugin.py` (14.878): arquivos de teste e do espelhamento do site; o `SKILL.md` não os cita. Não vi nenhum.
- **copy-thief:** li inteiros `SKILL.md`, `README`, `LICENSE`, `CLAUDE`, `AGENTS`, `SECURITY`, `CONTRIBUTING`, `copilot-instructions`, `.gitignore`, `briefing.md`, `qa-review.md`, `form.html`, `reference/05`, `07`, `09` e o `swipe-file.md`. **As referências 01, 02, 03, 04 (menos o fim), 06, 08 e os 3 modelos foram varridos só por títulos e endereços** (zero endereços), não linha a linha.
- **offers:** `SKILL.md` e `LICENSE` inteiros; das referências li trechos (`scarcity-urgency` início, `guarantee-design` "baixo valor", `offer-formats` "produto de informação", `bonus-stacking` "valores inflados") e varri as 8 por títulos, endereços e comandos; `evals.json` só o começo.
- **frontend-design e canvas-design:** `SKILL.md` e `LICENSE.txt` inteiros de cada; da pasta de fontes só a lista de nomes e tamanhos.
- **pdf-design:** inteiros `SKILL.md`, `rules.md`, `LICENSE`, `AGENTS.md`, `marketplace.json`. **`print.mjs` e `brand.mjs` (25 KB e 28 KB) e `fonts.mjs` foram lidos por varredura de padrões de rede, processo e arquivo, mais os trechos de início, de busca de navegador e de porta; não linha a linha.** `page-types.md` saiu truncado na conversão (as etiquetas HTML foram comidas), `themes.md` só os títulos; `base.css`, os 6 temas, o `README` e os exemplos não foram abertos.
- **Todos:** o texto de cada licença está no commit fixado; não li o histórico de commits nem avisos de segurança do GitHub. Estrelas e downloads não foram usados como prova.

## Reconferência da ficha (pedido recebido)

| Pedido | Cumprido? |
|---|---|
| Abrir o `SKILL.md` e todo arquivo que ela cita, na página pública; fixar o SHA; ler a licença | **Sim, com as lacunas acima.** SHA pelos 6 e licença pelas 6 (lida inteira); nem todo arquivo foi lido linha a linha (lista em "O que não li") |
| Por skill: SHA e data; arquivos e tamanhos; o que roda; o que serve em 5 linhas; o que não pode entrar; rascunho da seção "Neste projeto" com prompt de entrada | Sim, nas 6 fichas |
| Recomendação por skill (copiar a pasta ou reescrever o método) | Sim: copiar 3 (`copy-thief`, `offers`, `frontend-design`), reescrever 3 (`meta-click-to-message-ads`, `canvas-design`, `pdf-design`) |
| Nada baixado, clonado, instalado ou executado; nada pago | Sim |
| Registrar com `pesquisa.py nova --tema ferramentas --quem pesquisador` | Ver o fim da resposta ao Maestro |
| Sem commit | Sim |

**Em aberto, de quem depende:**
- Dono: existe ou vai existir página de vendas (afeta o uso da `copy-thief`)? Quem responde o WhatsApp e em qual número (afeta a meta de resposta)? Quer manter a regra do travessão do autor (hoje fora)?
- Revisor de risco: veto sobre as seções "Neste projeto" e sobre a conferência da lista de anúncio da Meta (`reference/09` do copy-thief, fonte secundária).
- Maestro/Opus: passos 2 a 7 do roteiro; fixar a pasta por cópia só depois do veto; atualizar `ECOSSISTEMA.md`, `EQUIPE.md` e o `QUADRO.md`.
