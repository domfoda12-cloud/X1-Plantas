# Contexto do Atualizador de documentos (oficina de código)

> Só o que importa para este papel. Antes de trabalhar, leia o [quadro](QUADRO.md). Entrou em 23/11/2026, adaptado do everything-claude-code (MIT; ficha `0209`).

## Decisões do dono que valem para você

- **Commit só com o `checar.py` em "Tudo certo"; nunca encadeado atrás de um checar filtrado** (lição do Maestro, 23/11). O commit é do Maestro, não seu.
- **Nada se baixa, instala ou roda da rede sem ficha** (`npx`, `npm install`, `npm ci`).
- **Leia barato** (22/11/2026): pasta no `INDICE.md`, o `RESUMO.md` dela e só então o documento. Documento novo: `python3 ferramentas/resumos.py`; programa novo entra no `MAPA-DO-SISTEMA.md`.
- **Arquivo fica junto do que tem a mesma função** (22/11/2026).

## O que já existe para você usar

- `resumos.py` gera os `RESUMO.md` e o `INDICE.md`; `--conferir` acusa documento fora do índice.
- Limites: `CLAUDE.md` 6500 caracteres, `contexto/*.md` 3500, `ferramentas/CLAUDE.md` e `video/CLAUDE.md` 2500 (o `checar.py` mede).

## Leia barato

O mapa: [`INDICE.md`](../INDICE.md). Quem chama quem: [`MAPA-DO-SISTEMA.md`](../MAPA-DO-SISTEMA.md).

## Lições

O que deu errado e não pode voltar (uma linha cada, com data).
