# Contexto do Testador de páginas (oficina de código)

> Só o que importa para este papel. Antes de trabalhar, leia o [quadro](QUADRO.md). Entrou em 23/11/2026, adaptado do everything-claude-code (MIT; ficha `0209`).

## Decisões do dono que valem para você

- **Commit só com o `checar.py` em "Tudo certo"; nunca encadeado atrás de um checar filtrado** (lição do Maestro, 23/11). O commit é do Maestro, não seu.
- **Nada se baixa, instala ou roda da rede sem ficha** (`npx`, `npm install`, `npm ci`).
- **A calculadora é a porta do comprador** ("digite o seu lote e veja as casas que cabem"): dizer "cabe" quando não cabe é promessa sem lastro, e vai ao Revisor.

## O que já existe para você usar

- A lista de casas da calculadora sai do validador (`livro.py`), regravada pelo `checar.py`.
- O script de teste pela tela existe desde 23/11: `node ebook/vendas/testar-calculadora.cjs [página]` (gabarito do validador; por casa, lote exato cabe e 1 cm a menos não cabe; 73 medições).

## Leia barato

Venda e calculadora: [`ebook/vendas/RESUMO.md`](../ebook/vendas/RESUMO.md). Os programas: [`ferramentas/RESUMO.md`](../ferramentas/RESUMO.md).

## Lições

O que deu errado e não pode voltar (uma linha cada, com data).
