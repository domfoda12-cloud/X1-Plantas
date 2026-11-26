# Último resumo de passagem

## 2026-11-26-0933-fluxos-fixos-ultra-max

**Tarefa:** construir os fluxos fixos "ultra max" do dono (ficha `2026-11-26-0721`, plano `pedidos/anexos/plano-fluxos-2026-11-26.md`).
**Feito:** mapa das conferências (`pedidos/anexos/mapa-conferencias-2026-11-26.md`). `ferramentas/fluxo.py`: texto e página contra as regras e o `PLANTAS.md`, passe com forma fixa, júri que recusa rodada incompleta, registro do gasto, lições sozinhas e prova que endurece. 5 fluxos em `.claude/workflows/` e o ensaio `ferramentas/fluxos-ensaio.cjs`, que roda no `checar.py` e confere a falha fechada. Guia: `pedidos/fluxos/LEIA-ME.md`.
**Rodado em peça real:** funil do WhatsApp (SIM SE da Vera aplicado; a calculadora diz "lote mínimo dela"), pág. 11 da C01 (SIM SE aplicado), rascunho C01V da parede da varanda (pronto para aplicar, salvo em `pedidos/anexos/rascunhos-prontos/`), calibração do júri (3 de 3 erros pegos) e a prova 5 (Caio, Rui e Vera: 5 de 6).
**Como conferir:** `python3 ferramentas/checar.py`; `python3 ferramentas/fluxo.py relatorio`; `pedidos/fluxos/RODADAS.md`.
**Não feito / ressalva:** o C01V não foi aplicado à oficial (outro passo, com a frase nova aprovada pela Vera). O peso dos jurados da regra 5 ainda não existe em programa. A regra do lote em post curto espera a Vera (texto da Olga no quadro).
**Decisão do dono pendente:** nenhuma deste trabalho.
**Próximo passo:** depois de cada fluxo, anote o total que a ferramenta devolve: `python3 ferramentas/fluxo.py gasto ultima <tokens>`. Sem isso, o `checar.py` fica vermelho.
