# Plano: a dor, do jeito indireto, nas 5 páginas que só têm a saída (25/11/2026)

**Quem escreveu:** Planejador. **Quem escreve as frases:** Redator, só depois do sim do dono. **Quem lê:** Revisor (o de risco tem veto).
**Base:** `pedidos/anexos/mapa-dor-solucao-do-ebook-2026-11-24.md`, seções 3, 5 e 6. Este plano não traz a frase final: traz onde, como, de onde vem a dor e quanto cabe.

**Recado do dono que manda em tudo:** a dor entra "daquele jeitinho": uma cena, um exemplo, um detalhe que o comprador reconhece. Nunca anunciada ("o problema é...", "você sofre com..."). Nenhum quadro de "problema".

**Regras que valem para as 5** (do mapa, seção 5): dor só de `ebook/referencias/MERCADO.md` ou dos dados da casa; o Marcos é fictício (a história dele não entra como fato); nada de custo, prazo ou aprovação; nada de "cabe com certeza" ("deve caber, confirme na prefeitura"); nada de "por etapas", "a casa que cresce" ou "sem quebrar parede"; os alertas "LEVE AO ENGENHEIRO" das págs. 9 e 13 não se mexem.

**Atenção, número de página:** os números 8, 12, 17, 22 e 23 são os do mapa (e-book de 24 páginas). O PDF gravado hoje (`ebook/saida/ebook.pdf`, 24/11 16:09, `casas_lancamento: 3`) tem **17 páginas**, e nele os textos estão nas págs. **8, 12, 5, 15 e 16** (conferido com `pdftotext`). Ache a página pelo texto, nunca pelo número. E o "para quem é" da C01 aparece **também na pág. 3** (a escolha pelo jeito de morar): mudar a C01 muda as duas.

## As 5 páginas

### 1. C01, "para quem é" (mapa: pág. 8; hoje: págs. 8 e 3)
- **Onde:** `ebook/fichas/textos.py`, linha 19, chave `TEXTOS["C01"]["para_quem"]`.
- **Hoje:** "Casal com 1 ou 2 filhos que quer dois quartos, varanda na entrada e banheiro largo, sem corredor comprido." (19 palavras)
- **Jeito indireto:** a pergunta que ele já se faz, no molde da E03: "num lote de 8 m, cabem 2 quartos e varanda?". Por quê: é a dúvida com que ele abre o e-book (o lote manda); a resposta já está na página (51 m², lote mínimo 8 x 13 m), então a pergunta não fica solta.
- **Fonte da dor:** `ebook/referencias/MERCADO.md`, linha 27 ("O lote manda") e linha 42 (medo de o terreno "não aceitar" a casa); dados da C01 em `ebook/plantas/` (51 m², lote mínimo 8 x 13 m, conferir no JSON antes de citar número).
- **Limite:** até 25 palavras (hoje 19). Tem de caber também na pág. 3, que é mais apertada. Nada de "cabe com certeza": "deve caber, confirme na prefeitura" se falar de caber.
- **O Revisor olha:** que é pergunta do comprador, não anúncio de problema; número igual ao da planta; nenhum "cabe com certeza"; pág. 3 sem quebra feia.

### 2. F01, "para quem é" (mapa: pág. 12; hoje: pág. 12)
- **Onde:** `ebook/fichas/textos.py`, linha 69, chave `TEXTOS["F01"]["para_quem"]`.
- **Hoje:** "Família de 4 ou 5 que precisa de 3 quartos com pouca área (71 m²), sem perder nenhum quarto." (21 palavras)
- **Jeito indireto:** o exemplo concreto da família que cresce: o filho que vem e precisa de quarto. Por quê: é a cena que ele vive (o 3º quarto como "quarto do filho que vem"), e a F01 responde exatamente isso.
- **Fonte da dor:** `MERCADO.md`, linha 26 ("o 3º quarto como escritório ou quarto do filho que vem"); D7 do mapa (linha 18). Só a parte da família: a parte "o dinheiro não dá" **não** entra (sem "por etapas", sem "a casa que cresce").
- **Limite:** até 25 palavras (hoje 21). Manter o 71 m².
- **O Revisor olha:** nenhuma promessa de ampliar depois; nada de "por etapas"; o Marcos não aparece como pessoa real.

### 3. Do e-book até a chave na mão, abertura nova (mapa: pág. 23; hoje: pág. 16)
- **Onde:** `ebook/gerador/livro.py`, linhas 1297 a 1310 (bloco "passos"). Hoje **não há** `<p class="abertura">`: a frase nova entra entre `{cab("passos")}` e `<ol class="passos">`, na linha 1310. Mudança de código pequena: o Redator escreve o texto, quem conduz encaixa.
- **Hoje:** nenhuma abertura; a única dor é "o orçamento deixa de ser chute" (linha 1307).
- **Jeito indireto:** a cena de quem só tem o desenho do parente ou do pedreiro e ouve "a prefeitura pede projeto". Por quê: é o retrato de quase todo comprador, e os 7 passos são a resposta direta.
- **Fonte da dor:** `MERCADO.md`, linha 28 ("Quem desenha a casa é o pedreiro, o parente ou o folheto") e linha 40 (o rascunho; "a prefeitura vai pedir projeto"). Não usar "cunhado" como fato do Marcos; "parente" serve.
- **Limite:** no máximo 2 linhas, uns 25 palavras. É a página mais cheia (7 passos e foto de 74 mm): se estourar, o detector do gerador para com erro; aí cortar a frase, não a foto (a foto é decisão do Designer).
- **O Revisor olha:** não sugerir que o e-book substitui o projeto; nada de prazo ou aprovação; não desmerecer o pedreiro.

### 4. Ficha do meu terreno, abertura (mapa: pág. 22; hoje: pág. 15)
- **Onde:** `ebook/gerador/livro.py`, linha 1295, o `<p class="abertura">` do bloco "ficha".
- **Hoje:** "Preencha com os dados da prefeitura e leve junto na primeira conversa com o engenheiro." (15 palavras)
- **Jeito indireto:** a pergunta que ele vai ouvir na primeira conversa ("qual é o recuo do seu lote?", "qual a taxa de ocupação?"). Por quê: mostra, sem dizer, o branco de chegar sem a resposta; a ficha é a resposta pronta.
- **Fonte da dor:** D8 do mapa (linha 19: `ebook/vendas/atributos-que-vendem.md`, linhas 14 e 15, que são hipótese do banco, linha 5); `MERCADO.md`, linha 65 ("Confira o recuo da sua cidade").
- **Limite:** até 30 palavras (2 linhas). A grade de campos e a foto de 60 mm vêm logo abaixo.
- **O Revisor olha:** tom de ajuda, não de susto; não pôr o engenheiro como adversário.

### 5. As palavras da obra, abertura (mapa: pág. 17; hoje: pág. 5)
- **Onde:** `ebook/gerador/livro.py`, linha 1225, o `<p class="abertura">` do glossário.
- **Hoje:** "As palavras que aparecem nas plantas, na prefeitura e na conversa com o engenheiro." (14 palavras)
- **Jeito indireto:** o detalhe que ele reconhece: a palavra ouvida no balcão da prefeitura e que não se entende ("habite-se", "taxa de ocupação"). Por quê: todo mundo já balançou a cabeça para uma palavra dessas; o glossário vem logo embaixo.
- **Fonte da dor:** `MERCADO.md`, linha 40 ("A prefeitura vai pedir projeto. Ele ainda não sabe como"); D3 e D8 do mapa (linhas 14 e 19). A palavra citada **tem de estar no glossário** da página (conferir na lista do próprio bloco).
- **Limite:** até 30 palavras (2 linhas).
- **O Revisor olha:** não fazer o leitor se sentir burro (é "ninguém explica", não "você não sabe"); a palavra citada existe no glossário.

## Pronto quando (vale para cada página)
1. O texto novo está no arquivo e na prévia: `python3 ebook/gerador/livro.py --previa <pasta>` termina **sem** "ERRO: página estourada" (`livro.py`, linha 2769), e o texto aparece nas páginas certas da prévia (C01 também na pág. 3).
2. A ficha do pedido (2130, segundo o mapa) tem "Revisor: ok" para aquela página.
3. `python3 ferramentas/checar.py` verde.
**Falha hoje:** os 5 textos são os de antes e a ficha 2130 não tem nenhum "Revisor: ok" (afirmação do mapa; não conferi a ficha).

## O que não conferi
- A ficha 2130 e se a decisão 1 do mapa ("quantas mudar?") já tem resposta do dono.
- A folga real de cada página em milímetros: os limites de palavras acima são pela régua do texto de hoje; quem manda é o detector do gerador.
- Por que o mapa fala em 24 páginas e o PDF gravado tem 17 (talvez o mapa use outro número de casas). Quem conduz confere antes do passo 4.

## Ordem do primeiro dia depois do reset
1. **Dono escolhe quantas páginas** (mapa, seção 6, pergunta 1: as 5, só as 2 das casas, ou nenhuma agora). Sem resposta, as frases não entram e o PDF segue o caminho de hoje.
2. **Redator escreve** com este plano, uma página por vez, na ordem 1 a 5 acima (as das casas primeiro: são as que mais ajudam a escolher).
3. **Revisor lê** (o de risco com veto) e escreve "Revisor: ok" ou o conserto na ficha.
4. **Gerar a prévia e conferir estouro:** `python3 ebook/gerador/livro.py --previa <pasta>`; abrir os PNG das páginas mexidas (e a pág. 3).
5. **"Gera o PDF"** só com o sim do dono.
6. **Leitura final no Fable** (`supervisor`), do PDF inteiro.
7. **PDF de emergência:** se algo travar entre 2 e 6, gerar o PDF com os textos de hoje (sem as frases), para a venda não esperar.
