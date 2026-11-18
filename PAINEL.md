# Painel X1-Plantas

> **Comece por aqui.** Este é o centro de controle do projeto: o que estamos construindo, como o dinheiro entra, em que fase estamos, o que fazer esta semana e o que decidir.
>
> A seção 1 se atualiza sozinha. Rode `python3 ferramentas/atualizar-painel.py` na raiz do projeto sempre que algo mudar (ver seção 11).

## 1. Situação agora

<!-- situacao:inicio -->
_Gerado por `ferramentas/atualizar-painel.py` em 18/11/2026. Não edite à mão._

| Indicador | Situação |
|---|---|
| **1º lançamento do e-book** | 0 de 12 prontas · 1 com 3D |
| Plantas no catálogo | 35 · ideia 34 · dados 0 · 3D 1 · pronta 0 |
| Progresso do 1º lançamento | `░░░░░░░░░░░░░░░░░░░░` 0/12 |
| Vídeo de anúncio | 5 de 5 versões renderizadas · apresentador não gravado |
| Avisos de conferência | 0 |

**Por categoria:**

| Categoria | Plantas | No 1º lançamento | Com 3D | Prontas |
|---|---|---|---|---|
| Compactas | 7 | 4 | 1 | 0 |
| Terreno estreito | 7 | 4 | 0 | 0 |
| Família | 7 | 3 | 0 | 0 |
| Especiais | 10 | 1 | 0 | 0 |
| Sobrados | 4 | 0 | 0 | 0 |
<!-- situacao:fim -->

## 2. O negócio em uma frase

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

**Uma planta trabalha três vezes:** vira página do e-book, post no Instagram e cena de vídeo. Por isso o gargalo do projeto é **produzir plantas** (fase 2).

**Para quem vendemos** (detalhes, dados e fontes em [`ESTRATEGIA.md`](ESTRATEGIA.md)):
- **Quem:** quem tem um lote e vai construir, quase sempre **com pedreiro e sem arquiteto** (85% das obras no Brasil são feitas assim, segundo CAU/BR e Datafolha), muitas vezes **por etapas**.
- **A primeira pergunta dessa pessoa:** "que casa cabe no meu lote?".
- **Os três diferenciais:** **ache pelo seu lote**, **veja em 3D antes de construir** e **casa que cresce**.
- **O que fica dos dois lados:** os pacotes baratos de "1.500 plantas" sem curadoria e as plantas avulsas que custam centenas de reais cada.

## 3. Estratégia do e-book: lançar cedo e crescer em levas

As 35 plantas do [catálogo](ebook/catalogo.md) levariam semanas para ficar prontas e validadas. A recomendação é **não esperar todas**:

| Lançamento | Plantas | Conteúdo | Por quê |
|---|---|---|---|
| **1º** | 12 | Térreas que o motor 3D já faz: 4 compactas, 4 estreitas, 3 família, 1 home office | Cobre os lotes mais comuns do público (5 x 25 a 12 x 25) e dá para fazer agora |
| **2º** | 12 | As outras térreas | Cada planta nova vira um post "planta da semana" |
| **3º** | 11 | Sobrados, edícula, geminadas, casas grandes | Exigem ajuste no motor 3D |

**Quem compra no 1º lançamento recebe o 2º e o 3º sem pagar de novo.** Isso:
- justifica comprar agora, sem esperar a versão completa;
- dá um motivo para voltar a falar com cada comprador a cada lançamento (e pedir indicação);
- permite subir o preço a cada lançamento, já que o e-book fica maior.

> O título não deve prometer "35 plantas" enquanto o e-book tiver 12. Ver as decisões pendentes (seção 9).

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

## 5. Fases

Cada fase tem um **critério para passar para a próxima**. Não pule o critério.

| Fase | O que fazer | Critério para avançar | Situação |
|---|---|---|---|
| **1. Testar o anúncio** | Gravar o apresentador, publicar as 5 versões como reels de teste, escolher a melhor | Uma versão com tempo médio assistido claramente acima das outras, e comentários "PLANTA" chegando | **Agora** |
| **2. Montar o 1º lançamento** | Motor 3D para várias plantas; 12 plantas em dados, 3D e página; PDF do e-book | 12 páginas revisadas por você, PDF fechado, preço decidido | Pode começar junto com a fase 1 |
| **3. Vender** | Funil ajustado para o e-book; anúncio com orçamento pequeno; medir custo por venda | Custo por venda abaixo do preço por 1 semana | Depois da 2 |
| **4. Crescer** | 2º e 3º lançamentos, "planta da semana" no Instagram, novos ganchos, outros países | — | Depois da 3 |

## 6. Esta semana

| # | Tarefa | Quem | Depende de | Pronto quando |
|---|---|---|---|---|
| 1 | Gravar o apresentador (corpo + 5 ganchos) | Apresentador | Nada | Gravação no celular, vertical, como em [`video/VIDEO.md`](video/VIDEO.md), seção 4 |
| 2 | Decidir título, preço e bônus do e-book | Você | Nada | Seção 9 preenchida |
| 3 | Adaptar o motor 3D para várias plantas | Claude | Nada | `render-planta.cjs` gera qualquer planta do catálogo pelo ID |
| 4 | Desenhar em dados as 11 plantas que faltam do 1º lançamento | Claude | Tarefa 3 | Situação `dados` no catálogo |
| 5 | Criar o perfil do Instagram | Você | Nada | Conta criada com o [`plano-perfil.md`](instagram/plano-perfil.md) |
| 6 | Revisar os textos do funil para o e-book e preencher preço | Parceiro | Tarefa 2 | Textos de [`ebook/vendas/`](ebook/vendas/) sem campos em branco |
| 7 | Montar e publicar os 5 reels de teste | Editor | Tarefas 1 e 5 | Linha preenchida no [registro de testes](instagram/INSTAGRAM.md#6-registro-dos-testes) |
| 8 | Subir o anúncio "Tem um lote 10 x 20?" com a Casa Compacta | Você | Tarefa 5 | Anúncio rodando com orçamento pequeno ([textos](video/anuncios/anuncio-facebook.md)) |

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
| 16/11 | Gancho principal: **"Vou te economizar os R$ 1.000 que um arquiteto te economizaria"**, em 5 versões para reels de teste |
| 16/11 | Visual: **blueprint azul que ganha vida** e vira **planta humanizada** em 3D |
| 16/11 | Edição no estilo do **Mino Lee**; retenção pelas regras do **Robert McKeaveney** ([`instagram/`](instagram/INSTAGRAM.md)) |
| 16/11 | Plantas **originais**; nada copiado de outros escritórios |
| 18/11 | Produto: **e-book com dezenas de plantas**, em vez de uma planta por vez |
| 18/11 | Lançar com **12 plantas** e crescer em levas (proposta da seção 3; confirme na seção 9) |
| 18/11 | Público principal: **quem tem um lote e vai construir com pedreiro, por etapas** ([estratégia](ESTRATEGIA.md)) |

## 9. Decisões pendentes

| Decisão | Opções | Recomendação |
|---|---|---|
| **Título** | "Planta Certa", "Casa Certa para o Seu Lote", "Cabe no Meu Lote" | Um título **sem número** e **com a palavra lote**, que é como o público fala. Ex.: **"Planta Certa: as casas que cabem no seu lote"**. Evite "prontas para construir": as plantas são de referência |
| **Preço** | R$ 47, R$ 67 ou R$ 97; preço único ou de lançamento | **R$ 67 de lançamento**, subindo no 2º e no 3º. Fica abaixo de uma planta avulsa (a partir de ~R$ 98 nos catálogos) e na faixa de compra por impulso. Confirme com a conta da seção 4 |
| **Pagamento e plataforma** | Pix direto; Kiwify; Hotmart | **Kiwify ou Hotmart**, com **Pix e cartão parcelado** e garantia de 7 dias. Já entregam checkout, área de membros e reembolso |
| **Order bump** | Nenhum; planilha de orçamento por etapa | **Planilha de orçamento por etapa**, a R$ 17–27, quando existir. Fala com quem constrói aos poucos |
| **Bônus** | Atualizações grátis; checklist de obra; os 7 erros; animações por QR code | Os quatro. As **atualizações grátis** são o mais forte |
| **Versão completa** (pranchas para obra) | Agora; depois; nunca | **Depois.** Exige projeto validado e assinado por arquiteto |
| **Planta grátis do funil** | Casa Compacta; outra | **Casa Compacta**: já tem 3D e aparece no vídeo |
| **Confirmar os 3 lançamentos** | Como na seção 3; ou outra divisão | Como na seção 3. Se os anúncios de **renda extra** (kitnet, edícula) forem bem, antecipe as especiais |
| **Ângulo do próximo anúncio** | Os 8 da [estratégia](ESTRATEGIA.md), seção 8 | **"Tem um lote 10 x 20?"**: concreto, a pessoa se reconhece na hora, e cada lote vira um anúncio |

Quando decidir, mova a linha para a seção 8 com a data.

## 10. Riscos e cuidados

| Risco | O que fazer |
|---|---|
| **Responsabilidade técnica.** Para construir e aprovar na prefeitura, a obra precisa de projeto com profissional habilitado | Escrever no e-book (capa interna e cada página) que as plantas são **de referência**, não projeto executivo, e que a obra precisa de responsável técnico. Confirmar o texto com um arquiteto |
| **Direito de arrependimento.** Compra pela internet pode ser cancelada em até 7 dias (Código de Defesa do Consumidor, art. 49) | Combinar com o parceiro como devolver o dinheiro; deixar a política escrita na oferta |
| **Direitos autorais** | Só plantas originais ou com licença escrita de venda. Nada de imagem de terceiros no e-book |
| **Regras de anúncio da Meta** para imóveis e construção | Conferir no Gerenciador de Anúncios antes de subir cada campanha, porque as regras mudam |
| **Medidas provisórias** | Nenhuma planta passa para `pronta` sem revisão de medidas |
| **Promessa do anúncio maior que o e-book** | O anúncio promete economia com um arquiteto; o e-book precisa mostrar, em cada planta, os erros que ela evita |

## 11. Rotina

| Quando | O quê | Quem |
|---|---|---|
| **Segunda** | Rodar `python3 ferramentas/atualizar-painel.py`, preencher os números da seção 7 e escolher as tarefas da semana (seção 6) | Você |
| **Terça a quinta** | Produção: plantas (Claude), gravação (apresentador), edição e publicação (editor) | Todos |
| **Quarta** | Conversa com o parceiro: o que as pessoas perguntam no WhatsApp vira gancho de vídeo e resposta no [FAQ](ebook/vendas/faq-compradores.md) | Você e parceiro |
| **Sexta** | Editor preenche o [registro de testes](instagram/INSTAGRAM.md#6-registro-dos-testes); você decide o gancho da semana seguinte | Editor e você |

**Para manter o painel em dia:**
- **Situação das plantas:** mude só a coluna **Situação** do [catálogo](ebook/catalogo.md). A seção 1 conta sozinha quando você roda o script.
- **O script também avisa** quando uma planta está como `3D` mas faltam arquivos, quando falta uma versão do vídeo e quando há link quebrado em qualquer guia.
- **Decisões:** ao decidir, mova a linha da seção 9 para a seção 8 com a data.

## 12. Quem faz o quê

| Pessoa | Responsabilidade | Onde trabalha |
|---|---|---|
| Você | Decisões, plantas (ideia e revisão) e anúncios | Este painel, [`ebook/`](ebook/EBOOK.md), [`video/`](video/VIDEO.md) |
| Parceiro | Funil: WhatsApp, sequência de mensagens, venda e reembolso | [`ebook/vendas/`](ebook/vendas/) |
| Editor | Edição e publicação dos vídeos do perfil | [`instagram/`](instagram/INSTAGRAM.md) |
| Apresentador | Gravação dos vídeos | [`video/VIDEO.md`](video/VIDEO.md), seção 3 (teleprompter) |
| Arquiteto | Validação das plantas e do texto de responsabilidade técnica | [`ebook/catalogo.md`](ebook/catalogo.md) |
| Claude | Dados das plantas, 3D, vídeos, páginas do e-book e textos | Todas as pastas |

## 13. Mapa do projeto

```
PAINEL.md                     ← este painel (centro de controle)
ESTRATEGIA.md                 público, posicionamento, oferta, ângulos e tom de voz
ferramentas/
  atualizar-painel.py           atualiza a seção 1 e confere arquivos e links
video/                        Vídeo de anúncio
  VIDEO.md                      guia: roteiro, teleprompter, gravação, edição
  saida/v1 … v5                 as 5 versões prontas
  anuncios/                     textos de anúncio, brief e checklist
  src/, render.cjs …            código do vídeo e do motor 3D
animacoes-3d/                 Animações 3D das plantas
  ANIMACOES-3D.md               guia: motor, estilo, entregas
  plantas/<nome>/               imagens e animação de cada planta
instagram/                    Espaço do editor
  INSTAGRAM.md                  guia: rotina, retenção, estilo, formatos, testes
  plano-perfil.md               identidade, pilares, primeiros posts
  referencias-mino-lee.md       análise completa das referências
ebook/                        O produto
  EBOOK.md                      guia: estrutura, página da planta, produção
  catalogo.md                   as 35 plantas, lançamento e situação de cada uma
  vendas/                       material do funil (parceiro)
```
