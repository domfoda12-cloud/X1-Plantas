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
# Onde estão os bônus (D35, 24/11/2026): título e frase da última página do e-book. Os bônus saem num arquivo separado,
# gerado junto (ebook/gerador/bonus.py); {a} e {b} são os nomes do config.json e {arquivo} o nome do PDF.
# Só aparece se o arquivo dos bônus sai. Texto novo: espera a leitura do Revisor de risco.
ONDE_BONUS = ("Os bônus", "{a} e {b} estão em outro arquivo, que vem junto com este e-book: {arquivo}.")

DUAS_PARTES = {
    "parte1": ("parte 1", "A casa do seu lote", "Uma casa por frente de terreno"),      # cada casa: aba amarela
    "parte2": ("parte 2", "Para qualquer casa", "Aba azul na borda"),                   # casas em geral: aba azul
    "aba_geral": "geral",
    # página reservada (casa que ainda não tem o cômodo a cômodo aprovado): só o quadro "página em preparo"
    "comodo": "cômodo a cômodo",
    "sum_comodo": "cômodo a cômodo na pág. {}",   # no sumário da página 2, na linha de cada casa
    "em_preparo": "Página em preparo",
}


# Página "A parede que não pode ter janela" (parte 2, casas em geral; D21, 24/11/2026). Texto do Redator, copiado sem
# mudar de pedidos/anexos/pagina-parede-sem-janela-texto.md (seção 3), com a conferência do Arquiteto e o veto do
# Revisor de 24/11 já aplicados, e também as trocas da leitura final da página montada (Revisor, 24/11). Os "rotulos" são as palavras dos croquis e da folha, do rascunho do Designer
# (ebook/plantas/rascunhos/parede_sem_janela.py). Só o modo --duas-partes usa. Mudou aqui, volta ao Revisor.
PAREDE = {
    "sobre": "Casas em geral",
    "titulo": "A parede que não pode ter janela",
    "sub": "E quatro jeitos de ela trabalhar para você",
    "abre": "Casa encostada no vizinho tem uma parede sem janela: o Código Civil não deixa abrir janela a menos de 1,5 m do terreno vizinho (art. 1.301; o engenheiro confirma). Só escapam aberturas de até 10 x 20 cm, a mais de 2 m do piso, e essas o vizinho pode tapar quando construir (art. 1.302). Não é defeito. A luz vem pelos outros lados, e essa parede trabalha para você.",
    "campos": ("O que fazer", "Cuidado", "Nas casas"),
    "ideias": [
        {"nome": "A cabeceira na parede sem janela",
         "faz": "Encoste a cabeceira da cama na parede da divisa, com prateleira em cima. A parede da janela fica livre: nenhum guarda-roupa tapando a luz.",
         "cuid": "Nicho na parede da divisa, só se o engenheiro aprovar. Prateleira presa na parede, sim.",
         "casas": "Família Compacta: o quarto casal, como no desenho. Casa Fita: no quarto da frente, desenhado com cama de solteiro, a de casal padrão (1,38 x 1,88 m) cabe com a cabeceira na divisa, com 1 criado e a escrivaninha no canto da janela, do lado do recuo. Meça antes de comprar."},
        {"nome": "A parede que guarda",
         "faz": "Guarda-roupa, estante, rack e geladeira na parede da divisa; a janela fica para a cama, o sofá e a pia.",
         "cuid": "Móvel colado esconde umidade: pergunte ao engenheiro pela impermeabilização do pé da parede. Fure só sabendo onde passa o cano.",
         "casas": "Casa Fita: guarda-roupa de 6 portas no quarto casal, rack na sala e geladeira na divisa, bancada embaixo da janela. Família Compacta: rack na sala."},
        {"nome": "A janela alta do outro lado",
         "faz": "Telhado mais alto no cômodo escuro, com uma faixa de janela virada para o recuo, a 1,5 m ou mais do vizinho, como toda janela.",
         "cuid": "Muda telhado e estrutura: o engenheiro diz se vale. O encontro dos dois telhados pede rufo bem feito, para não dar goteira.",
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
        "geladeira": "geladeira", "aereo": "armário aéreo", "pia": "pia", "janela": "janela", "recuo": "recuo",
        "esquema": "esquema, não é das 3 casas", "distancia": "1,5 m ou mais", "janela_alta": "janela alta", "rufo": "rufo",
        "comodo_escuro": ("cômodo", "escuro"), "telha": ("telha", "translúcida"), "vao": "vão no forro", "calha": "calha",
        "agua": ("a água fica", "no seu lote"),
        "selo": ("Imagem ilustrativa", "croquis: os móveis e a prateleira são sugestão"),
    },
}


# Páginas "cômodo a cômodo" de cada casa (parte 1 do modo --duas-partes; D20, 24/11/2026). Só o modo --duas-partes usa.
# COMODO: os rótulos fixos da folha e do desenho, do rascunho do Designer (ebook/plantas/rascunhos/comodo_a_comodo.py,
# A9 e D31), com as trocas do Revisor e do Arquiteto (pedidos/anexos/veto-pagina-prova-E03-2026-11-24.md e
# veto-pagina-prova-F01-C01-2026-11-24.md). Mudou aqui, volta ao Revisor.
COMODO = {
    "eti": "Cômodo a cômodo",
    "ideia": "Ideia:", "cuidado": "Cuidado:",
    "perguntas": "Pergunte ao seu engenheiro ou eletricista",
    "tomadas": "Tomadas:",
    "atencao": "Atenção (8).",
    "ref": "Em destaque na página anterior, com a parede ampliada.",
    "selo": {"E03": "Imagem ilustrativa: móveis e acabamentos não vêm junto",
             "C01": "Imagem ilustrativa: móveis e acabamentos são sugestão",
             "F01": "Imagem ilustrativa: móveis e acabamentos são sugestão"},
    "detalhe": {"E03": "Detalhe da cozinha, ampliado", "C01": "Detalhe do hall, ampliado"},
    "destaque": {"F01": "Destaque: na planta, as cotas do ponto de luz e o vão da sala",
                 "C01": "Destaque: o hall, ampliado ao lado da planta"},
    # a legenda de cada planta: (marca desenhada, frase)
    "legenda": {
        "E03": [("amarelo", "Em amarelo, a parede de cada número."),
                ("trac", "Tracejado bege: o que fica por cima (o maleiro do hall)."),
                ("recuo", "Tracejado azul: o recuo, área aberta."),
                ("porta", "A porta de entrada também é amarela, como no resto do e-book."),
                ("medida", "Em azul, medida em metros.")],
        "F01": [("amarelo", "Em amarelo, a parede de cada número."),
                ("ponto", "Pontilhado amarelo: aqui não há parede; a sala é aberta para a cozinha (veja o 2)."),
                ("trac", "Tracejado bege: o maleiro, em cima do guarda-roupa do quarto casal."),
                ("verde", "Tracejado verde: a faixa livre ao lado da casa e o fundo do lote, área aberta."),
                ("porta", "A porta de entrada também é amarela, como no resto do e-book."),
                ("medida", "Em azul, medida em metros.")],
        "C01": [("amarelo", "Em amarelo, a parede de cada número."),
                ("ponto", "Pontilhado amarelo: a divisa da varanda; o desenho não mostra a parede, mas esse lado é fechado (veja o 1)."),
                ("trac", "Tracejado bege: o que fica por cima (o maleiro do hall)."),
                ("ven", "Tracejado azul: veneziana em cima da porta (fica acima da altura do corte)."),
                ("porta", "A porta de entrada também é amarela, como no resto do e-book."),
                ("medida", "Em azul, medida em metros.")],
    },
    # palavras dentro do desenho; os números ({}) vêm dos dados e do validador, no livro.py
    "desenho": {"luz": "ponto de luz", "vao": "vão livre {}", "faixa": "faixa livre {} m", "recuo": "recuo {} m",
                "fundo": ("fundo: {} m no lote de {} x {}", "({} m no lote mínimo, de {} x {})"),
                "frente": "frente: {} m até a rua, recuo de referência (cortada no desenho)"},
}

# COMODOS: o texto de cada casa, copiado sem mudar dos arquivos aprovados pelo Revisor de risco (seção "TEXTO DA
# PÁGINA" de pedidos/anexos/pagina-prova-comodo-a-comodo-E03-texto.md, pagina-comodo-a-comodo-C01-texto.md e
# pagina-comodo-a-comodo-F01-texto.md). "dim" e as medidas dentro das frases são conferidas pelo livro.py contra o
# validador a cada geração: se o dado mudar, o gerador avisa e falha. Em "perguntas": (pergunta, complemento, os
# números a que ela aponta). Mudou aqui, volta ao Revisor.
COMODOS = {'E03': {'titulo': 'Antes de fechar a parede',
         'sub': '7 lugares da Casa Fita, cômodo a cômodo',
         'abre': 'Tomada, cano e armário se decidem com a parede aberta. Cada número aponta um lugar da planta, com '
                 'a medida para levar à obra.',
         'nota': 'Os pontos de tomada desta página são sugestão; o mínimo é o eletricista que confere na norma '
                 'vigente.',
         'itens': [{'n': 1,
                    'nome': 'Quarto da frente',
                    'dim': '3,20 x 2,89 m',
                    'resto': '',
                    'ideia': 'Tomada nas duas paredes de cabeceira (divisa e recuo): o quarto vira solteiro, duas '
                             'camas ou casal sem extensão no chão. O eletricista confere.',
                    'cuid': 'Nicho na divisa, a parede de 15 cm que separa do vizinho: prateleira, sim; nicho, só se '
                            'o engenheiro aprovar.'},
                   {'n': 2,
                    'nome': 'Sala',
                    'dim': '3,20 x 3,54 m',
                    'resto': '',
                    'ideia': 'Sofá embaixo da janela, rack na divisa e 1,92 m entre os dois: esse vão é o corredor '
                             'da casa. Mesa de centro, só pequena.',
                    'cuid': 'A porta do quarto da frente abre direto na sala: do sofá, vê-se a cama.'},
                   {'n': 3,
                    'nome': 'Cozinha e copa',
                    'dim': '3,20 x 3,14 m',
                    'resto': '',
                    'ideia': 'Janela de 1,70 m sobre a pia: torneira de bancada; tomada sob a janela ou nos 22,5 cm '
                             'até a porta. Eletricista e encanador conferem.',
                    'cuid': 'Fechar a parede sem marcar tomada e torneira da pia: depois do acabamento, não sobra '
                            'parede. Decida antes do reboco.'},
                   {'n': 4,
                    'nome': 'Banheiro',
                    'dim': '2,19 x 1,58 m',
                    'resto': '',
                    'ideia': 'Antes de fechar a parede, peça ao encanador o teste do encanamento e um registro só do '
                             'banheiro.',
                    'cuid': 'Janela dentro do box de 0,90 m pega água do chuveiro: o material dela, decida com o '
                            'pedreiro.'},
                   {'n': 5,
                    'nome': 'Hall',
                    'dim': '0,89 x 2,94 m',
                    'resto': '',
                    'ideia': 'Maleiro por cima do hall, acima das portas: 0,89 x 2,94 m, com uns 40 a 70 cm conforme '
                             'o pé-direito. Eletricista confere a luz.',
                    'cuid': 'Hall de 89 cm: estante ou armário tira a passagem. Na parede da divisa, só ganchos e '
                            'quadros.'},
                   {'n': 6,
                    'nome': 'Quarto casal (fundos)',
                    'dim': '3,20 x 2,99 m',
                    'resto': '',
                    'ideia': 'Cabe cama queen: 75 cm no pé e uns 70 de cada lado. Um segundo interruptor na '
                             'cabeceira apaga a luz com você deitado; eletricista confere.',
                    'cuid': 'Cômodo novo no fundo do lote tapa a única janela deste quarto. Ampliar pede projeto '
                            'novo.'},
                   {'n': 7,
                    'nome': 'Recuo lateral (direita)',
                    'dim': '1,5 x 16,1 m',
                    'resto': '',
                    'ideia': 'Marque com trena: janela a 1,5 m da divisa, o mínimo do Código Civil (art. 1.301). A '
                             'sua cidade pode pedir mais.',
                    'cuid': 'Telhado no recuo tira boa parte da luz de 4 cômodos; se a janela ainda conta como '
                            'ventilação, quem diz é o código de obras.'}],
         'perguntas': [('Ao eletricista:',
                        'a tomada da bancada cabe na faixa sob a janela da cozinha ou nos 22,5 cm até a porta?',
                        [3]),
                       ('Ao engenheiro:',
                        'a parede da divisa é estrutural? Leva impermeabilização no pé, do lado do vizinho?',
                        [1, 5]),
                       ('Ao engenheiro:',
                        "a caixa d'água vai em cima do hall e do banheiro? O maleiro atrapalha o acesso a ela?",
                        [5])],
         'alvenaria': 'Se a sua casa for de alvenaria estrutural, parede não se corta depois: nicho, cano e fio só '
                      'onde o projeto previu. Quem diz é o engenheiro.'},
 'C01': {'titulo': 'Antes de fechar a parede',
         'sub': '8 lugares da Casa Compacta, cômodo a cômodo',
         'abre': 'Tomada, cano e armário se decidem com a parede aberta. Cada número aponta um lugar da planta, com '
                 'a medida para levar à obra.',
         'nota': 'Os pontos de tomada desta página são sugestão; o mínimo é o eletricista que confere na norma '
                 'vigente.',
         'veneziana': 'Serviço: não tem janela. A ventilação vem de uma veneziana de 0,90 x 0,50 m em cima da porta '
                      'de fora, que só cabe com pé-direito de uns 2,80 m. Ela deixa passar menos ar e quase nenhuma '
                      'luz: o engenheiro confere se a ventilação e a luz do serviço bastam no código de obras da sua '
                      'cidade.',
         'itens': [{'n': 1,
                    'nome': 'Varanda',
                    'dim': '3,35 x 1,20 m',
                    'resto': '(uns 3,20 m entre a divisa e o quarto)',
                    'ideia': 'Ganchos de rede entre a divisa e o quarto (uns 3,20 m); na divisa, só em parede ou '
                             'pilar que o engenheiro aprove. Rede armada fecha a entrada.',
                    'cuid': 'Não feche a varanda: a única janela da sala dá para ela; fechada, a sala fica sem '
                            'janela para fora. A lateral da divisa já é fechada (Código Civil, art. 1.301; o '
                            'engenheiro confirma).'},
                   {'n': 2,
                    'nome': 'Quarto da frente',
                    'dim': '2,85 x 3,09 m',
                    'resto': '',
                    'ideia': 'Três tomadas baixas na parede da rua, que não tem janela: no meio e perto de cada '
                             'ponta. Duas camas hoje, casal amanhã. Eletricista confere.',
                    'cuid': 'Guarda-roupa: 95 cm dele ficam atrás do box. Parede bem impermeabilizada e vão atrás do '
                            'móvel; o pedreiro confere.'},
                   {'n': 3,
                    'nome': 'Sala e jantar',
                    'dim': '3,14 x 3,99 m',
                    'resto': '',
                    'ideia': 'Troque a TV de parede: no desenho, ela está na parede do quarto. Na divisa, num rack '
                             'de até 1,35 m, com o sofá de 2 lugares na parede do quarto, a 1,86 m dela. Eletricista '
                             'confere.',
                    'cuid': 'Do jeito da planta, a TV fica na parede de 12 cm do quarto da frente, logo depois do pé '
                            'de uma cama: o som passa.'},
                   {'n': 4,
                    'nome': 'Hall',
                    'dim': '1,04 x 1,68 m',
                    'resto': '',
                    'ideia': 'Maleiro sobre o hall inteiro, acima das 3 portas: 1,04 x 1,68 m para mala e cobertor. '
                             'Luz do teto: o eletricista confere.',
                    'cuid': 'Altura: uns 40 a 70 cm, conforme o pé-direito. Tampo e peso que aguenta: marceneiro ou '
                            'pedreiro confere.'},
                   {'n': 5,
                    'nome': 'Banheiro',
                    'dim': '1,84 x 1,68 m',
                    'resto': '',
                    'ideia': 'Este banheiro tem cano só dele: peça ao encanador um registro só do banheiro e o teste '
                             'do encanamento antes do reboco.',
                    'cuid': 'Box: parede de 12 cm, com o guarda-roupa do quarto atrás. Prateleira, sim; nicho, só se '
                            'o pedreiro garantir.'},
                   {'n': 6,
                    'nome': 'Quarto casal',
                    'dim': '2,94 x 3,19 m',
                    'resto': '',
                    'ideia': 'Espera do ar-condicionado antes do reboco: tomada alta e dreno na parede da janela, '
                             'condensadora no fundo. Eletricista e pedreiro conferem.',
                    'cuid': 'Queen não cabe: a passagem fica com 34 cm do lado da janela. Casal padrão (1,38 x 1,88 '
                            'm) cabe.'},
                   {'n': 7,
                    'nome': 'Cozinha',
                    'dim': '1,83 x 2,95 m',
                    'resto': '',
                    'ideia': 'Bancada de apoio em L sob a janela do fundo: 1,21 m, para micro-ondas e '
                             'liquidificador. Eletricista confere a tomada.',
                    'cuid': 'A parede da pia é a da cabeceira do casal: caixas de tomada não ficam costas com '
                            'costas. Eletricista confere.'},
                   {'n': 8,
                    'nome': 'Serviço',
                    'dim': '1,19 x 2,89 m',
                    'resto': '',
                    'ideia': 'Prateleira em cima da máquina, na divisa, para sabão e balde. Na parede do fundo, não: '
                             'em cima da porta fica a veneziana.',
                    'cuid': 'A veneziana (0,90 x 0,50 m) só cabe com pé-direito de uns 2,80 m. Ventilação e luz, o '
                            'engenheiro confere.'}],
         'perguntas': [('Ao engenheiro:',
                        'qual vai ser o pé-direito da obra? Com menos de uns 2,80 m, como fica a ventilação do '
                        'serviço?',
                        [8]),
                       ('Ao eletricista:', 'a caixa da TV pode ir na divisa? Por onde desce o fio da antena?', [3]),
                       ('Ao engenheiro:',
                        'o recuo de 1,5 m da divisa é medido até a face de fora da parede?',
                        [2, 5])],
         'alvenaria': 'Se a sua casa for de alvenaria estrutural, parede não se corta depois: nicho, cano e fio só '
                      'onde o projeto previu. Quem diz é o engenheiro.'},
 'F01': {'titulo': 'Antes de fechar a parede',
         'sub': '8 lugares da Casa Família Compacta, cômodo a cômodo',
         'abre': 'Tomada, cano e armário se decidem com a parede aberta. Cada número aponta um lugar da planta, com '
                 'a medida para levar à obra.',
         'nota': 'Os pontos de tomada desta página são sugestão; o mínimo é o eletricista que confere na norma '
                 'vigente.',
         'itens': [{'n': 1,
                    'nome': 'Sala e jantar',
                    'dim': '4,45 x 3,55 m',
                    'resto': '',
                    'ideia': 'Ponto de luz da mesa: 3,75 m da parede da divisa e 1,70 m da parede da frente, medidos '
                             'por dentro. Antes, o engenheiro diz onde passa a viga; o eletricista confere.',
                    'cuid': 'Quem entra e vai aos quartos passa entre TV e sofá (1,45 m): sem mesa de centro.'},
                   {'n': 2,
                    'nome': 'Cozinha',
                    'dim': '2,04 x 3,49 m',
                    'resto': '',
                    'ideia': 'Parede da pia sem janela: cabe armário aéreo nos 2,59 m depois da porta do serviço. '
                             'Antes de furar, o encanador marca os canos.',
                    'cuid': 'Sem ponto de depurador sobre o fogão, o cheiro de fritura vai à sala, aberta para a '
                            'cozinha. Eletricista confere.'},
                   {'n': 3,
                    'nome': 'Serviço',
                    'dim': '1,59 x 2,09 m',
                    'resto': '',
                    'ideia': 'Torneira e ralo do lado de fora da porta, na faixa livre de 1,5 m ao lado da casa. O '
                             'encanador confere lugar e caimento.',
                    'cuid': 'Entre tanque e máquina, uns 91 cm: o caminho da cozinha ao quintal. Cesto e balde, só '
                            'em prateleira.'},
                   {'n': 4,
                    'nome': 'Banheiro',
                    'dim': '1,59 x 2,38 m',
                    'resto': '',
                    'ideia': 'Antes de fechar a parede, peça ao encanador o teste do encanamento e um registro só do '
                             'banheiro.',
                    'cuid': 'Tomada da pia: do lado mais longe do box; a distância, o eletricista confere.'},
                   {'n': 5,
                    'nome': 'Corredor',
                    'dim': '6,49 x 0,98 m',
                    'resto': '',
                    'ideia': 'Luz do corredor com interruptores paralelos: acende na sala, apaga perto do banheiro. '
                             'O eletricista confere.',
                    'cuid': 'Estante de 30 cm de fundo derruba a passagem de 98 cm para 68 cm. Aqui, corredor não '
                            'vira depósito.'},
                   {'n': 6,
                    'nome': 'Quarto casal',
                    'dim': '2,62 x 3,29 m',
                    'resto': '',
                    'ideia': 'O guarda-roupa de 6 portas não cabe. O de 4 portas cabe, e um maleiro em cima dele, '
                             'até o teto, compensa.',
                    'cuid': 'Queen cabe só no limite: 64 cm no pé e 7 cm sobrando com os criados. Meça antes de '
                            'comprar.'},
                   {'n': 7,
                    'nome': 'Quarto 3 (o do canto, atrás do banheiro)',
                    'dim': '2,62 x 3,29 m',
                    'resto': '',
                    'ideia': 'Estudo, escritório ou hóspede: tomada e internet na parede do quarto do meio, fora das '
                             'costas da tomada da cama de lá. Eletricista confere.',
                    'cuid': 'Guarda-roupa na parede do banheiro: impermeabilização do lado do banheiro e vão atrás '
                            'do móvel. O pedreiro confere.'},
                   {'n': 8,
                    'nome': 'Fundo do lote',
                    'dim': '10,0 x 3,7 m',
                    'resto': 'no lote de 10 x 15 (1,5 m no lote mínimo, de 10 x 12,8)',
                    'ideia': 'Com a rua ao sul, a melhor para esta casa, o fundo fica ao norte: o lado do sol, para '
                             'varal e horta.',
                    'cuid': 'Cômodo no fundo tapa a janela dos 3 quartos. Ampliar pede projeto novo do arquiteto.'}],
         'perguntas': [('Ao engenheiro:',
                        'a sala é aberta para a cozinha e o corredor, sem parede entre eles: onde passam as vigas, e '
                        'o ponto de luz da mesa fica livre delas? A janela de 2,40 m leva verga e contraverga?',
                        [1]),
                       ('Ao engenheiro:',
                        'os canos da pia, do banheiro e do serviço descem num trecho só, na parede comum dos três?',
                        [2, 3, 4]),
                       ('Ao eletricista:',
                        'a máquina tem circuito próprio? O circuito do serviço e do banheiro tem DR?',
                        [3, 4])],
         'alvenaria': 'Se a sua casa for de alvenaria estrutural, parede não se corta depois: nicho, cano e fio só '
                      'onde o projeto previu. Quem diz é o engenheiro.'}}
