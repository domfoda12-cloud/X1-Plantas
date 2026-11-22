# E-book: plantas de casas térreas

> Parte do projeto X1-Plantas. Painel geral: [`../PAINEL.md`](../PAINEL.md).
>
> **Esta pasta é o produto.** Hoje: um PDF A4 de 61 páginas com 24 casas térreas, cada uma com a planta mobiliada, a casa desenhada no lote, a ficha com os números do validador, a vista da rua e a casa em 3D. O catálogo propõe 35 casas no total; as outras 11 ainda são ideia.

## Nesta pasta

| Arquivo | Para que serve |
|---|---|
| `EBOOK.md` | Este guia: o que o PDF tem hoje, página por página, e o que falta |
| `catalogo.md` | As 35 casas propostas: as 24 que estão no PDF e as 11 que ainda são ideia |
| `plantas/PLANTAS.md` | Ficha de cada uma das 24, gerada pelo validador (a fonte dos números) |
| `fichas/textos.py` | Os textos de cada casa: gancho, para quem é, para quem não serve, erros que evita, perguntas |
| `gerador/` | O gerador do PDF (`livro.py`) e os textos fixos (`paginas.py`) |
| `config.json` | Os campos do dono: título, preço, bônus, contato, plantas grátis |
| `referencias/` | Pesquisa: público, concorrentes, regras do arquiteto |
| `vendas/` | Material do funil, que fica com o parceiro: planta grátis, WhatsApp, perguntas, objeções, calculadora de lote |

## 1. O produto

- **O que é:** um e-book em PDF com 24 casas térreas (`ebook/saida/ebook.pdf`, 61 páginas). Mais 11 casas estão propostas no [catálogo](catalogo.md).
- **Para quem:** quem vai construir no Brasil, principalmente a primeira casa, e ainda não sabe que planta cabe no terreno e no bolso. Persona: [`referencias/persona-e-mercado.md`](referencias/persona-e-mercado.md).
- **Promessa:** "Encontre a planta certa para o seu terreno antes de gastar com projeto". A planta é de referência: o projeto da obra é de um arquiteto ou engenheiro.
- **As 24 casas:** dados em `plantas/dados/`, prévias em `plantas/previas/`, fichas em [`plantas/PLANTAS.md`](plantas/PLANTAS.md). Todas passam no validador (`python3 ferramentas/plantas.py validar`; regras em [`referencias/regras-do-arquiteto.md`](referencias/regras-do-arquiteto.md)). Nenhuma foi revisada ainda por um arquiteto registrado.
- **Gerar:** `python3 ebook/gerador/livro.py [--previa DIR]` gera `ebook/saida/ebook.pdf` e as 6 plantas grátis (`planta-gratis-<ID>.pdf`). Imagem 3D de uma casa: `python3 ferramentas/imagens3d.py ID` (sai em `visual/3d/ID.jpg`). O gerador antigo (`gerar.py`) foi apagado em 21/11: imprimia promessas vetadas.
- **Direção visual:** azul de projeto `#0B4FA8`, amarelo `#FFC857`, títulos em Bricolage Grotesque, texto em Inter. Prévia aprovada como direção em 20/11: [`visual/plano-visual.html`](visual/plano-visual.html).
- **Idioma e moeda:** português do Brasil, preços em R$.

## 2. O PDF, página por página

Fonte: `gerador/livro.py`, função `montar`.

| Pág. | Página | O que mostra |
|---|---|---|
| 1 | Capa | "Que casa cabe no seu lote?" (provisório até o dono decidir o título), "24 plantas de casas térreas", a C01 mobiliada e a fita métrica com quantas casas cabem em cada frente de lote |
| 2 | Como usar este e-book | Três passos (medir a frente, achar as casas, levar ao engenheiro) e o aviso completo de planta de referência |
| 3 | Ache pelo seu lote | Cada frente de lote, de 5 a 14 m, com as casas que cabem e a página de cada uma; os recuos de referência usados |
| 4 | Ache pelo jeito da sua família | As casas por jeito de morar (mora sozinho, casal com filhos, família de 4, trabalha em casa…) |
| 5 | Como ler uma planta | A C01 com a legenda de parede, porta, janela, cota, área e móveis |
| 6 | As palavras da obra | Glossário: recuo, taxa de ocupação, ART e RRT, alvará, habite-se e outras |
| 7–8 | Os 7 erros que saem caro | Cada erro, por que sai caro e o jeito certo |
| 9 | Índice rápido | As 24 com área, quartos, banheiros, lote mínimo e página |
| 10–57 | As 24 casas | Duas páginas por casa (seção 3), na ordem Compactas, Terreno estreito, Família, Especiais |
| 58 | Terreno e recuos | O que a prefeitura define, onde descobrir e a conta do espaço para a casa |
| 59 | Ficha do meu terreno | Campos para preencher com os dados da prefeitura |
| 60 | Do e-book até a chave na mão | 7 passos, do escolher ao habite-se, com responsável técnico em todos |
| 61 | Agora é com você | Perguntas para fazer em qualquer casa, bônus e contato (campos do dono ainda em aberto) |

## 3. As duas páginas de cada casa

| Página esquerda | Página direita |
|---|---|
| ID, categoria e lote mínimo; nome da casa | "Cabe num lote de X x Y": a casa desenhada no lote, com os recuos |
| Gancho (`fichas/textos.py`): frente, quartos e área | **Informação da casa:** área fechada, medidas por fora, varanda e garagem, área coberta total, quartos, banheiros, corredor, janela, melhor lado da rua, se pode espelhar |
| Planta grande mobiliada, com nome e área de cada cômodo e as cotas | **Atenção: leve ao engenheiro:** os avisos do validador, quando houver |
| Para quem é | **Vista da rua:** foto ilustrativa em 3 casas (C03, E07 e F01, de `visual/openart/fachadas/`), desenho simplificado nas outras 21 |
| Erros que esta casa evita (dos 7) | **A casa em 3D:** imagem do nosso motor, sem telhado, nas 24 (`visual/3d/`) |
| | Por que esta planta é assim (do validador), para quem não serve e perguntas para o engenheiro |

Toda página de casa tem no rodapé: "Planta de referência. O projeto para a prefeitura é assinado por arquiteto ou engenheiro habilitado." A aba amarela na borda mostra a frente do lote.

**O que o PDF não tem hoje:** blueprint separado, perspectivas 3D, animação, QR code e checklist de obra. Não prometa nenhum deles em texto de venda.

## 4. Como uma casa entra no e-book

| Passo | O que acontece | Onde |
|---|---|---|
| 1. Ideia | Nome, área, quartos, lote e destaque | [`catalogo.md`](catalogo.md) |
| 2. Dados | A planta desenhada em código: cômodos, paredes, janelas, portas | `plantas/projetos.py` |
| 3. Validação | O validador confere medida, janela, circulação, lote e sol; só entra com 0 erros | `python3 ferramentas/plantas.py validar` |
| 4. Textos | Gancho, para quem é, erros que evita, perguntas; Revisor de risco revisa | `fichas/textos.py` |
| 5. Imagem 3D | A casa mobiliada vista de cima | `python3 ferramentas/imagens3d.py ID` |
| 6. Página | O gerador monta as duas páginas | `python3 ebook/gerador/livro.py` |
| 7. Revisão de arquiteto registrado | Ainda não feita para nenhuma casa | Fora do repositório |

Ao terminar, mude a coluna **Situação** do catálogo. O andamento geral fica no [painel](../PAINEL.md).

## 5. Lançamentos e decisões

- **Levas (proposta):** o catálogo divide as 35 casas em 3 levas: 12, 12 e 11. O PDF de hoje já tem as 24 das levas 1 e 2. **[lançamento: sair com 12 ou com 24, a definir pelo dono]** (`PAINEL.md`, seção 9).
- **Título, preço, bônus, contato e promessa de atualização** são campos do dono em `config.json`; as opções estão no [painel](../PAINEL.md), seção 9, e a oferta recomendada na [estratégia](../ESTRATEGIA.md), seção 7. **[garantia: a definir pelo dono]**.
- **Linguagem:** o e-book é lido por quem constrói com pedreiro. Explique todo termo técnico na primeira vez que aparecer ([estratégia](../ESTRATEGIA.md), seção 9).
- **Plantas grátis do funil:** 5 casas (C01, E03, E02, F01 e C06; a E07 saiu em 22/11, porque está na fila do redesenho; lista em `config.json`, chave `plantas_gratis`). Qual mandar para cada lote: [`vendas/material-gratuito.md`](vendas/material-gratuito.md).

## 6. Funil de vendas

1. A **planta grátis** são as duas páginas de uma casa do e-book e uma página que mostra as outras que cabem no mesmo lote ([`vendas/material-gratuito.md`](vendas/material-gratuito.md)).
2. A primeira mensagem pergunta o **tamanho do terreno**.
3. A resposta mostra as casas do e-book que cabem nele ([`vendas/sequencia-whatsapp.md`](vendas/sequencia-whatsapp.md)).

Faltam os campos entre [colchetes]: título, preço, forma de pagamento, datas, garantia e bônus, que dependem do dono.

## 7. Cuidados

- **Plantas originais.** Só entram plantas desenhadas para o produto, ou com licença escrita que permita a venda.
- **Medidas de referência** até um arquiteto registrado revisar.
- **Ilustração.** Móveis e acabamentos são ilustrativos. O e-book não substitui projeto aprovado na prefeitura nem responsável técnico pela obra. Isso está escrito nas páginas 2 e 60 e no rodapé de cada casa.

## 8. O que falta

- **Decisões do dono:** título, preço, bônus, contato do parceiro, promessa de atualização, garantia, e se o 1º lançamento sai com 12 ou 24 casas.
- **Revisão de um arquiteto registrado** nas 24 casas, nas regras e no texto do aviso legal.
- **Animação e QR por casa:** ficam para a frente de animações, por último (decisão do dono, 20/11/2026). Só entram no PDF quando existirem de verdade.
- **Imagens da C01 antiga:** a foto de fachada `visual/openart/fachadas/C01.jpg` e o mockup `visual/mockups/casa-c01-celulares.png` eram de antes do redesenho de 22/11/2026. A foto saiu do e-book em 22/11 (a C01 usa a vista da rua simplificada); o mockup continua antigo.
- **Peso do arquivo:** a meta do plano de 20/11 era abaixo de 15 MB, para mandar pelo WhatsApp; o `ebook.pdf` de hoje tem 23 MB.
