# Vídeo: reel de referência no lugar do cachorro caramelo, POV do caramelo no WhatsApp, zoom out, memes brasileiros

**Estado:** aberta

**Prompt (palavra por palavra):** https://www.instagram.com/reel/DTw4bqHE5zj/?hl=en
Ao inves de um  cachorro caramelo adicione esse video a lista de referencia,  use o video para o video princiapl do ads/instagram e no video do whatsapp mostre a casa pela perspectiva de um caramelo, tambem quero que em algum momento a camera diminua o zoom dando um efeito especial no video( you can look for one to use in the editor references)
Durante a procura de referencias procure memes brasileiros atemporais como esse

*Recado de 22/11 20:54 (vinha no lugar do prompt, corrigido pela auditoria do Fable):* Ill be out for a while, go full potent back in the project if youre done fixing all systematical error, or improvements

*Recado de 22/11 21:07:* Crie branches e planos diferente para cada passo

*Recado de 22/11 21:07:* 1. Sim, a crianca e o cachorro dancando na frente da casa

*Recado de 22/11 21:08:* Sao 2 videos, 1 mostrando uma previa do que eles vao ver no ebook, outro fazendo a divulgacao do produto, o principal é a divulgacao mas a previa também é bem importante

**O que ele pediu, parte por parte:** 1) O reel DTw4bqHE5zj (menino dançando 'Tô de boa, desce um pouquinho' ao lado do cachorrinho, 2016) entra na lista de referências e toma o lugar do cachorro caramelo no **vídeo principal** (anúncio e Instagram). 2) No **vídeo do WhatsApp** (a prévia que vai ao cliente), a casa aparece do ponto de vista de um vira-lata caramelo. 3) Em algum momento, a câmera faz um zoom out com efeito especial, tirado das referências de edição. 4) Em toda busca de referência, procurar memes brasileiros atemporais como esse.

**Por que ele pediu, ou o que quer descobrir:** Ele quer referência brasileira que todo mundo reconhece e que não envelhece (antes recusou o 'morango do amor' por ser de 2025). O meme dá o reconhecimento instantâneo nos 3 primeiros segundos; o caramelo, que é afeto brasileiro, vira o olhar do vídeo do WhatsApp. O zoom out é o momento de 'uau' da edição.

**Objetivo dele:** Vídeos que o brasileiro reconhece na hora, param o dedo e fazem querer a casa.

**Ligação com as ideias gerais do projeto:** Fio 2 (Brasil de agora, humor de família, nada de referência velha... aqui 'atemporal'), fio 7 (MinoAI na frente, referência real como direção), fio 1 (parece de verdade).

**Perguntas que me fiz:** Pode usar o clipe original? Não sem autorização: é imagem de uma criança e de terceiros; em anúncio pago, só **recriado** (o clima, o gesto, a frase), nunca o vídeo dele (o Revisor confere). 'Vídeo do WhatsApp' é a prévia (21/11: 'vai para o cliente no WhatsApp'). A casa: a E07 está sendo redesenhada; o vídeo usa a casa aprovada quando o dono aprovar. Zoom out: o kit da MinoAI tem `05-motion-kits/pipeline/make_zoom2.py` (achado na busca). Ponto de vista do caramelo: câmera a uns 40 cm do chão, andando pela casa; sai no motor 3D (ilustração) ou na filmagem do dono com o celular baixo; realista no OpenArt só com o 'sim'.

**Pronto quando:** Plano vetado (2 rodadas do time e o Fable); roteiro dos dois vídeos com o momento do meme, o POV do caramelo e o zoom out marcados no tempo; resumo da produção e custo prontos para o 'sim' do dono; nada gerado nem gasto antes disso.

**Suposições (o dono não disse):** 'Vídeo do WhatsApp' = a prévia do WhatsApp. O meme é recriado, não copiado. A casa é a que o dono aprovar no redesenho (hoje a E07). Os memes atemporais vão ao caderno `pesquisas/video.md`.

**Quem executa:** Maestro (Opus): plano e conferência. Diretor (MinoAI): ideia principal e o zoom out do kit. `editor-video`: roteiro. `redator`: frase na tela. `revisor-de-risco`: direito de imagem do meme e da criança (Fable na peça final). `arquiteto`: a casa do POV bate com a planta. `pesquisador`: memes brasileiros atemporais. `supervisor` (Fable): veto final do plano.

**Conferência:** (no fim)

**Resultado:** (a preencher)


## Plano detalhado, versão 4 (depois do veto do Fable)

**Veto do Fable (22/11):** VETO, com 7 correções, todas aplicadas abaixo: (1) a ficha tinha o prompt errado (corrigido; `pedido.py` agora mostra o prompt que copia e aceita `--de`); (2) **fato errado:** o escaneamento não abre o principal; pela fala do dono ele entra "after the hook lands, before the CTA", então a abertura (gancho) está livre, e os segundos 9,38 a 11,25 vinham de um plano substituído; (3) suposições viraram decisões: agora são perguntas ao dono (passo 3); (4) produzir só depois do resumo, das instruções e do custo confirmados (`video/CLAUDE.md`); (5) zoom out vem dentro dos roteiros, com o efeito trazido pelo Diretor; (6) memes atemporais são regra permanente, não uma busca só; (7) motor 3D é rascunho, não peça final ("quero REALISTA").

Objetivo de todos: o brasileiro reconhece na hora, para o dedo, e quer a casa.

| # | Tipo | Passo | Quem | Pronto quando |
|---|---|---|---|---|
| 1 | P | Reel em `video/REFERENCIAS.md`: só o link e a análise; repost (sem direitos); ano "a confirmar"; regra: recriar a situação, nunca o menino, o rosto, o áudio ou a música | Maestro | seção nova |
| 2 | P | **Regra permanente:** toda busca de referência procura também memes brasileiros atemporais; lista tudo, com a coluna "dá para recriar em anúncio?" (não: criança, rosto de alguém, cena de TV ou novela, marca, música protegida). Primeira busca: 3 candidatos e a origem da frase "Tô de boa, desce um pouquinho" | `pesquisador` acha; `editor-video` conclui; `revisor-de-risco` marca a coluna | regra nos contextos do Pesquisador, do Diretor e do Editor; 3 linhas no caderno |
| 3 | Dono | **Perguntas ao dono** (com o padrão se não responder): (a) onde entra o meme: **como gancho, nos primeiros segundos** (padrão, já que a abertura está livre) ou no meio; (b) qual é o "vídeo do WhatsApp": a **prévia** (padrão), o convite ou o anúncio com locução; (c) "ads/instagram": o principal vai ao Facebook Ads e ao Instagram? (hoje a ordem é: o anúncio com locução vai a WhatsApp e Facebook Ads, não ao Instagram); (d) quer teste A/B? (padrão: não, ele não pediu; a versão B recolocaria o caramelo que ele mandou tirar); (e) em qual vídeo vai o zoom out (padrão: no fim da prévia, abrindo para a casa no lote); (f) quem dança na recriação (ele, família com autorização escrita, ator); (g) PLANTA ou LOTE; aviso junto: o clipe original não pode ser usado, só recriado | Maestro pergunta | respostas na ficha |
| 4 | P | Ideia principal de cada vídeo (Diretor, com fonte), qual é o principal-base, e o efeito de zoom out com a fonte (o `make_zoom2.py` do kit só existe no Mac: o Diretor confirma lá) | Maestro com o Diretor; `revisor-de-risco` olha a ideia do meme | ideia + efeito + SIM do Revisor |
| 5 | G | **Roteiro do principal** com o meme no lugar que o dono escolher, o zoom out se for nele, o texto no primeiro quadro; tempo de cada quadro saído do roteiro novo (nada de segundos herdados) | `editor-video`; `redator` (texto); `arquiteto` (casa e lote) | roteiro |
| 6 | G | **Roteiro da prévia do WhatsApp:** o que fica da prévia atual (o e-book por dentro, pedir a medida do lote) + o POV do caramelo pelo caminho da planta aprovada (40 cm, FOV de uns 60°, vão das portas, janela só céu sem prometer "casa clara") + zoom out se for nela; até 5 MB, comprimido | `editor-video`; `arquiteto` confere o mapa | roteiro + mapa aprovado |
| 7 | P | Resumo da produção, lista de instruções e custo de cada vídeo. Rotas: filmagem do dono com o celular (realista, custo zero) ou OpenArt (realista, crédito, só com o "sim"); motor 3D só como rascunho e guia de câmera | Maestro | resumo pronto |
| 8 | Dono | "Sim" ao resumo, às instruções e ao custo (regra de `video/CLAUDE.md`) | dono | resposta |
| 9 | G | Produzir **o principal**; edição final na MinoAI, no Mac; Revisor no Fable | `editor-video` | principal aprovado pelo dono |
| 10 | G | Depois, produzir **a prévia**, com a casa aprovada no redesenho (ficha `1616`), sem rascunho na F03 | `editor-video` | prévia aprovada pelo dono |
| 11 | P | Medir, se o dono quiser teste: o que muda entre as versões e o número do parceiro | `estrategista` | proposta ao dono |

## Ramos do plano: um caminho para cada resposta do dono (pedido de 22/11, "crie branches e planos diferentes para cada passo")

Cada pergunta do passo 3 abre ramos. O ramo marcado **(padrão)** é o que se faz se o dono não responder. Os passos citados são os da versão 4.

**R1 · Onde entra o meme**
| Ramo | O que muda | Custo e risco | Para quem |
|---|---|---|---|
| R1a · gancho, 0 a 3 s **(escolhido pelo dono, 22/11: "a criança e o cachorro dançando na frente da casa")** | Passo 5 abre com a recriação; o escaneamento vem logo depois, como manda a fala do dono | Mais reconhecimento nos 3 s; se o meme não for reconhecido sem o áudio, o gancho cai | quem não conhece a marca |
| R1b · no meio (antes da chamada) | Abertura fica com a casa pronta e o gancho de texto; o meme vira o respiro antes do "comenta PLANTA" | Menos risco no gancho; o meme pesa menos | quem já parou |
| R1c · nos dois vídeos | Gancho no principal e de novo na prévia | Reforça a marca; dobra a produção da recriação | — |

**R2 · Qual é o "vídeo do WhatsApp"**
| Ramo | O que muda |
|---|---|
| R2a · a prévia **(escolhido pelo dono, 22/11: "1 mostrando uma prévia do que eles vão ver no e-book, outro fazendo a divulgação"; o principal é a divulgação, a prévia também é bem importante)** | Passo 6 como está: e-book por dentro + POV do caramelo + pedir a medida do lote; até 5 MB |
| R2b · o convite (F03) | Passo 6 parte do convite ("extremamente convidativo", uma casa só); POV entra no passeio; F03 só se o dono aceitar a F03, senão a casa aprovada |
| R2c · o anúncio com locução | O POV entra no anúncio com a voz do dono; o roteiro dele (`ANUNCIO-LOCUCAO.md`) muda; precisa da gravação |

**R3 · Instagram**
| Ramo | O que muda |
|---|---|
| R3a · o principal vai ao Facebook Ads e ao Instagram **(padrão: perguntar antes, porque mexe numa ordem dele)** | Duas saídas do mesmo vídeo: 4:5 (feed) e 9:16 (Reels), até 12 MB |
| R3b · Instagram só orgânico, Facebook Ads só o anúncio com locução | Fica a ordem de hoje; o principal com meme vira Reel do perfil |

**R4 · Teste A/B**
| Ramo | O que muda |
|---|---|
| R4a · sem teste **(padrão)** | Passo 11 sai; produz-se uma versão |
| R4b · teste com verba pequena | Passo 9 produz também a versão B (sem o meme, ou com o gancho antigo); o Estrategista mede retenção depois do trecho que muda, comentários, custo por contato e conversão do parceiro |
| R4c · teste orgânico | As duas versões no perfil do Instagram, sem gasto; só depois que o perfil existir |

**R5 · Zoom out**
| Ramo | O que muda |
|---|---|
| R5a · fim da prévia **(padrão)** | A câmera do caramelo sobe e abre para a casa no lote do "Cabe a partir de" |
| R5b · no principal | O zoom out fecha o escaneamento: da planta para a casa no lote |
| R5c · nos dois | O mesmo efeito vira assinatura da marca |

**R6 · Quem dança na recriação** (o dono quer **uma criança e um cachorro**, na frente da casa: ramos refeitos abaixo, em veto)
| Ramo | O que muda | Custo e risco |
|---|---|---|
| R6a · o dono | Ele filma junto com os planos do celular | Zero; autorização dele mesmo; mais autêntico |
| R6b · família | Autorização escrita guardada antes | Zero; mais um passo |
| R6c · ator | Contratar (decisão do dono) | Pago; mais controle |
| R6d · sem pessoa: só o cachorro reagindo e a frase na tela **(padrão)** | Nenhuma autorização | Zero; o meme fica mais fraco |

**R7 · PLANTA ou LOTE**: R7a PLANTA **(padrão, é o que os textos já usam)**; R7b LOTE (troca a chamada nos dois vídeos e no funil do parceiro).

**Rotas de produção (vale para todos os ramos):** filmagem do dono com o celular (realista, custo zero, espera ele filmar) ou OpenArt (realista, crédito, só com o "sim"). Motor 3D só para rascunho e guia de câmera.

## Qualidade do veto (régua de 5 pontos, nota do Maestro)

| Rodada | Agente | Nota | Por quê | Repreensão |
|---|---|---|---|---|
| 1 | Editor | 5 | Achou que o meme na abertura contrariava uma ordem do dono, com a linha de `VIDEO.md`; a música do meme; quem dança; suposição "5 anos" | — |
| 1 | Revisor | 5 | Veto com correção; criança, repost, bandeira (marcado "o jurídico confirma") | — |
| 1 | Arquiteto | 5 | Caminho da câmera sai da planta; FOV, peitoril, quintal; lote conferido no validador | — |
| 1 | Estrategista | 3 | Bom no custo e na medida, mas afirmou "Tô de boa é frase de música" sem fonte | Sim: linha em `contexto/estrategista.md`, "Lições" |
| 2 | Editor | 5 | Duas falhas reais (áudio suposto, falta a versão B) | — |
| 2 | Revisor | 4 | SIM correto, apontou o que fica em aberto; nada novo a acrescentar | — |
| 2 | Arquiteto | 5 | Lote fixo ia envelhecer com o redesenho | — |
| 2 | Estrategista | 5 | Achou o erro do teste: media os 3 s, iguais nas duas versões | — |
| 3 | Editor, Estrategista | 4 | SIM com uma melhoria de ordem cada | — |
| — | Maestro | 1 | Prompt errado na ficha; aceitei como fato que o escaneamento abria o vídeo (resumo errado, não a fala do dono); marquei "confirmado" um ano tirado de repost; deixei suposição virar decisão no passo 5 | Sim: regras 8, 11 e 12 de `contexto/CONVIVENCIA.md` e o `pedido.py` que mostra o prompt |
| Fable | Supervisor | 5 | Achou o prompt errado, o fato errado com a linha de onde vinha, e cada suposição; correção em cada item | — |
| — | Revisão das notas | — | O Editor (rodada 1) citou uma linha real de `VIDEO.md`, mas a linha contradizia a fala do dono na mesma página. Não é repreensão: a página é que estava errada (corrigida). As notas da rodada 1 sobre a abertura estavam erradas porque eu as dei sem conferir a fala | — |
