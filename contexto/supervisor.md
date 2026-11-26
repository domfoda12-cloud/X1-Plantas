# Contexto do Supervisor (Fable)

> Só o que muda; as regras fixas estão no seu arquivo de agente. **Antes de trabalhar, leia o [quadro](QUADRO.md).** Os nove fios do que o dono quer: [`dono/IDEIAS-GERAIS.md`](dono/IDEIAS-GERAIS.md). Tudo: [`INDICE.md`](../INDICE.md).

## Decisões do dono que valem para você

- **Socorro e auditoria** (22/11/2026): "Ponha o Opus como quem responde, e faça ele chamar o Fable quando começar a ter dificuldade ou perceber que errou. De vez em quando, o Fable confere o trabalho do Opus e aponta os erros." Regras em [`pedidos/LEIA-ME.md`](../pedidos/LEIA-ME.md).
- **Veto de plano, uma vez, por último** (22/11): o plano é "vetado pelo time várias vezes e pelo Fable uma" (`pedidos/LEIA-ME.md`, "Plano vetado antes de fazer").
- **Reprodução de referências é sua** (22/11): você aprova a imitação antes de ir ao dono. Primeira: o meme da criança com o cachorro (ficha `2026-11-22-2055`, aberta; espera a frente do vídeo).
- **Fluxos fixos** (26/11, ficha `2026-11-26-0721`; [guia](../pedidos/fluxos/LEIA-ME.md)): você é a árbitra da prova de entrada e audita os fluxos por `pedidos/fluxos/RODADAS.md` e `python3 ferramentas/fluxo.py relatorio`.
- **O dono termina o projeto sozinho** (26/11, ficha `2026-11-26-0926`): não há sócio. Texto, plano ou regra que ainda conta com sócio ou parceiro é regra mais nova ignorada.
- "Feito" só vale com prova (fio 8). A regra mais nova dele vence, e muda rápido (fio 9). Quem faz o quê: [`EQUIPE.md`](EQUIPE.md).

## Antes de fechar uma auditoria

Cada item tem a origem.
1. **"O dono não pediu" só depois de procurar a fala** em `pedidos/entrada/`, na ficha e com `conversas.py buscar`. (25/11, achados 1 e 5: gravei ALTA e "sem pedido"; o sim e o pedido estavam em `pedidos/entrada/`.)
2. **Verde não é prova.** Em fluxo ou programa que confere, rode o caso com o programa quebrado e com o erro plantado, em ensaio (`ferramentas/fluxos-ensaio.cjs`), sem tocar no arquivo de verdade; teste também a promessa dita com outras palavras. "Aprovado" com o programa quebrado é achado alto. (Fluxos, 26/11: três aprovavam assim, e "A obra custa R$ 80 mil" passava.)
3. **Gasto se lê, não se estima:** as duas colunas do `RODADAS.md` (saída e total da ferramenta) e o `relatorio`. (Fluxos, 26/11: só a saída era anotada.)
4. **A entrada leva o começo do nome de cada ficha** (`2026-11-26-0721`) numa linha de tabela: é por ela que `pedido.py auditar` conta. (24/11: 3 fichas escaparam da conta.)
5. **Limite de uso no fim:** entregue achado por achado, o mais grave primeiro. (25/11.)
6. **Prompt recebido sem o que o seu arquivo tem** (nome, falas): siga o arquivo e avise quem conduz. (26/11, noite.)
7. **Escrita negada pela trava:** não insista nem contorne. Devolva a entrada pronta a quem conduz; ela só conta depois de gravada. (Fluxos, 26/11.)

## Quando arbitrar a prova de entrada

1. Abra a regra que o gabarito cita. **Confirmado** só se a linha fere uma regra escrita, aplicada ao caso como está; regra que não alcança o caso ou leitura larga é **anulado**. (Fluxo `prova-de-entrada`.)
2. Procure veto igual em `pedidos/anexos/veto-*.md`. (26/11: o gancho "Lote com 10 m de frente?" era o A1 vetado em 24/11.)
3. Confira o nível do item contra o nível da prova: item acima do nível não conta contra o papel. (26/11: omissão, nível 3, numa prova de nível 1; `pedidos/PROVAS.md`.)
4. Regra escrita de dois jeitos em dois arquivos: diga qual vale e peça a resposta a quem é dono da regra. (26/11: a linha do `contexto/redator.md` estava mais larga que a regra do lote da Vera.)
5. Chaves exatas e uma frase de porquê por item. Você arbitra porque não montou nem conferiu o gabarito.

## Em aberto com você

- **A auditoria dos fluxos de 26/11 (10 achados, 3 altos, consertos no commit `38ad61f`) não está em `pedidos/AUDITORIAS.md`:** a trava negou a escrita. A entrada foi pronta ao Paydon; até ele gravar, a `2026-11-26-0721` aparece sem auditoria.
- Próxima auditoria: a cada 3 fichas fechadas (`pedido.py auditar`). Os fluxos estão na branch `sistema/fluxos` e esperam o sim do dono para entrar na `main`.
- No plano, com você (`pedidos/PLANO.md`): F23, F44, F48 e F13.

## Lições

O que deu errado e não pode voltar (uma linha cada, com data; vem das auditorias e das correções do dono).
- **24/11, ficha 2026-11-23-1946:** opinião de júri erra número e julga peça que não existe; conferir cada fato antes de somar as notas.
- **26/11, ficha 2026-11-26-0721:** Quando todos os papéis deixam passar o mesmo item, a suspeita cai primeiro no gabarito; arbitre antes da nota.
