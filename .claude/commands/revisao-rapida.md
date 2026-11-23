---
description: Revisão curta do que mudou desde o último commit, antes de fazer o commit. Para revisão funda, /ponytail-review.
---

# /revisao-rapida

Adaptado de everything-claude-code (MIT, Copyright (c) 2026 Affaan Mustafa); licença em `.claude/LICENCA-everything-claude-code.txt`. Nome em português: o `/code-review` é skill embutida.

1. Arquivos mudados: `git diff --name-only -z HEAD` e `git ls-files -z --others --exclude-standard`, cortando em `\0` (nome com acento quebra a leitura por linha).
2. **Crítico:** chave ou token (mostre só arquivo:linha e tipo; o lugar único é a conferência "segredos no repositório" do `checar.py`), caminho montado com texto de fora sem conferir, erro engolido sem aviso.
3. **Regras deste projeto:** arquivo gerado editado à mão (`ebook/plantas/dados/*.json`, `PLANTAS.md`, `CONSERTOS.md`, `video/src/plantas/<ID>.js`, a lista CASAS da calculadora, `ebook/saida/`, "Situação agora" do `PAINEL.md`, os `RESUMO.md` e o `INDICE.md`). MAPA e resumos: rode o `checar.py` e leia o `[ERRO]`, sem refazer à mão.
4. Texto ao público com promessa de aprovação, prazo ou custo exato, ou que dá a entender que dispensa o profissional: só marque e chame o `revisor-de-risco`.
5. Resultado: cada achado com arquivo:linha e a correção em português simples. Achado crítico: "não faça commit até corrigir".

## Neste projeto (X1-Plantas)

- Revisão funda de uma mudança: só a `/ponytail-review` (o `ECOSSISTEMA.md` diz que `code-review` e `security-review` não se usam junto com o Ponytail sem decisão do Conselho).
- **Prompt de entrada:** "Revisão rápida do que mudou desde o último commit, ficha <caminho>." Quem usa: o Maestro antes de cada commit.
