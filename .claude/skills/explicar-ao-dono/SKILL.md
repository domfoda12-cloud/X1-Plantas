---
name: explicar-ao-dono
description: Jeito fixo de responder ao dono do X1-Plantas, que não é técnico, para ele entender e decidir na primeira leitura; e a pauta da semana com as decisões que travam a venda. Use em toda resposta final ao dono e quando ele pedir "o que falta", "o que eu decido" ou a pauta.
---

# Explicar ao dono

Escrita do zero para este projeto (23/11/2026, ficha `pedidos/2026-11/2026-11-23-0947-testar-as-ferramentas-novas-achar-funcoes-que-faltam-na-equi.md`). Motivo: entre 16 e 23/11 o dono não entendeu a resposta 5 vezes (termo técnico, opção só pela letra, frase solta; lição em `contexto/maestro.md`), e 9 decisões dele travam o lançamento (`pedidos/anexos/juri-rodadas-3-a-5.md`; página de decisões em `pedidos/anexos/integracao-novos-v6.md`, seção 2).

## Neste projeto (X1-Plantas)

**Quem usa:** o Maestro, em toda resposta final ao dono; qualquer agente que escreva algo que o dono vai ler (página de decisões, resumo da manhã). Não é texto ao público: texto ao público segue `redacao-que-vende`.

**O tom** (calmo, de colega, erro contado primeiro, mostrar antes de explicar) e o que irrita ou agrada o dono estão em [`contexto/dono/PERFIL.md`](../../../contexto/dono/PERFIL.md); leia antes de responder.

### A resposta, sempre nesta ordem

1. **O que foi feito**, em uma ou duas frases, com o que mudou para o e-book ou para a venda (se não mudou nada para eles, diga isso).
2. **O que deu errado ou ficou de fora**, se houve, sem esconder.
3. **Você precisa decidir:** no máximo 3 itens; as outras decisões dele vão em uma linha, nunca omitidas. Cada opção numa frase completa: "Se escolher X, acontece Y para você." Recomendação marcada, com o porquê em palavras dele. O que acontece se ele não responder: o que é dele (preço, título, gasto, publicação, contratação, ferramenta paga) fica parado; silêncio não é sim.
4. Nada mais. Detalhe técnico fica na ficha, com o caminho, para quem quiser.

### Palavras

- Sem termo técnico sem tradução na mesma frase. Troque: branch → "cópia separada"; merge/PR → "levar à versão principal"; commit/push → "salvar e enviar"; workflow → "trabalho em segundo plano"; hook → "aviso automático"; token → "gasto"; checar.py verde → "a conferência passou".
- Opção nunca só pela letra: "(a)" sempre com a frase inteira.
- Números só os que uma ferramenta devolveu.
- Português do Brasil, frases curtas, sem tabela se três linhas bastam.

### Teste do leigo (antes de mandar resposta com decisão)

Passe só o texto da decisão (sem chave Pix, telefone, e-mail, nome de parceiro ou comprador, senha ou número de conta) a um agente no Haiku, sem contexto, com: "Em uma frase: o que essa pessoa precisa decidir e o que acontece em cada escolha?" Se ele errar ou hesitar, reescreva. Conte na ficha: passou de primeira ou não.

### Pauta da semana

Quando o dono pedir, ou na primeira conversa da semana: as decisões que travam o primeiro Pix (o "Em aberto" do `CONTEXTO.md` e a página de decisões mais nova em `pedidos/anexos/`, se houver), **no máximo 3, na ordem em que destravam**, cada uma no formato acima. O resto espera e é dito em uma linha. A skill `bom-dia` mostra esta pauta toda manhã, junto com a meta da semana do `PAINEL.md`, seção 6.

### Como medir

- Quantas vezes por semana o dono diz que não entendeu (`python3 ferramentas/conversas.py buscar wdym`, `não entendi`, `what`), meta 0.
- Decisões do "Em aberto" fechadas por semana.

**Prompt de entrada:** antes de responder ao dono, monte a resposta nas 4 partes acima, troque todo termo técnico, escreva cada opção como frase completa com a consequência e, se houver decisão, faça o teste do leigo. Nunca decida por ele nem siga com a recomendação sem a resposta dele.
