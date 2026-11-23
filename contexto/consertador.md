# Contexto do Consertador (oficina de código)

> Só o que importa para este papel. Antes de trabalhar, leia o [quadro](QUADRO.md). Entrou em 23/11/2026, adaptado do everything-claude-code (MIT; ficha `0209`).

## Decisões do dono que valem para você

- **Commit só com o `checar.py` em "Tudo certo"; nunca encadeado atrás de um checar filtrado** (lição do Maestro, 23/11). O commit é do Maestro, não seu.
- **Nada se baixa, instala ou roda da rede sem ficha** (`npx`, `npm install`, `npm ci`).
- **Erro achado é corrigido antes de seguir** (`CLAUDE.md`), sem cortar aviso legal nem enfraquecer conferência.

## O que já existe para você usar

- `python3 ferramentas/checar.py` diz cada falha numa linha `[ERRO]`; `[AVISO]` não bloqueia (o PDF com preço e contato pendentes é aviso até o dono decidir).
- O `video/` usa npm com `package-lock.json`; o three está travado na 0.170.0. Instalar é com `npm ci`, só com ficha.

## Leia barato

Os programas: [`ferramentas/RESUMO.md`](../ferramentas/RESUMO.md). Quem chama quem: [`MAPA-DO-SISTEMA.md`](../MAPA-DO-SISTEMA.md).

## Lições

O que deu errado e não pode voltar (uma linha cada, com data).
