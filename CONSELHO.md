# O Conselho: quem opina, quem decide e quais skills cada um usa

> Lido por toda sessão via [`CLAUDE.md`](CLAUDE.md). Para rodar: a skill `conselho` (`/conselho <tarefa>`). Painel: [`PAINEL.md`](PAINEL.md).

## 1. Por que existe

Temos muitas skills, conectores e scripts. Usar todos em toda tarefa gasta tempo e dinheiro; usar o errado gera trabalho jogado fora. O Conselho é um filtro rápido: cada especialista olha a tarefa pelo seu ângulo, diz se a skill dele ajuda a **vender mais, gastar menos ou arriscar menos**, e só o que passa é usado.

## 2. Os membros

| Membro | Pergunta que sempre faz | Skills e ferramentas que ele propõe | Agente |
|---|---|---|---|
| **Maestro: MinoAI Frontier** (preside e **opina sempre, em primeiro**) | "Isso faz o comprador parar, comentar e mandar o Pix?" | Método da MinoAI (`search_mino_method`), ganchos virais (`search_viral_hooks`), análise de gancho (`analyze_hook`), números das contas (`get_account_stats`), edição no Mac | No Mac, é a própria sessão com a MinoAI. Em qualquer outra sessão, a opinião dele vem das ferramentas da MinoAI Frontier, citando a fonte ([`MAESTRO.md`](MAESTRO.md)) |
| **Redator** | "Que atributo faz o Marcos querer comprar?" | `/redacao-que-vende`, banco de [atributos](ebook/vendas/atributos-que-vendem.md), ganchos virais da MinoAI Frontier | [`redator`](.claude/agents/redator.md) |
| **Estrategista** | "Quanto isso muda o custo por venda?" | Painel (seções 4 e 7), números das contas, preço da concorrência | [`estrategista`](.claude/agents/estrategista.md) |
| **Arquiteto** | "Está tecnicamente certo e é verdade?" | `ferramentas/plantas.py` (validar, prévia, fichas), [regras](ebook/referencias/regras-do-arquiteto.md). No código das ferramentas: `/ponytail` (a menor mudança que resolve, sem cortar validação), `/ponytail-review` (revisão de uma mudança) e `/ponytail-audit` (auditoria do repositório inteiro) | [`arquiteto`](.claude/agents/arquiteto.md) |
| **Revisor de risco** (veto) | "Isso promete algo que não podemos cumprir?" | [Relatório jurídico](reports/Arquiteto%20e%20engenheiro%20na%20constru%C3%A7%C3%A3o%20residencial.md), [FAQ](ebook/vendas/faq-compradores.md), tom de voz | [`revisor-de-risco`](.claude/agents/revisor-de-risco.md) |
| **Designer** | "Parece profissional ou parece genérico?" | `impeccable` (só para detectar o genérico e opinar), gerador do e-book, `artifact-design`. Pede imagens à MinoAI (OpenArt), não gera | [`designer`](.claude/agents/designer.md) |
| **Pesquisador** | "Temos fonte para isso?" | TinyFish (busca e leitura; recursos pagos só com o "sim"), `deep-research`, `watch` para vídeos | [`pesquisador`](.claude/agents/pesquisador.md) |
| **Editor de vídeo e imagem: MinoAI Frontier** | "Segura a atenção nos 3 primeiros segundos? A imagem faz querer a casa?" | **Edição de vídeo:** MinoAI Frontier (no Mac/PC do dono). **Criação de imagem e vídeo gerado:** MinoAI usando o OpenArt (plugin `openart:*`: `performance-ads`, `hook-variants`, `ugc`, `tvc`…). Base 3D/2D: `video/render*.cjs` | [`editor-video`](.claude/agents/editor-video.md) |

## 3. Como uma opinião é dada

Cada membro responde em **uma linha**, sempre no mesmo formato:

```text
[Membro] SIM | NÃO | SIM, SE … · skill: <qual> · efeito: venda +/0/- · custo: R$ ou minutos · por quê: <uma frase>
```

## 4. Como se decide

0. **O Maestro (MinoAI Frontier) opina em toda tarefa, sem exceção**, de bolso ou completa, antes dos outros. A opinião dele é baseada nas ferramentas da MinoAI, com a fonte, e aparece para o dono junto com a entrega (decisão do dono, 20/11/2026).
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

Pedido do dono (20/11/2026): "toda skill nova no ecossistema alcança tudo". Vale para skill do projeto (`.claude/skills/`), agente (`.claude/agents/`), plugin e conector. Nada é usado antes de passar por estes passos:

1. **Ler o que ela roda.** Ganchos, acesso à rede, dados que saem do projeto, arquivos fora da pasta. O Revisor de risco confere e pode vetar uma parte (foi o que aconteceu com os ganchos do Ponytail).
2. **Conselho de bolso** decide se entra, com o Maestro primeiro.
3. **Registrar** na tabela de membros (seção 2: quem usa e quando) e no registro de decisões (seção 7).
4. **Ensinar o projeto.** Toda skill do projeto ganha a seção `## Neste projeto (X1-Plantas)` no `SKILL.md`; todo agente lê `CLAUDE.md` e o seu `contexto/<agente>.md` (não o histórico inteiro) e escreve um resumo de passagem em `contexto/entregas/` ao terminar. A seção diz o que ler antes, o idioma, as regras que não mudam, onde ela entra no fluxo e que ela nunca corta os avisos legais. Plugin e conector, que ficam fora do repositório, recebem o mesmo texto na mensagem do primeiro uso.
5. **Rodada de alcance.** Rodar a skill uma vez sobre o que já existe onde ela se aplica (exemplo: auditoria no código já escrito, Redator nos textos já publicados). O resultado vai para o `CONTEXTO.md`, e o que precisar de "sim" vai para "Em aberto".
6. **Inventário:** todo nome entra em [`ECOSSISTEMA.md`](ECOSSISTEMA.md) com status (integrado, liberado não usado, ferramenta do Claude Code). Plugin e conector que abrem sessão ou agente próprio recebem o texto de entrada de lá.
7. **Conferência automática.** O `python3 ferramentas/checar.py` dá erro se alguma skill de `.claude/skills/` não tiver a seção "Neste projeto" ou não estiver citada aqui, ou se algum agente de `.claude/agents/` não estiver citado aqui.

## 7. Registro de decisões do Conselho

| Data | Tarefa | Votos | Decisão | Resultado medido |
|---|---|---|---|---|
| 20/11/2026 | Criar o Conselho e o Redator | Maestro SIM, Estrategista SIM (menos retrabalho), Revisor SIM, SE o veto valer para todo texto público | Criado | A medir: tempo até a primeira peça aprovada |
| 20/11/2026 | Adicionar o Ponytail (skills de código) | Maestro: neutro (é código, não toca venda nem vídeo; o método da MinoAI não fala de ferramenta de código). Estrategista SIM (menos código e retrabalho nas ferramentas). Revisor SIM, só as skills: os ganchos do plugin gravam fora do projeto e podem mandar dados para um webhook | Entraram só as 3 skills em `.claude/skills/` (ponytail, ponytail-review, ponytail-audit), sem ganchos | A medir: erros achados pelo `checar.py` depois de cada mudança de código |
| 21/11/2026 | Vídeo principal E07 com OpenArt, trilha original de 128 BPM e logo | Maestro SIM, SE (1º segundo contido); Editor SIM, SE; Arquiteto SIM, SE (textos e rede); Revisor SIM, SE (selos, lote junto do "Cabe", sem marcas); Designer SIM, SE (sem ciano, papel real) | Aprovado com condições ([plano](video/plano-principal-e07.md), seção 7) | A medir: tempo médio assistido e % que chega ao drop (7,5 s) |
| 22/11/2026 | Selo "Imagem ilustrativa" nos vídeos | Revisor exigia; **o dono tirou a condição** | Sai o selo; o aviso legal fica pequeno, num canto, parado. Registrado em `video/CLAUDE.md` e `contexto/revisor-de-risco.md` | A medir: nenhuma reclamação de "achei que a casa existia" no WhatsApp |
