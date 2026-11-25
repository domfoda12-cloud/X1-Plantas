# Prompt audit (25/11/2026)

> Pedido do dono (25/11): "prompt audit", com o reel do comando `prompt-audit` da skill `claude-api` ("Era isso que quis dizer"). Feito com o roteiro da skill: relatório e diff proposto. **Nada foi aplicado.** O diff está em `prompt-audit-2026-11-25.diff`, ao lado deste arquivo.

## Suposições

- **Escopo:**
  - Os 4 `CLAUDE.md` (raiz, `ebook/`, `video/`, `ferramentas/`).
  - Os 11 agentes de `.claude/agents/`.
  - As 7 skills escritas pelo projeto (`bom-dia`, `conselho`, `design-editorial`, `explicar-ao-dono`, `oferta-e-whatsapp`, `redacao-que-vende`, `triagem-email`).
  - `ferramentas/salvar.py`, só a linha de atribuição.
- **Fora do escopo:**
  - As skills de terceiros copiadas (`marketing-psychology`, `ponytail*`, `make-pdf`): só a busca de padrões, sem edição, porque uma atualização delas desfaz a mudança.
  - `.claude/settings.json`: a regra da skill manda não ler.
  - Os `contexto/*.md`.
- **Modelo-alvo:** Claude Opus 5.5 (o dono trocou a sessão para ele em 25/11). Cada agente que fixa o próprio modelo é medido contra ele: `ajudante` no Haiku, `pesquisador` no Sonnet, `supervisor` no Fable, o resto no Opus.

## Resumo

Os arquivos estão limpos dos vícios do reel. Não há MAIÚSCULAS gritando, "pense passo a passo" nem tags de rascunho.

**Os problemas que importam são outros:**
- regras que o próprio dono mudou e que continuam escritas do jeito antigo;
- um "pare e espere" que um agente não consegue cumprir;
- o nome do modelo fixo no programa de salvar.

**As três de maior efeito:**
1. **O Planejador e a skill do Conselho ainda mandam trabalhar em paralelo** ("Agora" com até 3 passos; Conselho completo com todos os agentes ao mesmo tempo). Isso contraria a sua regra de 24/11, 20:45 (uma tarefa por vez, no máximo 2 agentes juntos), que está no quadro e na tarefa agendada.
2. **"Pare e espere a aprovação"** no Redator e na skill de oferta: o Redator roda como agente e não tem como esperar. Ontem ele avisou que a skill mandava parar e escreveu assim mesmo.
3. **"Pense antes, na medida do trabalho"** em 11 agentes e no `CLAUDE.md`. No Opus 5.5 o raciocínio está sempre ligado e quem controla a profundidade é a configuração (`effort`), não o texto. O que você quer, pelo pedido de 24/11 ("todo mundo planejando muito bem"), é um **plano escrito**. A troca proposta diz isso.

**Contagem:**
- Grupo 1 (texto datado): 2 achados que viram edição, mais 3 avisos.
- Grupo 2 (arquivos de regra): 6 achados que viram edição, mais 3 avisos.
- Grupo 3 (descrição de ferramenta): zero.
- Grupo 4 (código que chama a API): não se aplica, o projeto não chama a API. A lista de agentes foi conferida: não há dois agentes fazendo a mesma coisa.

## Achados com edição proposta (no diff)

| # | Onde | Trecho | Padrão | Por que está velho | Confiança | Ação |
|---|---|---|---|---|---|---|
| 1 | `.claude/agents/planejador.md:13` e `:20` | "**Agora** (no máximo 3 passos...)"; "de 1 a 3 passos abertos, sempre" | Grupo 2: regras que se contradizem | A regra do dono de 24/11, 20:45 (`contexto/QUADRO.md`, `decisoes-do-dono-2026-11-23.md`) é uma tarefa principal e no máximo um apoio. A regra do Planejador é anterior. | Alta | reescrever: "uma tarefa principal ... e no máximo um passo de apoio" |
| 2 | `.claude/skills/conselho/SKILL.md:14` | "abra os agentes de `.claude/agents/` em paralelo" | Grupo 2: regras que se contradizem | O mesmo: no máximo 2 agentes juntos (24/11, 20:45). | Alta | reescrever: "no máximo dois de cada vez" |
| 3 | `.claude/agents/redator.md:60`; `.claude/skills/oferta-e-whatsapp/SKILL.md:25` e `:67` | "**pare e espere a aprovação**" | Grupo 2: grau de liberdade errado | Um agente devolve o trabalho uma vez e acaba, não tem como esperar. Ontem o Redator escreveu que a skill mandava parar e seguiu mesmo assim (`oferta-so-casa-compacta-2026-11-24.md:23`). A regra que se quer é "aprovação antes do texto, salvo se o pedido já a traz". | Média | reescrever: "devolva primeiro o diagnóstico e a estrutura...; se o pedido já traz a aprovação, escreva e diga que pulou a parada" |
| 4 | `ebook/CLAUDE.md:12` | "O e-book está no rascunho 1 e fechado. Faltam ... título, preço, bônus, WhatsApp e promessa de atualização." | Grupo 2: fato velho | O `ebook/config.json` já tem `preco: "R$ 47"` e os 2 bônus, e o e-book foi refeito com 3 casas em 23/11. | Alta | reescrever com o que falta de fato: título, WhatsApp e promessa de atualização |
| 5 | `.claude/agents/redator.md:15` | "Os atributos mais fortes do rascunho 1 são..." | Grupo 2: fato velho | O "rascunho 1" foi substituído (lançamento com 3 casas, 23/11). A lista continua valendo como hipótese. | Média | reescrever: "...até um teste de venda mostrar outros, são..." |
| 6 | `CLAUDE.md:50`; `.claude/skills/conselho/SKILL.md:18` e `:29` | "commit e push"; "faça commit"; "faça o commit e o push na branch `main`" | Grupo 2: fato velho / contradição | Desde 23/11 o projeto salva com `ferramentas/salvar.py`: ele roda o `checar.py` e só salva verde. Nenhum arquivo de regra cita esse programa, e um agente que siga o texto pode salvar com o `checar.py` vermelho. | Média | reescrever para `python3 ferramentas/salvar.py "mensagem"` |
| 7 | `ferramentas/salvar.py:13` | `Co-Authored-By: Claude Fable 5.2` | Grupo 1d: fóssil de modelo | A sessão roda no Claude Opus 5.5 desde 25/11, e todo commit continua assinado com o modelo antigo. | Alta | reescrever para `Claude Opus 5.5`. Aviso: o nome volta a envelhecer na próxima troca de modelo; o certo seria ler o nome da sessão, que é mudança de código (fica para você decidir). |
| 8 | `CLAUDE.md:15` e a linha 10 dos 11 agentes | "**Pense antes**, na medida do trabalho (mais para o que é grande...)" | Grupo 1b: texto que dirige a profundidade do raciocínio, e "planeje antes" | No Opus 5.5 o raciocínio está sempre ligado e a profundidade se regula pela configuração. Texto pedindo para "pensar mais" não muda isso e pode levar a planejar demais. Por trás da linha há um pedido seu de verdade (22 e 24/11), um plano que se possa ver, e ele fica. | Média | reescrever: "**Plano antes de trabalho grande**: entrega pública, cara ou com mais de 3 passos começa por um plano curto escrito (o que vai fazer, o que supõe, 'pronto quando')" |

## Avisos, sem edição

| # | Onde | O que é | Por que não entra no diff | Confiança |
|---|---|---|---|---|
| 9 | `ferramentas/plano.py:201`, `:207`, `:272` | O código ainda aceita até 3 passos em "Agora" e enche até 3. | É código, não texto. Se o achado 1 entrar, o `plano.py` precisa do mesmo limite, senão o Planejador e a ferramenta brigam. O Planejador apontou isso em 24/11. | Alta (contradição), fora do escopo do diff |
| 10 | `.claude/agents/planejador.md:13-35` | São 24 regras, muitas nascidas de um incidente ("Prova 4", "conserto de planta"). | Padrão "acúmulo de remendos" (1d). Juntar em princípios é trabalho grande, e o resultado precisa ser comparado: só vale com uma prova antes e depois. | Média |
| 11 | 7 agentes: "**Reconfira antes de entregar**: releia os pedidos do dono na ficha, um por um..." | Parece o "confira duas vezes" do reel, mas pede uma entrega concreta (a lista de pedidos cumpridos e não cumpridos), que você usa para conferir. | A lista de preservação manda manter o critério de qualidade. Não é ritual. | Baixa |
| 12 | Todos os arquivos: "(dono, 22/11/2026)" ao lado das regras | Padrão "narrativa histórica" (Grupo 2). | A data é a prova de que a regra é sua ("nada do que ele faz é por acaso"). Tirar quebraria o histórico. | Baixa |
| 13 | `.claude/agents/editor-video.md:21` | "o sistema antigo `render.cjs` foi apagado em 22/11/2026...; volta pelo git" | Narrativa histórica, mas diz onde recuperar o arquivo. | Baixa |
| 14 | `.claude/skills/marketing-psychology/SKILL.md` (24 KB) e `ponytail*` | Skills de terceiros, longas. Carregam só quando são chamadas. | Editar a cópia desfaz na próxima atualização. Se pesarem, o caminho é tirar a skill, pela mesa do Conselho. | Baixa |

## Conferido e limpo

- **Caminhos citados:** todos existem, exceto o `render.cjs`, que foi apagado de propósito (achado 13).
- **Arquivos de regra entre si:** fora dos achados 1, 2 e 6, não se contradizem.
- **Descrições dos agentes** (o texto que decide quando cada um é chamado): curtas e certas. Nada a mudar.

## Como aplicar

Você escolhe os achados. Para aplicar o diff inteiro:

```bash
git apply -p1 pedidos/anexos/prompt-audit-2026-11-25.diff
```

Você também pode aplicar só parte dele. O `CLAUDE.md` e o `salvar.py` só mudam com o seu "sim" (regra do projeto). Se o achado 1 entrar, o `plano.py` (aviso 9) precisa mudar junto.
