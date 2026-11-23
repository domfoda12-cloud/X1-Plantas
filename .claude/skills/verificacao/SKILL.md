---
name: verificacao
description: Conferência do X1-Plantas antes de entregar ou fazer commit, num quadro só em português (Plantas, Checar, PDF, Painel, Fichas, Segredos). Dois modos, rápido (só o checar.py) e completo (mais painel, ruff como aviso e git status). Não corrige nada; erro vai ao /build-fix. Use antes de toda entrega e de todo commit, ou quando o dono pedir "confere tudo" ou /verificacao.
---

# Verificação

Adaptado de everything-claude-code (skills/verification-loop e commands/verify, juntos numa porta só; MIT, Copyright (c) 2026 Affaan Mustafa; licença em `LICENSE` nesta pasta e em `.claude/LICENCA-everything-claude-code.txt`). Origem: `ORIGEM.md`.

Ela só confere e relata. Não corrige, não faz commit, não faz push.

## Modo rápido

1. `python3 ferramentas/checar.py` (ele já roda `plantas.py validar`, `resumos.py --conferir`, `pedido.py conferir`, o PDF numa pasta temporária, o painel e a conferência "segredos no repositório"; nada é repetido).
2. Leia as linhas `[ERRO]` e `[AVISO]`. A saída tem de terminar em "Tudo certo".

## Modo completo

O rápido e mais:

3. `python3 ferramentas/atualizar-painel.py`: tem de dizer zero avisos.
4. `ruff check ferramentas/` só como **aviso** (há achados antigos); se o ruff não existir, pule sem erro e diga "ruff: não conferido".
5. Depois do checar: `git status` e `git diff --stat`. Lembre que o `checar.py` **regrava** arquivos (dados das plantas, `PLANTAS.md`, `CONSERTOS.md`, `video/src/plantas/`, calculadora, "Situação agora" do `PAINEL.md`): o diff pode ter mudança que não é sua. Se a calculadora (`ebook/vendas/calculadora-lote.html`) mudou, a página publicada no claude.ai precisa ser republicada.

## Segredos

O lugar único é a conferência "segredos no repositório" do `checar.py`. Mostre só o que ela mostra: arquivo:linha e tipo, nunca o valor.

## Quadro final

| Item | Resultado |
|---|---|
| Plantas | OK / ERRO (do `validador das plantas`) |
| Checar | OK / N problemas |
| PDF | OK / página estourada / campo pendente (aviso) |
| Painel | OK / N avisos |
| Fichas | OK / ERRO (do `pedido.py conferir`) |
| Segredos | OK / arquivo:linha |

Última linha, só com tudo OK:
- na `main`: "Pronto para commit e push";
- numa `sistema/<assunto>`: "Pronto para commit e pull request";
- numa `claude/*` (conversa na nuvem): "Pronto para commit e levar à main".

Com qualquer ERRO: "Não faça commit; leve ao `/build-fix`".

Fora daqui: pyright (baixa do npm e consulta a rede), `npm install`, `npm audit`, build, cobertura, commit e push.

## Neste projeto (X1-Plantas)

- Antes, leia o `contexto/QUADRO.md` e a ficha aberta em `pedidos/`. Português do Brasil, palavras simples.
- Ela não toca os avisos legais ("Planta de referência", "Não substitui o profissional", seção 9 do `ESTRATEGIA.md`) e não muda conferência para passar.
- Entra no fluxo: antes de toda entrega e de todo commit (regra do `CLAUDE.md`: commit só com "Tudo certo"); o `/ponto-de-volta` e o `/build-fix` a chamam. Membro do Conselho pelo `CONSELHO.md`.
- **Prompt de entrada:** "Rode a `verificacao` no modo <rápido|completo> e devolva o quadro final. Não corrija nada; nunca encadeie commit atrás de um checar filtrado." Quem usa: o Maestro (Opus).
