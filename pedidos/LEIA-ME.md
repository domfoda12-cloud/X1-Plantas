# Pedidos do dono: como cada prompt vira trabalho

> Regra do dono (22/11/2026). Todo prompt dele é guardado, interpretado por um modelo e executado por outro, para o modelo caro pensar e o barato fazer o que é simples.

## O caminho de um prompt

1. **Entrada (automática).** O gancho `UserPromptSubmit` (em `.claude/settings.json`) chama `ferramentas/guardar-pedido.py`, que grava o prompt, palavra por palavra, em `pedidos/entrada/`. Essa pasta fica fora do git: é a caixa de entrada.
2. **Interpretação (Fable).** A conversa principal lê o prompt e escreve a **ficha** em `pedidos/AAAA-MM/AAAA-MM-DD-HHMM-assunto.md` (modelo abaixo): o que ele pediu, o que isso quer dizer, o que está pronto quando acabar, o que foi suposto e quem executa. Assunto pessoal do dono não vira ficha no repositório.
3. **Execução (outro modelo).** O Fable passa o trabalho pela ferramenta de agentes, com a ficha no pedido, e não executa ele mesmo o que a tabela manda delegar.
4. **Conferência (Fable).** O Fable confere o resultado contra a ficha, preenche "Resultado" e responde ao dono.

## Quem faz o quê

| Tipo de pedido | Modelo | Como chamar |
|---|---|---|
| Ler o prompt, interpretar, dividir, conferir e responder ao dono | **Fable** | a conversa principal |
| Trabalho do projeto: planta, texto, vídeo, código, design, revisão de risco | **Opus** | o agente do papel (`arquiteto`, `redator`, `designer`, `editor-video`, `estrategista`, `revisor-de-risco`); sem papel certo, agente geral com `model: opus` |
| Pesquisa a fundo: o Arquiteto aprender na web, norma, mercado, concorrente | **Sonnet** | `pesquisador` |
| Tarefa simples **para o dono** (não para os agentes): organizar um evento, responder uma pergunta, uma busca rápida, um lembrete | **Haiku** | `ajudante` |

- Na dúvida entre dois modelos, vale a regra do projeto: **qualidade primeiro** para o que vai ao público; o mais barato para o que é simples e pessoal.
- Pergunta curta sobre o próprio projeto, que o Fable já sabe responder sem trabalho, ele responde direto: abrir agente para isso gasta mais do que economiza.
- Tarefa de uma linha (trocar uma palavra, rodar a conferência) o Fable faz: delegar custa mais que fazer.
- O Revisor de risco continua com veto, e o dono continua decidindo preço, título, gasto e publicação.

## Modelo da ficha

```
# <assunto>
**Prompt (palavra por palavra):** …
**O que ele pediu:** …
**O que isso quer dizer para o projeto:** …
**Pronto quando:** …
**Suposições (o dono não disse):** …
**Quem executa:** <agente> (<modelo>)
**Resultado:** … (preenchido no fim, com os arquivos)
```

## Limites honestos

- A conversa principal só é o Fable se o dono a deixar nesse modelo (`/model`). A regra de delegar vale com qualquer modelo na conversa principal.
- O gancho só roda em conversa aberta **neste repositório**. Prompt antigo: `contexto/dono/PROMPTS.md`.
