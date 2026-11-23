# Primeiro uso das duas skills novas (roteiro de entrada, passo "rodar uma vez sobre o que já existe")

> 23/11/2026. Skills: `.claude/skills/oferta-e-whatsapp/` e `.claude/skills/design-editorial/` (leitura das 6 fontes em [`skills-entrada-passo1.md`](skills-entrada-passo1.md)). **Nenhum arquivo do e-book ou da venda foi editado:** são achados para o Redator, o Designer e o dono. Até 5 por peça. Números aqui são só os que um comando devolveu (contagem de caracteres) ou o que se vê na imagem; nada foi medido em pontos ou milímetros.

## 1. `oferta-e-whatsapp` sobre `ebook/vendas/RESPOSTAS-RAPIDAS.md`

**O que já passa:** a saudação e a ausência já fazem a primeira pergunta (a medida do lote); a ausência não promete prazo; nenhuma urgência ou escassez; a garantia é a de 7 dias da entrega do link; `/arquiteto` e `/custo` seguram a seção 9; `/3d` leva "Imagem ilustrativa" e "Planta de referência"; não há depoimento nem número de clientes.

| # | Achado | Onde | De quem é |
|---|---|---|---|
| 1 | **Só existe uma mensagem já preenchida** ("Oi! Quero a planta grátis da Casa Compacta."), igual para todo mundo. Com mais de um anúncio ou origem (Direct do Instagram, anúncio A, anúncio B), não dá para saber qual trouxe a conversa, e o custo por venda por anúncio fica sem conta. O método pede um texto diferente por anúncio. | "Instagram: quem comenta PLANTA", link `wa.me` | Redator escreve; o dono decide quantos anúncios |
| 2 | **Falta o kit do anúncio pago que abre o WhatsApp:** não há as 3 frases de partida (até 80 caracteres) nem as perguntas que dizem se a conversa é de comprador. Hoje só "tem a medida do lote?" faz esse papel; "quando vai construir" só aparece depois do Pix, no `/recebi`. | arquivo inteiro | Redator, quando o dono decidir anunciar |
| 3 | **Buraco na oferta para quem cabe a Casa Compacta:** ela já recebeu essa casa de graça, e o `/confia` diz que a planta grátis "é igual às páginas do e-book". O `/oferta` não diz o que ela ganha a mais com essa mesma casa. Na equação de valor, é a peça "resultado" que fica fraca justamente para o lote mais comum (8 x 15). | `/oferta`, `/confia` | **Dono** (o que vai de graça está em aberto); Estrategista propõe |
| 4 | **Seis respostas passam de 300 caracteres** (contagem do texto com os colchetes: `/oferta` 476, `/arquiteto` 380, `/caro` 353, `/custo` 349, `/confia` 332, `/3d` 301). O próprio arquivo cita um limite de 512 por resposta rápida, de fonte não oficial: o `/oferta`, com nome e casa preenchidos, pode encostar nele. Testar no celular antes de ligar anúncio; se cortar, dividir em duas. | `/oferta` | Redator; teste do dono no celular |
| 5 | **Falta dizer onde se anota o preço e a origem de cada pessoa.** O arquivo manda "anote qual foi" o preço (R$ 47 ou R$ 67), mas não diz onde. Sem isso o teste de preço e o custo por venda não fecham; e a anotação tem nome e telefone, então não pode vir para o repositório (LGPD): planilha do dono, e aqui só a contagem. | cabeçalho, `/pix`, `/recebi` | Dono (onde anota); Estrategista (o que contar) |

Menor, fora dos 5: o `/recebi` faz duas perguntas na mesma mensagem (a regra é um pedido por mensagem).

## 2. `design-editorial` sobre a página da Casa Compacta (`ebook/plantas/rascunhos/estilo-final-C01.png`)

**O que já passa:** a planta é o elemento memorável e ocupa a maior parte da folha; a folha está cheia, sem vão que pareça erro; identidade do projeto (azul, amarelo, quadriculado); o aviso "Planta de referência. O projeto para a prefeitura é assinado por arquiteto ou engenheiro habilitado." está no rodapé, inteiro e descoberto; nada cai da folha.

| # | Achado | Pergunta ou vício da skill | De quem é |
|---|---|---|---|
| 1 | **A lista "Erros que esta casa evita" está numerada 1, 2, 4.** Parece erro de impressão (falta o 3). Se o número é o do erro no capítulo do e-book, a folha precisa dizer isso; se não é, tirar o número. | "Numerar o que não é sequência; pular número" | Designer, com o Redator |
| 2 | **A mesma informação aparece três vezes no topo:** o lote 8 x 15 está no rótulo, no subtítulo ("8 m de frente") e na pastilha amarela; "51 m²" e "2 quartos" aparecem duas vezes cada (subtítulo e pastilhas). Tirar uma camada dá mais altura para a planta. | "A mesma informação três vezes"; "tire um acessório" | Designer |
| 3 | **Etiquetas de cômodo cobrem o desenho:** a de BANHEIRO fica por cima da pia e encosta no vaso; a de SERVIÇO cobre o arco da porta; a de SALA E JANTAR pisa na borda do tapete. | "Nada se sobrepõe" | Designer (posição da etiqueta no gerador; o gerador está com outro agente agora) |
| 4 | **Três larguras na mesma folha, sem o lote desenhado:** "8 m de frente" no subtítulo, "8 m" na aba amarela da borda e a cota de 6,50 m em cima da planta. No primeiro olhar não fica claro que 8 m é o lote e 6,50 m é a casa; o lote inteiro não aparece nesta folha. Uma palavra resolve ("casa: 6,50 m", "lote: 8 m"). | "Dá para entender só pela manchete?" | Designer, com o Arquiteto |
| 5 | **Rótulo em caixa alta com ponto no meio** ("C01 · COMPACTAS · CABE NUM LOTE DE 8 x 15 M") e a legenda da planta no mesmo molde, em letra de máquina pequena. É o vício mais reconhecível do visual genérico e, na prévia, são as linhas mais difíceis de ler. A manchete-conclusão ("cabe num lote de 8 x 15 m") está escondida justamente ali. | Lista de vícios; "a manchete diz a conclusão" | Designer; mexe em estilo já aprovado, então é **opção para o dono** |

Não conferido: tamanho de letra em pontos e contraste por medida (só olhei a prévia); as outras folhas da casa (lote, 3D, ficha); se a folha final do `livro.py` é igual a este rascunho.
