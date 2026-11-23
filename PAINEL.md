# Painel X1-Plantas

> **Comece por aqui.** Este é o centro de controle do projeto: o que estamos construindo, como o dinheiro entra, em que frente estamos, o que fazer esta semana e o que decidir.
>
> **Quem rege é o Maestro**, a sessão do Claude no seu computador: conduz a semana por este painel e decide; a **MinoAI Frontier**, o Diretor, dá a ideia principal do conteúdo, edita o vídeo e gera a imagem. Ver [`instagram/MINOAI-FRONTIER.md`](instagram/MINOAI-FRONTIER.md#maestro-e-diretor-a-sessão-do-claude-no-seu-computador-com-a-minoai-frontier).
>
> A seção 1 se atualiza sozinha: rode `python3 ferramentas/atualizar-painel.py` na raiz do projeto sempre que algo mudar. **Atenção:** ela conta pela coluna "Situação" do [catálogo](ebook/catalogo.md), que está atrasada; a verdade de hoje está na seção 2.
>
> O que o dono acabou de pedir: [`contexto/QUADRO.md`](contexto/QUADRO.md). O que espera decisão dele: [`CONTEXTO.md`](CONTEXTO.md), "Em aberto". Onde está cada documento: [`INDICE.md`](INDICE.md).

## 1. Situação agora

<!-- situacao:inicio -->
_Gerado por `ferramentas/atualizar-painel.py` em 23/11/2026, a partir dos arquivos que existem. Não edite à mão._

| Indicador | Situação |
|---|---|
| **Casas desenhadas e validadas** | 24 de 35 no catálogo |
| Progresso do catálogo | `██████████████░░░░░░` 24/35 |
| Casas com imagem 3D | 24 de 24 |
| Casas com foto de fachada | 3 (C03, E07, F01) |
| PDF do e-book | gerado, 22 MB · 5 plantas grátis |
| Vídeos em `video/saida/` | 2 pastas (convite, principal) · 0 versões antigas (`v1` a `v5`, com a C01 velha) |
| Avisos de conferência | 0 |

**Por categoria:**

| Categoria | No catálogo | Desenhadas | Com 3D |
|---|---|---|---|
| Compactas | 7 | 7 | 7 |
| Terreno estreito | 7 | 7 | 7 |
| Família | 7 | 5 | 5 |
| Especiais | 10 | 5 | 5 |
| Sobrados | 4 | 0 | 0 |

Ainda só no catálogo (ideia): F06, F07, S01, S02, S06, S08, S10, O01, O02, O03, O04.
<!-- situacao:fim -->

## 2. Em que pé está (escrito à mão, 22/11/2026)

- **E-book:** as **24 casas** estão desenhadas, validadas e no PDF (`ebook/saida/ebook.pdf`, rascunho 1), cada uma com imagem 3D estática (`ebook/visual/3d/`). Há **5 plantas grátis** para o funil (C01, E03, E02, F01, C06; a E07 saiu, na fila do redesenho). O dono reprovou o arranjo das plantas em 22/11: a **C01 foi redesenhada** (50 m²) e é o modelo; quais das outras 23 refazer, e quando, é decisão dele.
- **Vídeo:** a frente foi **aberta pelo dono em 21/11**. Ficaram em `video/saida/` só o convite (F03, o último feito) e o principal de 21/11; o resto foi apagado em 22/11 para refazer do zero. Toda instrução dele sobre vídeo: [`video/VIDEO.md`](video/VIDEO.md#vídeo-tudo-o-que-o-dono-pediu-não-se-perde).
- **Animações 3D completas:** ainda não começaram (as imagens 3D paradas já estão no e-book).
- **Organização:** tudo na `main`, a única branch. Cada pedido do dono vira ficha em [`pedidos/`](pedidos/LEIA-ME.md) e é executado pelo modelo certo. Índice e resumos por pasta: [`INDICE.md`](INDICE.md).
- **Não há venda nem anúncio rodando.** Custo por venda ainda não medido.

## 3. O negócio em uma frase

**Um e-book com dezenas de plantas de casas originais**, em blueprint, planta humanizada e 3D, para quem vai construir no Brasil e ainda não sabe qual casa cabe no terreno e no bolso. As pessoas chegam pelos vídeos, ganham uma planta grátis no WhatsApp e compram o e-book.

```
                 ┌──────────────────────────────┐
                 │  Animações 3D (as plantas)   │
                 └───┬──────────────┬───────────┘
        imagens e    │              │  imagens e animação
        animações    ▼              ▼  de cada planta
   ┌──────────────────────┐   ┌──────────────────┐
   │ Vídeo de anúncio     │   │ E-book (produto) │
   │ + Instagram (editor) │   └────────▲─────────┘
   └──────────┬───────────┘            │ compra
              │ comentário "PLANTA"    │
              ▼                        │
   ┌──────────────────────────────────┴──┐
   │ Funil no WhatsApp (parceiro):       │
   │ planta grátis → conversa → oferta   │
   └─────────────────────────────────────┘
```

**Uma planta trabalha três vezes:** vira página do e-book, post no Instagram e cena de vídeo.

**Para quem vendemos** (detalhes, dados e fontes em [`ESTRATEGIA.md`](ESTRATEGIA.md)):
- **Quem:** quem tem um lote e vai construir, quase sempre **com pedreiro e sem arquiteto** (a maioria das obras particulares, segundo a pesquisa CAU/BR e Datafolha de 2015; em texto público, sem percentual), muitas vezes **por etapas**.
- **A primeira pergunta dessa pessoa:** "que casa cabe no meu lote?".
- **Os três diferenciais:** **ache pelo seu lote**, **veja em 3D antes de construir** e **casa que cresce**.
- **Lançar com 12 ou com as 24 casas, preço, garantia, título e bônus:** decisão do dono, **em aberto** ([`CONTEXTO.md`](CONTEXTO.md)). As recomendações estão em [`ESTRATEGIA.md`](ESTRATEGIA.md), seção 7.

## 4. A conta que diz se o anúncio paga

O anúncio só se paga se **o custo para gerar uma venda for menor que o preço do e-book**.

```
custo por venda = custo por contato ÷ taxa de conversão
```

- **Custo por contato:** quanto o Facebook Ads cobra, em média, por cada pessoa que chama no WhatsApp. Aparece no Gerenciador de Anúncios.
- **Taxa de conversão:** de cada 100 pessoas que chamam no WhatsApp, quantas compram. Quem mede é o parceiro.

**Exemplo só para mostrar a conta** (não é previsão; troque pelos seus números assim que tiver):

| Custo por contato | Conversão | Custo por venda | Com o e-book a R$ [preço] |
|---|---|---|---|
| R$ 3,00 | 3% | R$ 100,00 | Paga se o preço for maior que R$ 100 |
| R$ 3,00 | 6% | R$ 50,00 | Paga se o preço for maior que R$ 50 |
| R$ 1,50 | 3% | R$ 50,00 | Paga se o preço for maior que R$ 50 |

**O que essa conta ensina:**
- **Dobrar a conversão vale o mesmo que cortar pela metade o custo do anúncio.** A conversão depende do funil e da planta grátis, que custam pouco para melhorar.
- O vídeo bom (tempo assistido alto) **baixa o custo por contato**, porque o Facebook entrega mais barato o que as pessoas assistem.
- Comece com **orçamento pequeno por dia** e só aumente quando o custo por venda estiver abaixo do preço por pelo menos uma semana.

Anote os números reais na tabela da seção 7.

## 5. Frentes, uma por vez

Ordem do dono: **e-book → animações → vídeo** ([`CLAUDE.md`](CLAUDE.md)). Cada frente tem um critério para dar por fechada.

| Frente | Situação | Fechada quando |
|---|---|---|
| **1. E-book** | **Agora.** Rascunho 1 com 24 casas; redesenho do arranjo começou pela C01 | O dono escolhe as casas a refazer e preenche título, preço, bônus e contato em `ebook/config.json`; Revisor de risco aprova; PDF final |
| **2. Animações 3D** | Não começou | As casas do lançamento com animação conferida contra a planta |
| **3. Vídeo** | Aberta pelo dono em 21/11; rascunhos esperando ele | Vídeo aprovado pelo dono e pelo Revisor, com a casa nova |
| **4. Vender** | Depois | Custo por venda abaixo do preço por 1 semana |

## 6. Esta semana

O que espera o dono está em [`CONTEXTO.md`](CONTEXTO.md), "Em aberto"; o que acabou de mudar, no [quadro](contexto/QUADRO.md). As tarefas dos agentes saem das fichas em [`pedidos/`](pedidos/LEIA-ME.md). Esta seção não repete essas listas.

## 7. Números para acompanhar

Preencha toda segunda-feira. Compare cada semana com a anterior, não com contas grandes.

| Frente | O que medir | Onde ver | Sinal de alerta |
|---|---|---|---|
| Vídeo | Tempo médio assistido; % que chega aos 27 s (o desfecho) | Instagram (estatísticas do reel) | Metade sai antes do erro 2: o gancho não prendeu |
| Vídeo | Custo por contato | Gerenciador de Anúncios | Subindo 3 semanas seguidas: trocar o gancho |
| Instagram | Comentários "PLANTA" por reel; seguidores novos | Instagram | 3 reels fracos seguidos diminuem o alcance do próximo |
| Funil | Contatos → compras (taxa de conversão) | Parceiro | Abaixo da semana anterior: revisar a planta grátis e a oferta |
| Funil | % que manda o tamanho do lote; **lote mais pedido** | Parceiro | Pouca gente manda o lote: mudar a primeira mensagem. O lote mais pedido define as próximas plantas e anúncios |
| E-book | Vendas; pedidos de reembolso | Plataforma de pagamento | Reembolsos: o e-book não entregou o que o anúncio prometeu |
| 3D | Plantas novas por semana | Seção 1 deste painel | Sem planta nova: o Instagram fica sem "planta da semana" |

| Semana | Custo por contato | Contatos | Vendas | Conversão | Custo por venda | Preço | Observação |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## 8. Decisões tomadas

| Data | Decisão |
|---|---|
| 16/11 | Tudo em **português do Brasil**, preços em **R$**. Brasil primeiro; outros países depois |
| 16/11 | **Sem landing page:** o anúncio leva direto ao WhatsApp |
| 16/11 | Anúncios no **Facebook Ads**, acompanhamento no **WhatsApp** |
| 16/11 | Plantas **originais**; nada copiado de outros escritórios |
| 18/11 | Produto: **e-book com dezenas de plantas**, em vez de uma planta por vez |
| 18/11 | Público principal: **quem tem um lote e vai construir com pedreiro, por etapas**, 25 a 50 anos ([`CLAUDE.md`](CLAUDE.md)) |
| 19/11 | Maestro e editor: **MinoAI Frontier** (desde 22/11: Diretor; o Maestro é a conversa principal) ([`instagram/MINOAI-FRONTIER.md`](instagram/MINOAI-FRONTIER.md#maestro-e-diretor-a-sessão-do-claude-no-seu-computador-com-a-minoai-frontier)) |
| 20/11 | **Qualidade primeiro** e **uma frente por vez** ([`CLAUDE.md`](CLAUDE.md)) |
| 21/11 | Frente de **vídeo aberta** pelo dono |
| 22/11 | **OpenArt só com o "sim" do dono a cada uso**, com resumo e custo antes |
| 22/11 | Selo "Imagem ilustrativa" **sai dos vídeos**; o aviso "Planta de referência…" continua ([`contexto/revisor-de-risco.md`](contexto/revisor-de-risco.md)) |
| 22/11 | A **`main` é a única branch**; índice e resumos por pasta; cada pedido vira ficha e vai ao modelo certo ([`pedidos/LEIA-ME.md`](pedidos/LEIA-ME.md)) |

O histórico completo, pedido por pedido, está em [`CONTEXTO-HISTORICO.md`](CONTEXTO-HISTORICO.md).

## 9. Decisões pendentes

Ficam num lugar só: [`CONTEXTO.md`](CONTEXTO.md), "Em aberto". As opções e a recomendação de título, preço, plataforma, garantia e bônus estão em [`ESTRATEGIA.md`](ESTRATEGIA.md), seção 7. Quando o dono decidir, a linha entra na seção 8 com a data.

## 10. Riscos e cuidados

| Risco | O que fazer |
|---|---|
| **Quem assina o desenho.** A Lei 5.194/1966 (art. 13) diz que plantas e projetos só têm valor jurídico diante das autoridades quando feitos por profissional habilitado; o art. 6º trata do exercício da profissão sem registro. As plantas do e-book são feitas por quem não é arquiteto nem engenheiro. ([pesquisa](reports/Arquiteto%20e%20engenheiro%20na%20construção%20residencial.md)) | Apresentar o e-book como **referência**, nunca como projeto. Ter um **arquiteto registrado** revisando e assinando as plantas, e confirmar com ele e com um advogado como isso aparece no produto. Não é parecer jurídico |
| **Responsabilidade técnica.** Para construir e aprovar na prefeitura, a obra precisa de projeto com profissional habilitado | Escrever no e-book (capa interna e cada página) que as plantas são **de referência**, não projeto executivo, e que a obra precisa de responsável técnico. Confirmar o texto com um arquiteto |
| **Direito de arrependimento.** Compra pela internet pode ser cancelada em até 7 dias (Código de Defesa do Consumidor, art. 49) | Combinar com o parceiro como devolver o dinheiro; deixar a política escrita na oferta |
| **Direitos autorais** | Só plantas originais ou com licença escrita de venda. Nada de imagem de terceiros no e-book |
| **Regras de anúncio da Meta** para imóveis e construção | Conferir no Gerenciador de Anúncios antes de subir cada campanha, porque as regras mudam |
| **Medidas provisórias** | Nenhuma planta passa para `pronta` sem revisão de medidas |
| **Promessa do anúncio maior que o e-book** | O anúncio promete economia com um arquiteto; o e-book precisa mostrar, em cada planta, os erros que ela evita |

## 11. Rotina

A rotina da semana está em [`instagram/MINOAI-FRONTIER.md`](instagram/MINOAI-FRONTIER.md#maestro-e-diretor-a-sessão-do-claude-no-seu-computador-com-a-minoai-frontier), seção 4. Para manter este painel em dia: mude só a coluna **Situação** do [catálogo](ebook/catalogo.md) e rode `python3 ferramentas/atualizar-painel.py` (ele também avisa link quebrado em qualquer guia).

## 12. Quem faz o quê

| Quem | Faz | Onde |
|---|---|---|
| **Dono** | Decide preço, título, bônus, gasto, publicação e contratação; diz "sim" a cada uso do OpenArt e a cada post | Este painel e [`CONTEXTO.md`](CONTEXTO.md) |
| **Maestro: a conversa principal (Opus)** e **Diretor: MinoAI Frontier** | O Maestro decide e rege; o Diretor dá a ideia do conteúdo e opina primeiro nele, com a fonte, e edita no computador do dono | [`instagram/MINOAI-FRONTIER.md`](instagram/MINOAI-FRONTIER.md#maestro-e-diretor-a-sessão-do-claude-no-seu-computador-com-a-minoai-frontier) |
| **Conselho** (Redator, Estrategista, Arquiteto, Designer, Editor de vídeo, Pesquisador; Revisor de risco com veto) | Opina e executa só o que foi aprovado | [`CONSELHO.md`](CONSELHO.md), `contexto/<papel>.md` |
| **Modelos** | A conversa principal interpreta e confere; Opus executa o trabalho do projeto; Sonnet pesquisa a fundo; Haiku faz a tarefa simples e pessoal do dono | [`pedidos/LEIA-ME.md`](pedidos/LEIA-ME.md) |
| **Parceiro** | Funil: WhatsApp, sequência de mensagens, venda e reembolso | [`ebook/vendas/`](ebook/vendas) |
| **Arquiteto registrado** (a contratar, decisão do dono) | Revisar as plantas e o texto de responsabilidade técnica | [`reports/`](reports/RESUMO.md) |

Antes de entregar: `python3 ferramentas/checar.py` sem erro e `python3 ferramentas/atualizar-painel.py` com zero avisos ([`CLAUDE.md`](CLAUDE.md)).

## 13. Mapa do projeto

Está no [`INDICE.md`](INDICE.md), gerado por `ferramentas/resumos.py`, com um resumo por pasta.
