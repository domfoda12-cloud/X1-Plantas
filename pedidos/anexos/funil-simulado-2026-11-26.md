# Funil simulado: do anúncio ao Pix, e onde a venda se perde (26/11/2026)

> Rui Lance (Estrategista), fila da noite de 26/11, item 6 (`noite-2026-11-26-fila.md`), para o sócio que pega o funil (ficha `2026-11-26-0058`). **Só análise: nenhum arquivo de venda foi editado. Nada aqui vai ao público.** Os consertos de texto vão ao Redator (Caio) e passam pela Revisora (Vera) antes de entrar no `RESPOSTAS-RAPIDAS.md`; os que tocam preço, o que vai de graça, bônus, dados do vendedor ou o PDF final são do dono.
>
> **Material simulado, palavra por palavra:** `ebook/vendas/RESPOSTAS-RAPIDAS.md` (atalhos), `ebook/vendas/WHATSAPP.md` (sequência Dia 0 a 7), `pedidos/anexos/kit-anuncio-whatsapp.md` (rascunho dos anúncios A e B), `ebook/vendas/calculadora-lote.html` (lista de casas e mensagem pronta), `ebook/saida/planta-gratis-C01.pdf` e `ebook/saida/ebook.pdf` (lidos com `pdftotext`).
>
> **Números:** só os do validador (`ebook/plantas/PLANTAS.md` e a lista da calculadora): Casa Compacta (C01) 51 m², 2 quartos, mínimo 8,0 x 13,0 m; Casa Fita (E03) 56 m², 2 quartos, mínimo 5,0 x 20,6 m; Casa Família Compacta (F01) 71 m², 3 quartos, mínimo 10,0 x 12,8 m. **Nenhuma taxa de conversão, custo por contato ou custo por venda foi medida:** toda frase sobre "quanto custa" um vazamento é raciocínio sobre a conta do `PAINEL.md`, seção 4, e está marcada como hipótese.

## 0. Antes das conversas: o que está desatualizado de verdade

A ficha da tarefa diz que "hoje o e-book tem 24 plantas". **Conferido: não é isso.** O catálogo desenhado tem 24 plantas (`PLANTAS.md`), mas o e-book que se vende tem **3 casas**: `ebook/config.json` (`casas_lancamento`: C01, E03, F01), `PAINEL.md` seção 8 (decisão do dono de 23/11) e o próprio `ebook/saida/ebook.pdf` (17 páginas, as 3 casas). A planta grátis de hoje já diz "Essa foi 1 de 3". **Então o "3 casas" das mensagens está certo e não deve virar "24"** (seria vender o que o PDF não tem). O que está desatualizado:

| Onde | O que diz | O que é hoje |
|---|---|---|
| `ebook/saida/planta-gratis-C01.pdf` (vai no `/planta`) | C01: "Sol: melhor com a rua ao norte; evite a rua ao sul" | Validador corrigido em 26/11: **rua ao sul** (`PLANTAS.md`). O PDF é de 25/11, antes do conserto |
| `ebook/saida/ebook.pdf` (vai no link do Drive) | C01 e E03 "rua ao norte" | **Rua ao sul** para as duas; F01 continua ao sul. Só muda com o "gera" do dono |
| `RESPOSTAS-RAPIDAS.md`, nota do `/planta` | "Não mande o PDF de hoje: ele ainda fala em 24 casas" | O PDF já fala em 3. O motivo para não mandar agora é outro (o sol). O sócio lê um motivo errado e não sabe o certo |
| `RESPOSTAS-RAPIDAS.md`, nota do `/confia` | "Só use 'igual às páginas do e-book' quando o PDF grátis novo, com as 3 casas, estiver pronto" | Já está com as 3; mas, de novo, com o sol trocado |
| `RESPOSTAS-RAPIDAS.md`, topo | "só envie o /oferta quando as 3 casas tiverem 3D refeito" | Não achei registro dizendo se o 3D foi dado por refeito (as 3 imagens de `ebook/visual/3d/` são de 25/11). **Não conferido**: o sócio não tem como saber |
| `WHATSAPP.md`, "Se a pessoa ainda não tem terreno" | "indique uma categoria do catálogo: até 2 pessoas, compactas; família, categoria F" | Fala do catálogo de 24. No e-book há uma casa de família só, a F01 |
| `WHATSAPP.md`, Dia 3 e "É caro" | "R$ [preço do concorrente, com fonte e data...]" | Colchete que nunca foi preenchido; o `/caro` do `RESPOSTAS-RAPIDAS.md` já não usa. Duas versões da mesma resposta |
| `atributos-que-vendem.md` | "24 casas pelo preço de uma planta", "as 24 trazem 3 perguntas", "Essas [11] casas cabem num 8 x 25" | No e-book à venda são 3; num 8 x 25 cabem 2 (C01 e E03). Arquivo do Redator, não vai ao sócio, mas alimenta anúncio |
| `/recebi` (e "Quando o Pix cair") | "Aqui está o seu e-book ..., com o arquivo dos bônus ... o bonus.pdf" | Em `ebook/saida/` não existe `bonus.pdf`; ele está com selo de rascunho (D23). A mensagem promete o que a pasta pode não ter |
| Mensagens de texto e o sol | Nenhum atalho fala do lado do sol | Certo. A única ficha em texto (WHATSAPP.md, seção 2 da planta grátis) já diz "melhor com a rua ao sul" |

**Os dados que o sócio precisaria ter e não estão escritos em lugar nenhum para ele:** o título atual ("Antes do primeiro tijolo", está no `config.json` e no PAINEL, mas o `RESPOSTAS-RAPIDAS.md` só diz "o atual até o dono escolher"), o preço desta semana (o teste R$ 47 x R$ 67 não tem data de início: pergunta 1 do `teste-de-preco-como-medir.md`, em aberto), chave Pix, nome de quem recebe, nome e CPF de quem vende, link do Drive, horário de atendimento e quem segura o celular do número +55 75 99122-5333.

**Suposições desta simulação** (o dono não disse): (1) os anúncios A e B do kit estão no ar (hoje nenhum roda); (2) é semana de R$ 47; (3) o sócio é quem atende e assina "[seu nome]"; (4) os colchetes do dono ainda estão vazios, porque não achei nenhum deles preenchido no repositório (e o CPF, por regra, nunca vai estar aqui). Onde o colchete do dono aparece, ele fica escrito como está, porque é exatamente o que o sócio teria na mão.

## 1. As 5 conversas

Legenda: **C** = comprador; **S** = sócio (o texto entre aspas é a mensagem colada, palavra por palavra, com o atalho usado); **AUTO** = sai sozinha; **>>** = o que o sócio precisa decidir; **PONTO** = onde a venda se perde ou trava.

### (a) Jefferson, lote 10 x 25, decidido, quer comprar rápido (anúncio B, Família Compacta)

1. C toca no anúncio B1; o WhatsApp abre com a mensagem já preenchida e ele só aperta enviar: `Oi! Vi a Família Compacta, de 3 quartos, para lote de 10 m.`
2. AUTO, saudação: "Oi! Que bom que você chamou. Aqui é [seu nome], do e-book [título do e-book]. / Me fala a medida do seu lote: frente x fundo (exemplo: 5 x 25 ou 10 x 15). Com ela eu te digo quais das 3 casas cabem no seu lote (se alguma cabe), com os recuos de referência."
   >> O sócio precisou colar a saudação com o título escrito; o arquivo não diz qual é o título atual.
3. C (22h14): `10x25. quanto é o ebook? quero ja comprar hj`
4. >> Duas medidas e uma pergunta de preço. O kit (rascunho, seção 2b) manda uma pessoa responder preço; o `RESPOSTAS-RAPIDAS.md` não tem regra para "perguntou preço logo de cara". A sequência do `WHATSAPP.md` põe a oferta no **Dia 3**, depois do 3D no Dia 1. O sócio abre a calculadora (se tiver ela no celular: ver vazamento 9): **3 casas cabem**.
5. S, `/cabe` (o modelo tem 2 linhas de casa; ele acrescenta uma terceira à mão): "Boa notícia, Jefferson! Com 10 x 25 m, cabe no seu lote, com os recuos de referência: / - Casa Família Compacta: 71 m², 3 quartos / - Casa Fita: 56 m², 2 quartos / - Casa Compacta: 51 m², 2 quartos / Os recuos da sua cidade, você confirma na prefeitura. / Quer ver como ela fica por dentro, em 3D, com os móveis desenhados para dar escala?"
   >> O texto diz "cabe" e "ela" com três casas na lista; e termina oferecendo 3D a quem perguntou preço. Se ele usasse a mensagem pronta da calculadora, o fecho seria outro ("Quer saber mais de alguma delas?"): duas ferramentas para o mesmo passo, com dois pedidos diferentes.
6. C: `sim mas e o valor??`
7. S, `/oferta`: "Jefferson, a Casa Família Compacta que cabe no seu lote está no e-book Antes do primeiro tijolo. São 3 casas térreas: Casa Compacta, Casa Fita (2 quartos, lote de 5 x 25 m) e Casa Família Compacta (3 quartos). / Cada uma vem com os móveis desenhados para dar escala, com as medidas, desenhada no lote, em 3D e com as perguntas para o engenheiro. Conferida medida por medida (não substitui o profissional). / R$ 47, no Pix, aqui mesmo. Você recebe por link e tem 7 dias para pedir o Pix de volta. / Te mando a chave Pix?"
8. C: `manda`
9. S, `/pix`: "Combinado, Jefferson! / Chave Pix: [chave Pix] / Nome: [nome de quem recebe] / Vendedor: [nome de quem vende], CPF [CPF] / Valor: R$ 47 / Confere o nome antes de confirmar. Pagou? Me manda o comprovante aqui que eu te envio o link do e-book."
   **PONTO 1 (trava a venda inteira): colchete sem dono preenchido.** Chave Pix, nome de quem recebe, nome de quem vende e CPF não estão em lugar nenhum que o sócio alcance; o CPF é do dono e fica só no celular dele (`CONTEXTO.md`). Às 22h o sócio não tem como mandar o `/pix`. O Jefferson, que estava pronto, espera até o dono acordar. Hipótese: comprador decidido que espera horas esfria; esse é o elo mais caro do funil, porque o custo do anúncio já foi gasto inteiro.
10. Supondo que passou: C (22h31) manda a foto do comprovante.
11. >> Regra do `/recebi`: "só mande depois de ver o Pix no aplicativo do banco; comprovante sozinho não basta". O banco é do dono (é o CPF dele). **PONTO 2: passo que o sócio não pode fazer.** Ele não vê o banco; ou acorda o dono, ou manda sem conferir (risco de comprovante falso), ou deixa o comprador pago esperando até de manhã (risco de "é golpe?" e de pedido de devolução).
12. S, `/recebi`: "Recebi, Jefferson. Obrigado pela confiança! / Aqui está o seu e-book Antes do primeiro tijolo, com o arquivo dos bônus: / [link do Drive] / No link estão o e-book e o bonus.pdf, com o checklist da obra por fase e as perguntas para levar ao engenheiro. / ..."
    **PONTO 3:** [link do Drive] também é do dono; e a mensagem promete o bonus.pdf, que não está em `ebook/saida/` e tem selo de rascunho. Se a pasta tiver só o e-book, a promessa feita na entrega não é cumprida (CDC, art. 30). E o e-book da pasta diz "rua ao norte" para a Casa Compacta e a Casa Fita: se o Jefferson tiver a rua ao norte e ler isso, ele escolhe com o dado errado.

**Onde perde:** no `/pix` (colchete do dono vazio) e na conferência do Pix (o sócio não tem o banco). Tudo antes disso funcionou, com dois atritos: a oferta foi adiada por uma mensagem de 3D para quem pediu preço, e o `/cabe` não fala três casas.

### (b) Daiane, lote 8 x 15, só cabe a Casa Compacta, que ela já ganha (Instagram, comentário PLANTA)

1. C comenta `PLANTA` num post às 21h50.
2. S, à mão (a ferramenta automática do Instagram não foi escolhida): "Te mandei no Direct, Daiane! A planta está lá." e, no Direct: "Oi, Daiane! A planta grátis é a Casa Compacta: 2 quartos, 51 m², cabe num lote de 8 x 15 m. / Toca no link e ela chega no seu WhatsApp, com a mensagem já escrita: / https://wa.me/5575991225333?text=... / Já separa a medida do seu lote (frente x fundo): lá eu te digo se ela cabe."
   >> Se o sócio só vê o comentário de manhã, a Daiane já esfriou (hipótese). Ninguém responde o Instagram à noite: ver vazamento 2.
3. C toca no link: `Oi! Quero a planta grátis da Casa Compacta.`
4. AUTO, saudação: "... Me fala a medida do seu lote: frente x fundo ... quais das 3 casas cabem ..."
5. S, `/planta` com o PDF anexado: "Aqui está, Daiane: a Casa Compacta, 51 m², 2 quartos, com varanda na entrada. / Ela cabe num lote de 8 x 15 m (no mínimo 8 x 13 m), com recuos de referência. / Qual é a medida do seu lote? Frente x fundo. Me fala que eu confiro se ela encaixa no seu."
   >> A nota do `/planta` manda **não** anexar o PDF de hoje ("fala em 24 casas"). O sócio fica entre mandar sem PDF (e quebrar o que o post prometeu) ou mandar o PDF que diz "melhor com a rua ao norte; evite a rua ao sul" para a Casa Compacta, o contrário do validador corrigido. É a terceira vez que pedem a medida a ela (Direct, saudação, `/planta`).
6. C: `oi recebi brigada. o meu é 8 por 15 certinho`
7. >> Calculadora: só a Casa Compacta.
8. S, `/cabe`: "Boa notícia, Daiane! Com 8 x 15 m, cabe no seu lote, com os recuos de referência: / - Casa Compacta: 51 m², 2 quartos / Os recuos da sua cidade, você confirma na prefeitura. / Quer ver como ela fica por dentro, em 3D, ...?"
9. C: `quero`
10. S, `/3d` com a imagem da C01: "Olha a Casa Compacta por dentro, Daiane, ... / No e-book ela vem com as medidas, desenhada no lote, com a vista da rua e as perguntas para levar ao engenheiro. / Quer saber tudo o que vem no e-book?"
11. C: `quero sim, quanto é? e a de 3 quarto cabe no meu? vi no pdf`
    (A página 3 da planta grátis diz "E se o lote for um pouco maior? ... Num lote de 10 x 15 m cabe a Casa Família Compacta".)
12. **PONTO: veto que trava sem saída.** O topo do `RESPOSTAS-RAPIDAS.md`: "não envie o /oferta a quem só cabe a Casa Compacta ... Espera a decisão do dono sobre o que vai de graça." Não existe outra mensagem para esse caso. O próprio `/3d` acabou de perguntar "Quer saber tudo o que vem no e-book?", e ela disse sim. O `/naocabe` não serve (uma casa cabe). Para a pergunta da casa de 3 quartos também não há resposta pronta. O sócio tem três saídas, todas ruins: (1) fica calado (perda e má impressão); (2) improvisa (texto sem Revisora); (3) manda o `/oferta` mesmo assim, que diz "a Casa Compacta que cabe no seu lote está no e-book" a quem já a tem, e lista duas casas que não cabem nela (pedido de devolução provável e o que a skill `oferta-e-whatsapp` proíbe).

**Onde perde:** no passo 12. A conserto já está escrito e aprovado com condição (versão B de `oferta-so-casa-compacta-2026-11-24.md`, SIM SE da Revisora em 24/11), mas depende de o PDF pago ter o que vem a mais (cômodo a cômodo da Casa Compacta, só no modo `--duas-partes`, e o ok do dono no cartão `j1-comodo-no-pago`). Hipótese de custo: o lote de 8 m de frente com 13 a 20,5 m de fundo é o retrato do comprador do projeto (persona: lotes de 5, 6, 8, 10 ou 12 m de frente); cada lead desse grupo gasta o anúncio inteiro e não pode comprar.

### (c) Seu Edson, desconfiado, "é golpe?" (anúncio A, Casa Fita, lote 5 x 25)

1. C toca no anúncio A1: `Oi! Vi a Casa Fita, para lote de 5 m de frente.`
2. AUTO, saudação (a mesma).
3. C: `boa tarde. meu lote é 5x25 sim. mas isso é golpe? ja cai em golpe de pix uma vez`
4. S, `/confia`: "Pergunta justa, Edson. Por isso a planta grátis vem antes: ela é igual às páginas do e-book, você já viu o que vai receber. / No Pix aparece o nome de quem recebe: [nome de quem recebe]. E você tem 7 dias, contados do link, para pedir o seu Pix de volta, sem precisar explicar. / Quer que eu te mostre as casas que cabem no seu lote?"
   **PONTO 1: resposta pronta com premissa falsa para quem veio do anúncio.** O Edson não recebeu planta grátis nenhuma: o anúncio A não promete nada de graça (kit, seção 1b) e a saudação não cita grátis. "Você já viu o que vai receber" é mentira para ele, e ele percebe. Além disso, [nome de quem recebe] está vazio.
5. C: `nao vi planta nenhuma nao. vcs tem cnpj? tem loja? qual o insta de vcs`
6. **PONTO 2: falta de resposta pronta.** Não há atalho para "tem CNPJ?", "quem são vocês?" nem "qual o Instagram?". A venda é com CPF de pessoa física (decisão do dono); o perfil comercial do WhatsApp ainda não tem nome, CPF, endereço e e-mail (Decreto 7.962/2013; kit, condição 3: "ainda faltam"); o Instagram é novo e não há depoimento (e não se inventa). O sócio não sabe o que pode dizer.
7. C: `da pra pagar no cartao ou depois q receber?`
8. Também sem atalho. A resposta existe só no FAQ do `WHATSAPP.md` ("Pix, direto aqui pelo WhatsApp"), que não é resposta rápida. "Pagar depois de receber" não tem resposta em lugar nenhum.
9. >> O sócio pode mandar a planta grátis da Casa Compacta como prova (a regra deixa: "Mande planta-gratis-C01.pdf para todo mundo"), mas nenhum atalho diz isso para o caso do anúncio, e o PDF tem o sol trocado. Se ele seguir o `/confia`, a próxima pergunta é "Quer que eu te mostre as casas que cabem", e o Edson já disse que o lote dele é 5 x 25.
10. C some.

**Onde perde:** no passo 4 (a frase pronta é falsa para a origem dele) e no 6 (nenhuma resposta sobre quem vende). Na equação de valor, é a peça (b), a chance que ele vê de dar certo, que o kit já apontava como a mais fraca para os anúncios A e B.

### (d) Kelly, sem terreno ainda (Instagram, comentário PLANTA)

1 a 5. Igual à (b): comentário, Direct, link, saudação, `/planta`.
6. C: `obg! ainda nao tenho terreno nao, to juntando pra comprar ano q vem`
7. S, `/semlote`: "Então é o melhor momento, Kelly: sabendo a casa que você quer, você procura um lote onde ela caiba. A Casa Compacta pede no mínimo 8 x 13 m, com recuos de referência. / Quantas pessoas vão morar na casa? Te digo qual das 3 combina mais."
   >> Só cita a medida da casa que ela já tem; as outras duas, que são o que se vende, ficam de fora.
8. C: `eu meu marido e os 2 menino`
9. **PONTO: falta de resposta pronta e dado desatualizado.** Não há atalho para a resposta da pergunta que o próprio `/semlote` fez. O `WHATSAPP.md` manda "indique uma categoria do catálogo: família, categoria F" (catálogo de 24; no e-book é a F01 só). O sócio improvisa algo como "a Família Compacta, 3 quartos, lote mínimo de 10 x 12,8 m". Depois, o `/oferta` começa com "a [casa que cabe] que cabe no seu lote", e a Kelly não tem lote: não há oferta pronta para ela.
10. C: `e qto fica pra construir uma dessa mais ou menos?`
11. S, `/custo`: "Essa todo mundo pergunta, Kelly. Valor exato e prazo de obra eu não consigo te dar: ... / Quer ver quais casas cabem no seu lote?"
    >> O fecho pede o lote que ela acabou de dizer que não tem.
12. C: `ta bom vou pensar`
13. S, `/pensar`: "Claro, Kelly, casa se decide com calma. A planta grátis fica com você. / ..." Fim.

**Onde perde:** no passo 9, e de novo no 11 (resposta pronta que termina num pedido que não serve a ela). Hipótese: quem não tem lote compra menos que quem tem (a persona do projeto "já tem o lote"); este é o vazamento mais barato dos cinco, mas acontece em toda conversa desse perfil, e o sócio perde tempo improvisando.

### (e) Robson, medida errada ("é uns 200 metros"), some no dia 2 (anúncio B)

1. C: `Oi! Vi a Família Compacta, de 3 quartos, para lote de 10 m.`
2. AUTO, saudação.
3. C (23h05): `boa noite. o meu é uns 200 metros`
4. >> A calculadora só aceita frente e fundo; não há atalho para "mandou a área". 200 m² pode ser 10 x 20 (cabem a Família Compacta e a Casa Compacta), 8 x 25 (cabem a Casa Compacta e a Casa Fita) ou 6,6 x 30 (só a Casa Fita). **Risco:** o sócio "chuta" 10 x 20 e manda um `/cabe` errado.
5. S, `/medida`: "Robson, para eu te dizer qual casa cabe, só preciso de duas medidas do seu lote: / 1. a frente (a largura que dá para a rua) / 2. o fundo (da rua até o muro de trás) / Pode mandar assim: 8 x 15. Se não souber de cabeça, a escritura ou o contrato do lote costumam ter. Qual é a sua?"
   >> O `/medida` não diz por que a área não basta; e a pergunta mais fácil para ele ("quantos metros de frente?") está misturada com a segunda.
6. C: `vou ver na escritura amanha q ta com minha sogra`
7. Dia 2: o Robson não volta.
   **PONTO: falta de resposta pronta e passo que o sócio não sabe fazer.** A sequência do `WHATSAPP.md` (Dia 1: 3D; Dia 3: oferta; Dia 5: dúvida; Dia 7: última) só serve para quem mandou a medida; não há mensagem "lembrete da medida" para quem sumiu antes. Não há etiqueta "esperando medida" na lista do kit (seção 7), então o sócio não sabe que o Robson está esperando nem quando cutucar. A regra "no máximo uma mensagem por dia" permite uma mensagem, mas nenhuma está escrita.
8. Dia 7: se o sócio seguir a sequência, o Dia 7 diz "Qualquer dúvida sobre o seu terreno, me chama." e encerra. O Robson, que tinha intenção (veio do anúncio, tem lote, ia olhar a escritura), sai sem nunca ter recebido a resposta que veio buscar.

**Onde perde:** no dia 2, por falta de um lembrete pronto e de um jeito de saber quem está esperando. É o mesmo passo que o `WHATSAPP.md` chama de "a mensagem mais importante da sequência" (a medida): hipótese, quem não manda a medida não compra, então cada lead perdido aqui custa o anúncio inteiro.

## 2. Vazamentos, do mais caro ao mais barato

A ordem segue a conta do `PAINEL.md`, seção 4 (custo por venda = custo por contato ÷ conversão). Sem número medido, ordenei por duas perguntas: **quantas conversas o vazamento atinge** (todas, um grupo de lote, um perfil) e **em que passo** (quanto mais perto do Pix, mais anúncio já foi gasto). É raciocínio, não dado.

| # | Onde | O que acontece | Conserto em uma frase | Depende de |
|---|---|---|---|---|
| 1 | `/pix` e `/recebi` (conversa a) | Chave Pix, nome de quem recebe, nome e CPF de quem vende e link do Drive estão vazios, e quem confere o Pix no banco é o dono: o sócio não fecha venda nenhuma sozinho, e o comprador pronto espera | Preencher os 5 dados no celular do negócio (CPF nunca no repositório) e combinar quem vê o Pix entrar e como avisa o sócio | **Dono** (dados, conta, link do Drive) |
| 2 | Entrada de toda conversa (a, b, e) | Ninguém definido para responder, nem horário ([horário] vazio, pergunta `p2` em aberto); o Instagram é respondido à mão; a persona usa o celular à noite: a primeira resposta pode demorar horas | Dono diz quem segura o celular do número +55 75 99122-5333 e em que horário; a ausência sai com o horário escrito | **Dono** (quem atende, horário, ferramenta do Instagram) |
| 3 | Lote só-Casa-Compacta, 8 a 9,9 m de frente e 13 a 20,5 m de fundo (conversa b) | O veto proíbe o `/oferta` e não deixa outra mensagem: a conversa morre logo depois de o `/3d` perguntar "Quer saber tudo o que vem no e-book?" | Aplicar a versão B de `oferta-so-casa-compacta-2026-11-24.md` (já com SIM SE da Revisora) quando o PDF pago tiver o cômodo a cômodo; até lá, uma mensagem honesta de saída ("a sua casa você já tem; o pago é para a obra") e a etiqueta "só C01" | **Dono** (o que vai de graça, ok do cômodo a cômodo no pago, "gera" do PDF em duas partes) |
| 4 | PDF da planta grátis e PDF pago (conversas a, b) | Os dois dizem "rua ao norte" para a Casa Compacta (e o pago, também para a Casa Fita), o contrário do validador corrigido em 26/11; a nota do `/planta` manda não anexar por um motivo velho ("24 casas"); o sócio manda dado errado ou não manda a planta que o post prometeu | Gerar de novo os dois PDFs com o "gera" do dono e trocar a nota do `/planta` pelo motivo certo | **Dono** ("gera" do PDF final) + texto da nota |
| 5 | Medida incompleta e quem some antes de mandar a medida (conversa e) | Não há atalho para "mandou a área" nem lembrete para o dia seguinte, nem etiqueta "esperando medida": a pergunta mais importante do funil fica sem segunda chance | Dois atalhos novos: `/area` (por que a área não basta e "me manda só a frente") e `/lembrete` (uma vez, no dia seguinte, pedindo só a frente), mais a etiqueta "esperando medida" | Só texto (Redator + Revisora) |
| 6 | Duas sequências que brigam (conversa a) | O `WHATSAPP.md` põe a oferta no Dia 3 e o kit põe 3D e "quando vai construir" antes do preço; os atalhos não dizem o que fazer quando a pessoa pergunta preço logo; o comprador decidido é adiado | Uma regra no topo do `RESPOSTAS-RAPIDAS.md`: "perguntou preço e a casa cabe: `/oferta` na hora"; a sequência Dia 0 a 7 vira só para quem não respondeu | Só texto |
| 7 | `/confia` e quem vende (conversa c) | Diz "você já viu o que vai receber" a quem veio do anúncio e não viu nada; não há resposta para "tem CNPJ?", "quem são vocês?", "cartão?", "pagar depois?"; o perfil comercial não tem os dados do vendedor | Versão do `/confia` que **manda** a planta grátis da Casa Compacta como amostra (a regra já deixa), atalhos `/quem` e `/formas`; dados do vendedor no perfil comercial | Texto + **dono** (dados no perfil; se aceita outra forma de pagar: opções na seção 3) |
| 8 | `/recebi` (conversa a) | Promete o bonus.pdf sem condição; ele não está em `ebook/saida/` e tem selo de rascunho: promessa na entrega que pode não ser cumprida, e pedido de devolução | `/recebi` em duas versões, com e sem bônus (as trocas da parte B de `oferta-so-casa-compacta-2026-11-24.md`), e o sócio abre a pasta antes de escolher | Texto + **dono** (se o bônus vai e quando) |
| 9 | Calculadora e `/cabe` (conversas a, b) | A calculadora é um arquivo HTML do repositório (compartilhar com o sócio: cartão C7, em aberto); o `/cabe` tem 2 linhas fixas e "cabe/ela" no singular, e termina num pedido diferente do da mensagem pronta da calculadora | Publicar a calculadora num link que abra no celular e escolher **uma** mensagem para o "cabe" (a da calculadora, que já sai com o número certo de casas) | **Dono** (compartilhar o link) + texto |
| 10 | Sem terreno (conversa d) | O `/semlote` só cita a Casa Compacta, a resposta "quantas pessoas" não tem atalho, o `WHATSAPP.md` fala de "categoria do catálogo" e `/oferta` e `/custo` terminam pedindo o lote que ela não tem | `/semlote` com as 3 medidas mínimas (5 x 20,6, 8 x 13 e 10 x 12,8 m) como "o lote que você procura" e uma `/oferta` sem a frase "que cabe no seu lote" | Só texto |

**Fora do top 10, mas anotado:** (11) a Daiane recebe três pedidos da medida seguidos (Direct, saudação, `/planta`); cortar o do `/planta` quando a saudação já pediu. (12) Não há atalho para "por que o meu amigo pagou R$ 67?": a skill `oferta-e-whatsapp` já tem a frase, falta virar atalho. (13) O `/oferta` tem 506 caracteres antes de preencher; um guia de terceiros fala em limite de 512 por resposta rápida (não confirmado na ajuda oficial: `pesquisas/`, tema ferramentas); o passo 6 do `RESPOSTAS-RAPIDAS.md` já manda testar. (14) Ninguém sabe se o 3D das 3 casas foi dado por refeito, condição do topo para usar o `/oferta`.

**Uma conta, só para mostrar o peso (hipótese, não dado):** pela fórmula do PAINEL, se metade das conversas morresse antes da medida (vazamento 5) e metade do resto caísse no veto (vazamento 3), a conversão final cairia para um quarto da que seria sem os dois, e o custo por venda subiria quatro vezes, com o mesmo gasto de anúncio. Os números reais saem da planilha do teste de preço na primeira semana: contar "conversas", "mandaram a medida", "só C01" e "pagou" separadamente já mostra qual dos dois pesa mais.

## 3. O que falta para o sócio operar sozinho

### 3a. Acesso e dados (tudo do dono; nada disso vai ao repositório)

- **O celular do número do negócio** (+55 75 99122-5333) com o WhatsApp Business, ou o aparelho com o número ligado como dispositivo extra. Hoje não está escrito quem segura (pergunta `p2`).
- **Os 5 dados do Pix e da entrega** já colados dentro dos atalhos: chave Pix, nome de quem recebe, nome e CPF de quem vende, link da pasta do Drive em "ver". Com isso, o `/pix` e o `/recebi` saem sem colchete.
- **Como ele sabe que o Pix caiu** sem ter o banco do dono: (a) o dono confere e manda "caiu" para o sócio; (b) a chave Pix passa a ser de uma conta que o sócio também vê; (c) o sócio manda o link na hora do comprovante e o dono confere depois. Recomendação: (a) para começar, porque não muda conta nem risco; custo: demora à noite. Decisão do dono.
- **O horário de atendimento**, para a mensagem de ausência e para a meta interna de responder rápido (meta nunca escrita ao cliente).
- **O título atual escrito para ele:** "Antes do primeiro tijolo" (o atual, até o dono escolher outro).
- **O preço desta semana e o dia em que a semana vira** (o teste começa por R$ 47; a data de início está em aberto no `teste-de-preco-como-medir.md`, pergunta 1).
- **A calculadora num link** que abra no celular dele (cartão C7).
- **A ferramenta que responde PLANTA no Instagram**, ou quem responde à mão e quando (está como suposição desde 23/11).

### 3b. Atalhos que não existem (texto do Redator, leitura da Revisora)

| Atalho proposto | Para quê |
|---|---|
| `/area` | A pessoa mandou só a área ("uns 200 metros") ou só uma medida |
| `/lembrete` | Uma vez, no dia seguinte, a quem não mandou a medida: pede só a frente |
| `/socompacta` | Saída honesta para o lote em que só cabe a Casa Compacta (até o dono decidir a oferta dela) |
| `/primeira-A`, `/primeira-B` | A "primeira resposta humana" do kit para os anúncios A e B (hoje só existe no rascunho) |
| `/quem` | "Quem são vocês? Tem CNPJ? É golpe?": quem vende, com os dados do perfil, sem inventar prova |
| `/formas` | "Aceita cartão? Posso pagar depois?": hoje é só Pix (decisão do dono) |
| `/doisprecos` | "Por que fulano pagou outro valor?", com a frase que a skill já tem |
| `/recebi-sembonus` | Entrega quando o bonus.pdf ainda não está na pasta |
| `/semlote2` | Resposta depois de "quantas pessoas vão morar" |
| `/casa3q` | "E a de 3 quartos cabe no meu?" para quem tem menos de 10 m de frente |

### 3c. Regras que ele não vai entender como estão escritas

- **Jargão interno nos arquivos que ele lê:** "veto do Revisor", "D23", "decisão 34", "p15", "SIM SE", "colchete", "recuos de referência", "Dia 0 a Dia 7", "etiqueta só C01". Precisa de um glossário de uma linha cada, ou de o texto do sócio não usar nada disso.
- **Três arquivos para uma conversa só** (`RESPOSTAS-RAPIDAS.md`, `WHATSAPP.md` e o kit, cerca de 66 KB juntos), com regras que se contradizem (oferta no Dia 3 ou logo; `/caro` com ou sem preço do concorrente). Ele precisa de **uma folha**: os 6 passos da conversa (saudação, medida, cabe, 3D, oferta, Pix e entrega) e, em cada passo, o atalho e o "se a pessoa disser X, mande Y".
- **A tabela "lote → o que mandar"** (kit, seção 2b) está no rascunho, não no arquivo que ele usa; é ela que impede o erro do veto.
- **Quando chamar o dono:** devolução fora dos 7 dias, reclamação, "quero falar com alguém", pergunta que nenhum atalho responde, pedido de nota ou CNPJ. Hoje só a devolução fora do prazo está escrita.
- **O que ele não pode fazer de jeito nenhum**, em linguagem dele: prometer aprovação na prefeitura, prazo ou custo de obra; dizer que dispensa pedreiro, engenheiro ou arquiteto; mandar mais coisa grátis; prometer casa nova; mandar mensagem a quem não pediu; anotar nome ou telefone fora da planilha do dono.
- **O que anotar e onde:** por pessoa, só o número (001, 002), a origem (A1, B1, PLANTA), o preço e se pagou, na planilha do dono; por semana, as 4 contagens que vão ao `PAINEL.md`, seção 7 (conversas, mandaram a medida, só C01, pagaram e não devolveram). Sem essas contagens, o custo por venda nunca sai do zero.

### 3d. Perguntas ao dono (curtas, com opções; a recomendação é minha)

1. **Quem confirma o Pix?** (a) você confere e avisa o sócio; (b) conta que os dois veem; (c) o sócio manda o link no comprovante e você confere depois. Recomendo (a) na primeira semana.
2. **Quem atende e quando?** (a) o sócio, num horário fixo que vai escrito na ausência; (b) os dois, em turnos; (c) você à noite, ele de dia. Recomendo (a), com o horário que inclua a noite, porque a persona usa o celular à noite (hipótese da persona, `MERCADO.md`).
3. **O lote em que só cabe a Casa Compacta:** (a) aplicar a versão B do `/oferta` quando o PDF em duas partes for gerado; (b) só a mensagem de saída, sem oferta, até mudar o que vai de graça; (c) não rodar o anúncio B até decidir. Recomendo (a), e (b) enquanto o PDF não sai.
4. **A quem desconfia:** (a) mandar a planta grátis da Casa Compacta como amostra, mesmo para quem veio do anúncio; (b) mandar também uma página da Casa Fita como imagem (é dar parte do pago: decisão sua); (c) só o `/confia` corrigido. Recomendo (a): não muda o que vai de graça.
5. **O "gera" dos PDFs com o sol corrigido** antes do sócio começar? (a) sim, antes do primeiro `/planta`; (b) o sócio não manda PDF até lá. Recomendo (a).

## Reconferência do pedido (ficha da tarefa, item 6 da fila)

- 1. Cinco conversas completas, só com as mensagens que existem, compradores (a) a (e): **cumpre** (seção 1; onde o sócio teria de acrescentar algo à mão, está marcado com >>).
- 2. O PONTO de cada conversa com o motivo: **cumpre** (marcado em cada uma).
- 3. Vazamentos em ordem, no máximo 10, com onde, o que acontece, conserto em uma frase e de quem depende: **cumpre** (seção 2; a ordem é raciocínio, sem número medido).
- 4. O que falta ao sócio: **cumpre** (seção 3).
- Não editar arquivo de venda: **cumpre** (só este arquivo foi criado).
- Não inventar número; nada de aprovação, prazo ou custo de obra; decisão do dono vira pergunta: **cumpre** (a única conta é hipótese marcada; as decisões estão na 3d).
- **Em aberto / não conferido:** se o 3D das 3 casas foi dado por refeito; se os colchetes do dono já estão preenchidos no celular (não há como ver daqui); se o anúncio B atrai mesmo lotes de 8 m (só a planilha diz).
