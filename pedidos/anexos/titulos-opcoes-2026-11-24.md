# Título do e-book: 3 opções no lugar de "Antes do primeiro tijolo" (24/11/2026)

> **Pedido do dono** (quadro de tarefas, cartão p14, 24/11): "B", ou seja, 3 opções de título novo. Motivo: "Antes do primeiro tijolo" abre a legenda de um vídeo de referência com 5,2 milhões de visualizações e pode parecer cópia. O título atual fica até ele escolher. **Quem escolhe é o dono.** Rascunho do Redator. **Ainda não passou pelo Revisor de risco**, e precisa passar antes de ir para a capa ou para um anúncio.
>
> Base: as 3 casas do lançamento (`ebook/config.json`, `casas_lancamento`) e os números do validador (`ebook/plantas/PLANTAS.md`): **C01** Casa Compacta, 51 m², cabe num lote de 8 x 15 m; **E03** Casa Fita, 56 m², 5 x 25 m; **F01** Família Compacta, 71 m², 10 x 15 m. A casa em 3D existe para as 3 (`ebook/visual/3d/C01.jpg`, `E03.jpg`, `F01.jpg`; vão ser refeitas sem espelhar). O PDF não fala de preço (dono, 24/11).

## Cabe na capa?

A capa usa Bricolage Grotesque 800 em 54 pt, numa caixa de 150 mm de largura (`ebook/gerador/livro.css`, `.capa-titulo`). Eu medi com a Bricolage Bold, somando 4% pelo peso 800, e o título atual sai como na capa: "Antes do / primeiro tijolo". As três opções novas cabem em 2 linhas. É uma estimativa: a conferência de verdade é a prévia da capa (`livro.py --previa`), que eu não rodei porque não posso mudar o `config.json`.

| Opção | Letras | Como quebra (estimativa) |
|---|---|---|
| A casa do seu lote | 18 | "A casa do seu / lote" (feia: o Designer força "A casa do / seu lote") |
| Errar na planta sai caro | 24 | "Errar na planta / sai caro" |
| Sua casa antes da obra | 22 | "Sua casa antes / da obra" (melhor forçar "Sua casa / antes da obra") |

**Atenção:** hoje a capa não mostra o `subtitulo` do `config.json`. Ela mostra uma frase fixa, "Casas organizadas pela frente do terreno…", e o dono decidiu em 23/11 que o subtítulo vai "só no anúncio". Por isso os subtítulos abaixo foram escritos para o anúncio e para o vídeo.

---

## Opção 1: o lote

```text
TEXTO: A casa do seu lote
SUBTÍTULO: 3 casas térreas desenhadas no lote: 5 x 25, 8 x 15 e 10 x 15 m. Mede a frente do seu e acha a sua.
ATRIBUTO CAMPEÃO: Achar pelo lote (5/5/3), somado à medida exata de cada casa, que vem do validador
POR QUE VENDE: é a pergunta que o Marcos já faz ("que casa cabe no meu lote?"), virada em resposta, com o número dele na frente.
O QUE MEDIR: resposta no WhatsApp com a medida do lote (é o sinal de comprador de verdade)
VARIAÇÃO PARA TESTE: "Mede o lote, escolhe a casa" (27 letras, cabe em 2 linhas): o mesmo ângulo, dito como uma ordem
```

- **Diferença das outras duas:** fala de **encaixe**: a medida dele e a casa que cabe nela. Não fala de medo nem de imagem.
- **Risco:** "do seu lote" pode soar como garantia de que cabe no lote dele, e essa frase é proibida (`atributos-que-vendem.md`, seção 3), porque depende do recuo da cidade. Para não soar assim, o subtítulo dá as 3 medidas exatas, e o anúncio leva "o recuo da sua cidade, o seu engenheiro confere". Outro risco: fica perto de "Que casa cabe no seu lote?", o título de trabalho que o dono achou "sem graça" (23/11). Pergunta para ele: aquele "sem graça" valia para o título de trabalho?
- **No WhatsApp:** "Oi, quero a casa do meu lote. Meu lote tem ___ de frente." É a mais natural das três. O comprador repete o título trocando só "seu" por "meu", e a medida que ele manda já serve para triar quem vai comprar.
- **Em voz alta no vídeo:** "Todo lote é uma conta. A casa certa é a resposta. **A casa do seu lote.**" O título fecha a frase-tese aprovada.

## Opção 2: o medo de errar

```text
TEXTO: Errar na planta sai caro
SUBTÍTULO: 3 casas térreas conferidas medida por medida, para você escolher antes de gastar. Não substitui o seu engenheiro.
ATRIBUTO CAMPEÃO: Casas conferidas (5/5/5), a única com nota 5 em exclusividade
POR QUE VENDE: nomeia a dor que ele já carrega (a parede que precisa ser quebrada, o quarto onde a cama não cabe) e oferece a conferência como alívio.
O QUE MEDIR: comentário (a frase puxa história de quem já errou) e clique
VARIAÇÃO PARA TESTE: mesmo título, com o subtítulo do lote: "3 casas conferidas, para lotes de 5, 8 e 10 m de frente. Não substitui o seu engenheiro."
```

- **Diferença das outras duas:** fala de **segurança**: o custo do erro e a conferência. Nem o lote nem a imagem aparecem no título.
- **Risco:** o título em si não promete nada, é uma constatação. Mas ele puxa, por perto, frases como "com ela você não erra" ou "sem erro", e essas o Revisor veta: nenhuma peça pode dizer que a planta evita o erro. "Conferido medida por medida" sempre vem seguido de "não substitui o profissional". O tom negativo também pode afastar quem ainda está sonhando. E "planta" também quer dizer planta de jardim: na busca, a frase só trouxe resultados de jardinagem e lavoura.
- **No WhatsApp:** "Oi, quero o Errar na planta sai caro" soa estranho. A mensagem já preenchida teria que ser outra, "Oi, quero ver as 3 casas conferidas". É a opção mais fraca neste ponto.
- **Em voz alta no vídeo:** é a mais forte como gancho de abertura ("Errar na planta sai caro. Errar na laje sai mais."). Pede uma imagem de prova logo depois.

## Opção 3: ver a casa antes

```text
TEXTO: Sua casa antes da obra
SUBTÍTULO: Veja mobiliada e em 3D a casa que cabe no seu lote, antes de gastar com a fundação. 3 casas térreas de referência.
ATRIBUTO CAMPEÃO: Ver antes de construir (5/5/3): as 3 casas do lançamento têm 3D e planta mobiliada
POR QUE VENDE: faz o Marcos e a família se verem dentro da casa: é o desejo, antes da conta.
O QUE MEDIR: clique e resposta no WhatsApp (pedido para ver a imagem)
VARIAÇÃO PARA TESTE: "Veja sua casa antes da obra" (27 letras, cabe em 2 linhas)
```

- **Diferença das outras duas:** fala de **desejo e de imagem**. Não fala de medida nem de medo.
- **Risco:** "sua casa" pode dar a entender que é um projeto feito para ele. Por isso o subtítulo diz "de referência". O 3D só pode ser citado enquanto as 3 casas tiverem a imagem pronta (frase vetada: "3D prometido onde não há"). E "antes da" lembra de leve o "Antes do" do título atual: a distância é boa, mas não é total.
- **No WhatsApp:** "Oi, quero ver minha casa antes da obra." É natural e pede o próximo passo, que é ver a imagem.
- **Em voz alta no vídeo:** funciona sobre a casa 3D se montando na tela, mas pede imagem para ter força. Dita sem imagem, é a mais fraca das três.

---

## Já existe com esse nome? (busca de 24/11/2026)

Primeiro procurei no caderno de pesquisas (`pesquisa.py buscar titulo`, depois cada frase): nada registrado. Depois busquei na web com a frase exata entre aspas, uma busca para cada título, mais uma busca na Hotmart.

| Título | O que achei | O que não conferi |
|---|---|---|
| A casa do seu lote | Nenhum e-book, curso ou vídeo com esse nome, nem com "casa do meu lote". Só artigos genéricos de planta por lote (Coohom) | Instagram, TikTok e YouTube por dentro (a busca geral quase não acha reels), Amazon Kindle, registro de marca no INPI |
| Errar na planta sai caro | Nenhum uso da frase. Os resultados foram de jardinagem e lavoura | Os mesmos |
| Sua casa antes da obra | Nenhuma página com esse nome. Na galeria do Planner 5D há uma planta chamada "Minha casa antes de ser construída", de usuário e sem venda | Os mesmos |

Perto, mas sem ser igual: na Hotmart há e-books de obra com "antes de" no nome ("Tudo o que você precisa saber antes de construir uma casa do zero", "Seu Imóvel Sem Arrependimentos"). Nenhum é de planta com esses títulos. O achado está registrado em `pesquisas/concorrentes.md`, como hipótese.

Fontes: [Hotmart, "Tudo o que você precisa saber antes de construir uma casa do zero"](https://hotmart.com/pt-br/marketplace/produtos/tudo-o-que-voce-precisa-saber-antes-de-construir-uma-casa-do-zero/W100626736G) · [Hotmart, "Seu Imóvel Sem Arrependimentos"](https://hotmart.com/pt-br/marketplace/produtos/seu-imovel-sem-arrependimentos/E105852820L) · [Planner 5D, galeria](https://planner5d.com/pt/gallery/floorplans/ZSbOSa/floorplans-cozinha-3d) · [Coohom, planta em lote 10x20](https://www.coohom.com/article/planta-de-casa-em-lote-10x20-como-planejar-um-projeto-funcional)

## Recomendação (quem escolhe é o dono)

**Recomendação do Redator: "A casa do seu lote".** Usa o atributo campeão com a medida exata, vira sozinha a frase do WhatsApp ("quero a casa do meu lote") e fecha a frase-tese do vídeo. Se o dono quiser mais impacto, teste "Mede o lote, escolhe a casa".

## Vontade, facilidade e pedido (conferência da marketing-psychology, feita por mim, sem rodar a skill inteira)

- **Opção 1:** tem vontade (é a casa dele), é fácil (é só medir) e o pedido é claro (mandar a medida).
- **Opção 2:** tem vontade (alívio do medo) e é fácil, mas no WhatsApp o pedido fica confuso.
- **Opção 3:** tem vontade (ver a casa) e o pedido é claro (pedir a imagem), mas a facilidade depende de a imagem estar pronta.

## Se o título mudar, revisar também

A frase "Antes do primeiro tijolo, mede a frente do seu lote…" aparece em `ebook/vendas/atributos-que-vendem.md` (linha 13 e combinação 2) e em `ebook/referencias/VISUAL.md` (linha 38). O motivo da troca, parecer cópia, vale para essas frases também. Eu não mexi nelas.

## Veto do Revisor de risco (24/11, rascunho): os três passam com troca

| Opção | Título | Subtítulo depois do Revisor |
|---|---|---|
| 1 | **A casa do seu lote** (fica, com "de referência" por perto na capa) | "3 casas térreas de referência, desenhadas para lotes de 5 x 25, 8 x 15 e 10 x 15 m. Mede a frente do seu e veja se uma delas serve. O recuo da sua cidade, o seu engenheiro confere." ("acha a sua" garantia que uma cabe) |
| 2 | **Errar na planta sai caro** (fica) | "3 casas térreas de referência, conferidas medida por medida. Não substitui o profissional. Escolha antes de gastar." |
| 3 | **Veja a casa antes da obra** (o original "Sua casa antes da obra" não passa: parece projeto sob medida) | "Veja mobiliadas e em 3D 3 casas térreas de referência, para lotes de 5 x 25, 8 x 15 e 10 x 15 m, antes de gastar com a fundação." |

Não conferido: a capa em prévia com cada título. Quem escolhe é o dono (cartão p14 do quadro).

## Opinião do Diretor (MinoAI Frontier), 24/11

> Busca feita pelo Redator com as duas ferramentas da MinoAI Frontier (`search_viral_hooks`, 4 buscas; `search_mino_method`, 3 buscas), em 24/11. Só está aqui o que a ferramenta devolveu: o criador, o link e a frase. As frases dos ganchos estão no original em inglês. Número de visualização não entra. **Atenção:** a biblioteca da MinoAI trata de gancho de vídeo curto (o começo do reels), não de título de livro. O que vale para a capa é uma leitura minha a partir do método, e está marcado assim. Nenhum gancho devolvido é brasileiro nem de planta de casa. O mais perto foram vídeos de obra e de casa nos EUA.

| Título | Para o dedo? | Dá o que comentar? | Ajuda a pagar? | Fonte devolvida |
|---|---|---|---|---|
| **A casa do seu lote** | **Médio.** É claro, e o método põe a clareza antes do mistério ("Be CLEAR before being fancy"). Só que sozinho não tem emoção nem número. O método manda pôr no gancho uma palavra do nicho e um número ("specific keywords names and numbers"): "lote" é a palavra, e o número (5 x 25, 8 x 15, 10 x 15 m) só aparece no subtítulo. | **Sim, se vier a pergunta.** Com "qual a frente do seu lote?", o espectador se reconhece ("oh yeah that's me", no ensino sobre identidade). A ferramenta não devolveu nada sobre comentário para este ângulo: o resto é leitura minha. | **Sim.** É a promessa da solução. No método, quem vende usa a estrutura de redação (problema, agitação, solução; atenção, interesse, desejo, ação) com o gancho na frente. | Aula "Mastering Viral Text Hooks", item 13 (sem link para nós) · [chamada de 02/06/2026](https://www.loom.com/share/e00232f7683e46c7b1fb69b8324f9a50?t=1941s) · [chamada de 06/08/2026](https://www.loom.com/share/13fa3f8a80f44c338134e6cce920caf4?t=2490s) · [chamada de 23/03/2025](https://www.loom.com/share/89df49c81f6b44a2b588259c4a975877) · gancho perto: [@flippedbyabby](https://www.instagram.com/p/DGnZHUbOpuV/), "none of them compared to the lot that this house is on" (o lote como o motivo da escolha) |
| **Errar na planta sai caro** | **Sim, é o mais forte.** O método pede palavra que dá emoção (medo, insegurança) e diz que os ganchos que mais funcionam são os negativos ou os de "você está perdendo". O gancho mais parecido com um título nosso, em todas as buscas, foi deste ângulo: [@itshannahzhang](https://www.instagram.com/p/DaBM835JTiM/), "The most expensive mistake that could cost you over $100,000…". | **Sim.** No método, o gancho negativo faz o espectador comentar antes mesmo de ver o vídeo inteiro. Que isso puxe a história de quem já errou na obra é leitura do Redator, não da ferramenta. | **Sim, se a solução vier logo.** Encaixa no "problema, agitação, solução" da chamada de 23/03/2025. O alerta vem do mesmo método: a prova mais forte é um número exato, e o gancho da @itshannahzhang tem um valor. Nós não temos um "quanto custa o erro" com conta e fonte, e por isso não dá para pôr número (regra do projeto). Além disso, "planta" quer dizer duas coisas, e o método pede clareza primeiro. | Aula "Mastering Viral Text Hooks", itens 5 e 13 (sem link) · [chamada "Straight Sauce", 06/02/2026](https://www.loom.com/share/3b78ecf544054750b3d06f0d64275ef8) · [chamada "Mastering Superhooks", 11/11/2025](https://www.loom.com/share/991211e6490344b283941f4204a7b8df) · [chamada de 23/03/2025](https://www.loom.com/share/89df49c81f6b44a2b588259c4a975877) · ganchos perto: [@itshannahzhang](https://www.instagram.com/p/DaBM835JTiM/); [@hormozi](https://www.instagram.com/p/DcWSweqBluh/), texto na tela "DON'T MAKE THIS #1 HIRING MISTAKE" |
| **Veja a casa antes da obra** | **Sim, com imagem. Sem imagem, não.** O método diz que contraste de antes e depois "contrast is what really makes things like hit with people", que o vídeo deve confirmar o gancho com imagem no primeiro ou segundo segundo e que texto que não bate com a imagem "kills trust". Os ganchos que vieram mostram a transformação, e não a dizem. | **Pouco.** A ferramenta não devolveu nada útil sobre comentário para este ângulo. | **Sim, se o 3D estiver pronto.** O gancho promete uma imagem, e o vídeo tem que mostrá-la na hora (as 3 casas vão ser refeitas sem espelhar). | [chamada de 21/07/2026](https://www.loom.com/share/47d91f75f07d444cb232cdf4b80e75a1?t=2288s) · [chamada "Mastering Superhooks", 11/11/2025](https://www.loom.com/share/991211e6490344b283941f4204a7b8df) · aula "Mastering Viral Text Hooks" (texto e imagem combinando; sem link) · ganchos perto: [@meshtimes](https://www.instagram.com/p/DHRtCjmSDrM/), "the place i rented vs. the home i'm making" (só texto, a sala vazia vira casa mobiliada); [@mrfourtoeight](https://www.instagram.com/p/DTOCYBjEmw7/), "Six months ago, I bought this place…" |

**Qual o método favorece como gancho falado de vídeo: "Errar na planta sai caro".** É o único dos três com a emoção que o método pede (medo, perda) e com um gancho comprovado do mesmo formato (o "most expensive mistake" da @itshannahzhang). Tem duas condições, tiradas do próprio método. Primeira: logo no segundo 1 ou 2, a imagem prova o que a frase diz (a planta, a casa em 3D). Segunda: o texto na tela não repete a fala ("Do not repeat the exact same information in both the spoken hook and the text hook"). Daí sai uma leitura do Redator, que ninguém testou: "Veja a casa antes da obra" rende mais como **imagem** e texto na tela do que como fala, e "A casa do seu lote" fecha a frase-tese no fim do vídeo. **Gancho de vídeo não é o mesmo que título do e-book, e quem escolhe o título é o dono** (cartão p14, decisão 34). Qualquer frase de vídeo tirada daqui passa de novo pelo Revisor de risco: nada de "sem erro" nem de "você não erra".

Não conferido: se algum desses ganchos funciona no Brasil ou com o público classe C (a biblioteca não devolveu nenhum criador brasileiro), e os vídeos de origem, que eu não assisti (li só a frase e a descrição devolvidas pela ferramenta).
