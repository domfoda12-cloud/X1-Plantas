# Veto do Revisor de risco: os 2 bônus (24/11/2026)

> Texto do Revisor, como ele entregou. As trocas são aplicadas pelo Redator.

[Revisor] Checklist (`/home/user/X1-Plantas/pedidos/anexos/bonus-checklist-da-obra.md`): SIM SE as trocas abaixo forem feitas. Perguntas (`/home/user/X1-Plantas/pedidos/anexos/bonus-perguntas-ao-engenheiro.md`): SIM SE tiver aviso no topo e a P9 for confirmada. Nenhum VETO. (d) Nenhum dos dois promete aprovação, prazo ou custo; as P18 e P26 a P29 só perguntam.

(a) Item [H] pode ir ao público quando é uma destas coisas: pergunta ao profissional, foto, nota guardada, ou algo que o dono olha e mostra ao engenheiro. Sai, ou vira pergunta, o [H] que afirma consequência ou ensina técnica:
- L39: cortar "com risco de choque".
- L43: cortar "Não puxe do vizinho." (não tem fonte; a pergunta à companhia basta).
- L49: "Se pular: a casa pode sair fora do lugar do projeto, invadindo o recuo ou o lote do vizinho. Obra fora das regras pode ser multada, embargada ou ter que demolir a parte irregular." É a frase do erro 5 que já está no e-book (`paginas.py` L42-43).
- L59: "A fundação fica embaixo de tudo: consertar depois é difícil." (sai "o serviço mais difícil da casa").
- L73: "Pergunte ao engenheiro: o produto usado é o que ele especificou?" (sai "aplicado como diz a embalagem").
- L81: "Pergunte ao engenheiro onde vão a verga e a contraverga nas janelas e nas portas, e confira que estão lá antes do reboco, como o projeto pede."
- L103: "Guarde a nota da madeira, com a espécie e o tratamento; pergunte ao engenheiro se é a especificada." (sai "sem cupim").

(b) O checklist não ensina a construir: não traz medida, traço nem bitola. O risco é o "Confira" repetido soar como fiscalização. O aviso de (f) e as trocas de (c) resolvem isso.

(c) Multa, demolição, assistência gratuita e concretagem:
- **Multa e demolição (L27):** passa assim: "Obra sem alvará pode ser multada e embargada, e a parte irregular pode ter de ser demolida; quem decide é a prefeitura." A base é o F2 mais o erro 5. "Perder o investimento" só entre aspas, citando o F2.
- **Assistência gratuita (L35):** li hoje no Planalto a Lei 11.888/2008. Art. 2º: "renda mensal de até 3 (três) salários mínimos", "direito à assistência técnica pública e gratuita para o projeto e a construção de habitação de interesse social". Art. 3º: o serviço depende de apoio da União a estados e municípios. Troca: "Se a renda da família é de até 3 salários mínimos, a Lei 11.888/2008 dá direito a assistência técnica pública e gratuita para projeto e construção de casa de interesse social. Pergunte na prefeitura se a sua cidade oferece: depende de programa local."
- **Travar a concretagem:**
  - L62: "Pergunte ao engenheiro: o seu contrato inclui ele ver as valas e a armação antes de concretar? Se incluir, combine como o pedreiro avisa ele antes."
  - L92: "Pergunte ao engenheiro: ele quer ser avisado antes de cada concretagem (pilar, viga, laje)? Quando tirar as escoras, quem decide é ele."
  - Saem "não deixe concretar sem a liberação dele" e "para ele liberar". A NBR 14931 não aparece no texto público, porque não foi lida.
  - L17: "Os momentos de falar com o engenheiro antes de seguir:".
- **L112:** "Pergunte ao engenheiro: o projeto elétrico segue a norma de instalações elétricas (NBR 5410)? Tem fio terra e DR nos circuitos do banheiro, da cozinha e da área de serviço?" É norma técnica: nunca escrever "lei".

(e) Troca em `/home/user/X1-Plantas/ebook/gerador/paginas.py` L49-50: "Se a família pode crescer, diga isso ao engenheiro antes do projeto: ele vê se o lote tem espaço e deixa livre o lado da ampliação, sem caixa d'água, fossa ou banheiro no caminho. As 3 casas deste e-book não trazem ampliação desenhada: aumentar a casa é projeto novo, do engenheiro ou do arquiteto." Bate com `como-mobiliar-as-3-casas.md` L46, L74 e L103 e com a P25.

(f) Os dois bônus precisam de aviso no topo, porque podem sair em PDF separado no Drive (isso é suposição do Redator; o dono não decidiu).
- **Checklist, no lugar da L13:** "Este checklist é para você, dono da obra, saber o que olhar, perguntar, fotografar e guardar em cada fase. Ele não ensina a construir, não substitui o engenheiro ou o arquiteto e não faz de você o fiscal da obra: a parte técnica é do responsável técnico, que assina a ART ou o RRT e decide medidas, materiais e o jeito de fazer. Alvará, recuos, habite-se e multas mudam de cidade para cidade: pergunte na sua prefeitura. A planta do e-book é de referência."
- **Perguntas, logo abaixo da L14:** "Esta folha só traz perguntas. Quem responde é o engenheiro ou o arquiteto habilitado, para o seu lote e a sua cidade. A casa do e-book é planta de referência: o projeto legal é dele, com ART ou RRT." O aviso do fim (L137) continua.

Resto das Perguntas:
- As 8 frases marcadas passam como estão.
- P9 (L56): no dado, só a C01 registra "divisa da esquerda" (`C01.json` L349). E03 e F01 só aparecem assim no `como-mobiliar` (L52 e L80); os JSON delas não registram divisa. O Arquiteto confirma; se não confirmar, a frase vira "a parede da divisa".
- A seção "Para a equipe" não vai ao público.

Nota fora do pedido (não é condição): `ebook/fichas/textos.py` L51, E03, diz "o mínimo da lei federal de loteamento". Isso contraria o item 1 de `leis-conferidas` ("nunca 'o mínimo que a lei permite'"). É do Redator.

Para o caderno (Maestro registra em `pesquisas/normas.md`): Lei 11.888/2008, arts. 2º e 3º, Planalto, lida em 24/11, confirmado.

Não conferi:
- O texto do F2: o PDF passa de 10 MB e a busca não abriu. Ficam sem conferir multas, contraverga, "desafiador" e "perder o investimento".
- As normas da ABNT.
- A divisa de E03 e F01 no JSON.
- A página pronta e se algo cobre o aviso: é do Designer.

Arquivos: não editei nada. As trocas são do Arquiteto (checklist) e do Redator (`paginas.py` e Perguntas). O tamanho (A4) e onde os bônus vão (Drive ou dentro do PDF) são do dono.

Reconferência da ficha (`pedidos/2026-11/2026-11-23-1946-...`):
- Veredito de cada bônus e os pontos (a) a (f): cumpro.
- Em aberto: a leitura do arquiteto registrado antes de publicar (checklist L184) e o Fable na peça final.
