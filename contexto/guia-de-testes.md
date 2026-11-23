# Contexto do Guia de testes (oficina de código)

> Só o que importa para este papel. Antes de trabalhar, leia o [quadro](QUADRO.md). Entrou em 23/11/2026, adaptado do everything-claude-code (MIT; ficha `0209`).

## Decisões do dono que valem para você

- **Commit só com o `checar.py` em "Tudo certo"; nunca encadeado atrás de um checar filtrado** (lição do Maestro, 23/11). O commit é do Maestro, não seu.
- **Nada se baixa, instala ou roda da rede sem ficha** (`npx`, `npm install`, `npm ci`).
- **Planta nova só entra se passar em `plantas.py validar`** (`CLAUDE.md`). Área e medida que vão ao público são do Arquiteto.

## O que já existe para você usar

- A lista `_casos` do `checar.py` já tem 17 casos (regra das paredes e régua das 51 referências), cada conta numa `lambda` dentro de `try`: um caso quebrado falha sozinho, sem derrubar o checar.
- A lista única dos arquivos que exigem caso antes do conserto está na skill `ponytail`, seção "Neste projeto".
- O unittest em `ferramentas/testes/` ficou adiado (sem testes, ele sai com código 5 e quebraria o checar).

## Leia barato

Os programas: [`ferramentas/RESUMO.md`](../ferramentas/RESUMO.md). As plantas: [`ebook/RESUMO.md`](../ebook/RESUMO.md).

## Lições

O que deu errado e não pode voltar (uma linha cada, com data).
