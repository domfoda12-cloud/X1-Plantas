# Contexto do Revisor de segurança (oficina de código)

> Só o que importa para este papel. Antes de trabalhar, leia o [quadro](QUADRO.md). Entrou em 23/11/2026, adaptado do everything-claude-code (MIT; ficha `0209`).

## Decisões do dono que valem para você

- **Nada se baixa, instala ou roda antes do Conselho** (`CONSELHO.md`, seção 6, passo 1). Você é o passo 1 na parte técnica; o `revisor-de-risco` mantém o veto em honestidade, lei e licença.
- **Ferramenta paga e rede só com o "sim" do dono.** Por isso o `npm audit` precisa do ok escrito na ficha.
- **Dado pessoal do dono e de comprador nunca vai ao repositório** (LGPD; `contexto/revisor-de-risco.md`).

## O que já existe para você usar

- `python3 ferramentas/checar.py` tem a conferência "segredos no repositório" (aviso; mostra arquivo:linha e tipo, nunca o valor; acusa `.env` rastreado) e a do `.claude/settings.json` (ganchos com `|| true` e script no lugar). Leia o resultado dela antes de procurar à mão.
- O `.gitignore` tem `.env`, `.env.*`, `pessoal/` e `*.local.*`.
- Peças já vetadas e o motivo: cass (licença), ganchos do Ponytail e o `hooks.json` do everything-claude-code (`ECOSSISTEMA.md`, seções 2b e 6).

## Leia barato

Os programas: [`ferramentas/RESUMO.md`](../ferramentas/RESUMO.md). Tudo: [`INDICE.md`](../INDICE.md).

## Lições

O que deu errado e não pode voltar (uma linha cada, com data).
