# O Conselho: quem opina, quem decide e quais skills cada um usa

> Lido por toda sessão via [`CLAUDE.md`](CLAUDE.md). Para rodar: `/conselho <tarefa>`. Painel: [`PAINEL.md`](PAINEL.md).

## 1. Por que existe

Temos muitas skills, conectores e scripts. Usar todos em toda tarefa gasta tempo e dinheiro; usar o errado gera trabalho jogado fora. O Conselho é um filtro rápido: cada especialista olha a tarefa pelo seu ângulo, diz se a skill dele ajuda a **vender mais, gastar menos ou arriscar menos**, e só o que passa é usado.

## 2. Os membros

| Membro | Pergunta que sempre faz | Skills e ferramentas que ele propõe | Agente |
|---|---|---|---|
| **Maestro** (preside) | "Isso é a coisa mais importante da semana?" | Painel, rotina, divisão de tarefas | a sessão principal; no Mac, a MinoAI Frontier ([`MAESTRO.md`](MAESTRO.md)) |
| **Redator** | "Que atributo faz o Marcos querer comprar?" | `/redacao-que-vende`, banco de [atributos](ebook/vendas/atributos-que-vendem.md), ganchos virais da MinoAI Frontier | [`redator`](.claude/agents/redator.md) |
| **Estrategista** | "Quanto isso muda o custo por venda?" | Painel (seções 4 e 7), números das contas, preço da concorrência | [`estrategista`](.claude/agents/estrategista.md) |
| **Arquiteto** | "Está tecnicamente certo e é verdade?" | `ferramentas/plantas.py` (validar, prévia, fichas), [regras](ebook/referencias/regras-do-arquiteto.md) | [`arquiteto`](.claude/agents/arquiteto.md) |
| **Revisor de risco** (veto) | "Isso promete algo que não podemos cumprir?" | [Relatório jurídico](reports/Arquiteto%20e%20engenheiro%20na%20constru%C3%A7%C3%A3o%20residencial.md), [FAQ](ebook/vendas/faq-compradores.md), tom de voz | [`revisor-de-risco`](.claude/agents/revisor-de-risco.md) |
| **Designer** | "Parece profissional ou parece genérico?" | `impeccable` (só para detectar o genérico e opinar), gerador do e-book, `artifact-design` | [`designer`](.claude/agents/designer.md) |
| **Pesquisador** | "Temos fonte para isso?" | TinyFish (busca e leitura; recursos pagos só com o "sim"), `deep-research`, `watch` para vídeos | [`pesquisador`](.claude/agents/pesquisador.md) |
| **Editor de vídeo** | "Segura a atenção nos 3 primeiros segundos?" | MinoAI Frontier (só no Mac/PC do dono), `video/render*.cjs` | [`editor-video`](.claude/agents/editor-video.md) |

## 3. Como uma opinião é dada

Cada membro responde em **uma linha**, sempre no mesmo formato:

```text
[Membro] SIM | NÃO | SIM, SE … · skill: <qual> · efeito: venda +/0/- · custo: R$ ou minutos · por quê: <uma frase>
```

## 4. Como se decide

1. **Quem fala:** o Maestro chama só quem tem a ver com a tarefa (texto → Redator, Revisor; planta → Arquiteto, Designer; anúncio → Redator, Estrategista, Editor, Revisor).
2. **Aprovado** quando a maioria dos chamados diz SIM e o Revisor de risco não vetou.
3. **Empate:** vence o lado com o maior efeito em venda; se ainda empatar, o mais barato.
4. **Veto do Revisor:** só por honestidade ou lei. Ele precisa dizer o que mudar para virar SIM.
5. **Reservado ao dono** (o Conselho só recomenda): preço, título, bônus, gasto com anúncio, publicar ou apagar post, contratar alguém, usar ferramenta paga.
6. **Registro:** decisões de entrega ao público vão para a seção 6 abaixo, com data. Decisões do dono vão para [`PAINEL.md`](PAINEL.md), seção 8.

## 5. Conselho de bolso x conselho completo

| | De bolso | Completo |
|---|---|---|
| Quando | Ajuste, texto interno, correção | Tudo o que vai ao público (anúncio, página do e-book, post), escolha de ferramenta paga, mudança de estratégia |
| Quem | Até 3 membros, opinião escrita pela própria sessão | Os membros chamados, cada um como subagente, em paralelo |
| Custo | Segundos | Minutos; vale quando o erro custaria uma venda ou um anúncio |

## 6. Registro de decisões do Conselho

| Data | Tarefa | Votos | Decisão | Resultado medido |
|---|---|---|---|---|
| 20/11/2026 | Criar o Conselho e o Redator | Maestro SIM, Estrategista SIM (menos retrabalho), Revisor SIM, SE o veto valer para todo texto público | Criado | A medir: tempo até a primeira peça aprovada |
