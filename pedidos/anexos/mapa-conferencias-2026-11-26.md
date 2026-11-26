# Mapa das conferências (26/11/2026)

> Passo 1 do plano `pedidos/anexos/plano-fluxos-2026-11-26.md` (ficha `2026-11-26-0721`). Fontes: as lições de `pedidos/LICOES.md` e do "Lições" de cada `contexto/<papel>.md`, as provas de `pedidos/PROVAS.md` e os vetos da Vera em `pedidos/anexos/veto-*.md`. Regra do dono: **tudo é conferido, pela conferência mais barata que pega o erro**: programa (zero token) primeiro, agente só onde precisa de juízo.
>
> Legenda da última coluna: **P** = programa (`ferramentas/fluxo.py` ou `checar.py`), **A** = agente, com o modelo que basta. "Novo" = não existia antes de hoje.

## 1. Texto que vai ao público (anúncio, legenda, WhatsApp, página do e-book)

| O que pode dar errado | De onde veio | Quem conferia | Quem confere agora |
|---|---|---|---|
| Frase vetada volta ("todas as casas cabem", "banheiro com giro", "ventilação cruzada", "recebe as próximas plantas", "em breve") | `contexto/redator.md`, lista da Vera | Vera, lendo | **P novo** (`fluxo.py texto`) |
| Promessa proibida: dispensa pedreiro ou engenheiro, aprovação garantida, custo exato de obra | `CLAUDE.md`, regras que não mudam; prova 1, plano 1 e 7 | Vera | **P novo** (padrões) + Vera no fim |
| Número da casa errado (área, lote, lado da rua) | prova 1, plano 7 (lote 8 x 20); lado do sol espelhado (26/11) | Vera, Nilo | **P novo**: área, lote e frente contra o `PLANTAS.md` |
| Lote ou recuo sem "a prefeitura confirma" | Vera, `/semlote`, 26/11 | Vera | **P novo** (aviso) |
| Preço dentro do PDF | dono, 24/11 | `checar.py` | P (já existia) |
| Nota interna no bloco ao cliente ("o dono decide", "sócio") | Vera, `/compactapreco`, 26/11 | Vera | **P novo** (aviso) |
| Frase que não vale para quem recebe ("aqui está" sem anexo) | Rui e Vera, `/confia`, 26/11 | Vera | A: Vera (juízo) |
| Afirmação maior que a peça ("cada palavra", "a conta muda") | Vera, 26/11 | Vera | A: conferência de fatos (Opus, quem não escreveu) |
| Diretor ausente em conteúdo público | prova 1 e 2 (passou por 4 de 5) | ninguém por regra | **P novo**: o passe do fluxo exige a ideia do Diretor com fonte |
| Palavra técnica ambígua ("lote comercial") | Vera, 24/11 | Vera | A: ângulo do comprador |

## 2. Página do e-book (prévia)

| O que pode dar errado | De onde veio | Quem conferia | Quem confere agora |
|---|---|---|---|
| Página estourada, link quebrado, bônus sem página | auditorias de 23 e 24/11 | `checar.py` | P (já existia) |
| Área do 3D diferente da do e-book | F7, 24/11 | `checar.py` | P (já existia) |
| Prévia mais velha que os dados da casa | 23/11 | `checar.py` | P (já existia) |
| Gravar em `ebook/saida/` sem o dono | 26/11, `livro.py --help` | `checar.py` | P (já existia) + o fluxo nunca grava lá |
| Texto da página com frase vetada ou número errado | igual ao item 1 | Vera | **P novo** (`fluxo.py texto` na prévia) |
| Visual genérico, Placa fora do lugar (voz do Lote Carente fora das placas) | quadro, 26/11 | Bia, Vera | A: Bia (designer), uma leitura |

## 3. Planta

| O que pode dar errado | De onde veio | Quem conferia | Quem confere agora |
|---|---|---|---|
| Medida abaixo do mínimo, porta que bate, móvel sobre móvel | validador e 3D | `plantas.py validar`, `checar.py` | P (já existia) |
| Rascunho passa no validador e falha no 3D | A6, 24/11 | `conferir-rascunho.py` | P (já existia), agora obrigatório no fluxo |
| Lado do sol de memória | 26/11 | Nilo | P (já existia: prova da tabela) |
| Afirmação técnica no texto da planta (ventilação, divisa, lei) | Nilo, 23 e 26/11 | Nilo | A: Nilo (arquiteto), juízo |

## 4. Decisão (júri e conselho de bolso)

| O que pode dar errado | De onde veio | Quem conferia | Quem confere agora |
|---|---|---|---|
| Rodada sem régua escrita | `CONSELHO.md` 5b, regra 0 | ninguém | **P novo** (`fluxo.py juri`) |
| Crítica sem arquivo e linha, ou linha que não existe | 5b, regra 1; ficha 1946 (jurado julgou peça que não existe) | presidente, às vezes | **P novo**: cada citação é aberta pelo programa |
| Menos de 2 defeitos por jurado | 5b, regra 1 (25/11) | ninguém | **P novo** |
| Presidente que também opinou; menos de 5 fatos conferidos | 5b, regra 3 | ninguém | **P novo** |
| Revisão anônima pulada | diagnóstico do júri (não rodava desde a rodada 3) | ninguém | **P novo**: a rodada sem ordenação é recusada |
| Piso 7 e média 8,5 calculados à mão | 5b, regra 4 | Maestro | **P novo** (o programa calcula) |
| Gasto não anotado | `CONSELHO.md`, "Custo" (2,95 milhões sem registro por rodada) | ninguém | **P novo**: rodada sem gasto é recusada |
| Decisão do dono já tomada sendo rediscutida | júri, melhoria 3 (9 respostas rediscutidas) | ninguém | A: presidente lê `decisoes-do-dono-2026-11-23.md` |

## 5. Passe entre agentes, salvar e passagem

| O que pode dar errado | De onde veio | Quem conferia | Quem confere agora |
|---|---|---|---|
| Agente entrega sem dizer o que supôs ou o que falta | ficha 0105 (25 pontos que os aplicadores não viram) | ninguém | **P novo**: passe com forma fixa (`fluxo.py passe`) |
| Arquivo dito "salvo" em pasta que o git ignora | auditoria 0116 (Canteiro) | ninguém | **P novo**: o passe abre cada arquivo com `git ls-files` |
| Hora escrita de cabeça, depois da hora real | maestro, 26/11 (duas vezes) | ninguém | **P novo** (`fluxo.py texto` avisa hora maior que `date -u`) |
| Commit com `checar.py` vermelho | maestro, 23/11 | `salvar.py` | P (já existia) |
| Suposição tratada como sim do dono | prova 1, plano 3; júri, 23/11 | Vera | A: ângulo do risco + campo "suposições" do passe |
| Lição esquecida no fim do trabalho | dono, 26/11: "Is it not doing this yet?" | ninguém | **P novo**: `fluxo.py registrar` grava a lição sozinho |
| Arquivo de contexto cheio barra a lição nova | `maestro.md` com 5.907 de 5.000 caracteres | ninguém (a lição era recusada) | **P novo**: as lições mais antigas vão inteiras para `pedidos/historico/licoes-<papel>.md`, com link no lugar |

## 6. O que fica com agente, e por quê

Juízo que nenhum programa faz: se o comprador entende, se a frase vale para quem a recebe, se a afirmação é maior que a peça, se a decisão aproxima o Pix. Para isso, **uma leitura por ângulo**, no modelo que basta: Haiku para rodar comando e devolver o resultado; Opus para conferir fatos e escrever; Vera (Fable) uma vez, na peça montada.

**Medir:** cada rodada grava o gasto (tokens de saída que o `budget.spent()` devolve) e quantos achados cada conferidor fez sozinho. Conferidor com 5 rodadas sem achado só dele é marcado para corte pelo `python3 ferramentas/fluxo.py relatorio` (o corte é decisão do Paydon, avisada ao dono).
