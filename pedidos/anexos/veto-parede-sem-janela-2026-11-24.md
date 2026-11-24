# Veto: página "A parede que não pode ter janela" (passo D19), 24/11/2026 · Revisor de risco, Opus (rascunho)

Vale como SIM do rascunho; a página montada no PDF ainda pede a leitura no Fable.

1. **Título e subtítulo:** SIM.
2. **Abertura:** SIM (bate com o art. 1.301, caput e §2º, e com o parágrafo único do art. 1.302). Ajuste opcional: "Na parede encostada, só escapam…".
3. **Ideia 1 (cabeceira na parede cega):** SIM. Família Compacta conferida nos dados. **Casa Fita passa como está:** o quarto da frente tem 3,20 x 2,89 m livres; com a cama de casal de cabeceira na divisa sobram 84 cm até o guarda-roupa e 1,49 m nos lados. Condição de montagem: a página da Casa Fita no PDF traz essa frase, senão "(página da casa)" aponta para nada.
4. **Ideia 2 (a parede que guarda):** SIM (guarda-roupa, rack e geladeira na divisa; bancada na parede do recuo, embaixo da janela de 1,70 m).
5. **Ideia 3 (janela alta do outro lado):** SIM ("o engenheiro diz se vale", "não está nas 3 casas" e a legenda "esquema" bastam).
6. **Ideia 4 (luz que vem de cima):** **SIM SE** "sem abrir a parede do vizinho" → "sem abrir janela na parede da divisa" (a parede é do dono da casa).
7. **Leve ao engenheiro:** SIM. Se couber, acrescentar "A prefeitura deixa a casa encostar na divisa?".
8. **Aviso:** SIM, inteiro. Página estourada cobrindo o aviso é veto.
9. **Croquis:** SIM (o 3 e o 4 com "esquema, não é das 3 casas"; no 1 e no 2, o que não está no dado leva "sugestão"). Croqui gerado por IA volta ao Revisor.

Nada de custo, prazo, aprovação ou dispensa de profissional. **Não conferido:** a página montada; "é onde mais entra goteira" (frase do Arquiteto, sem número); o desempenho da telha translúcida.

## Leitura final da página montada, 24/11/2026 (Revisor, Fable)

**SIM SE**, com as 2 trocas obrigatórias e as recomendadas abaixo, aplicadas em seguida no gerador (`ebook/gerador/paginas.py`, `PAREDE`, e `ebook/gerador/livro.py`) e no texto (`pagina-parede-sem-janela-texto.md`).

**Obrigatórias**
1. Ideia 1, "Nas casas": "Família Compacta: o quarto casal, como no desenho. Casa Fita: no quarto da frente, desenhado com cama de solteiro, a de casal cabe com a cabeceira na divisa." (sai o "(página da casa)", que apontava para nada).
2. Ao lado do selo "Imagem ilustrativa": "croquis: os móveis e a prateleira são sugestão" (no lugar de "móveis e prateleira não vêm junto").

**Recomendadas (todas aplicadas)**
3. Título da ideia 1: "A cabeceira na parede sem janela".
4. Ideia 3, "Cuidado": "Muda telhado e estrutura: o engenheiro diz se vale. O encontro dos dois telhados pede rufo bem feito, para não dar goteira."
5. Rótulos dos croquis: "telha clara" → "telha translúcida"; "aéreo" → "armário aéreo".
6. Legenda "esquema, não é das 3 casas": fundo branco atrás das letras, para a hachura do chão não passar por cima.
7. Página "Terreno e recuos": "Em área urbana, o Código Civil (art. 1.301) não deixa abrir janela a menos de 1,5 m do terreno vizinho (o engenheiro confirma)."

**Pendência para o Arquiteto:** com a cama de casal no quarto da frente da Casa Fita, a escrivaninha ainda é usável?


## Frase da Casa Fita na ideia 1, 24/11/2026 (Arquiteto conferiu; Revisor, Fable, deu a frase)

O Arquiteto conferiu na E03: a cama de casal cabe com a cabeceira na divisa e a porta abre, mas só com 1 criado e com a escrivaninha mudando para o canto da janela. O Revisor trocou a frase por: "Casa Fita: no quarto da frente, desenhado com cama de solteiro, a de casal padrão (1,38 x 1,88 m) cabe com a cabeceira na divisa, com 1 criado e a escrivaninha no canto da janela, do lado do recuo. Meça antes de comprar." Aplicada no `PAREDE` do gerador e no texto. Se o Arquiteto confirmar a queen, "padrão (1,38 x 1,88 m)" pode sair.
