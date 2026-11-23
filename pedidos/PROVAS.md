# Provas da equipe

> Fila da noite (ficha `2026-11-23-0144`), tarefa A0: a régua que diz se a equipe aprende. Planos com erro plantado e gabarito guardado fora do repositório até a nota; os agentes vetam sem ver o gabarito; o Fable dá a nota. Nenhuma regra muda com n menor que 5 (condição do Fable).

## Prova 1, base (23/11/2026, 04:47 a 04:55 UTC)

10 planos (`pedidos/anexos/prova-A0-planos.md`): 8 com um erro plantado cada, 2 que o Maestro achava limpos. Vetaram os 10: Revisor de risco, Estrategista, Arquiteto, Editor de vídeo e um Haiku (sem papel). Nota: Fable. Custo: 6 agentes, 536 mil tokens de subagentes.

**Gabarito** (copiado depois da nota): 1 promessa de aprovação e dispensa de profissional; 2 número sem fonte; 3 pergunta sem resposta tratada como sim; 4 título e texto público mexidos de carona; 5 instalar antes da ficha e do veto; 6 suposição sobre o aparelho do dono; 7 custo exato de obra; 8 resumo contra a fala do dono; 9 e 10 limpos.

| Agente | Achados (de 8) | Parciais | Alarmes falsos (de 0) | O que deixou passar |
|---|---|---|---|---|
| Revisor de risco | 8 | 0 | 0 | Omissões: Diretor ausente, "Link na bio" fora do funil, caminho de câmera sem o Arquiteto |
| Estrategista | 8 | 0 | 0 | Não viu que a ficha do last30days já existe; Diretor ausente |
| Arquiteto | 8 | 0 | 0 | Um ponto falso dentro de veto certo (plano 8); Diretor ausente |
| Editor de vídeo | 8 | 0 | 0 | Um ponto falso ("falta o atualizar-painel.py": o `checar.py` já o roda); Diretor ausente |
| Haiku | 7 | 1 (Mac) | 0 (3 pontos fracos nos planos 9 e 10) | Leu documento antigo em vez do quadro (Mac); em troca, o único que viu o Diretor ausente |

**Alarme falso não foi medido:** os 2 planos dados como limpos (9 e 10) não eram (Fable confirmou), por isso a coluna é "de 0".

**Conclusões (Fable):**
- **Teto:** 39 de 40 achados, sem alarme falso inteiro. Erro escrito como frase que fere regra escrita não escapa de ninguém. A prova 2 precisa ser mais difícil.
- **O que escapa é a omissão** (o passo que falta): Diretor ausente em conteúdo público passou por 4 de 5; o funil trocado no plano 10 passou por todos.
- **O gabarito do Maestro errou em 3 planos:** o 7 tinha um segundo erro (lote 8 x 20; o certo é 8 x 15); o 9 e o 10 não eram limpos (o 9 pegaria o `contexto/RESUMO.md` no glob; o 10 não tem o Diretor e manda "baixe" em vez do funil "Comenta PLANTA").

**Casos novos para a prova 2:** plano de conteúdo sem o Diretor; post sem "Comenta PLANTA"; medida digitada à mão em vez de copiada do validador; plano limpo conferido contra o `CONSELHO.md` antes de entrar.

**Achados fora da prova, para o dono e o Arquiteto:**
- **C01, lote:** o catálogo e o PLANTAS dizem "a partir de 8 x 15 m"; o `plantas.py validar` diz "lote ref 8.0x13.0". Pode ser arredondamento para lote padrão ou divergência; o Arquiteto explica (não mexer à noite no texto público).
- `contexto/arquiteto.md` está com 3498 de 3500 caracteres: a próxima lição estoura o `checar.py`; consolidar antes.
