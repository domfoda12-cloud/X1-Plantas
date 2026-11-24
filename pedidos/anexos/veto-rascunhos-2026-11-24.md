# Veto do Revisor de risco: porta, Casa Fita, kit do anúncio, guia, pôster C e "como mobiliar" (24/11/2026)

> Texto do Revisor, como ele entregou.

[Revisor] Veredito por item. Usei a ficha 1946-refazer, porque nenhuma ficha veio com o pedido. Não editei nada.
1. SIM. Os dados confirmam a frase. A C01, que é a planta da página, tem uma segunda porta para fora, ext→serviço nos fundos (C01.json, L294). A soleira cinza aparece no desenho. Antes de gravar, rode o `--conferir` para ver se a abertura passou a estourar a página.
2. SIM. Saiu a menção à lei, que era o risco (leis-conferidas, item 1). O "como o de 5 x 25 m" amarra o fundo.
3. Kit, por anúncio:
 - A1: SIM SE trocar a 1ª linha (L122) "Lote de 5 m de frente? Cabe uma casa de 2 quartos." por "Lote de 5 x 25 m? Cabe uma casa de 2 quartos, com os recuos de referência." Motivo: um lote de 5 x 15 lê "cabe" no trecho que o anúncio mostra antes do corte, e a E03 pede 20,6 m de fundo.
 - A2, B1 e B2: SIM. Os números batem com o PLANTAS.md (56 e 71 m², "3 quartos nos fundos, longe da rua", mesa de 4). O humor não ensina gambiarra.
 - C1 e C2: SIM no texto, mas não rodam até o dono decidir o que vai de graça (colchete aberto).
 - Saudação: SIM SE trocar "eu te digo qual casa cabe" por "eu te digo quais das 3 casas cabem no seu lote (se alguma cabe), com os recuos de referência", E quem chegar do Instagram com "Quero a planta grátis" continuar recebendo o /planta. O post prometeu, e isso vira contrato (CDC, art. 30).
 - Nota: o achado da seção 9 sobre a L5 do RESPOSTAS-RAPIDAS está velho. A linha já diz "frente de 8 a 9,9 m e fundo de 13 a 20,5 m".
4. Guia: SIM SE tirar "Checklist da obra por fase" do bloco "No e-book, além desta casa" (p. 4) até ele existir no PDF. O gerador só lista o nome, vindo do config.json (livro.py, L1231), e não tem página de checklist. O "3D" só vale com o 3D refeito no PDF final.
 - "devem caber, com os recuos de referência", as perguntas da prefeitura e o bloco do sol: SIM. Não prometem número, prazo nem aprovação, e o "o seu engenheiro" não soa como serviço incluído.
 - Linha de LGPD, se o dono quiser: use "Seu número serve só para este atendimento; se quiser, peça e eu apago." Não use "fica só nesta conversa", porque não temos como garantir.
5. Pôster C: SIM SE duas trocas.
 - (a) Tirar as ondas de som do carro da PAMONHA ou o "Zzz" da família. Juntos, dizem "dorme apesar do barulho", e a planta não mede som. O kit já evitou "longe do barulho".
 - (b) poster-C.py, L317: "Ache a frente do seu lote" passa a "Ache a frente e o fundo do seu lote", porque a E03 pede 20,6 m de fundo.
 - Chinelos no recuo: SIM. São escala e piada, não construção. As legendas "Na cena" batem com o PLANTAS.md.
 - Selo e aviso estão presentes, sem pessoa real nem marca. Os lotes e as casas conferem em escala.
6. Mobiliar: SIM SE três trocas.
 - (a) mobiliar.py, L88: troque "Não abra basculante nela por conta própria (Código Civil, art. 1.302)" por "Janela nela, não: o Código Civil não deixa abrir a menos de 1,5 m do vizinho (art. 1.301)". O 1.301 proíbe janela a menos de 1,5 m do vizinho; o 1.302 só dá ao vizinho o direito de exigir o desfazimento ou de tapar abertura pequena. "Por conta própria" sugere que com projeto pode.
 - (b) L74: acrescente ", se o guarda-roupa for para a parede da divisa" depois de "80 cm entre elas". Pelo doc (como-mobiliar, L57), no lugar da escrivaninha sobram 34 cm.
 - (c) L119: troque o título "A sala de 4,60 m pede viga." por "O vão da sala é de 4,60 m." O validador só diz que o engenheiro confere a laje e as vigas.
 - Queen: as frases "não estaciona, sobram 34 cm" (C01) e "cabe até queen, 75 e 70 cm" (E03) batem com o doc: SIM. O art. 1.300 na C01: SIM. As "ideias para conversar com o engenheiro" deixam a decisão com ele: SIM. As 3 páginas têm o aviso e o selo, sem estouro.
Achado fora do pedido (para o Maestro): o PDF lista "Checklist da obra por fase" em "O que vem junto" sem ter o conteúdo. Se o PDF final for assim ao cliente, é veto (CDC, arts. 30 e 37).
Não conferi: as imagens B-p1 a B-p4 do guia (rodapé e estouro), o PDF de lançamento e a calculadora. Os textos de 3 e 4 eu conferi pelos .md, não pelas imagens.
Reconferência: os itens 1 a 6 estão todos respondidos. Ficam em aberto com o dono o grátis (anúncio C) e a saudação.
