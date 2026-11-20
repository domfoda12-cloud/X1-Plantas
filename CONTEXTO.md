# Contexto do projeto: tudo o que o dono pediu, e o que cada pedido quer dizer

> **Leia antes de qualquer tarefa.** Cada pedido do dono tem um motivo e continua valendo até ele dizer o contrário. Toda sessão (nuvem, Mac, MinoAI Frontier) acrescenta aqui, no fim, cada pedido novo com a data e o que ele quer dizer na prática. Regra em [`CLAUDE.md`](CLAUDE.md).

## O que nunca muda

| O dono disse | O que isso quer dizer |
|---|---|
| "O objetivo é a alegria do consumidor, e a alegria dele me mandar o Pix" | Toda entrega é julgada por duas coisas: o comprador fica feliz com o que recebe? Ele paga? |
| "Pensa como um marketeiro, público brasileiro" | Português do Brasil, R$, Pix, WhatsApp, quem constrói com pedreiro por etapas. Ver [persona](ebook/referencias/persona-e-mercado.md) |
| "Sempre do ponto de vista de um arquiteto profissional" | Toda planta passa pelo validador e explica o porquê de cada decisão |
| "Não tem landing page" | Venda por anúncio (Facebook e Instagram) → comentário → WhatsApp. O parceiro cuida do funil, o dono cuida do material e do anúncio |
| "Mantenha todo o contexto, tudo o que eu faço significa algo" | Este arquivo. Nada do que foi pedido se perde entre conversas |
| "Quero a opinião da MinoAI sempre, ele é o maestro" | Toda entrega traz a opinião do Maestro, tirada das ferramentas da MinoAI Frontier, com a fonte |
| "Falo muito de eficiência, mas a prioridade é sempre a maior qualidade" | Peça final sempre na melhor configuração; economia só em rascunho e teste ([`CLAUDE.md`](CLAUDE.md)) |
| "Foque em uma coisa por vez, não misture tudo ao mesmo tempo" | Uma frente por vez, do começo ao fim, antes de abrir outra. Ordem atual: e-book → animações → vídeo |
| "Ótimo ao máximo, TUDO" | Fazer completo e bem feito, sem atalho que prejudique a qualidade |
| "Continue trabalhando sem pedir permissão" (para tarefas internas) | Avançar sozinho no que é interno; decisões de dinheiro, título, preço e publicação continuam com o dono |

## Linha do tempo dos pedidos

| Quando | Pedido | O que virou |
|---|---|---|
| Início | Vender no X1 "planta de casas", não é campanha de Natal (outra sessão) | Produto: e-book de plantas |
| Início | Adicionar o repositório, tudo em português, Facebook Ads + WhatsApp, Brasil primeiro e talvez fora depois | Repositório `X1-Plantas`, branch `planta-de-casas-anuncio` |
| Início | Sem landing page; dono faz material e anúncio, parceiro faz o funil | [`ebook/vendas/`](ebook/vendas/) com a sequência do WhatsApp |
| Fase de vídeo | Brief criativo; procurar plantas e pensar em animar em 3D; perfil de Instagram de arquitetura | [`video/anuncios/brief-criativo.md`](video/anuncios/brief-criativo.md), [`animacoes-3d/`](animacoes-3d/), [`instagram/plano-perfil.md`](instagram/plano-perfil.md) |
| Fase de vídeo | Seguir o reel de referência; prestar atenção na retenção; o cliente precisa se interessar pelas plantas | Regras de edição em [`instagram/MINOAI-FRONTIER.md`](instagram/MINOAI-FRONTIER.md) e [`instagram/referencias-mino-lee.md`](instagram/referencias-mino-lee.md) |
| Fase de vídeo | Clipes menos travados: blueprint azul ganhando vida; gancho "vou te salvar os R$ 1.000 que um arquiteto te salvaria" | Motor 3D com blueprint que ganha vida; 5 versões de gancho em `video/saida/` |
| Fase de vídeo | Narrador sempre falando, sem pausa, sempre um visual prendendo a atenção | Regra de roteiro em [`video/VIDEO.md`](video/VIDEO.md) |
| Fase de vídeo | Referências do perfil minolee.mp4 e de 3 reels; juntar tudo de valioso ao editor | [`instagram/referencias-mino-lee.md`](instagram/referencias-mino-lee.md) |
| Fase de vídeo | Não precisa verificar preço de arquiteto | Fora das pesquisas |
| Organização | Dezenas de plantas num e-book com grande variação; pastas Vídeo, Animações 3D, Instagram, E-book e um painel que controla tudo | [`PAINEL.md`](PAINEL.md), [`ebook/catalogo.md`](ebook/catalogo.md) com 35 plantas em 3 lançamentos |
| Organização | Não só revisar, melhorar o conteúdo; um chat por frente | Chats na nuvem por frente (branches `frente-*`) |
| Organização | MinoAI Frontier como editor e depois como maestro | [`MAESTRO.md`](MAESTRO.md) |
| Organização | Roteiro "volto pro Brasil com casas na mala" | [`video/roteiro-lancamento.md`](video/roteiro-lancamento.md) |
| Ferramentas | Skills para o e-book (Impeccable só para opinar sobre o genérico; Karpathy); ferramenta de pesquisa melhor (TinyFish), por meios brasileiros e sites oficiais | Pesquisa jurídica em [`reports/`](reports/); TinyFish no Pesquisador |
| 19–20/11/2026 | Analisar os 5 catálogos de porcelanato; linguagem que convence; visual melhor; animações; pelo menos 20 plantas como um arquiteto; pesquisa de público com uma persona alinhada ao arquiteto; como as casas são de verdade no Brasil | 24 plantas validadas ([`ebook/plantas/PLANTAS.md`](ebook/plantas/PLANTAS.md)), [persona "Marcos"](ebook/referencias/persona-e-mercado.md), [regras do arquiteto](ebook/referencias/regras-do-arquiteto.md), [análise dos catálogos](ebook/referencias/analise-catalogos-porcelanato.md), [linguagem e animação](ebook/referencias/linguagem-visual-e-animacao.md) |
| 20/11/2026 | Um redator que sempre pensa em bons atributos, com o objetivo no dinheiro | Agente [`redator`](.claude/agents/redator.md), skill `/redacao-que-vende`, [banco de atributos](ebook/vendas/atributos-que-vendem.md) |
| 20/11/2026 | Um ecossistema de skills que se entendem, dão opinião e só usam a skill quando concordam | [Conselho](CONSELHO.md), skill `/conselho`, 7 agentes em `.claude/agents/` |
| 20/11/2026 | Depois disso, começar o e-book; exemplo de skills juntas: MinoAI + OpenArt para imagens e animações | [Fluxo OpenArt + MinoAI](animacoes-3d/OPENART-MINOAI.md) (OpenArt sem conector; usado no navegador ou por API com chave) |
| 20/11/2026 | Segurar as animações 3D, deixar por último | Motor preparado para as 24, render parado; passo 9 do plano |
| 20/11/2026 | Primeiro o roteiro passo a passo e como o e-book vai ficar; "visualize it" | [`ebook/PLANO-EBOOK.md`](ebook/PLANO-EBOOK.md) e a prévia visual (página privada no claude.ai, fonte em [`ebook/visual/plano-visual.html`](ebook/visual/plano-visual.html)) |
| 20/11/2026 | O objetivo é a alegria do consumidor, que vira Pix | Primeira regra do [`CLAUDE.md`](CLAUDE.md) e do Redator |
| 20/11/2026 | Manter todo o contexto | Este arquivo |
| 20/11/2026 | "Quero que pareça mais inovador" | Prévia nova: capa fita métrica, vitrine pelo lote, casa desenhada no lote com recuos e bússola, ficha "Informação da casa" no formato da tabela nutricional, orelhas por largura de lote, e-book vivo por QR |
| 20/11/2026 | "A edição de vídeo é responsabilidade e a criação de imagem será o Mino usando o OpenArt" | MinoAI Frontier dona da edição de vídeo e da criação de imagem, com o plugin OpenArt (falta autorizar a conta). [`MAESTRO.md`](MAESTRO.md), [`CONSELHO.md`](CONSELHO.md), [fluxo](animacoes-3d/OPENART-MINOAI.md) |
| 20/11/2026 | "A MinoAI está fazendo algo aqui? Ele é o maestro. Quero a opinião dele sempre" | MinoAI Frontier opina em toda tarefa, primeiro, com as ferramentas dele e a fonte ([`CONSELHO.md`](CONSELHO.md), regra 0). Primeira opinião registrada na prévia do e-book |

| 20/11/2026 | "Economizar o máximo do OpenArt, mas enfeitado; pode começar, mas não use o primeiro modelo" | Plano de economia em [`animacoes-3d/OPENART-MINOAI.md`](animacoes-3d/OPENART-MINOAI.md): modelo de imagem em vez do padrão de vídeo, rascunho antes, uma imagem para vários formatos, teto de 6. OpenArt ainda sem autorização |
| 20/11/2026 | "Prepare tudo o que precisa ser preparado, e dale. EFICIÊNCIA" | E-book gerado: [`ebook/saida/ebook.pdf`](ebook/saida/ebook.pdf) (61 páginas) e a planta grátis C01 com a página-ímã; 3 mockups grátis em `ebook/visual/mockups/` |

| 20/11/2026 | "Esquece o limite de crédito do OpenArt, volta para ele" | Sem teto de crédito. Geração começa assim que a conta do OpenArt for autorizada (ainda pede login) |

| 20/11/2026 | "Continue melhorando sem o OpenArt, estou longe do computador" | Plantas mobiliadas com portas, vista da rua de cada casa, B-roll grátis do e-book folheado (`video/broll/ebook-folheando.mp4`) e revisão completa do Revisor de risco (8 vetos e 16 ajustes aplicados; "o que o arquiteto pensou" virou "por que esta planta é assim" até um arquiteto assinar) |

| 20/11/2026 | "Continue procurando melhorias em loop" | Loop autônomo. Rodada 1: juntados os posts de `frente-instagram` e o roteiro do vídeo 2 de `frente-video`, com números corrigidos pelo validador; a E07 foi redesenhada e agora cabe em lote de 8 m (3 quartos, suíte, 72 m²), o que torna verdadeira a promessa do vídeo 2 |

| 20/11/2026 | "Expanda a base de dados: procure animações 3D de plantas ganhando vida. Só pare quando os tokens acabarem" | [`animacoes-3d/REFERENCIAS-BLUEPRINT.md`](animacoes-3d/REFERENCIAS-BLUEPRINT.md): 11 referências com links, anatomia do efeito, 10 melhorias para o motor e roteiro de 12 s revisado. Loop continua |

| 20/11/2026 | (loop) Revisão do Revisor de risco nos posts e no vídeo 2 | 9 vetos e 10 ajustes aplicados: posts com o 3D antigo da C01 saem do calendário até o 3D novo; números da C01 e da F03 corrigidos; vídeo 2 sem a "virada" da divisa (a E07 não encosta), com aviso de planta de referência e planta grátis C01; material gratuito agora é o PDF novo |

| 20/11/2026 | (loop) Conferência do funil e dos anúncios | Anúncio "Tem um lote 10 x 20?" com a contagem real (14 casas; 8 x 25: 11; 10 x 25: 17; 12 x 25: 22); WhatsApp manda o PDF novo e diz "a partir de 8 x 15"; "todas em 3D" virou "mobiliadas e desenhadas no lote" (o 3D é o último passo) |

| 20/11/2026 | (loop) Ferramenta de venda | Calculadora de lote para o parceiro: frente x fundo → casas que cabem, com página do e-book e mensagem pronta ([`ebook/vendas/calculadora-lote.html`](ebook/vendas/calculadora-lote.html), página privada no claude.ai: https://claude.ai/artifact/1aTFXGXffcoWXPeBXsdYA6) |

| 20/11/2026 | (loop) Planta grátis por lote | 6 plantas grátis prontas (C01, E03, E02, E07, F01, C06): o parceiro manda a que cabe no lote do cliente ([`ebook/vendas/material-gratuito.md`](ebook/vendas/material-gratuito.md)) |

| 20/11/2026 | "Procure referências de projetos similares; se for internacional, adapte aos termos do Brasil" | [`ebook/referencias/projetos-similares.md`](ebook/referencias/projetos-similares.md): Só Projetos, Planta Pronta, Projeto Pronto, Archshop, sites americanos de "terreno estreito" e Etsy. Corrigida a afirmação de que ninguém busca pelo terreno; ficha ganhou medidas da casa e "pode espelhar"; âncora de preço com fonte |
| 20/11/2026 | "A operação está rodando no computador correto?" | Não é o computador do dono: a sessão roda num contêiner na nuvem, e tudo fica salvo no GitHub (branch `planta-de-casas-anuncio`). A edição de vídeo da MinoAI precisa do Mac do dono |

| 20/11/2026 | "OpenAI deve estar liberado" | Uma sessão nova procurou as ferramentas do OpenArt e também não achou: o plugin continua pedindo login. Sessão arquivada |
| 20/11/2026 | "A qualidade da imagem está baixa: quero o mais perto possível de HD, Full HD, 4K" | Tudo em alta: prévias das 24 plantas e imagens 2D em 3200 x 4000, páginas do e-book em 2382 x 3372, mockups em 2160 x 2700, posts do Instagram em 2160 x 2700, B-roll em 2160 x 3840 (4K vertical). O PDF já era vetorial. Os carrosséis agora usam as plantas validadas, sem o 3D antigo |

| 20/11/2026 | "OpenArt adicionado" e "aprenda a tirar o máximo de cada crédito com resultado muito bom" | Primeira rodada feita pela MinoAI com o OpenArt (GPT Image 2.5 Sunburst, não o primeiro modelo): 6 imagens finais em 2048 x 2560 com recortes 9:16 e 1:1 em `ebook/visual/openart/final/`, cerca de 200 créditos. Guia de preços e hábitos em [`animacoes-3d/OPENART-MINOAI.md`](animacoes-3d/OPENART-MINOAI.md): rascunho a 5, final em 4K média a 20, alta (70) só na peça principal; casa só a partir da nossa vista da rua; vídeo começa no PixVerse V6 (50). A vista da rua de todas as casas foi corrigida (porta não fica mais sobre a janela) |

| 20/11/2026 | "A prioridade deve ser sempre a maior qualidade" | Regra no topo do `CLAUDE.md`. OpenArt: rascunho continua barato; final passa a ser na qualidade máxima útil, com teste lado a lado Sunburst extra-alta x Kling 3 Omni 4K para escolher o melhor |

| 20/11/2026 | (loop) Rodada final do OpenArt em extra-alta | 6 finais em 2048 x 2560 (lote na qualidade máxima) com recortes 9:16 e 1:1; teste mostrou máxima quase igual à extra-alta, então extra-alta é o padrão. Saldo: 2.757 créditos. Fotos entraram no e-book com "Imagem ilustrativa": mãos medindo (como usar), lote com trena (ficha do terreno), planta no canteiro (próximos passos), família (página final) e papel azul no fundo da capa |

| 20/11/2026 | "Preste atenção no limite semanal e separe quanto gastar em cada uma das três partes que faltam: e-book, animações, vídeo" | [`ORCAMENTO.md`](ORCAMENTO.md): animações 45% (1.500 créditos do OpenArt), vídeo 30% (800), e-book 25% (450). A sessão não enxerga o limite semanal: o dono informa a porcentagem e a tabela vira número. Recomendação: uma sessão nova por parte |

| 20/11/2026 | "De vez em quando, sempre confira se tem erro no código" | `python3 ferramentas/checar.py` confere a sintaxe de todo .py/.cjs/.js, o validador das 24 plantas, o motor 3D e o painel; regra no `CLAUDE.md` (rodar de vez em quando e sempre antes de entregar). Primeira rodada: tudo certo |

| 20/11/2026 | (e-book, tarefa 1) Fachadas realistas | C01, E07, F01 e C03 com foto realista da fachada (OpenArt, a partir da nossa vista da rua, 4K extra-alta) no lugar do desenho, com "Imagem ilustrativa gerada a partir da vista da rua desta planta"; as outras casas mantêm o desenho. Conferência de página estourada agora mede o miolo (achou e corrigiu 3 páginas); avisos repetidos do validador viram uma frase só |
| 20/11/2026 | "Adicione este vídeo como referência… melhor edição que já vi… absorva os conceitos no vídeo curto" (CONDOR XIII, Payton Talbott) | [`video/REFERENCIA-CONDOR.md`](video/REFERENCIA-CONDOR.md): 7 conceitos levados para o reel de planta (tese antes do assunto, letra como janela, planta invertida que gira, série numerada CASA I, II…, ritmo de mixtape guiado pela música, cortes por semelhança), com o Maestro e o Revisor. O YouTube bloqueou o download na nuvem, então os conceitos vêm da descrição, da miniatura e da imprensa. Falta assistir quadro a quadro no Mac |
| 20/11/2026 | "O analyze hook é ferramenta da MinoAI? Se sim, faça funcionar" | Sim, é da MinoAI Frontier, mas só aceita TikTok e Instagram. Funcionou nos 7 reels do Instagram do Payton (mesma dupla de edição, um deles trecho do ECDYSIS XII): mais 6 conceitos na seção 1b de [`video/REFERENCIA-CONDOR.md`](video/REFERENCIA-CONDOR.md) (corte por metáfora, imagem que ilustra a frase, legenda irônica, detalhes na batida, fim forte sem silêncio, erros a evitar). Nenhum reel é trecho do CONDOR XIII |
| 20/11/2026 | "Preste muita atenção nos B-rolls e nas escolhas de música dele" | Seção 1c de [`video/REFERENCIA-CONDOR.md`](video/REFERENCIA-CONDOR.md): tipos de B-roll (metáfora animal e da natureza, ritual em close, terreno de terra filmado como revista, mídia misturada) e padrão da música (contraste com a imagem, som de assinatura, faixas fora das paradas, nostalgia, letra como legenda, música autoral), com a fonte de cada faixa (rótulos do Instagram e playlist de fã com 100 faixas). Tudo levado para o reel de planta, com os cuidados de direito autoral (anúncio só com música licenciada) |
| 20/11/2026 | "Como assim música própria, minha? O Payton não produz música, no máximo usa remixes" | Corrigido em [`video/REFERENCIA-CONDOR.md`](video/REFERENCIA-CONDOR.md): saiu a ideia de música composta para o X1-Plantas; o princípio agora é o **remix** (faixa licenciada mais lenta, com eco ou cortada). O "Music Produced by Payton Talbott" dos créditos vale só para o filme Files of Lars |
| 20/11/2026 | "O e-book está pronto?" → "Comece e termine no geral o draft 1" | **Rascunho 1 do e-book fechado** (61 páginas + 6 grátis), depois da revisão final do Conselho (Revisor de risco, Arquiteto e Redator lendo o PDF inteiro). Principais correções: (1) paredes com espessura: as medidas da casa são por fora e a área de cada cômodo é por dentro, e o validador confere os mínimos pelo lado de dentro; (2) desenho: a ampliação da C03 foi para trás da área de serviço e não tapa mais a janela do quarto casal; os quartos da E04 abrem janela para o pátio; a S09 abre janela para a rua do lado; o banheiro da suíte da F02 ficou mais largo; (3) honestidade: saiu a promessa de 3D, a regra de recuo cita a exceção da E03, "um sexto do piso" vale só para sala e quartos (cozinha é um oitavo), "corredor comprido evitado" só aparece onde é verdade, o acesso pelo corredor externo das casas estreitas é dito com clareza, e a "Área coberta total" entrou na ficha; (4) a planta 2D usa as mesmas posições de porta e janela da vista da rua e das fotos; a foto da F01 perdeu duas aberturas falsas na parede da divisa (retoque local, sem crédito); (5) texto: título "Cabe num lote de 8 x 15.", perguntas gerais numa lista única na última página ("Agora é com você"), sol explicado uma vez, palavras difíceis explicadas. Conferência: 24 plantas, 0 erros; checar.py tudo certo |
| 20/11/2026 | (Revisor de risco, reconferência) | Os 3 vetos foram resolvidos e o veto novo também: o banheiro da S03 Casa Acessível cresceu para 3,2 x 1,9 m (cabe o giro de 1,50 m), e o validador agora confere isso. O detector de página estourada passou a medir em modo de impressão (achou e corrigiu 8 páginas). Para publicar, falta só o dono: bônus e WhatsApp do parceiro na página 61 |

## Em aberto (esperando o dono)

- Assistir ao CONDOR XIII quadro a quadro no Mac (o YouTube bloqueia a nuvem), ou mandar 3 a 5 momentos favoritos com o minuto, para completar [`video/REFERENCIA-CONDOR.md`](video/REFERENCIA-CONDOR.md).
- Informar quanto resta do limite semanal (claude.ai, Configurações → Uso) para fechar o orçamento em números.


- Compartilhar a calculadora de lote com o parceiro (menu Share da página) para ele usar no WhatsApp.
- Os 5 vídeos de anúncio (`video/saida/v1` a `v5`) usam o 3D antigo da Casa Compacta: refazer quando o 3D for liberado.

- Testar a palavra do comentário "PLANTA" contra "LOTE" ([`ebook/referencias/concorrentes.md`](ebook/referencias/concorrentes.md)): "PLANTA" também é usada por criadores de jardinagem.

- Decidir se o e-book promete as próximas casas de graça (o texto só aparece se `promessa_atualizacao` for preenchido em `ebook/config.json`, porque oferta escrita obriga).


- Aprovar o plano do e-book (formato A4 de cerca de 60 páginas, capa "Que casa cabe no seu lote?", começar os passos 1 a 6).
- Título, preço, bônus, lançar com 12 ou 24 plantas, contato do parceiro.
- Arquiteto registrado para revisar as 24 plantas (o rascunho 1 já mostra medidas por fora e áreas por dentro; ele confere as casas apertadas que o validador marcou: E02, E03, suítes da E01, E05 e E07).
- Preencher no `ebook/config.json`: título, preço, bônus, WhatsApp do parceiro e, se quiser, `promessa_atualizacao`. São os únicos espaços reservados do rascunho 1 (página 61).
- Depois do rascunho 1: regenerar as imagens 2D dos posts e o 3D das casas que mudaram (C03, E04, F02, S09) quando a frente de animação abrir.
- Gravar o apresentador; criar o Instagram; configurar a MinoAI Frontier no Mac.
- Atualizar o relatório jurídico com Caixa e Confea (pedido antes, sem resposta).
- Reels 1 e 6 usam o vídeo 3D antigo da Casa Compacta: usar o B-roll do e-book ou esperar o 3D novo.
