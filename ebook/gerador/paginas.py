"""Textos fixos do e-book que o gerador (livro.py) usa: o aviso completo, os 7 erros, o glossário e a legenda de leitura.

Os textos de cada casa ficam em ebook/fichas/textos.py. Toda mudança de texto passa pelo Revisor de risco.
As funções de página antigas (capa, página dupla com QR e animação, bônus) saíram em 22/11/2026: o livro.py não as usava
e elas prometiam coisas que o e-book não tem.
"""

AVISO_COMPLETO = """
<p><strong>As plantas deste e-book são de referência.</strong> Elas servem para você comparar opções e
escolher a casa certa para o seu terreno e para a sua família antes de gastar com projeto.</p>
<p>Elas <strong>não são projeto executivo nem projeto legal</strong>: não servem para aprovar a obra na
prefeitura nem para construir direto a partir delas. Para construir, contrate um profissional habilitado
(arquiteto ou engenheiro). Ele vai adaptar a planta ao seu terreno, à posição do sol e às regras da sua
cidade, fazer os projetos que a obra exige e assumir a responsabilidade técnica, com RRT (arquiteto) ou
ART (engenheiro).</p>
<p>As medidas são de referência e precisam ser conferidas pelo arquiteto ou engenheiro que você contratar. Móveis, pisos e acabamentos são ilustrativos.</p>
"""

ERROS = [
    ("Ignorar o sol",
     "Quarto que pega o sol da tarde (poente) acumula calor e fica quente à noite. O lado que quase não recebe "
     "sol tende a ficar úmido. Os dois viram gasto com ar-condicionado e com mofo.",
     "Descubra o norte do terreno com a bússola do celular. Quartos para o <strong>nascente</strong> (leste) "
     "pegam o sol da manhã e tendem a ficar mais frescos à tarde. A planta pode ser espelhada ou girada para casar com o seu "
     "terreno: isso se decide com o arquiteto."),
    ("Corredor comprido",
     "Cada metro de corredor é piso, parede, reboco, pintura e telhado pagos que não viram cômodo. "
     "Ninguém mora no corredor.",
     "Prefira um <strong>hall</strong> pequeno que distribui as portas dos quartos e do banheiro. Corredor, "
     "só onde não tiver outro jeito."),
    ("Banheiro de frente para a sala",
     "Quem está na sala vê e ouve o banheiro. É desconfortável para a família e para a visita, e consertar "
     "depois que a parede sobe é caro.",
     "A porta do banheiro abre para o <strong>hall</strong> ou para a circulação, fora da linha de vista "
     "do sofá e da mesa."),
    ("Banheiro sem janela",
     "Sem ventilação natural, a umidade do banho fica dentro de casa. O mofo aparece no teto e no armário, "
     "e o exaustor vira conta de luz para sempre.",
     "Janela alta para fora da casa (<strong>peitoril</strong> por volta de 1,50 m, para ter privacidade). "
     "Se não der, o duto de ventilação precisa estar no projeto. Muitos códigos de obras exigem ventilação."),
    ("Esquecer os recuos",
     "Projeto fora das regras do lote é reprovado na prefeitura. Obra fora das regras pode ser multada, "
     "embargada ou ter que demolir a parte irregular.",
     "Antes de escolher a planta, descubra os <strong>recuos</strong> e as taxas do seu lote na prefeitura. "
     "A seção Terreno e recuos mostra como."),
    ("Não prever ampliação",
     "A família cresce e a casa precisa de mais um quarto. Se ninguém pensou nisso, a ampliação quebra "
     "paredes, mexe no telhado ou não cabe no lote.",
     "Se a família pode crescer, diga isso ao engenheiro antes do projeto: ele vê se o lote tem espaço e deixa livre "
     "o lado da ampliação, sem caixa d'água, fossa ou banheiro no caminho. As casas deste e-book não trazem "
     "ampliação desenhada: aumentar a casa é projeto novo, do engenheiro ou do arquiteto."),
    ("Construir sem ver a casa pronta",
     "Mudar de ideia com a obra andando é o mais caro de tudo: quebrar, refazer e pagar o material duas vezes. "
     "E quase sempre acontece porque a pessoa só entendeu a casa quando viu as paredes de pé.",
     "Veja a casa antes do primeiro tijolo, na <strong>planta com os móveis em escala</strong> e na <strong>casa em 3D</strong>: se a cama cabe, se o "
     "sofá fica de frente para a TV, se a cozinha tem bancada. É o que cada planta deste e-book mostra."),
]

GLOSSARIO = [
    ("Área construída", "Área total da casa, medida por fora das paredes. É a que conta para a prefeitura e para o orçamento."),
    ("Área útil", "Área de piso por dentro das paredes, a que você realmente usa. É menor que a construída."),
    ("Área fechada", "A parte da casa com paredes e telhado, medida por fora, sem contar varanda nem garagem."),
    ("Cota", "Número na planta que mostra uma medida, em metros. Ex.: 6,50 m de frente."),
    ("Divisa", "Linha que separa o seu lote do vizinho ou da rua."),
    ("Hall", "Espaço pequeno que liga os cômodos. Substitui o corredor comprido."),
    ("Nascente e poente", "Nascente é o lado onde o sol nasce (leste). Poente é onde ele se põe (oeste)."),
    ("Peitoril", "Altura da base da janela até o piso. Janela de banheiro costuma ter peitoril alto."),
    ("Pé-direito", "Altura do piso até o teto. O mínimo é definido pelo código de obras da sua cidade."),
    ("Planta baixa", "Desenho da casa vista de cima, como se as paredes fossem cortadas na altura das janelas."),
    ("Planta humanizada", "Planta baixa com móveis, pisos e jardim, para você entender o uso de cada cômodo."),
    ("Recuo", "Distância mínima entre a casa e a divisa do lote: na frente, nos lados e nos fundos."),
    ("Suíte", "Quarto com banheiro próprio, que abre só para ele."),
    ("Taxa de ocupação", "Quanto do lote a casa pode cobrir, vista de cima. Ex.: 60% de um lote de 200 m² = 120 m²."),
    ("Coeficiente de aproveitamento", "Quanto se pode construir somando todos os andares. Ex.: coeficiente 1 num lote de 200 m² = até 200 m² construídos."),
    ("Taxa de permeabilidade", "Parte do lote que precisa ficar sem piso, com terra ou grama, para a chuva infiltrar."),
    ("ART e RRT", "Documentos em que o engenheiro (ART, no CREA) ou o arquiteto (RRT, no CAU) assume a responsabilidade técnica."),
    ("Alvará e habite-se", "Alvará é a licença para começar a obra. Habite-se é a certidão de que a casa pronta pode ser ocupada."),
]

LEGENDA_LEITURA = [
    ("Cotas", "As medidas da casa por fora das paredes, em metros. Aqui, 6,50 m de frente e 8,50 m de fundo."),
    ("Porta", "O arco mostra para que lado a folha abre. Confira se ela não bate em móvel."),
    ("Janela", "O trecho da parede com linhas finas. A largura dela aparece na cota."),
    ("Tracejado azul", "Veneziana em cima da porta (fica acima da altura do corte)."),
    ("Parede", "A faixa escura. Nas contas do e-book, a externa tem 15 cm e a interna 12 cm."),
    ("Nome e área do cômodo", "A área livre, por dentro das paredes, em m². Compare com o seu cômodo de hoje."),
    ("Móveis", "Desenhados em escala, para mostrar que a cama, o sofá e a mesa cabem."),
    ("Ficha", "Nome da planta, área total, quartos e banheiros."),
    ("A casa em 3D", "A mesma planta com paredes e móveis, vista de cima e sem telhado, na página de cada casa."),
    ("Sol", "Em cada casa testamos as quatro posições da rua em relação ao sol, numa conta simples. A ficha diz o melhor e o pior lado; o arquiteto confere para o clima da sua cidade."),
]

# Sobretítulo e título de cada página fixa: um lugar só (D17, 24/11/2026). O livro.py e o sumário do modo
# --duas-partes leem daqui. No e-book em duas partes (cada casa primeiro, casas em geral depois) os sobretítulos
# que dizem o tempo ("Antes de escolher") ficam fora de ordem: quem reescreve é o Redator, aqui, e o Revisor confere.
SOBRE = {
    "usar": "Antes de começar",
    "ache": "Comece aqui",
    "familia": "Comece aqui",
    "ler": "Antes de escolher",
    "palavras": "Antes de escolher",
    "erros": "Antes da laje",
    "indice": "Índice rápido",
    "terreno": "Depois de escolher",
    "ficha": "Depois de escolher",
    "passos": "Depois de escolher",
    "fim": "Fim (e começo da obra)",
}
TITULOS = {
    "usar": "Como usar este e-book",
    "ache": "Qual casa cabe no seu lote?",
    "ler": "Como ler uma planta",
    "palavras": "As palavras da obra",
    "erros": "Os 7 erros que saem caro",
    "terreno": "Terreno e recuos",
    "ficha": "Ficha do meu terreno",
    "passos": "Do e-book até a chave na mão",
    "fim": "Agora é com você",
}

# E-book em duas partes (decisão do dono, 24/11/2026: "uma parte falando de cada casa específica, e outra parte
# falando de casas no geral"). Só o modo --duas-partes do livro.py usa, e só em prévia. TEXTO PROVISÓRIO, do esboço
# do Designer (pedidos/anexos/mapa-duas-partes-do-ebook-2026-11-24.md): o Redator dá os nomes e o Revisor confere.
DUAS_PARTES = {
    "parte1": ("parte 1", "A casa do seu lote", "Uma casa por frente de terreno"),      # cada casa: aba amarela
    "parte2": ("parte 2", "Para qualquer casa", "Aba azul na borda"),                   # casas em geral: aba azul
    "aba_geral": "geral",
    # página reservada (ainda rascunho em outro script; entra no D20): só o quadro "página em preparo"
    "comodo": "cômodo a cômodo",
    "em_preparo": "Página em preparo",
}


# Página "A parede que não pode ter janela" (parte 2, casas em geral; D21, 24/11/2026). Texto do Redator, copiado sem
# mudar de pedidos/anexos/pagina-parede-sem-janela-texto.md (seção 3), com a conferência do Arquiteto e o veto do
# Revisor de 24/11 já aplicados. Os "rotulos" são as palavras dos croquis e da folha, do rascunho do Designer
# (ebook/plantas/rascunhos/parede_sem_janela.py). Só o modo --duas-partes usa. Mudou aqui, volta ao Revisor.
PAREDE = {
    "sobre": "Casas em geral",
    "titulo": "A parede que não pode ter janela",
    "sub": "E quatro jeitos de ela trabalhar para você",
    "abre": "Casa encostada no vizinho tem uma parede sem janela: o Código Civil não deixa abrir janela a menos de 1,5 m do terreno vizinho (art. 1.301; o engenheiro confirma). Só escapam aberturas de até 10 x 20 cm, a mais de 2 m do piso, e essas o vizinho pode tapar quando construir (art. 1.302). Não é defeito. A luz vem pelos outros lados, e essa parede trabalha para você.",
    "campos": ("O que fazer", "Cuidado", "Nas casas"),
    "ideias": [
        {"nome": "A cabeceira na parede cega",
         "faz": "Encoste a cabeceira da cama na parede da divisa, com prateleira em cima. A parede da janela fica livre: nenhum guarda-roupa tapando a luz.",
         "cuid": "Nicho na parede da divisa, só se o engenheiro aprovar. Prateleira presa na parede, sim.",
         "casas": "Família Compacta: o quarto casal, como no desenho. Casa Fita: no quarto da frente, a cama de casal cabe com a cabeceira na divisa (página da casa)."},
        {"nome": "A parede que guarda",
         "faz": "Guarda-roupa, estante, rack e geladeira na parede da divisa; a janela fica para a cama, o sofá e a pia.",
         "cuid": "Móvel colado esconde umidade: pergunte ao engenheiro pela impermeabilização do pé da parede. Fure só sabendo onde passa o cano.",
         "casas": "Casa Fita: guarda-roupa de 6 portas no quarto casal, rack na sala e geladeira na divisa, bancada embaixo da janela. Família Compacta: rack na sala."},
        {"nome": "A janela alta do outro lado",
         "faz": "Telhado mais alto no cômodo escuro, com uma faixa de janela virada para o recuo, a 1,5 m ou mais do vizinho, como toda janela.",
         "cuid": "Muda telhado e estrutura: o engenheiro diz se vale. O encontro dos dois telhados pede rufo bem feito: é onde mais entra goteira.",
         "casas": "Não está nas 3 casas: leve a ideia ao engenheiro."},
        {"nome": "A luz que vem de cima",
         "faz": "No ponto mais longe da janela, uma telha translúcida ou uma claraboia traz a luz do dia, sem abrir janela na parede da divisa.",
         "cuid": "Com forro ou laje embaixo, é preciso abrir um vão neles. Estrutura, vedação, calha e calor: o engenheiro escolhe se e como. A chuva não pode cair no vizinho (art. 1.300).",
         "casas": "Não está nas 3 casas: leve a ideia ao engenheiro."}],
    "engenheiro": "Leve ao engenheiro",
    "perguntas": [
        "Esta parede da divisa é estrutural? Posso prender armário alto ou fazer nicho nela?",
        "O pé da parede da divisa leva impermeabilização? Como fica o lado de fora, se o vizinho ainda não construiu?",
        "Para onde vai a chuva do telhado deste lado? O código de obras da minha cidade pede mais de 1,5 m para janela perto da divisa?",
        "A prefeitura deixa a casa encostar na divisa?"],
    "rotulos": {
        "muro": "parede da divisa, sem janela", "vizinho": "lado do vizinho", "sugestao": "sugestão",
        "janela_livre": "janela livre", "prateleira": "prateleira", "cabeceira": ("cabeceira", "na divisa"),
        "casa_quarto": ("Família Compacta", "quarto casal"),
        "geladeira": "geladeira", "aereo": "aéreo", "pia": "pia", "janela": "janela", "recuo": "recuo",
        "esquema": "esquema, não é das 3 casas", "distancia": "1,5 m ou mais", "janela_alta": "janela alta", "rufo": "rufo",
        "comodo_escuro": ("cômodo", "escuro"), "telha": "telha clara", "vao": "vão no forro", "calha": "calha",
        "agua": ("a água fica", "no seu lote"),
        "selo": ("Imagem ilustrativa", "croquis: móveis e prateleira não vêm junto"),
    },
}
