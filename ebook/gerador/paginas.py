"""Textos e modelos de cada página do e-book. Cada função devolve uma lista de páginas em HTML.

Os campos entre [colchetes] dependem das decisões do painel (PAINEL.md, seção 9) ou da
validação do arquiteto: aparecem destacados em amarelo no PDF até alguém preencher.
"""
import re
from html import escape

# ------------------------------------------------------------------ textos fixos
AVISO_CURTO = ("Planta de referência, não é projeto executivo. Medidas de referência e móveis ilustrativos. "
               "Para construir, a obra precisa de responsável técnico (arquiteto ou engenheiro).")

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

PARA_QUEM_PADRAO = {
    "C": "Quem vai construir a primeira casa com orçamento curto.",
    "E": "Quem tem lote estreito, de 5 a 8 m de frente.",
    "F": "Família com filhos que precisa de 3 ou 4 quartos.",
    "S": "Quem precisa de um uso ou de um terreno específico.",
    "O": "Quem tem lote pequeno e quer separar a área social dos quartos.",
}

CUIDADOS_PADRAO = [
    "Confira os recuos da sua prefeitura para o seu lote.",
    "Veja de que lado nasce o sol no seu terreno: o ideal é o sol da manhã nos quartos.",
    "A obra precisa de um profissional habilitado (arquiteto ou engenheiro).",
]

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
     "Deixe livre o lado por onde a casa vai crescer, sem caixa d'água, fossa ou banheiro no caminho. "
     "Converse com o engenheiro para a estrutura já ficar pronta para isso."),
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


# ------------------------------------------------------------------ utilidades
def ph(texto):
    """Destaca campos [entre colchetes] para ninguém esquecer de preencher."""
    return re.sub(r"\[[^\]]+\]", lambda m: f'<span class="ph">{m.group(0)}</span>', texto)


def md(texto):
    """Markdown mínimo das fichas: **negrito** e escape de HTML."""
    t = escape(texto)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    return ph(t)


def pagina(conteudo, classe="", rodape=True, aviso=None):
    pe = ""
    if rodape:
        pe = (f'<footer class="rodape"><span class="aviso">{aviso or ""}</span>'
              f'<span class="num">{{{{NUM}}}}</span></footer>')
    return f'<section class="pagina {classe}">{conteudo}{pe}</section>'


def pg(ctx, chave):
    n = ctx.get("inicio", {}).get(chave)
    return str(n) if n else "?"


def numero_quartos(q):
    return q if not q.isdigit() else q


# ------------------------------------------------------------------ 1. capa
def capa(ctx):
    c = ctx["config"]
    p = ctx.get("capa")
    img = f'<div class="imagem"><img src="{p["imagens"]["02"]}" alt=""></div>' if p else ""
    leg = f'<div class="legenda">Na capa: {p["id"]} · {escape(p["nome"])}, {p["area"]}, planta humanizada.</div>' if p else ""
    html = f"""
    <div class="grade"></div>
    <div class="texto">
      <div class="sobretitulo">E-book de plantas de casas</div>
      <h1>{ph(escape(ctx['titulo']))}</h1>
      <div class="sub">{escape(c['subtitulo'])}. Blueprint, planta humanizada e 3D de cada casa,
      para você escolher a planta certa para o seu terreno antes de gastar com projeto.</div>
      <div class="selo">{ph(ctx['n_plantas'])} plantas originais</div>
    </div>
    {img}{leg}"""
    return [pagina(html, "capa", rodape=False)]


# ------------------------------------------------------------------ 2. capa interna
def capa_interna(ctx):
    c = ctx["config"]
    itens = [
        ("Como usar este e-book", "como_usar"),
        ("Como ler uma planta", "como_ler"),
        ("Os 7 erros que saem caro", "erros"),
        ("Índice rápido das plantas", "indice"),
        ("As plantas", ctx["entram"][0]["id"] if ctx["entram"] else ""),
        ("Terreno e recuos", "terreno"),
        ("Próximos passos", "proximos"),
        ("Bônus", "bonus"),
    ]
    sumario = "".join(f'<li><span>{t}</span><span class="pontos"></span><span class="pg">{pg(ctx, k)}</span></li>'
                      for t, k in itens)
    rascunho = ""
    if not ctx["completo"]:
        rascunho = (f'<div class="caixa amarela"><strong>Rascunho.</strong> Este PDF tem {ctx["n_entram"]} de '
                    f'{ctx["n_previstas"]} plantas previstas para o {c["lancamento_atual"]}º lançamento. '
                    f'Ele se completa sozinho conforme as plantas ganham 3D.</div>')
    html = f"""
    <div class="sobretitulo">Antes de começar</div>
    <h1>Leia isto primeiro</h1>
    <div class="caixa amarela" style="margin-top:6mm">{AVISO_COMPLETO}
      <p class="pequeno" style="margin:0">{ph('[Texto a confirmar com um arquiteto antes do lançamento.]')}</p>
    </div>
    <h2>Sumário</h2>
    <ul class="sumario">{sumario}</ul>
    {rascunho}
    <p class="pequeno" style="position:absolute;left:16mm;right:16mm;bottom:20mm">
      {ph(escape(ctx['titulo']))} · {c['lancamento_atual']}º lançamento · © {c['ano']}.
      Plantas originais, desenhadas para este e-book. Uso pessoal: proibida a reprodução, a revenda e o uso
      das plantas para fins comerciais sem autorização. Quem compra recebe os próximos lançamentos sem pagar de novo.
    </p>"""
    return [pagina(html)]


# ------------------------------------------------------------------ 3. como usar
def como_usar(ctx):
    html = f"""
    <div class="sobretitulo">Parte 1</div>
    <h1>Como usar este e-book</h1>
    <p class="abertura">Três perguntas filtram as plantas que servem para você. Responda nesta ordem:
    primeiro o terreno, depois a família, por último o bolso.</p>

    <div class="caixa azul">
      <h3>1. Qual é o tamanho do seu terreno?</h3>
      <p>Meça a <strong>frente</strong> (o lado da rua) e o <strong>fundo</strong>. No índice rápido, cada
      planta tem o <strong>lote mínimo</strong>: ela serve se a frente e o fundo do seu lote forem iguais ou
      maiores que os dela.</p>
      <table>
        <tr><th>Frente do lote</th><th>Comece por</th></tr>
        <tr><td>5 a 8 m</td><td>Terreno estreito (E) e sobrados (O)</td></tr>
        <tr><td>8 a 10 m</td><td>Compactas (C) e terreno estreito (E)</td></tr>
        <tr><td>10 a 12 m</td><td>Compactas (C), família (F) e especiais (S)</td></tr>
        <tr><td>12 m ou mais</td><td>Família (F) e especiais (S)</td></tr>
      </table>
      <p class="pequeno" style="margin:0">O lote mínimo é uma indicação. Os recuos da sua cidade podem pedir
      um lote maior: confira na seção Terreno e recuos (página {pg(ctx, 'terreno')}).</p>
    </div>

    <div class="caixa azul">
      <h3>2. Quantas pessoas vão morar na casa?</h3>
      <table>
        <tr><th>Quem mora</th><th>Quartos</th><th>Onde procurar</th></tr>
        <tr><td>1 ou 2 pessoas</td><td>studio ou 1</td><td>Compactas (C02, C03)</td></tr>
        <tr><td>Casal com 1 ou 2 filhos</td><td>2</td><td>Compactas (C) e terreno estreito (E)</td></tr>
        <tr><td>Família maior ou com avós</td><td>3 ou 4</td><td>Família (F) e Casa Multigeração (S10)</td></tr>
        <tr><td>Quem trabalha em casa</td><td>2 + escritório</td><td>Casa Home Office (S04)</td></tr>
      </table>
    </div>

    <div class="caixa azul">
      <h3>3. Quanto você pode gastar na obra?</h3>
      <p>Para uma primeira ideia, multiplique a área da planta pelo <strong>CUB</strong> (Custo Unitário
      Básico da construção), que o Sinduscon de cada estado publica todo mês:</p>
      <p style="font-size:12pt;font-weight:700;color:var(--azul)">área da planta (m²) × CUB do seu estado (R$/m²) = estimativa inicial</p>
      <p class="pequeno" style="margin:0">O CUB não inclui terreno, projetos, fundação especial, taxas e muro.
      A obra real costuma custar mais. O orçamento de verdade sai dos projetos, com o profissional.</p>
    </div>

    <h3>Depois das três perguntas</h3>
    <p>Marque no índice rápido (página {pg(ctx, 'indice')}) as plantas que passaram nos três filtros, leia a
    página dupla de cada uma e leve as duas ou três preferidas para conversar com um arquiteto ou engenheiro.</p>"""
    return [pagina(html)]


# ------------------------------------------------------------------ 4. como ler uma planta
SIMBOLOS = [
    ("Parede", '<rect x="20" y="34" width="120" height="12" fill="none" stroke="#fff" stroke-width="2"/>'),
    ("Porta: o arco mostra para que lado ela abre",
     '<line x1="20" y1="60" x2="55" y2="60" stroke="#fff" stroke-width="3"/><line x1="105" y1="60" x2="140" y2="60" stroke="#fff" stroke-width="3"/>'
     '<line x1="55" y1="60" x2="55" y2="12" stroke="#fff" stroke-width="2"/><path d="M55 12 A48 48 0 0 1 103 60" fill="none" stroke="#fff" stroke-width="1.5"/>'),
    ("Janela: linhas finas dentro da parede",
     '<rect x="20" y="34" width="120" height="12" fill="none" stroke="#fff" stroke-width="2"/>'
     '<rect x="50" y="34" width="60" height="12" fill="#0B4FA8" stroke="#fff" stroke-width="1"/>'
     '<line x1="50" y1="40" x2="110" y2="40" stroke="#fff" stroke-width="1"/>'),
    ("Cota: medida em metros",
     '<line x1="20" y1="44" x2="140" y2="44" stroke="#fff" stroke-width="1.5"/><line x1="14" y1="50" x2="26" y2="38" stroke="#fff" stroke-width="1.5"/>'
     '<line x1="134" y1="50" x2="146" y2="38" stroke="#fff" stroke-width="1.5"/><text x="80" y="34" fill="#fff" font-size="14" font-family="Inter,Arial" text-anchor="middle">3,00 m</text>'),
]

# Posições (em % da imagem) das marcas sobre o blueprint da planta usada como exemplo (C01).
MARCAS_C01 = [(57, 4.8), (36, 18), (52, 10), (34, 47), (27, 30), (34, 77), (14, 89.5)]
LEGENDA_LEITURA = [
    ("Cotas", "As medidas da casa por fora das paredes, em metros. Aqui, 6,50 m de frente e 8,50 m de fundo."),
    ("Porta", "O arco mostra para que lado a folha abre. Confira se ela não bate em móvel."),
    ("Janela", "O trecho da parede com linhas finas. A largura dela aparece na cota."),
    ("Parede", "A faixa escura. Nas contas do e-book, a externa tem 15 cm e a interna 12 cm."),
    ("Nome e área do cômodo", "A área livre, por dentro das paredes, em m². Compare com o seu cômodo de hoje."),
    ("Móveis", "Desenhados em escala, para mostrar que a cama, o sofá e a mesa cabem."),
    ("Ficha", "Nome da planta, área total, quartos e banheiros."),
    ("A casa em 3D", "A mesma planta com paredes e móveis, vista de cima e sem telhado, na página de cada casa."),
    ("Sol", "Em cada casa testamos as quatro posições da rua em relação ao sol, numa conta simples. A ficha diz o melhor e o pior lado; o arquiteto confere para o clima da sua cidade."),
]


def como_ler(ctx):
    exemplo = next((p for p in ctx["entram"] if p["id"] == "C01"), None)
    if exemplo:
        marcas = "".join(f'<span class="marca" style="left:{x}%;top:{y}%">{i}</span>'
                         for i, (x, y) in enumerate(MARCAS_C01, start=1))
        fig = f'<div class="fig"><img src="{exemplo["imagens"]["01"]}" alt="">{marcas}</div>'
    else:
        fig = '<div class="fig caixa azul">[blueprint de exemplo]</div>'
    legenda = "".join(f'<li><span class="n">{i}</span><span><strong>{t}.</strong> {d}</span></li>'
                      for i, (t, d) in enumerate(LEGENDA_LEITURA, start=1))
    simbolos = "".join(f'<div class="simbolo"><svg viewBox="0 0 160 80">{s}</svg>{t}</div>' for t, s in SIMBOLOS)
    p1 = f"""
    <div class="sobretitulo">Parte 2</div>
    <h1>Como ler uma planta</h1>
    <p class="abertura">Toda planta deste e-book vem em duas versões: o <strong>blueprint</strong> azul, com as
    medidas, e a <strong>planta humanizada</strong>, com móveis e pisos. Comece pelo blueprint.</p>
    <div class="leitura">{fig}<ol class="legenda-leitura">{legenda}</ol></div>
    <h2>Os símbolos</h2>
    <div class="simbolos">{simbolos}</div>
    <p class="pequeno" style="margin-top:4mm">Na planta, a frente da casa (lado da rua) fica no alto da página.
    O 3D e a planta humanizada mostram a mesma casa, na mesma posição.</p>"""
    termos = "".join(f'<div><dt>{t}</dt><dd>{d}</dd></div>' for t, d in GLOSSARIO)
    p2 = f"""
    <div class="sobretitulo">Parte 2 · continuação</div>
    <h1>Glossário</h1>
    <p class="abertura">As palavras que aparecem nas plantas, na prefeitura e na conversa com o arquiteto.</p>
    <dl class="glossario">{termos}</dl>"""
    return [pagina(p1), pagina(p2)]


# ------------------------------------------------------------------ 5. os 7 erros
def _erro(i, t, porque, certo, exemplos):
    ex = ""
    if exemplos:
        ex = '<p class="pequeno" style="margin-top:1mm">Veja nas plantas: ' + ", ".join(exemplos) + ".</p>"
    return (f'<div class="erro{" ultimo" if i == 7 else ""}"><div class="n">{i}</div><div>'
            f'<h3>{"O mais caro: " if i == 7 else ""}{t}</h3><p>{porque}</p>'
            f'<p class="certo"><strong>O jeito certo:</strong> {certo}</p>{ex}</div></div>')


def sete_erros(ctx):
    exemplos = {i: [] for i in range(1, 8)}
    for p in ctx["entram"]:
        for n, _ in p["ficha"]["erros"]:
            if n in exemplos:
                exemplos[n].append(f'{p["id"]} {escape(p["nome"])} (p. {ctx["paginas_plantas"].get(p["id"], "?")})')
    blocos = [_erro(i, *e, exemplos[i]) for i, e in enumerate(ERROS, start=1)]
    p1 = f"""
    <div class="sobretitulo">Parte 3</div>
    <h1>Os 7 erros que saem caro</h1>
    <p class="abertura">Os mesmos do vídeo, com o jeito certo. Cada planta deste e-book mostra, na página dela,
    quais desses erros ela evita.</p>
    {''.join(blocos[:4])}"""
    p2 = f"""
    <div class="sobretitulo">Parte 3 · continuação</div>
    {''.join(blocos[4:])}
    <div class="caixa amarela" style="margin-top:5mm"><strong>Use como lista de conferência.</strong> Antes de
    fechar a sua planta, com ou sem arquiteto, passe pelos 7 itens. Cada um que você confere agora é uma parede
    que não vai ser quebrada depois.</div>"""
    return [pagina(p1), pagina(p2)]


# ------------------------------------------------------------------ 6. índice rápido
def indice(ctx, linhas_por_pagina=24):
    lanc = ctx["config"]["lancamento_atual"]
    blocos, atual = [], None
    for p in ctx["plantas"]:
        if p["letra"] != atual:
            atual = p["letra"]
            blocos.append(("cat", p))
        blocos.append(("planta", p))
    # Distribui as linhas pelas páginas, sem deixar título de categoria sozinho no fim
    paginas_linhas, pag = [], []
    for i, b in enumerate(blocos):
        limite = linhas_por_pagina - (1 if b[0] == "cat" else 0)
        if len(pag) >= limite:
            paginas_linhas.append(pag)
            pag = []
        pag.append(b)
    if pag:
        paginas_linhas.append(pag)

    def linha(b):
        tipo, p = b
        if tipo == "cat":
            return f'<tr class="categoria"><td colspan="7">{p["letra"]}. {escape(p["categoria"])}</td></tr>'
        n = ctx["paginas_plantas"].get(p["id"])
        if n:
            onde = f'<span class="etiqueta aqui">p. {n}</span>'
        elif p["lancamento"] <= lanc:
            onde = '<span class="etiqueta">em produção</span>'
        else:
            onde = f'<span class="etiqueta">{p["lancamento"]}º lançamento</span>'
        nome = f'<strong>{escape(p["nome"])}</strong>' if n else escape(p["nome"])
        return (f'<tr><td>{p["id"]}</td><td>{nome}</td><td class="num">{p["area"]}</td><td>{p["quartos"]}</td>'
                f'<td>{p["banheiros"]}</td><td class="num">{p["lote"]} m</td><td>{onde}</td></tr>')

    cab = ('<tr><th>ID</th><th>Planta</th><th class="num">Área</th><th>Quartos</th><th>Banh.</th>'
           '<th class="num">Lote mín.</th><th>Página</th></tr>')
    saida = []
    for i, linhas in enumerate(paginas_linhas):
        topo = ("""<div class="sobretitulo">Parte 4</div><h1>Índice rápido</h1>
        <p class="abertura">Todas as plantas, por categoria. As que estão neste PDF têm o número da página;
        as outras chegam nos próximos lançamentos, sem custo para quem já comprou.</p>"""
                if i == 0 else '<div class="sobretitulo">Parte 4 · continuação</div>')
        saida.append(pagina(f'{topo}<table>{cab}{"".join(linha(b) for b in linhas)}</table>'
                            '<p class="pequeno">Lote mínimo = frente x fundo, em metros. Confira os recuos da sua '
                            'cidade antes de escolher.</p>'))
    return saida


# ------------------------------------------------------------------ 7. página dupla da planta
def _dados(p):
    def d(valor, rotulo, classe=""):
        return f'<div class="dado {classe}"><div class="valor">{valor}</div><div class="rotulo">{rotulo}</div></div>'
    quartos = p["quartos"]
    return "".join([
        d(p["area"], "área construída"),
        d(quartos, "quartos" if quartos != "1" else "quarto"),
        d(p["banheiros"], "banheiros" if p["banheiros"] not in ("1", "1 cada") else "banheiro"),
        d(f'{p["lote"]} m', "lote mínimo"),
        d(escape(p["destaque"]), "destaque", "destaque"),
    ])


def _cabecalho(p, cont=False):
    return (f'<div class="cabecalho-planta"><div><span class="id">{p["id"]}</span><h1>{escape(p["nome"])}</h1></div>'
            f'<div class="cat">{p["letra"]}. {escape(p["categoria"])}{" · continuação" if cont else ""}</div></div>')


def pagina_dupla(p, ctx, gratis=False):
    f = p["ficha"]
    erros = ""
    if f["erros"]:
        itens = "".join(f'<li><span class="n">{n}</span><span><strong>{ERROS[n - 1][0]}:</strong> {md(t)}</span></li>'
                        for n, t in f["erros"] if 1 <= n <= 7)
        erros = f'<div><h2>Erros que esta planta evita</h2><ul class="erros-evita">{itens}</ul></div>'
    else:
        erros = '<div><h2>Erros que esta planta evita</h2><p>[erros que evita]</p></div>'
    esquerda = f"""
    {_cabecalho(p)}
    <div class="topo">
      <div class="principal"><img src="{p['imagens']['02']}" alt="Planta humanizada"></div>
      <div class="ficha">{_dados(p)}</div>
    </div>
    <div class="baixo">
      <div><h2>Para quem é</h2><p>{md(f['para_quem'])}</p></div>
      {erros}
    </div>"""

    por_que = "".join(f"<li>{md(t)}</li>" for t in f["por_que"])
    cuidados = "".join(f"<li>{md(t)}</li>" for t in f["cuidados"])
    if gratis:
        c = ctx["config"]
        fim = (f'<div class="chamada">{ph("Essa é 1 das " + ctx["n_plantas"] + " plantas do e-book " + escape(c["titulo"]) + ".")} '
               f'Me conta o tamanho do seu terreno que eu te mostro quais cabem nele.</div>')
    else:
        if p.get("qr"):
            qr = f'<div class="qr ok"><img src="{p["qr"]}" alt="QR code"></div>'
        else:
            qr = f'<div class="qr">{ph("[QR code da animação]")}</div>'
        fim = (f'<div class="animacao">{qr}<div><strong>Veja a casa ganhar vida.</strong> Aponte a câmera do '
               f'celular para o código e assista à animação de 12 segundos: o blueprint se desenha, as paredes '
               f'sobem e a casa aparece mobiliada.</div></div>')
    direita = f"""
    {_cabecalho(p, cont=True)}
    <div class="imagens">
      <div><div class="blueprint"><img src="{p['imagens']['01']}" alt="Blueprint"></div>
        <div class="rotulo-img">Blueprint com cotas, em metros</div></div>
      <div class="perspectivas">
        <div class="persp"><img src="{p['imagens']['03']}" alt="Perspectiva 3D"></div>
        <div class="persp"><img src="{p['imagens']['04']}" alt="Perspectiva 3D lateral"></div>
      </div>
    </div>
    <div class="textos">
      <div><h2>Por que essa planta funciona</h2><ul class="por-que">{por_que}</ul></div>
      <div><h2>Cuidados antes de construir</h2><ul class="check">{cuidados}</ul></div>
    </div>
    {fim}"""
    return [pagina(esquerda, "planta-esq", aviso=AVISO_CURTO), pagina(direita, "planta-dir", aviso=AVISO_CURTO)]


# ------------------------------------------------------------------ páginas de encaixe
def enchimento(ctx, posicao):
    """Página útil usada quando uma página dupla precisa começar numa página par."""
    if not ctx.get("_guia_planta"):
        ctx["_guia_planta"] = True
        html = """
        <div class="sobretitulo">As plantas</div>
        <h1>Como ler a página de cada planta</h1>
        <p class="abertura">Cada planta ocupa duas páginas, lado a lado. Abra o PDF em visualização de duas
        páginas (ou imprima frente e verso) para ver as duas juntas.</p>
        <div class="duas-colunas">
          <div class="caixa azul"><h3>Página da esquerda</h3><ul>
            <li>Nome e ID da planta (ex.: C01).</li>
            <li>Planta humanizada grande: os móveis mostram o uso de cada cômodo.</li>
            <li>Ficha: área, quartos, banheiros e lote mínimo.</li>
            <li>Para quem é e os erros que ela evita.</li></ul></div>
          <div class="caixa azul"><h3>Página da direita</h3><ul>
            <li>Blueprint com as medidas.</li>
            <li>Duas perspectivas 3D, de lados opostos.</li>
            <li>Por que a planta funciona e os cuidados antes de construir.</li>
            <li>QR code da animação.</li></ul></div>
        </div>
        <div class="caixa amarela"><strong>Leve para o arquiteto.</strong> Anote o ID da planta que você gostou.
        Com ele, o profissional entende de cara o tamanho, a distribuição e o estilo de casa que você quer.</div>"""
        return [pagina(html)]
    html = '<div class="sobretitulo">Anotações</div><h1>Minhas anotações</h1><div class="anotacoes"></div>'
    return [pagina(html)]


# ------------------------------------------------------------------ 8. terreno e recuos
LOTE_SVG = """
<svg viewBox="0 0 400 520" xmlns="http://www.w3.org/2000/svg" font-family="Inter,Arial" font-size="13">
  <rect x="0" y="0" width="400" height="520" rx="10" fill="#0B4FA8"/>
  <text x="200" y="26" fill="#FFC857" font-weight="700" text-anchor="middle">RUA</text>
  <rect x="60" y="40" width="280" height="440" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="6 4"/>
  <rect x="102" y="152" width="238" height="244" fill="rgba(255,200,87,.25)" stroke="#FFC857" stroke-width="2"/>
  <rect x="140" y="170" width="182" height="238" fill="rgba(255,255,255,.18)" stroke="#fff" stroke-width="2"/>
  <text x="231" y="285" fill="#fff" font-weight="700" text-anchor="middle">C01</text>
  <text x="231" y="302" fill="#fff" text-anchor="middle" font-size="11">6,50 x 8,50 m</text>
  <line x1="200" y1="40" x2="200" y2="152" stroke="#FFC857" stroke-width="1.5"/>
  <text x="206" y="100" fill="#FFC857">recuo frontal 4 m</text>
  <line x1="60" y1="300" x2="102" y2="300" stroke="#FFC857" stroke-width="1.5"/>
  <text x="81" y="290" fill="#FFC857" text-anchor="middle" font-size="11">1,5 m</text>
  <line x1="200" y1="396" x2="200" y2="480" stroke="#FFC857" stroke-width="1.5"/>
  <text x="206" y="445" fill="#FFC857">fundos 3 m</text>
  <text x="200" y="505" fill="#fff" text-anchor="middle" font-size="12">Lote 10 x 20 m · área livre para construir em amarelo</text>
  <text x="70" y="62" fill="#fff" font-size="11">divisa</text>
</svg>"""


def terreno(ctx):
    p1 = f"""
    <div class="sobretitulo">Parte 5</div>
    <h1>Terreno e recuos</h1>
    <p class="abertura">A planta só serve se couber nas regras do seu lote. Confira isto <strong>antes</strong>
    de escolher, não depois de pagar o projeto.</p>
    <div class="duas-colunas">
      <div>
        <h3>O que a prefeitura define para o seu lote</h3>
        <ul>
          <li><strong>Recuos:</strong> distância mínima da casa até a rua, os vizinhos e os fundos.</li>
          <li><strong>Taxa de ocupação:</strong> quanto do lote a casa pode cobrir.</li>
          <li><strong>Coeficiente de aproveitamento:</strong> quanto se pode construir no total.</li>
          <li><strong>Taxa de permeabilidade:</strong> quanto do lote fica sem piso.</li>
          <li><strong>Uso permitido:</strong> se pode casa, comércio, duas casas no mesmo lote.</li>
        </ul>
        <h3>Onde descobrir</h3>
        <ul>
          <li>No <strong>Plano Diretor</strong>, na <strong>lei de zoneamento</strong> (uso e ocupação do solo)
          e no <strong>código de obras</strong> da sua cidade, quase sempre no site da prefeitura.</li>
          <li>Melhor ainda: peça na prefeitura a <strong>consulta prévia</strong> do seu lote (o nome muda de
          cidade para cidade: certidão de uso do solo, informação básica, viabilidade). Leve o número da
          matrícula ou do IPTU.</li>
          <li>Em <strong>condomínio ou loteamento</strong>, leia também o regulamento: ele costuma ter regras
          próprias, mais rígidas que as da prefeitura.</li>
          <li>O <strong>Código Civil</strong> (art. 1.301) proíbe abrir janela, terraço ou varanda a menos de
          1,5 m da divisa com o vizinho.</li>
        </ul>
      </div>
      <div class="lote-fig">{LOTE_SVG}
        <p class="pequeno" style="margin-top:2mm"><strong>Exemplo, com números fictícios.</strong> Lote de
        10 x 20 m com recuo frontal de 4 m, lateral de 1,5 m de um lado e 3 m nos fundos: sobram
        8,5 x 13 m = 110,5 m² para a casa. A Casa Compacta (6,50 x 8,50 m) cabe com folga.
        Os números do seu lote são os da sua prefeitura.</p>
      </div>
    </div>
    <div class="caixa amarela"><strong>A conta que você faz em casa:</strong> (frente − recuos laterais) ×
    (fundo − recuo frontal − recuo de fundos) = espaço para a casa. Se a planta escolhida não couber nesse
    retângulo, procure outra no índice rápido.</div>"""

    campos = ["Endereço do lote", "Frente (m)", "Fundo (m)", "Área do lote (m²)", "Recuo frontal (m)",
              "Recuos laterais (m)", "Recuo de fundos (m)", "Taxa de ocupação (%)", "Taxa de permeabilidade (%)",
              "Lado do nascente (leste)", "Regras do condomínio", "Plantas que cabem (IDs)"]
    linhas = "".join(f"<div>{c}</div>" for c in campos)
    p2 = f"""
    <div class="sobretitulo">Parte 5 · continuação</div>
    <h1>Ficha do meu terreno</h1>
    <p class="abertura">Preencha com os dados da prefeitura e leve junto quando for conversar com o arquiteto.</p>
    <div class="linhas-preencher">{linhas}</div>
    <h2>Antes de comprar um terreno</h2>
    <ul>
      <li>Escolha a casa primeiro e procure um lote em que ela caiba, com os recuos.</li>
      <li>Veja a posição do sol: lote com a frente para o sul deixa o fundo (e o quintal) com sol.</li>
      <li>Pergunte se o lote tem água, esgoto e luz na rua: ligar de longe custa caro.</li>
      <li>Terreno em declive pede fundação e muro de arrimo: peça uma avaliação do engenheiro.</li>
    </ul>"""
    return [pagina(p1), pagina(p2)]


# ------------------------------------------------------------------ 9. próximos passos
def proximos_passos(ctx):
    passos = [
        ("Escolha 2 ou 3 plantas", "Use o índice rápido e as três perguntas da parte 1. Anote os IDs."),
        ("Confira as regras do seu lote", "Faça a consulta prévia na prefeitura e preencha a ficha do terreno."),
        ("Contrate um profissional habilitado",
         "Arquiteto (registrado no CAU) ou engenheiro civil (registrado no CREA). Ele adapta a planta ao "
         "seu terreno, ao sol e às regras da cidade, e emite a RRT ou a ART da obra."),
        ("Aprove o projeto na prefeitura", "Com o projeto legal aprovado, a prefeitura emite o alvará de construção."),
        ("Faça os projetos complementares e o orçamento",
         "Estrutural, elétrico e hidráulico. Com eles, o orçamento deixa de ser estimativa."),
        ("Construa com acompanhamento", "A obra precisa de responsável técnico do começo ao fim."),
        ("Regularize a casa pronta",
         "Peça o habite-se na prefeitura e averbe a construção na matrícula do imóvel, no cartório."),
    ]
    itens = "".join(f"<li><h3>{t}</h3><p>{d}</p></li>" for t, d in passos)
    html = f"""
    <div class="sobretitulo">Parte 6</div>
    <h1>Próximos passos</h1>
    <p class="abertura">Do e-book até a chave na mão. A ordem importa: cada passo evita retrabalho no seguinte.</p>
    <ol class="passos">{itens}</ol>
    <div class="caixa amarela"><h3>Responsabilidade técnica</h3>{AVISO_COMPLETO}
      <p class="pequeno" style="margin:0">{ph('[Texto a confirmar com um arquiteto antes do lançamento.]')}</p></div>"""
    return [pagina(html)]


# ------------------------------------------------------------------ 10. bônus
def bonus(ctx):
    c = ctx["config"]
    itens = "".join(f"<li>{ph(escape(b))}</li>" for b in c.get("bonus", []))
    html = f"""
    <div class="sobretitulo">Parte 7</div>
    <h1>Bônus</h1>
    <p class="abertura">O que vem junto com o e-book.</p>
    <div class="caixa azul"><ul>{itens}</ul></div>
    <h2>Próximos lançamentos</h2>
    <p>Este e-book cresce em levas. Quem compra agora recebe as próximas plantas sem pagar de novo: o índice
    rápido (página {pg(ctx, 'indice')}) mostra quais já estão a caminho.</p>
    <h2>Dúvidas</h2>
    <p>Fale com a gente pelo {ph(escape(c.get('contato', '[contato]')))}.</p>"""
    return [pagina(html)]
