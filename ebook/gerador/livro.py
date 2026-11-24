"""Gera o e-book (título em ebook/config.json: "Antes do primeiro tijolo"; PDF A4) a partir das plantas validadas.

Edição de lançamento: só as casas de "casas_lancamento" no config.json (lista vazia ou ausente = todas).
As outras continuam no projeto e no validador; contagens, índices e páginas saem das casas da edição.

Uso:
    python3 ebook/gerador/livro.py                 PDF em ebook/saida/ebook.pdf, as plantas grátis
                                                   (ebook/saida/planta-gratis-<ID>.pdf, as de config.json)
                                                   e a lista de casas da calculadora do parceiro
                                                   (ebook/vendas/calculadora-lote.html)
    python3 ebook/gerador/livro.py --previa DIR    salva um PNG de cada página em DIR; gera tudo numa pasta
                                                   temporária e NÃO mexe em ebook/saida nem na calculadora
    python3 ebook/gerador/livro.py --conferir      confere numa pasta temporária, sem mexer em ebook/saida
                                                   nem na calculadora

    python3 ebook/gerador/livro.py --previa DIR --duas-partes
                                                   prévia do e-book em duas partes (D17, 24/11/2026): casas pela frente
                                                   do lote; abertura, parte 1 (cada casa), parte 2 (casas em geral, com
                                                   a aba azul "geral"), fecho; sumário na página 2. Sem --previa, recusa.

O PDF oficial e a calculadora só são gravados sem --previa e sem --conferir.

Tudo sai dos dados: plantas e números de ebook/plantas/projetos.py (via ferramentas/plantas.py),
textos de cada casa de ebook/fichas/textos.py, textos gerais de ebook/gerador/paginas.py
(7 erros, glossário, terreno, próximos passos) e ebook/config.json (título, preço, bônus, contato).
Direção visual: a prévia em ebook/visual/plano-visual.html (resumo em ebook/EBOOK.md).
"""
import html
import json
import os
import re
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
EBOOK = AQUI.parent
RAIZ = EBOOK.parent
SAIDA = EBOOK / "saida"
sys.path.insert(0, str(RAIZ / "ferramentas"))
sys.path.insert(0, str(AQUI))
sys.path.insert(0, str(EBOOK / "fichas"))
import plantas as PL  # noqa: E402
import planta3d as P3  # noqa: E402
import math  # noqa: E402
import paginas as TX  # noqa: E402
import textos as FICHAS  # noqa: E402

E = html.escape
AVISO = "Planta de referência. O projeto para a prefeitura é assinado por arquiteto ou engenheiro habilitado."
CATEGORIAS = {"C": "Compactas", "E": "Terreno estreito", "F": "Família", "S": "Especiais"}
CORES = {"sala": "#E9D8BD", "estar": "#E9D8BD", "jantar": "#E9D8BD", "cozinha": "#D3E1CC", "servico": "#D9E5D1",
         "banho": "#CFE2E8", "lavabo": "#CFE2E8", "casal": "#EEDCC2", "dorm": "#F1E4CF", "circ": "#F4EFE6",
         "escritorio": "#E4DEF1", "varanda": "#E7E3DA", "garagem": "#DEDCD8", "patio": "#CFE3BB", "externo": "#CFE3BB"}
ABERTOS = {"varanda", "garagem", "patio", "externo"}
ORI = PL.ORI_NOME


def m(v):
    return f"{v:.2f}".replace(".", ",")


def m1(v):
    return f"{v:.1f}".replace(".", ",")


# ------------------------------------------------------------------ desenhos (SVG)
def _geometria(p):
    """Paredes, janelas, portas e móveis na posição de verdade, a mesma do 3D (P3.paredes_reais e P3.para_desenho):
    parede externa de 15 cm para dentro da face de fora, interna de 12 cm no eixo; a janela e a porta da parede externa
    vão junto, 7,5 cm para dentro. Paredes em caixas (x0, y0, x1, y1), em metros, frente em y=0 (24/11/2026)."""
    paredes, janelas, portas, moveis = P3.construir(p)
    caixas = [(a, f - e / 2, b, f + e / 2) if o == "h" else (f - e / 2, a, f + e / 2, b)
              for (o, f, a, b, e, _, _) in P3.paredes_reais(p, paredes)]
    _, janelas, portas = P3.para_desenho(p, paredes, janelas, portas)
    return caixas, janelas, portas, moveis


def _svg_paredes(caixas, Y, cor, extra=0, dx=0, dy=0):
    """As paredes como retângulos cheios (extra: borda a mais em volta, para o contorno da maquete)."""
    return (f'<g fill="{cor}">' + "".join(
        f'<rect x="{f3(x0 - extra / 2 + dx)}" y="{f3(Y(y1) - extra / 2 + dy)}" width="{f3(x1 - x0 + extra)}" height="{f3(y1 - y0 + extra)}"/>'
        for x0, y0, x1, y1 in caixas) + "</g>")


def svg_planta(p, nomes=True, cotas=True, pad=0.5, moveis=False, humanizada=False, estilo="revista"):
    """Planta com a frente da casa para baixo: o leitor entra por baixo, como chega da rua.
    humanizada=True: a planta humanizada com o entorno (svg_humanizada), no estilo "revista" ou "maquete".
    Sem ela, o desenho simples de cores chapadas (miniaturas da galeria e imagens2d.py)."""
    if humanizada:
        return svg_humanizada(p, estilo)
    fut = [c for c in p["comodos"] if c["tipo"] == "futuro"]
    Dm = max([p["D"]] + [c["y1"] for c in fut])
    Wm = max([p["W"]] + [c["x1"] for c in fut])
    pb = 1.1 if cotas else pad
    pl = 1.1 if cotas else pad
    Y = lambda y: Dm - y
    s = [f'<svg viewBox="{-pl} {-pad} {Wm + pl + pad} {Dm + pad + pb}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Planta da {E(p["nome"])}">']
    rotulos = []
    for c in p["comodos"]:
        x0, y0, x1, y1, t = c["x0"], c["y0"], c["x1"], c["y1"], c["tipo"]
        w, h = x1 - x0, y1 - y0
        if t == "futuro":
            s.append(f'<rect x="{x0}" y="{Y(y1)}" width="{w}" height="{h}" fill="#FFF6DE" stroke="#E0A92E" stroke-width=".06" stroke-dasharray=".25 .18"/>')
            s.append(f'<text x="{x0 + w / 2}" y="{Y(y0 + h / 2)}" text-anchor="middle" font-size=".28" font-weight="700" fill="#9A6B00">AMPLIAÇÃO</text>')
            s.append(f'<text x="{x0 + w / 2}" y="{Y(y0 + h / 2) + .36}" text-anchor="middle" font-size=".22" fill="#9A6B00">{E(c["nome"].split(" (")[0])}</text>')
            continue
        aberto = t in ABERTOS  # a parede do cômodo fechado vem depois, na posição de verdade (_geometria)
        s.append(f'<rect x="{x0}" y="{Y(y1)}" width="{w}" height="{h}" fill="{CORES.get(t, "#EEE")}"'
                 + (' stroke="#B9B3A8" stroke-width=".03"/>' if aberto else "/>"))
        if nomes and min(w, h) >= 1.15 and t not in ("circ", "externo"):
            nome = "PÁTIO" if t == "patio" else c["nome"].upper()
            fs = max(min(.34, (w - .2) / (len(nome) * .74)), .17)
            halo = 'stroke="#FBF8F2" stroke-width=".09" paint-order="stroke" stroke-linejoin="round"'
            rotulos.append(f'<text x="{x0 + w / 2}" y="{Y(y0 + h / 2) - .04}" text-anchor="middle" font-size="{fs:.3f}" font-weight="700" fill="#1E2733" {halo}>{E(nome)}</text>')
            if t not in ABERTOS:
                rotulos.append(f'<text x="{x0 + w / 2}" y="{Y(y0 + h / 2) + .3}" text-anchor="middle" font-size=".22" class="mono" fill="#56616E" {halo}>{m1(p["_r"].metricas["util"][c["id"]][2] if "_r" in p else w * h)} m²</text>')
    caixas, jan3d, portas_ext, mov = _geometria(p)
    if moveis:
        for mv in mov:
            rot = math.degrees(mv.get("rot", 0) or 0)
            s.append(f'<g transform="translate({mv["x"]:.3f} {Y(mv["y"]):.3f}) scale(1 -1) rotate({-rot:.2f})">{_movel(mv)}</g>')
    s.append(_svg_paredes(caixas, Y, "#2A3340"))  # o vão da porta já fica aberto na parede
    if moveis:
        for d in portas_ext:
            r = d["r"]
            (hx, hy), (ax, ay), (bx, by) = PL.porta_dobradica(p, d)  # dobradiça no canto (o arco do motor saía espelhado)
            sweep = 1 if (bx - hx) * (Y(ay) - Y(hy)) - (Y(by) - Y(hy)) * (ax - hx) > 0 else 0
            s.append(f'<path d="M{bx:.3f} {Y(by):.3f} A{r} {r} 0 0 {sweep} {ax:.3f} {Y(ay):.3f}" fill="none" stroke="#C2683F" stroke-width=".025" stroke-dasharray=".06 .04"/>')
            s.append(f'<line x1="{hx:.3f}" y1="{Y(hy):.3f}" x2="{bx:.3f}" y2="{Y(by):.3f}" stroke="#C2683F" stroke-width=".04"/>')
    # janelas e porta de entrada nas mesmas posições do motor 3D (a mesma da vista da rua e das imagens)
    for j in (j for j in jan3d if j.get("tipo") != "veneziana"):  # a veneziana vem depois da soleira
        x0s, y0s, x1s, y1s = j["seg"]
        if abs(y0s - y1s) < 1e-6:
            x, y, w, h = min(x0s, x1s), Y(y0s) - .07, abs(x1s - x0s), .14
        else:
            x, y, w, h = x0s - .07, Y(max(y0s, y1s)), .14, abs(y1s - y0s)
        s.append(f'<rect x="{x:.3f}" y="{y:.3f}" width="{w:.3f}" height="{h:.3f}" fill="#8ED2FF" stroke="#0B4FA8" stroke-width=".03"/>')
    # a porta de entrada em amarelo (a da seta ENTRADA, mesmo passando pela varanda); as outras para fora, soleira cinza
    ent = porta_de_entrada(p)["id"]
    for d in portas_ext:
        if d["id"] == ent:
            s.append(_soleira(p, d, Y, .2, "#FFC857", "entrada"))
        elif str(d["id"]).startswith("ext-"):
            s.append(_soleira(p, d, Y, .2, SOLEIRA_FORA, "fora"))
    if ent is None:
        s.append(_soleira_beira(p, Y, .2))
    s.extend(_veneziana(p, j, Y) for j in jan3d if j.get("tipo") == "veneziana")
    s.extend(rotulos)
    if cotas:
        s.append(f'<g stroke="#0B4FA8" stroke-width=".03" fill="#0B4FA8" font-size=".3" class="mono">'
                 f'<line x1="0" y1="{Dm + .5}" x2="{p["W"]}" y2="{Dm + .5}"/>'
                 f'<line x1="0" y1="{Dm + .38}" x2="0" y2="{Dm + .62}"/><line x1="{p["W"]}" y1="{Dm + .38}" x2="{p["W"]}" y2="{Dm + .62}"/>'
                 f'<text x="{p["W"] / 2}" y="{Dm + .92}" text-anchor="middle" stroke="none">{m(p["W"])} m</text>'
                 f'<line x1="-.5" y1="{Dm - p["D"]}" x2="-.5" y2="{Dm}"/>'
                 f'<text x="-.62" y="{Dm - p["D"] / 2}" text-anchor="middle" stroke="none" transform="rotate(-90 -.62 {Dm - p["D"] / 2})">{m(p["D"])} m</text></g>')
    s.append("</svg>")
    return "".join(s)



# ------------------------------------------------------------------ planta humanizada
# Decisão do dono (23/11/2026): estilo 1 (planta humanizada de revista) nas páginas das casas,
# estilo 3 (maquete sobre o papel azul) na capa e no Instagram. Tudo sai do validador e do motor 3D:
# paredes, portas, janelas e móveis nas mesmas posições da imagem 3D e da vista da rua.
f3 = lambda v: f"{v:.3f}"

CORES_MOVEIS = {"madeira": "#C99A6B", "madeira_esc": "#8A6040", "sofa": "#8FA58A", "sofa_esc": "#748C70", "almofada": "#F2C14E",
                "tapete": "#EFE4D2", "tapete_b": "#C7AE8A", "vaso_flor": "#E07A5F", "livro": "#3D6FB6", "cadeira": "#E9DCC6",
                "bancada": "#E6E2DC", "inox": "#CFD6DD", "inox_esc": "#A9B3BD", "geladeira": "#F4F6F8", "louca": "#FFFFFF",
                "agua": "#D6EBF5", "box": "#DCEFF6", "vidro": "#7FC3E8", "armario": "#F1E9DC", "luz": "#FFE3A1",
                "vaso_planta": "#B9774E", "folha": ["#5E9C4E", "#7DB55E", "#4A8540"], "folha_l": "#3F6E35", "carro": "#E2B1A8",
                "poltrona": "#E3C9A6", "manta_pe": "#E07A5F", "manta_pe_l": "#F6D1C3"}
PISO_REAL = {"madeira": ["#D8B184", "#D1A877", "#DDBA8F", "#CFA673"], "madeira_l": "#A87E51", "porc": "#EEEBE6", "porc_l": "#D2CBC0",
             "banho": "#E6F1F4", "banho_l": "#BFD6DD", "varanda": "#E5D3BE", "varanda_l": "#C9B091", "grama": "#BFDCA0",
             "grama_l": "#94BF6E", "calcada": "#E3E1DC", "calcada_l": "#C9C5BD"}
PISO = {"sala": "pMadeira", "estar": "pMadeira", "jantar": "pMadeira", "casal": "pMadeira", "dorm": "pMadeira", "circ": "pMadeira",
        "escritorio": "pMadeira", "cozinha": "pPorc", "servico": "pPorc", "banho": "pAzulejo", "lavabo": "pAzulejo",
        "varanda": "pVaranda", "garagem": "pCalcada", "patio": "pGrama", "externo": "pGrama"}


def _etiqueta_pilula(fundo, texto, sub):
    def f(cx, cy, lw, lh, nome, m2, fs, cor, linha=False):
        x, y = cx - lw / 2, cy - lh / 2
        if linha:  # uma linha só: nome à esquerda, área à direita (cômodo apertado)
            return (f'<rect x="{f3(x + .03)}" y="{f3(y + .05)}" width="{f3(lw)}" height="{f3(lh)}" rx=".12" fill="#000" opacity=".12"/>'
                    f'<rect x="{f3(x)}" y="{f3(y)}" width="{f3(lw)}" height="{f3(lh)}" rx=".12" fill="{fundo}"/>'
                    f'<rect x="{f3(x)}" y="{f3(y)}" width=".07" height="{f3(lh)}" rx=".035" fill="{cor}" stroke="#00000022" stroke-width=".005"/>'
                    f'<text x="{f3(x + .17)}" y="{f3(cy + fs * .36)}" font-size="{fs:.3f}" font-weight="800" letter-spacing=".01" fill="{texto}">{E(nome)}</text>'
                    f'<text x="{f3(x + lw - .1)}" y="{f3(cy + fs * .36)}" text-anchor="end" font-size=".16" class="mono" font-weight="700" fill="{sub}">{E(m2)}</text>')
        return (f'<rect x="{f3(x + .03)}" y="{f3(y + .05)}" width="{f3(lw)}" height="{f3(lh)}" rx=".14" fill="#000" opacity=".12"/>'
                f'<rect x="{f3(x)}" y="{f3(y)}" width="{f3(lw)}" height="{f3(lh)}" rx=".14" fill="{fundo}"/>'
                f'<rect x="{f3(x)}" y="{f3(y)}" width=".07" height="{f3(lh)}" rx=".035" fill="{cor}" stroke="#00000022" stroke-width=".005"/>'
                f'<text x="{f3(cx + .02)}" y="{f3(y + .1 + fs * .85)}" text-anchor="middle" font-size="{fs:.3f}" font-weight="800" letter-spacing=".01" fill="{texto}">{E(nome)}</text>'
                f'<text x="{f3(cx + .02)}" y="{f3(y + .1 + fs + .17)}" text-anchor="middle" font-size=".16" class="mono" font-weight="700" fill="{sub}">{E(m2)}</text>')
    return f


def _entrada_seta(cx, cy, px=None):
    """Seta ENTRADA em cx; a pílula do texto em px (perto da borda do desenho, ela chega para dentro)."""
    px = cx if px is None else px
    return (f'<g data-seta="entrada"><path d="M{f3(cx)} {f3(cy - .32)} l-.2 .22 h.12 v.3 h.16 v-.3 h.12 z" fill="#FFC857" stroke="#17202B" stroke-width=".015"/>'
            f'<rect x="{f3(px - .55)}" y="{f3(cy + .2)}" width="1.1" height=".24" rx=".12" fill="#FFC857" stroke="#17202B" stroke-width=".012"/>'
            f'<text x="{f3(px)}" y="{f3(cy + .365)}" text-anchor="middle" font-size=".14" font-weight="800" fill="#17202B" letter-spacing=".015">ENTRADA</text></g>')


# Portas para fora (24/11/2026): a página "Como ler uma planta" diz "a porta de entrada é amarela". Por isso só a porta
# por onde se entra na casa (a da seta ENTRADA, mesmo passando pela varanda) tem soleira e folha amarelas; as outras
# portas para fora (serviço, escritório, cozinha pela lateral) têm a soleira cinza de cimento. O checar.py conta: uma só.
SOLEIRA_FORA = "#A8A39A"


def porta_de_entrada(p):
    """A porta por onde se entra na casa: {"id": porta do motor 3D ou None, "lado": lado da porta da rua}.
    Da rua direto num cômodo fechado: "ext-<cômodo>". Da rua para varanda, garagem ou corredor aberto: a porta desse
    espaço para dentro da casa (sala primeiro). Passagem sem folha (varanda aberta para a sala): id None, e o desenho
    marca a beira da varanda onde o caminho chega. Porta da frente primeiro (a última, a mesma do _entrada_x do motor);
    sem porta na frente, a da lateral que dá na sala."""
    tipo = {c["id"]: c["tipo"] for c in p["comodos"]}
    social = ("sala", "estar", "jantar")
    ext = [q for q in p.get("portas", []) if q[0] == "ext"]
    frente = [q for q in ext if q[2] == "frente"]
    q = frente[-1] if frente else min(ext, key=lambda q: tipo[q[1]] not in social)
    alvo = q[1]
    if tipo[alvo] not in ABERTOS:
        return {"id": f"ext-{alvo}", "lado": q[2]}
    outro = lambda d: d[0] if d[1] == alvo else d[1]
    cands = [d for d in p.get("portas", []) if d[0] != "ext" and alvo in d[:2] and tipo[outro(d)] not in ABERTOS]
    if not cands:
        return {"id": None, "lado": q[2]}
    d = min(cands, key=lambda d: (len(d) > 2 and d[2] == "aberto", tipo[outro(d)] not in social))
    return {"id": None if len(d) > 2 and d[2] == "aberto" else f"{d[0]}-{d[1]}", "lado": q[2]}


def _soleira(p, d, Y, larg, cor, marca):
    """Soleira no vão da porta d (da dobradiça à ponta da folha fechada), com data-porta para o checar.py contar."""
    (hx, hy), (ax, ay), _ = PL.porta_dobradica(p, d)
    if abs(ay - hy) < 1e-6:
        x, y, w, h = min(hx, ax), Y(hy) - larg / 2, d["r"], larg
    else:
        x, y, w, h = hx - larg / 2, Y(max(hy, ay)), larg, d["r"]
    return (f'<rect data-porta="{marca}" x="{f3(x)}" y="{f3(y)}" width="{f3(w)}" height="{f3(h)}" fill="{cor}"'
            f' stroke="#17202B" stroke-width="{f3(larg * .12)}"/>')


def _veneziana(p, j, Y, cor="#0B4FA8"):
    """Veneziana em cima da porta de fora (j["tipo"] == "veneziana"): acima do corte da planta, então vai tracejada, como
    o arquiteto desenha o que fica no alto, com a palavra do lado de fora da parede (D1, 24/11/2026)."""
    x0, y0, x1, y1 = j["seg"]
    e, t = .2, .13  # meia largura do tracejado; tamanho da letra
    if abs(y0 - y1) < 1e-6:
        fora = 1 if y0 > p["D"] / 2 else -1  # para onde fica o lado de fora (y da planta)
        caixa = (min(x0, x1), Y(y0) - e / 2, abs(x1 - x0), e)
        tx, ty, rot = (x0 + x1) / 2, Y(y0 + fora * .3) + t / 3, 0
    else:
        fora = 1 if x0 > p["W"] / 2 else -1
        caixa = (x0 - e / 2, Y(max(y0, y1)), e, abs(y1 - y0))
        tx, ty, rot = x0 + fora * .3, Y((y0 + y1) / 2), -90
    x, y, w, h = caixa
    return (f'<rect x="{f3(x)}" y="{f3(y)}" width="{f3(w)}" height="{f3(h)}" fill="none" stroke="{cor}" stroke-width=".03" stroke-dasharray=".07 .05"/>'
            f'<text x="{f3(tx)}" y="{f3(ty)}" text-anchor="middle" font-size="{t}" font-weight="700" fill="{cor}" letter-spacing=".01"'
            f' transform="rotate({rot} {f3(tx)} {f3(ty)})">VENEZIANA</text>')


def _soleira_beira(p, Y, larg):
    """Entrada sem folha de porta (varanda aberta para a sala): a soleira amarela na beira da varanda, onde o caminho chega."""
    ex = p["_entrada_x"]
    return (f'<rect data-porta="entrada" x="{f3(ex - .45)}" y="{f3(Y(0) - larg / 2)}" width=".9" height="{f3(larg)}"'
            f' fill="#FFC857" stroke="#17202B" stroke-width="{f3(larg * .12)}"/>')


# 1) Humanizada de revista: pisos de verdade, móveis com sombra, jardim, etiqueta em pílula (páginas das casas)
EST_REVISTA = dict(nome="rv", linha="#5E5548", lw=.018, cor=CORES_MOVEIS, piso=PISO_REAL, rua="#9AA1AA", rua_txt="#4F5B69",
                   beiral="#9C8B76", sombra="rgba(40,30,20,.16)", parede="#2B2F36", janela_fundo="#FFFFFF", vidro="#5DB4E6",
                   arco="#8E8678", folha_porta="#8A5A3C", arvore=["#7DAF5C", "#8DBE69", "#6C9F4E", "#B5D88F"], cota="#0B4FA8",
                   escala="#17202B", etiqueta=_etiqueta_pilula("#FFFFFF", "#17202B", "#4F5B69"))
# 3) Maquete sobre o papel azul de projeto: paredes brancas com sombra (capa e Instagram)
EST_MAQUETE = dict(nome="mq", linha="#6B7380", lw=.014,
                   cor={**CORES_MOVEIS, "sofa": "#6F9FA0", "sofa_esc": "#4F8283", "almofada": "#FFC857", "madeira": "#C38E5D",
                        "tapete": "#F3EDE4", "tapete_b": "#D9C7AE", "manta_pe": "#0B4FA8", "manta_pe_l": "#7FA7DE"},
                   piso={**PISO_REAL, "madeira": ["#D9AE7C", "#CFA16C", "#E0B988", "#C99A65"], "grama": "#A9D38A", "grama_l": "#86BC63", "calcada": "#EDEBE7"},
                   manta_fixa=["#E9A27E", "#9DB8DD"], rua="#08397A", rua_txt="#DCE7F7", beiral="#8C7C68", sombra="rgba(20,30,50,.20)",
                   parede="#FFFFFF", parede_contorno="#4A5563", parede_sombra="rgba(5,20,45,.35)", janela_fundo="#BFE3FA",
                   vidro="#0B4FA8", arco="#A99F92", folha_porta="#9A6A44", arvore=["#6FA85A", "#86BE6A", "#5E9A4C", "#C3E3A0"],
                   cota="#FFC857", escala="#FFC857", sombra_lote="rgba(3,25,60,.35)", etiqueta=_etiqueta_pilula("#17202B", "#FFFFFF", "#FFC857"))
ESTILOS = {"revista": EST_REVISTA, "maquete": EST_MAQUETE}


def _movel(mv, S=None, sombra=False):
    """Móvel visto de cima, em coordenadas locais (cabeceira/encosto no lado -y). Com sombra=True, só a silhueta."""
    S = S or EST_REVISTA
    t, w, d = mv["tipo"], mv.get("w", .45), mv.get("d", .4)
    L, sw, K = S["linha"], S["lw"], S["cor"]

    def R(x, y, ww, hh, fill="#FFFFFF", rx=.04, extra=""):
        if sombra:
            return f'<rect x="{f3(x)}" y="{f3(y)}" width="{f3(ww)}" height="{f3(hh)}" rx="{rx}"/>'
        return f'<rect x="{f3(x)}" y="{f3(y)}" width="{f3(ww)}" height="{f3(hh)}" rx="{rx}" fill="{fill}" stroke="{L}" stroke-width="{sw}" {extra}/>'

    def C(x, y, r, fill="#FFFFFF", st=True):
        if sombra:
            return f'<circle cx="{f3(x)}" cy="{f3(y)}" r="{f3(r)}"/>'
        borda = f' stroke="{L}" stroke-width="{sw}"' if st else ""
        return f'<circle cx="{f3(x)}" cy="{f3(y)}" r="{f3(r)}" fill="{fill}"{borda}/>'

    def ln(x0, y0, x1, y1, cor=None, wd=None):
        if sombra:
            return ""
        return f'<line x1="{f3(x0)}" y1="{f3(y0)}" x2="{f3(x1)}" y2="{f3(y1)}" stroke="{cor or L}" stroke-width="{wd or sw * .7}" stroke-linecap="round"/>'

    if t in ("camaCasal", "camaSolteiro"):
        n = 2 if t == "camaCasal" else 1
        manta = S["manta_fixa"][n - 1] if S.get("manta_fixa") else mv.get("manta", "#B9C7D6")
        o = R(-w / 2 - .03, -d / 2 - .03, w + .06, d + .06, K["madeira_esc"], .05)   # estrado
        o += R(-w / 2, -d / 2, w, d, "#FFFFFF", .05)                                  # colchão
        o += R(-w / 2, -d / 2 + d * .34, w, d * .66, manta, .05)                      # edredom
        o += R(-w / 2, -d / 2 + d * .34, w, .12, "#FFFFFF", .03)                      # dobra do lençol
        o += R(-w / 2 + .04, d / 2 - .38, w - .08, .26, K["manta_pe"], .03)           # manta no pé
        o += ln(-w / 2 + .1, d / 2 - .25, w / 2 - .1, d / 2 - .25, K["manta_pe_l"], .018)
        lw = (w - .16) / n
        return o + "".join(R(-w / 2 + .08 + i * lw + .03, -d / 2 + .07, lw - .06, .32, "#FFFFFF", .08) for i in range(n))
    if t == "sofa":
        o = R(-w / 2, -d / 2, w, d, K["sofa"], .08)
        o += R(-w / 2 + .02, -d / 2 + .02, w - .04, .22, K["sofa_esc"], .06)
        o += R(-w / 2 + .02, -d / 2 + .02, .17, d - .04, K["sofa_esc"], .06) + R(w / 2 - .19, -d / 2 + .02, .17, d - .04, K["sofa_esc"], .06)
        k = 3 if w > 1.8 else 2
        cw = (w - .4) / k
        o += "".join(R(-w / 2 + .2 + i * cw + .015, -d / 2 + .26, cw - .03, d - .3, K["sofa"], .06) for i in range(k))
        return o + R(-w / 2 + .22, -d / 2 + .22, .3, .22, K["almofada"], .07, 'transform="rotate(-12)"')
    if t == "rack":  # rack com a TV (a faixa escura), como na imagem 3D
        return R(-w / 2, -d / 2, w, d, K["madeira"], .03) + R(-w * .42, -d / 2 + .04, w * .84, .07, "#24282E", .02) + ln(-w / 2 + .1, .05, w / 2 - .1, .05, K["madeira_esc"])
    if t == "tapete":
        if sombra:
            return ""
        return (f'<rect x="{f3(-w / 2)}" y="{f3(-d / 2)}" width="{f3(w)}" height="{f3(d)}" rx=".05" fill="{K["tapete"]}" stroke="{K["tapete_b"]}" stroke-width=".03"/>'
                f'<rect x="{f3(-w / 2 + .12)}" y="{f3(-d / 2 + .12)}" width="{f3(w - .24)}" height="{f3(d - .24)}" rx=".03" fill="none" stroke="{K["tapete_b"]}" stroke-width=".04"/>'
                f'<rect x="{f3(-w / 2 + .22)}" y="{f3(-d / 2 + .22)}" width="{f3(w - .44)}" height="{f3(d - .44)}" rx=".02" fill="none" stroke="{K["tapete_b"]}" stroke-width=".015" stroke-dasharray=".06 .05"/>')
    if t == "mesaCentro":
        return R(-w / 2, -d / 2, w, d, K["madeira"], .06) + C(-.08, -.22, .07, K["vaso_flor"]) + R(.02, .08, .2, .28, K["livro"], .02)
    if t == "mesaJantar":
        cad = "".join(R(sx * (w / 2 + .14) - .17, sz - .17, .34, .34, K["cadeira"], .08) for sx in (-1, 1) for sz in (-.3, .3))
        return cad + R(-w / 2, -d / 2, w, d, K["madeira"], .05)
    if t == "bancada":
        o = R(-w / 2, -d / 2, w, d, K["bancada"], .02)
        o += R(-w / 2 + .3, -d / 2 + .1, .5, .38, K["inox"], .06) + R(-w / 2 + .36, -d / 2 + .15, .38, .28, K["inox_esc"], .05)
        o += R(w / 2 - .72, -d / 2 + .06, .56, .48, "#2A2D33", .04)
        for dx in (-.13, .13):
            for dy in (-.11, .11):
                o += C(w / 2 - .44 + dx, -d / 2 + .3 + dy, .075, "#2A2D33")
                if not sombra:
                    o += f'<circle cx="{f3(w / 2 - .44 + dx)}" cy="{f3(-d / 2 + .3 + dy)}" r=".045" fill="none" stroke="#6B7078" stroke-width=".012"/>'
        return o
    if t == "geladeira":
        return R(-w / 2, -d / 2, w, d, K["geladeira"], .05) + R(-w / 2 + .05, d / 2 - .1, w - .1, .05, "#C9CED4", .02)
    if t in ("tanque", "pia"):
        agua = "" if sombra else f'<ellipse cx="0" cy=".04" rx="{f3(w * .32)}" ry="{f3(d * .3)}" fill="{K["agua"]}" stroke="{L}" stroke-width="{sw * .7}"/>'
        return R(-w / 2, -d / 2, w, d, K["louca"], .05) + agua + C(0, -d / 2 + .07, .03, K["inox_esc"])
    if t == "maquina":
        return R(-w / 2, -d / 2, w, d, K["louca"], .05) + C(0, .03, min(w, d) * .32, K["inox"]) + C(0, .03, min(w, d) * .2, K["agua"])
    if t == "vaso":
        if sombra:
            return R(-.19, -.31, .38, .16) + '<ellipse cx="0" cy=".06" rx=".17" ry=".23"/>'
        return (R(-.19, -.31, .38, .16, K["louca"], .04) + f'<ellipse cx="0" cy=".06" rx=".17" ry=".23" fill="{K["louca"]}" stroke="{L}" stroke-width="{sw}"/>'
                f'<ellipse cx="0" cy=".08" rx=".1" ry=".14" fill="{K["agua"]}"/>')
    if t == "box":
        if sombra:
            return ""
        return (f'<rect x="{f3(-w / 2)}" y="{f3(-d / 2)}" width="{f3(w)}" height="{f3(d)}" fill="{K["box"]}" opacity=".8"/>'
                + ln(-w / 2, d / 2, w / 2, d / 2, K["vidro"], .03)
                + ("" if mv.get("sem_ralo") else C(0, 0, .05, K["inox"]) + C(-w / 2 + .14, -d / 2 + .14, .07, K["inox"])))
    if t == "armario":
        n = max(2, round(w / .5))
        o = R(-w / 2, -d / 2, w, d, K["armario"], .02)
        o += "".join(ln(-w / 2 + w * i / n, -d / 2, -w / 2 + w * i / n, d / 2) for i in range(1, n))
        return o + "".join(ln(-w / 2 + w * (i + .5) / n - .05, d / 2 - .06, -w / 2 + w * (i + .5) / n + .05, d / 2 - .06, K["madeira_esc"], .025) for i in range(n))
    if t == "escrivaninha":
        return R(-w / 2, -d / 2, w, d, K["madeira"], .03) + R(-.18, -d / 2 + .06, .36, .24, "#3A3F47", .02) + C(0, d / 2 + .22, .2, K["cadeira"])
    if t == "criado":
        return R(-.22, -.2, .44, .4, K["madeira"], .04) + ("" if sombra else C(0, 0, .11, K["luz"], st=False) + C(0, 0, .06, "#FFFFFF"))
    if t == "planta":
        r = .25 * mv.get("s", 1)
        if sombra:
            return f'<circle r="{f3(r)}"/>'
        o = C(0, 0, r * .55, K["vaso_planta"])
        for i in range(8):
            o += f'<ellipse cx="{f3(r * .5)}" cy="0" rx="{f3(r * .52)}" ry="{f3(r * .2)}" fill="{K["folha"][i % 3]}" stroke="{K["folha_l"]}" stroke-width="{sw * .6}" transform="rotate({i * 45 + 10})"/>'
        return o + C(0, 0, r * .18, K["folha"][2], st=False)
    if t == "carro":
        return R(-w / 2, -d / 2, w, d, K["carro"], .35) + R(-w / 2 + .15, -d * .2, w - .3, d * .35, "#B9C7D6", .15)
    if t == "poltrona":
        return R(-w / 2, -d / 2, w, d, K["poltrona"], .08) + R(-w / 2, -d / 2, w, .16, K["sofa_esc"], .06)
    return ""


def _bbox_movel(mv):
    t = mv["tipo"]
    w, d = mv.get("w", .45), mv.get("d", .4)
    if t == "criado":
        w, d = .44, .4
    if t == "vaso":
        w, d = .4, .62
    if t == "planta":
        w = d = .5 * mv.get("s", 1)
    r = mv.get("rot", 0) or 0
    c, s = abs(math.cos(r)), abs(math.sin(r))
    hw, hd = c * w / 2 + s * d / 2, s * w / 2 + c * d / 2
    return (mv["x"] - hw, mv["y"] - hd, mv["x"] + hw, mv["y"] + hd)


def _ralos(mv):
    """Ralo e chuveiro do box, no desenho do validador (y para cima): os mesmos dois círculos que _movel desenha."""
    th = mv.get("rot", 0) or 0
    return [(mv["x"] + lx * math.cos(th) + ly * math.sin(th), mv["y"] - lx * math.sin(th) + ly * math.cos(th))
            for lx, ly in ((0, 0), (-mv.get("w", .45) / 2 + .14, -mv.get("d", .4) / 2 + .14))]


def _inter(a, b):
    return max(0, min(a[2], b[2]) - max(a[0], b[0])) * max(0, min(a[3], b[3]) - max(a[1], b[1]))


def _area(b):
    return (b[2] - b[0]) * (b[3] - b[1])


MOVEIS_TIRADOS = {}  # móvel que o motor 3D pôs em cima de outro: sai do desenho e vai para o aviso ao Arquiteto


def _moveis_sem_choque(pid, moveis):
    ficam, tirados = [], []
    for mv in moveis:
        if mv["tipo"] == "tapete":
            ficam.append(mv)
            continue
        b = _bbox_movel(mv)
        if mv["tipo"] == "vaso":  # o vaso nunca sai: se bater no box, quem sai é o box
            caixa = next((o for o in ficam if o["tipo"] == "box" and _inter(b, _bbox_movel(o)) > 0), None)
            if caixa:
                ficam.remove(caixa)
                tirados.append(f'box ({caixa.get("amb", "?")}) por baixo do vaso')
            ficam.append(mv)
            continue
        choque = next((o for o in ficam if o["tipo"] != "tapete" and _inter(b, _bbox_movel(o)) > .4 * min(_area(b), _area(_bbox_movel(o)))), None)
        if choque:
            tirados.append(f'{mv["tipo"]} ({mv.get("amb", "?")}) em cima de {choque["tipo"]}')
            continue
        ficam.append(mv)
    MOVEIS_TIRADOS[pid] = tirados
    return ficam


def _arvore(x, y, r, K):
    o = f'<circle cx="{f3(x + .12)}" cy="{f3(y + .14)}" r="{f3(r)}" fill="#000" opacity=".13"/><circle cx="{f3(x)}" cy="{f3(y)}" r="{f3(r)}" fill="{K[0]}"/>'
    for i in range(6):
        a = math.radians(i * 60 + 15)
        o += f'<circle cx="{f3(x + math.cos(a) * r * .55)}" cy="{f3(y + math.sin(a) * r * .55)}" r="{f3(r * .42)}" fill="{K[i % 2 + 1]}"/>'
    return o + f'<circle cx="{f3(x - r * .2)}" cy="{f3(y - r * .25)}" r="{f3(r * .3)}" fill="{K[3]}" opacity=".8"/>'


def _piso(tipo, x, y, w, h, K):
    """Piso desenhado em vetor (tábua, porcelanato, azulejo, grama). Sem <pattern>: o Chrome transforma padrão
    em imagem no PDF (pesava uns 70 KB por cômodo e borrava na impressão)."""
    x1, y1 = x + w, y + h
    if w <= 0 or h <= 0:
        return ""
    if tipo == "madeira":  # tábuas de 1,20 m x 18 cm, desencontradas (vinílico ou laminado)
        o = [f'<rect x="{f3(x)}" y="{f3(y)}" width="{f3(w)}" height="{f3(h)}" fill="{K["madeira"][0]}"/>']
        row = 0
        yy = y
        while yy < y1 - 1e-6:
            hh = min(.18, y1 - yy)
            xx = x - [0, .6, .3, .9][row % 4]
            i = 0
            while xx < x1 - 1e-6:
                a, b = max(xx, x), min(xx + 1.2, x1)
                if b - a > 1e-3:
                    o.append(f'<rect x="{f3(a)}" y="{f3(yy)}" width="{f3(b - a)}" height="{f3(hh)}" fill="{K["madeira"][(i + 2 * row) % len(K["madeira"])]}" stroke="{K["madeira_l"]}" stroke-width=".007"/>')
                xx += 1.2
                i += 1
            yy += .18
            row += 1
        return "".join(o)
    if tipo == "grama":  # fundo verde e tufos curtos (um caminho só)
        tufos = []
        for gx in range(int(w / .5) + 1):
            for gy in range(int(h / .5) + 1):
                bx, by = x + gx * .5, y + gy * .5
                for dx, dy, ex, ey in ((.08, .12, .02, -.06), (.3, .3, -.02, -.06), (.4, .1, .015, -.05), (.15, .42, .02, -.05), (.22, .2, -.015, -.05)):
                    if bx + dx < x1 and by + dy < y1:
                        tufos.append(f"M{bx + dx:.2f} {by + dy:.2f}l{ex} {ey}")
        return (f'<rect x="{f3(x)}" y="{f3(y)}" width="{f3(w)}" height="{f3(h)}" fill="{K["grama"]}"/>'
                f'<path d="{"".join(tufos)}" stroke="{K["grama_l"]}" stroke-width=".012" stroke-linecap="round"/>')
    passo, fundo, linha, esp = {"porc": (.6, "porc", "porc_l", .012), "banho": (.3, "banho", "banho_l", .01),
                                "varanda": (.45, "varanda", "varanda_l", .014), "calcada": (.4, "calcada", "calcada_l", .012)}[tipo]
    d = "".join(f"M{x + k * passo:.3f} {y:.3f}V{y1:.3f}" for k in range(1, int(w / passo - 1e-6) + 1))
    d += "".join(f"M{x:.3f} {y + k * passo:.3f}H{x1:.3f}" for k in range(1, int(h / passo - 1e-6) + 1))
    return (f'<rect x="{f3(x)}" y="{f3(y)}" width="{f3(w)}" height="{f3(h)}" fill="{K[fundo]}"/>'
            + (f'<path d="{d}" stroke="{K[linha]}" stroke-width="{esp}" fill="none"/>' if d else ""))


PISO_TIPO = {k: {"pMadeira": "madeira", "pPorc": "porc", "pAzulejo": "banho", "pVaranda": "varanda", "pCalcada": "calcada", "pGrama": "grama"}[v] for k, v in PISO.items()}


def svg_humanizada(p, estilo="revista"):
    """Planta humanizada com o entorno: recuos de referência, muro da divisa, jardim, caminho da entrada, calçada e rua.
    A frente da casa fica para baixo (o leitor chega da rua). Medidas e áreas do validador; o resto do motor 3D."""
    S = ESTILOS[estilo]
    W, D = p["W"], p["D"]
    MET = p["_r"].metricas
    REC = MET["recuos"]
    caixas, janelas, portas, moveis = _geometria(p)
    mov = _moveis_sem_choque(p["id"], moveis)
    fut = [c for c in p["comodos"] if c["tipo"] == "futuro"]
    Dm = max([D] + [c["y1"] for c in fut])
    Wm = max([W] + [c["x1"] for c in fut])
    Y = lambda y: Dm - y
    portas_h = [(d, *PL.porta_dobradica(p, d)) for d in portas]
    # o que a etiqueta do cômodo não pode cobrir: móvel e louça (peso 1), piso do box (.5: é chão, mas tem o ralo)
    # e o giro da porta, medido no quarto de círculo de verdade (o canto do quadrado fora do arco fica livre)
    LOUCA = {"vaso": 2, "pia": 2, "tanque": 2, "maquina": 2, "box": .4}
    obst = [(*_bbox_movel(mv), LOUCA.get(mv["tipo"], 1)) for mv in mov if mv["tipo"] != "tapete"]
    for mv in mov:  # o ralo e o chuveiro do box pesam como louça
        if mv["tipo"] == "box":
            obst += [(px - .12, py - .12, px + .12, py + .12, 2) for px, py in _ralos(mv)]
    giros = []
    for d, H, A, B in portas_h:
        xs, ys = (H[0], A[0], B[0]), (H[1], A[1], B[1])
        giros.append(((min(xs), min(ys), max(xs), max(ys)), H, d["r"]))

    def cobre(bb, pesos=True):
        """Área da etiqueta (bb) em cima de móvel, box ou giro de porta; com pesos=False, a área pura."""
        tot = sum(_inter(bb, o[:4]) * (o[4] if pesos else 1) for o in obst)
        for g, (hx, hy), r in giros:
            a = _inter(bb, g)
            if a <= 0:
                continue
            ix0, iy0, ix1, iy1 = max(bb[0], g[0]), max(bb[1], g[1]), min(bb[2], g[2]), min(bb[3], g[3])
            pts = [(ix0 + (ix1 - ix0) * (i + .5) / 6, iy0 + (iy1 - iy0) * (k + .5) / 6) for i in range(6) for k in range(6)]
            tot += a * sum(math.hypot(x - hx, y - hy) <= r + .05 for x, y in pts) / 36 * (.6 if pesos else 1)
        return tot

    pl, pr, pt, pb = 1.25, .95, 1.3, 2.15  # margens: cota à esquerda, cota em cima, jardim e rua embaixo
    vb = (-pl, -pt, Wm + pl + pr, Dm + pt + pb)
    # letra mínima: na página da casa a planta ocupa uns 171 x 165 mm; casa estreita e comprida sai em escala menor,
    # então etiquetas e cotas crescem (kl) para ficarem do tamanho das casas largas (nome do cômodo com ~3,6 mm)
    kl = min(1.7, max(1.0, 13.85 / min(171 / vb[2], 165 / vb[3])))
    s = [f'<svg viewBox="{f3(vb[0])} {f3(vb[1])} {f3(vb[2])} {f3(vb[3])}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Planta humanizada da {E(p["nome"])}">',
         ]
    K = S["piso"]
    # terreno: só o que os recuos de referência deixam ver (recuo 0 = muro da divisa)
    jx0 = -min(.8, REC["esq"])
    jx1 = Wm + min(.7, REC["dir"])
    jy_fundo = Y(Dm) - min(.7, REC["fundos"])
    if S.get("sombra_lote"):  # o lote "pousado" sobre o papel azul (sombra em vetor, sem filtro: imprime nítido)
        s.append(f'<rect x="{f3(jx0 + .12)}" y="{f3(jy_fundo + .16)}" width="{f3(jx1 - jx0)}" height="{f3(Dm + 1.25 - jy_fundo)}" fill="{S["sombra_lote"]}"/>')
    s.append(_piso("grama", jx0, jy_fundo, jx1 - jx0, Dm + 1.25 - jy_fundo, K))
    s.append(_piso("calcada", -pl, Dm + 1.25, vb[2], .42, K))
    s.append(f'<rect x="{f3(-pl)}" y="{f3(Dm + 1.67)}" width="{f3(vb[2])}" height="{f3(pb - 1.67 + .01)}" fill="{S["rua"]}"/>')
    s.append(f'<text x="{f3(W / 2)}" y="{f3(Dm + 1.95)}" text-anchor="middle" font-size=".2" font-weight="700" letter-spacing=".12" fill="{S["rua_txt"]}">RUA</text>')
    for lado, xm, xt in (("esq", -.2, -.34), ("dir", W + .08, W + .44)):
        if REC[lado] == 0:
            hach = "".join(f"M{f3(xm)} {f3(yy + .12)}l.12 -.12" for yy in [jy_fundo + k * .12 for k in range(int((Dm + 1.25 - jy_fundo) / .12))])
            s.append(f'<rect x="{f3(xm)}" y="{f3(jy_fundo)}" width=".12" height="{f3(Dm + 1.25 - jy_fundo)}" fill="#E4E1DA" stroke="#8F887C" stroke-width=".01"/>'
                     f'<path d="{hach}" stroke="#B5AFA4" stroke-width=".02"/>')
            s.append(f'<text x="{f3(xt)}" y="{f3(Dm + .75)}" font-size=".15" fill="#7A7467" transform="rotate(-90 {f3(xt)} {f3(Dm + .75)})">divisa</text>')
    # caminho da rua até a entrada
    ex = p.get("_entrada_x")
    if ex is None:
        frente = [c for c in p["comodos"] if c["y0"] == 0 and c["tipo"] == "varanda"]
        ex = (frente[0]["x0"] + frente[0]["x1"]) / 2 if frente else None
    if ex is not None:
        ex = min(max(ex, .5), W - .5)
        s.append(_piso("calcada", ex - .45, Dm, .9, 1.25, K))
    # entrada pela lateral (sem porta na frente, ex.: E03): o caminho sobe pelo recuo do lado até a porta de entrada
    ent = porta_de_entrada(p)
    lado_ent, y_ent = None, None
    if ex is None and ent["lado"] in ("esq", "dir") and REC[ent["lado"]] > 0:
        d = next(d for d in portas if d["id"] == ent["id"])
        y_ent = max(PL.porta_dobradica(p, d)[0][1], PL.porta_dobradica(p, d)[1][1])
        a, b = (jx0, 0) if ent["lado"] == "esq" else (W, jx1)
        cx = (a + b) / 2
        lado_ent = (cx, max(-pl + .6, min(cx, Wm + pr - .6)))
        s.append(_piso("calcada", a, Y(y_ent) - .1, b - a, Dm + 1.25 - Y(y_ent) + .1, K))
    ex_livre = ex if ex is not None else (lado_ent[1] if lado_ent else None)  # onde não pode ter árvore na frente
    # árvores nos recuos (longe do caminho)
    KA = S["arvore"]
    if REC["dir"] >= 1:
        if not (lado_ent and ent["lado"] == "dir" and .9 < y_ent + .4):
            s.append(_arvore(W + .38, Y(.9), .3, KA))
        if not (lado_ent and ent["lado"] == "dir" and D - 1.5 < y_ent + .4):
            s.append(_arvore(W + .4, Y(D - 1.5), .26, KA))
    postas = []
    for x, r in ((W - .9, .42), (.55, .3), (W / 2, .34)):
        if len(postas) == 2 or (ex_livre is not None and abs(x - ex_livre) < r + .5) or any(abs(x - x2) < r + r2 + .1 for x2, r2 in postas):
            continue
        postas.append((x, r))
        s.append(_arvore(x, Dm + .64, r, KA))
    if REC["fundos"] >= 1:
        s.append(_arvore(min(1.7, W / 2), jy_fundo + .32, .26, KA))
    # pisos e ampliação
    for c in p["comodos"]:
        x0, y0, x1, y1 = c["x0"], c["y0"], c["x1"], c["y1"]
        if c["tipo"] == "futuro":
            s.append(f'<rect x="{f3(x0)}" y="{f3(Y(y1))}" width="{f3(x1 - x0)}" height="{f3(y1 - y0)}" fill="#FFF6DE" fill-opacity=".85" stroke="#E0A92E" stroke-width=".05" stroke-dasharray=".25 .18"/>')
            s.append(f'<text x="{f3((x0 + x1) / 2)}" y="{f3(Y((y0 + y1) / 2))}" text-anchor="middle" font-size=".26" font-weight="800" fill="#9A6B00">AMPLIAÇÃO</text>')
            s.append(f'<text x="{f3((x0 + x1) / 2)}" y="{f3(Y((y0 + y1) / 2) + .32)}" text-anchor="middle" font-size=".2" fill="#9A6B00">{E(c["nome"].split(" (")[0])}</text>')
            continue
        s.append(_piso(PISO_TIPO.get(c["tipo"], "porc"), x0, Y(y1), x1 - x0, y1 - y0, K))
        if c["tipo"] in ("varanda", "garagem"):  # beiral
            s.append(f'<rect x="{f3(x0)}" y="{f3(Y(y1))}" width="{f3(x1 - x0)}" height="{f3(y1 - y0)}" fill="none" stroke="{S["beiral"]}" stroke-width=".025" stroke-dasharray=".14 .08"/>')

    # móveis: tapete, sombra, móveis
    def tr(mv, dx=0, dy=0):
        return f'translate({mv["x"] + dx:.3f} {Y(mv["y"]) + dy:.3f}) scale(1 -1) rotate({-math.degrees(mv.get("rot", 0) or 0):.2f})'
    s += [f'<g transform="{tr(mv)}">{_movel(mv, S)}</g>' for mv in mov if mv["tipo"] == "tapete"]
    s.append(f'<g fill="{S["sombra"]}">' + "".join(f'<g transform="{tr(mv, .045, .06)}">{_movel(mv, S, sombra=True)}</g>' for mv in mov if mv["tipo"] != "tapete") + "</g>")
    i_moveis = len(s)  # os móveis entram aqui depois das etiquetas (o ralo encostado numa etiqueta não é desenhado)
    s.append("")
    # paredes de verdade, com os vãos das portas: externa de 15 cm para dentro da face de fora, interna de 12 cm no
    # eixo (as do validador e do 3D, P3.paredes_reais); o móvel encostado para na face de dentro
    if S.get("parede_sombra"):
        s.append(_svg_paredes(caixas, Y, S["parede_sombra"], dx=.09, dy=.11))
    if S.get("parede_contorno"):
        s.append(_svg_paredes(caixas, Y, S["parede_contorno"], extra=.035))
    s.append(_svg_paredes(caixas, Y, S["parede"]))
    # janelas (mesma posição do 3D e da vista da rua); a veneziana em cima da porta vem depois das portas, tracejada
    for j in (j for j in janelas if j.get("tipo") != "veneziana"):
        x0, y0, x1, y1 = j["seg"]
        t = .15
        if abs(y0 - y1) < 1e-6:
            x, y, w, h = min(x0, x1), Y(y0) - t / 2, abs(x1 - x0), t
            ls = [(x, Y(y0) - t / 4, x + w, Y(y0) - t / 4), (x, Y(y0) + t / 4, x + w, Y(y0) + t / 4), (x, Y(y0), x + w, Y(y0))]
        else:
            x, y, w, h = x0 - t / 2, Y(max(y0, y1)), t, abs(y1 - y0)
            ls = [(x0 - t / 4, y, x0 - t / 4, y + h), (x0 + t / 4, y, x0 + t / 4, y + h), (x0, y, x0, y + h)]
        s.append(f'<rect x="{f3(x)}" y="{f3(y)}" width="{f3(w)}" height="{f3(h)}" fill="{S["janela_fundo"]}" stroke="{S["parede"] if estilo == "revista" else S["parede_contorno"]}" stroke-width=".012"/>')
        for k, (a, b, c, d) in enumerate(ls):
            s.append(f'<line x1="{f3(a)}" y1="{f3(b)}" x2="{f3(c)}" y2="{f3(d)}" stroke="{S["vidro"] if k == 2 else "#2B2F36"}" stroke-width="{.03 if k == 2 else .008}"/>')
    # portas: arco do giro e folha aberta, com a dobradiça no canto (PL.porta_dobradica). A porta de entrada (a da seta
    # ENTRADA, mesmo passando pela varanda) tem soleira e folha amarelas; as outras para fora, a soleira cinza de cimento
    for d, (hx, hy), (ax, ay), (bx, by) in portas_h:
        r = d["r"]
        va, vb_ = (ax - hx, Y(ay) - Y(hy)), (bx - hx, Y(by) - Y(hy))
        sweep = 1 if vb_[0] * va[1] - vb_[1] * va[0] > 0 else 0
        e_entrada = d["id"] == ent["id"]
        if e_entrada:
            s.append(_soleira(p, d, Y, .13, "#FFC857", "entrada"))
        elif str(d["id"]).startswith("ext-"):
            s.append(_soleira(p, d, Y, .1, SOLEIRA_FORA, "fora"))
        s.append(f'<path d="M{f3(bx)} {f3(Y(by))} A{r} {r} 0 0 {sweep} {f3(ax)} {f3(Y(ay))}" fill="none" stroke="{S["arco"]}" stroke-width=".015" stroke-dasharray=".05 .035"/>')
        if e_entrada:  # folha amarela com contorno escuro (lê no piso de madeira e no papel azul)
            s.append(f'<line x1="{f3(hx)}" y1="{f3(Y(hy))}" x2="{f3(bx)}" y2="{f3(Y(by))}" stroke="#17202B" stroke-width=".085" stroke-linecap="round"/>'
                     f'<line x1="{f3(hx)}" y1="{f3(Y(hy))}" x2="{f3(bx)}" y2="{f3(Y(by))}" stroke="#FFC857" stroke-width=".05" stroke-linecap="round"/>')
        else:
            s.append(f'<line x1="{f3(hx)}" y1="{f3(Y(hy))}" x2="{f3(bx)}" y2="{f3(Y(by))}" stroke="{S["folha_porta"]}" stroke-width=".05" stroke-linecap="round"/>')
    if ent["id"] is None:
        s.append(_soleira_beira(p, Y, .13))
    s.extend(_veneziana(p, j, Y) for j in janelas if j.get("tipo") == "veneziana")  # azul nos dois estilos: o amarelo da capa some no gramado
    if ex is not None:
        s.append(_entrada_seta(ex, Dm + .62))
    elif lado_ent:  # entrada pela lateral: a seta sobe pelo corredor do lado; a pílula chega para dentro do desenho
        s.append(_entrada_seta(lado_ent[0], Dm + .62, lado_ent[1]))
    # etiquetas dos cômodos, no ponto com menos móvel e porta por baixo
    etiquetas = []
    for c in p["comodos"]:
        t = c["tipo"]
        w, h = c["x1"] - c["x0"], c["y1"] - c["y0"]
        if t in ("circ", "futuro", "externo") or min(w, h) < .95:
            continue
        nome = "PÁTIO" if t == "patio" else c["nome"].upper()
        area = m1(MET["util"][c["id"]][2]) + " m²"
        m2 = area + (" · coberta" if t in ("varanda", "garagem") else "")
        fs0 = max(min(.26, (w - .3) / (len(nome) * .68)), .15)
        # tamanhos a tentar: pílula de 2 linhas (nome em cima, área embaixo), cada vez menor; se nenhuma couber sem
        # encostar em móvel ou porta, a pílula de 1 linha ("NOME  7,3 m²"), mais baixa, para cômodo apertado
        dois = lambda fs, kmax, kmin=1.0, folga=.09: (fs, False, max(len(nome) * fs * .68, len(m2) * .16 * .62) + .26, fs + .4, kmax, kmin, folga)
        tentativas = [dois(fs0 * q, kl) for q in (1, .88, .78, .7)]
        if kl > 1:  # sem lugar livre no tamanho cheio: cresce menos antes de voltar ao tamanho de antes
            tentativas += [dois(fs0 * q, (1 + kl) / 2) for q in (1, .88, .78)] + [dois(fs0 * q, 1.0) for q in (.88, .78, .7)]
        tentativas += [(fs, True, len(nome) * fs * .68 + len(m2) * .16 * .62 + .45, fs + .2, kl, 1.0, .09) for fs in (.22, .19, .16)]
        # cômodo apertado (banheiro, serviço): a pílula de 2 linhas um pouco menor antes de cobrir louça ou giro de porta
        # (só se ficar livre e com letra de no mínimo .13 m, uns 6 pt na página; senão vale a de tamanho normal que menos cobre)
        tentativas += [dois(fs0 * .7, k, k, .05) for k in (.88, .78) if fs0 * .7 * k >= .13]
        cx0, cy0 = (c["x0"] + c["x1"]) / 2, (c["y0"] + c["y1"]) / 2
        escolha, reserva = None, None
        for fs, linha, lw, lh, kmax, kmin, folga in tentativas:
            kr = max(kmin, min(kmax, (w - .16) / lw, (h - .16) / lh))  # cresce só até caber no cômodo
            parede = .18 if linha else .1  # folga da parede
            if linha and lw > w - 2 * parede:
                continue
            lw, lh = lw * kr, lh * kr
            x0, y0, x1, y1 = c["x0"] + parede, c["y0"] + parede, c["x1"] - parede, c["y1"] - parede
            melhor = None
            for i in range(25):
                for k in range(25):
                    cx = x0 + lw / 2 + max(0, x1 - x0 - lw) * i / 24
                    cy = y0 + lh / 2 + max(0, y1 - y0 - lh) * k / 24
                    bb = (cx - lw / 2 - folga, cy - lh / 2 - folga, cx + lw / 2 + folga, cy + lh / 2 + folga)
                    sc = cobre(bb) * 20 + math.hypot(cx - cx0, cy - cy0) * .15
                    if melhor is None or sc < melhor[0]:
                        melhor = (sc, cx, cy, bb)
            sobra = cobre(melhor[3], pesos=False)
            if sobra < .01:
                escolha = (sobra, melhor, fs, linha, lw, lh, kr)
                break
            peso = cobre(melhor[3])
            if not linha and kmin >= 1 and (reserva is None or peso < reserva[0] - .01):
                reserva = (peso, (sobra, melhor, fs, linha, lw, lh, kr))  # sem lugar livre: a de 2 linhas que menos cobre
        escolha = escolha or reserva[1]
        _, melhor, fs, linha, lw, lh, kr = escolha
        cx, cy = melhor[1], Y(melhor[2])
        s.append(f'<g transform="translate({f3(cx)} {f3(cy)}) scale({kr:.3f}) translate({f3(-cx)} {f3(-cy)})">'
                 + S["etiqueta"](cx, cy, lw / kr, lh / kr, nome, m2, fs, CORES.get(t, "#EEE"), linha) + "</g>")
        etiquetas.append((melhor[1] - lw / 2 - .12, melhor[2] - lh / 2 - .12, melhor[1] + lw / 2 + .12, melhor[2] + lh / 2 + .12))
    # ralo e chuveiro do box: se uma etiqueta encosta neles, saem (o círculo colado no nome parecia uma letra a mais)
    encosta = lambda mv: any(e[0] <= px <= e[2] and e[1] <= py <= e[3] for px, py in _ralos(mv) for e in etiquetas)
    mov = [{**mv, "sem_ralo": True} if mv["tipo"] == "box" and encosta(mv) else mv for mv in mov]
    s[i_moveis] = "".join(f'<g transform="{tr(mv)}">{_movel(mv, S)}</g>' for mv in mov if mv["tipo"] != "tapete")
    # cotas (do validador) e escala gráfica
    cz = S["cota"]
    s.append(f'<g stroke="{cz}" stroke-width=".022" fill="{cz}" font-size="{.26 * min(kl, 1.35):.3f}" class="mono">'
             f'<line x1="0" y1="-.92" x2="{f3(W)}" y2="-.92"/><line x1="0" y1="-1.04" x2="0" y2="-.8"/><line x1="{f3(W)}" y1="-1.04" x2="{f3(W)}" y2="-.8"/>'
             f'<text x="{f3(W / 2)}" y="-1.03" text-anchor="middle" stroke="none" font-weight="700">casa {m(W)} m</text>'
             f'<line x1="-.72" y1="{f3(Y(D))}" x2="-.72" y2="{f3(Dm)}"/><line x1="-.84" y1="{f3(Y(D))}" x2="-.6" y2="{f3(Y(D))}"/><line x1="-.84" y1="{f3(Dm)}" x2="-.6" y2="{f3(Dm)}"/>'
             f'<text x="-.84" y="{f3(Y(D / 2))}" text-anchor="middle" stroke="none" font-weight="700" transform="rotate(-90 -.84 {f3(Y(D / 2))})">casa {m(D)} m</text></g>')
    ec, ex0, ey = S["escala"], Wm + pr - 2.15, Dm + 1.98  # régua de escala na faixa da rua, fora da calçada
    s.append(f'<g font-size=".15" class="mono" font-weight="700" fill="{ec}">' + "".join(
        f'<rect x="{f3(ex0 + i * .5)}" y="{f3(ey)}" width=".5" height=".07" fill="{ec if i % 2 == 0 else "#fff"}" stroke="{ec}" stroke-width=".01"/>' for i in range(4))
        + f'<text x="{f3(ex0)}" y="{f3(ey - .04)}">0</text><text x="{f3(ex0 + 1)}" y="{f3(ey - .04)}" text-anchor="middle">1</text><text x="{f3(ex0 + 2)}" y="{f3(ey - .04)}" text-anchor="end">2 m</text></g>')
    s.append("</svg>")
    return "".join(s)


ICONES = {
    "area": '<svg viewBox="0 0 24 24" fill="none" stroke="#0B4FA8" stroke-width="2.2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h6V3"/></svg>',
    "cama": '<svg viewBox="0 0 24 24" fill="none" stroke="#0B4FA8" stroke-width="2.2"><path d="M3 18V8M3 14h18v4M21 14v-2a3 3 0 0 0-3-3h-7v5"/><circle cx="7" cy="11" r="1.6"/></svg>',
    "banho": '<svg viewBox="0 0 24 24" fill="none" stroke="#0B4FA8" stroke-width="2.2"><path d="M4 12h16v2a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5zM6 12V6a2 2 0 0 1 4 0"/></svg>',
    "lote": '<svg viewBox="0 0 24 24" fill="none" stroke="#17202B" stroke-width="2.2"><path d="M3 7h18M3 7v10M21 7v10M7 7v3M11 7v3M15 7v3M19 7v2"/></svg>',
}


def chips(p, gancho=""):
    """Os números da casa em pílulas, logo abaixo do nome (do validador). Só o que o gancho ainda não diz:
    o lote fica no título da página da direita ("Cabe num lote de ..."). Com menos de 2 pílulas, a fileira sai."""
    r = p["_r"].metricas
    b = p["banheiros"]
    quartos = p["quartos_txt"].replace(" (+1 depois)", "")
    area = f"{n0(r['area_fechada'])} m²"
    itens = ([f'<span class="chip"><i>{ICONES["area"]}</i>{area} fechados</span>'] if area not in gancho else []) + \
            ([f'<span class="chip"><i>{ICONES["cama"]}</i>{E(quartos)}</span>'] if quartos not in gancho else []) + \
            [f'<span class="chip"><i>{ICONES["banho"]}</i>{b} banheiro{"s" if b > 1 else ""}</span>']
    return f'<div class="chips">{"".join(itens)}</div>' if len(itens) > 1 else ""


def svg_fachada(p, legenda=True):
    """Vista frontal simplificada: o que se vê da rua, com janelas, porta, platibanda e uma pessoa para escala."""
    cs = [c for c in p["comodos"] if c["tipo"] not in ("futuro",)]
    fechados = [c for c in cs if c["tipo"] not in ABERTOS]
    PD, PLAT = 2.8, .6
    W = p["W"]
    H = PD + PLAT
    s = [f'<svg viewBox="-1.6 -.6 {W + 3.2} {H + 1.2}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Vista frontal simplificada">']
    Yv = lambda z: H - z
    # céu suave e chão
    # céu e chão passam da moldura: com overflow visível (CSS .vistas) enchem a caixa toda; em outro lugar ficam cortados
    s.append(f'<rect x="-40" y="-40" width="{W + 80}" height="{H + 40}" fill="#EEF4FB"/>')
    s.append(f'<rect x="-40" y="{H}" width="{W + 80}" height="40" fill="#D9D3C4"/>')
    # para cada faixa de x, o cômodo fechado mais à frente
    xs = sorted({round(v, 3) for c in cs for v in (c["x0"], c["x1"])})
    for a, b in zip(xs, xs[1:]):
        m = (a + b) / 2
        frente = [c for c in fechados if c["x0"] - 1e-6 <= m <= c["x1"] + 1e-6]
        cob = [c for c in cs if c["tipo"] in ("varanda", "garagem") and c["x0"] - 1e-6 <= m <= c["x1"] + 1e-6 and c["y0"] < .01]
        if frente:
            y0 = min(c["y0"] for c in frente)
            tom = "#FBFAF7" if y0 < .01 else "#ECE8E1"
            s.append(f'<rect x="{a:.3f}" y="{Yv(PD + PLAT):.3f}" width="{b - a:.3f}" height="{PD + PLAT:.3f}" fill="{tom}"/>')
        if cob:
            s.append(f'<rect x="{a:.3f}" y="{Yv(PD + .25):.3f}" width="{b - a:.3f}" height=".25" fill="#DCD6CB"/>')
    # colunas das varandas e garagens
    for c in cs:
        if c["tipo"] in ("varanda", "garagem") and c["y0"] < .01:
            for x in (c["x0"] + .08, c["x1"] - .08):
                s.append(f'<rect x="{x - .08:.3f}" y="{Yv(PD):.3f}" width=".16" height="{PD:.3f}" fill="#CFC8BB"/>')
    # contorno
    s.append(f'<line x1="-1.6" y1="{H}" x2="{W + 1.6}" y2="{H}" stroke="#17202B" stroke-width=".05"/>')
    s.append(f'<rect x="0" y="0" width="{W}" height="{PLAT}" fill="#E3DED5"/>')
    # janelas e porta da frente
    # Mesmas posições de porta e janela do motor 3D (ferramentas/planta3d.py): a janela nunca fica sobre a porta
    por_id = {c["id"]: c for c in cs}
    _, jan3d, portas3d, _ = P3.construir(p)
    frontal = lambda c: all(not (o["tipo"] not in ABERTOS and o["y1"] <= c["y0"] + 1e-6 and o["x0"] < c["x1"] and o["x1"] > c["x0"]) for o in cs)
    for j in jan3d:
        c = por_id.get(j["id"])
        x0s, y0s, x1s, y1s = j["seg"]
        if not c or c["tipo"] in ABERTOS or abs(y0s - y1s) > 1e-6 or abs(y0s - c["y0"]) > 1e-6 or not frontal(c):
            continue
        a, b = min(x0s, x1s), max(x0s, x1s)
        pe = j["peitoril"]
        vg = j["verga"]  # 2,2 m na janela; na veneziana em cima da porta, o topo dela
        s.append(f'<rect x="{a:.3f}" y="{Yv(vg):.3f}" width="{b - a:.3f}" height="{vg - pe:.3f}" fill="#9CCBE8" stroke="#2A3340" stroke-width=".04"/>')
        s.append(f'<line x1="{(a + b) / 2:.3f}" y1="{Yv(vg):.3f}" x2="{(a + b) / 2:.3f}" y2="{Yv(pe):.3f}" stroke="#2A3340" stroke-width=".03"/>')
    for d in portas3d:
        # porta de entrada: da rua (ext-*) ou de uma varanda/garagem para um cômodo fechado que se vê da rua
        partes = str(d["id"]).split("-", 1)
        if abs(math.sin(d["a0"])) > 1e-6 or len(partes) != 2:
            continue
        a_id, b_id = partes
        alvo = por_id.get(b_id)
        if not alvo or alvo["tipo"] in ABERTOS or abs(d["y"] - alvo["y0"]) > 1e-6 or not frontal(alvo):
            continue
        if a_id != "ext" and (a_id not in por_id or por_id[a_id]["tipo"] not in ABERTOS):
            continue
        a = d["x"] if abs(d["a0"]) < 1e-6 else d["x"] - d["r"]
        s.append(f'<rect x="{a:.3f}" y="{Yv(2.1):.3f}" width="{d["r"]:.3f}" height="2.1" fill="#B98A5E" stroke="#2A3340" stroke-width=".04"/>')
        s.append(f'<circle cx="{a + d["r"] - .15:.3f}" cy="{Yv(1.05):.3f}" r=".04" fill="#2A3340"/>')
    # enfeites: arbustos e pessoa de 1,70 m para escala
    for x in (-.9, W + .9):
        s.append(f'<circle cx="{x}" cy="{H - .35}" r=".45" fill="#8DB46C"/><circle cx="{x + .3}" cy="{H - .25}" r=".32" fill="#7AA25A"/>')
    px = W + 1.15
    s.append(f'<g fill="#5B6675"><circle cx="{px}" cy="{Yv(1.58):.3f}" r=".12"/><rect x="{px - .14}" y="{Yv(1.45):.3f}" width=".28" height=".65" rx=".1"/>'
             f'<rect x="{px - .12}" y="{Yv(.8):.3f}" width=".1" height=".8"/><rect x="{px + .02}" y="{Yv(.8):.3f}" width=".1" height=".8"/></g>')
    if legenda:
        s.append(f'<text x="{W / 2}" y="{H + .45}" text-anchor="middle" font-size=".26" class="mono" fill="#4F5B69">vista da rua · pessoa de 1,70 m para escala</text>')
    s.append("</svg>")
    return "".join(s)


def svg_lote(p):
    r = p["_r"].metricas
    LW, LD = r["lote"]
    rec = r["recuos"]
    pad, rua = .4, 1.6
    Y = lambda y: LD - y
    fut = [c for c in p["comodos"] if c["tipo"] == "futuro"]
    s = [f'<svg viewBox="{-pad - 1.2} {-pad - .3} {LW + pad * 2 + 2.4} {LD + pad + rua + 1.1}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A casa no lote mínimo">']
    s.append(f'<rect x="0" y="0" width="{LW}" height="{LD}" fill="#F3E6C4" stroke="#17202B" stroke-width=".07" stroke-dasharray=".3 .15"/>')
    hx, hy = rec["esq"], rec["frente"]
    for c in fut:
        s.append(f'<rect x="{hx + c["x0"]}" y="{Y(hy + c["y1"])}" width="{c["x1"] - c["x0"]}" height="{c["y1"] - c["y0"]}" fill="none" stroke="#E0A92E" stroke-width=".07" stroke-dasharray=".25 .15"/>')
    s.append(f'<rect x="{hx}" y="{Y(hy + p["D"])}" width="{p["W"]}" height="{p["D"]}" fill="#0B4FA8"/>')
    s.append(f'<text x="{hx + p["W"] / 2}" y="{Y(hy + p["D"] / 2) + .2}" text-anchor="middle" font-size=".6" font-weight="800" fill="#fff" class="tit">{p["id"]}</text>')
    s.append(f'<rect x="-1.2" y="{LD + .15}" width="{LW + 2.4}" height="{rua}" fill="#C9CED6"/>')
    s.append(f'<text x="{LW / 2}" y="{LD + .15 + rua / 2 + .18}" text-anchor="middle" font-size=".5" font-weight="700" fill="#4F5B69" letter-spacing=".1">RUA</text>')
    s.append(f'<text x="{LW / 2}" y="-.12" text-anchor="middle" font-size=".36" class="mono" fill="#17202B">frente mínima {m(LW)} m</text>')
    s.append(f'<text x="-.45" y="{LD / 2}" text-anchor="middle" font-size=".42" class="mono" fill="#17202B" transform="rotate(-90 -.45 {LD / 2})">fundo mínimo {m(LD)} m</text>')
    s.append(f'<text x="{LW / 2}" y="{Y(rec["frente"] / 2) + .15}" text-anchor="middle" font-size=".36" class="mono" fill="#6B5A2E">recuo {m1(rec["frente"])} m</text>')
    ang = {"sul": 0, "norte": 180, "leste": 90, "oeste": -90}[r["orientacao"]["melhor"]]
    s.append(f'<g transform="translate({LW + .65} .75) rotate({ang})"><circle r=".55" fill="#fff" stroke="#17202B" stroke-width=".04"/>'
             f'<path d="M0 -.48 L.16 .1 L0 0 L-.16 .1 Z" fill="#C0392B"/>'
             f'<text y="-.6" text-anchor="middle" font-size=".32" font-weight="800" fill="#17202B">N</text></g>')
    s.append("</svg>")
    return "".join(s)


def icone(tipo):
    base = '<svg viewBox="0 0 20 20" class="ico" aria-hidden="true"><circle cx="10" cy="10" r="9.5" fill="#E7EFFA"/>'
    if tipo == "sol":
        raios = "".join(f'<line x1="{10 + 5 * c:.2f}" y1="{10 + 5 * s:.2f}" x2="{10 + 6.6 * c:.2f}" y2="{10 + 6.6 * s:.2f}" stroke="#E0A92E" stroke-width="1.3" stroke-linecap="round"/>'
                        for c, s in [(1, 0), (.707, .707), (0, 1), (-.707, .707), (-1, 0), (-.707, -.707), (0, -1), (.707, -.707)])
        return base + '<circle cx="10" cy="10" r="3.2" fill="#E0A92E"/>' + raios + "</svg>"
    if tipo == "ar":
        return base + "".join(f'<path d="M4 {y} h9 a2 2 0 1 0 -2 -2" fill="none" stroke="#0B4FA8" stroke-width="1.3" stroke-linecap="round"/>' for y in (7, 10.5, 14)) + "</svg>"
    if tipo == "agua":
        return base + '<path d="M10 4 C13 8.5 14.5 10.5 14.5 12.5 A4.5 4.5 0 0 1 5.5 12.5 C5.5 10.5 7 8.5 10 4 Z" fill="#4AA3DF"/></svg>'
    return base + '<path d="M5 15 L10 5 L15 15 Z" fill="none" stroke="#0B4FA8" stroke-width="1.4" stroke-linejoin="round"/></svg>'


POUCAS = 6  # edição com até 6 casas: "Ache a sua casa" numa página só e a régua só com as frentes da edição


def svg_fita(contagem, paginas=None):
    """A fita métrica amarela (capa e fim). Com muitas casas, as frentes de 5 a 14 m e quantas casas cabem em cada uma.
    Na edição pequena (até POUCAS casas), só as frentes que existem, numa régua ajustada a elas, e embaixo
    a página da casa (paginas: frente -> números de página), ou a contagem se não houver página (planta grátis)."""
    frentes = sorted(f for f, n in contagem.items() if n)
    pequena = sum(contagem.values()) <= POUCAS and frentes
    if pequena:
        folga = max(.8, (frentes[-1] - frentes[0]) * .12)
        lo, hi = frentes[0] - folga, frentes[-1] + folga
    else:
        lo, hi, frentes = 4.2, 14.8, list(range(5, 15))
    W = 1000
    X = lambda v: (v - lo) / (hi - lo) * W
    s = [f'<svg viewBox="0 0 {W} 150" class="fita" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">',
         f'<rect width="{W}" height="150" fill="#FFC857"/>']
    for c in range(int(lo * 10) + 1, int(hi * 10)):
        h = 34 if c % 10 == 0 else 22 if c % 5 == 0 else 12
        s.append(f'<line x1="{X(c / 10):.1f}" y1="0" x2="{X(c / 10):.1f}" y2="{h}" stroke="#1D1A12" stroke-width="{2 if c % 10 == 0 else 1}"/>')
    s.append("</svg>")

    def embaixo(f):
        pags = [str(n) for n in (paginas or {}).get(f, []) if isinstance(n, int) and n]
        if pequena and pags:
            return ("pág. " if len(pags) == 1 else "págs. ") + " e ".join(pags)
        n = contagem.get(f, 0)
        return f"{n} casas" if n > 1 else "1 casa" if n == 1 else "—"
    marcas = "".join(f'<div class="marca" style="left:{(f - lo) / (hi - lo) * 100:.2f}%"><b>{f} m</b><small>{embaixo(f)}</small></div>' for f in frentes)
    return f'<div class="fita-box{" pequena" if pequena else ""}">{"".join(s)}<div class="marcas">{marcas}</div></div>'


FOTOS = EBOOK / "visual" / "openart" / "final"
CACHE_FOTOS = EBOOK / ".cache" / "fotos"


def arquivo_foto(pasta, nome):
    """A foto em JPEG (o padrão, mais leve) ou em PNG, o que existir."""
    jpg = pasta / f"{nome}.jpg"
    return jpg if jpg.exists() else pasta / f"{nome}.png"


def _jpeg(origem, largura, recorte=None, pos_y=.5, pos_x=.5, nome=None):
    """A foto em JPEG no cache (ebook/.cache/fotos), com no máximo `largura` px de largura.
    recorte = largura/altura da moldura: corta antes de embutir só o que aparece na página (object-fit: cover com
    object-position pos_x/pos_y), na mesma resolução de antes. O PDF não carrega a parte escondida da foto."""
    from PIL import Image
    CACHE_FOTOS.mkdir(parents=True, exist_ok=True)
    marca = f"-r{recorte:.3f}-{pos_x:.2f}-{pos_y:.2f}" if recorte else ""
    destino = CACHE_FOTOS / f"{nome or origem.stem}-{largura}{marca}.jpg"
    if not destino.exists() or destino.stat().st_mtime < origem.stat().st_mtime:
        im = Image.open(origem).convert("RGB")
        if recorte:
            if im.width / im.height > recorte:  # foto mais larga que a moldura: corta os lados
                w = round(im.height * recorte)
                x = round((im.width - w) * pos_x)
                im = im.crop((x, 0, x + w, im.height))
            else:  # mais alta: corta em cima e embaixo
                h = round(im.width / recorte)
                y = round((im.height - h) * pos_y)
                im = im.crop((0, y, im.width, y + h))
        lw = min(largura, im.width)
        im.resize((lw, round(im.height * lw / im.width)), Image.LANCZOS).save(destino, "JPEG", quality=88, optimize=True, progressive=True)
    return destino


MIOLO_MM = 176  # largura do miolo da página (livro.css, .miolo): a foto de largura inteira ocupa isso


def foto(nome, altura_mm, legenda="Imagem ilustrativa.", pos="center", pasta=None, largura=1800, fundo=False):
    """Foto final do OpenArt em JPEG de alta qualidade (até 1800 px, uns 260 dpi na largura do miolo).
    Com altura_mm, a foto ocupa a largura do miolo e é cortada antes, só com o que aparece na moldura."""
    origem = arquivo_foto(pasta or FOTOS, nome)
    if not origem.exists():
        origem = origem.with_suffix(".jpg")
    if not origem.exists():
        return ""
    py = pos.split()[-1] if pos != "center" else "50%"
    pos_y = float(py.rstrip("%")) / 100 if py.endswith("%") else .5
    destino = _jpeg(origem, largura, MIOLO_MM / altura_mm if altura_mm else None, pos_y,
                    nome=f"{(pasta.name + '-') if pasta else ''}{nome}")
    src = os.path.relpath(destino, SAIDA)
    estilo = f"height:{altura_mm}mm" if altura_mm else ""  # sem altura: quem manda é o CSS (ex.: .vistas)
    if fundo:  # a imagem inteira na moldura (object-fit: contain); a sobra mostra a própria imagem desfocada
        from PIL import Image, ImageFilter, ImageEnhance
        borrada = destino.with_name(destino.stem + "-fundo.jpg")
        if not borrada.exists() or borrada.stat().st_mtime < destino.stat().st_mtime:
            im = Image.open(destino).convert("RGB")
            im = im.resize((160, round(im.height * 160 / im.width)), Image.LANCZOS).filter(ImageFilter.GaussianBlur(5))
            ImageEnhance.Brightness(im).enhance(.92).save(borrada, "JPEG", quality=80)
        estilo += f";background:url('{os.path.relpath(borrada, SAIDA)}') center/cover"
    return (f'<figure class="foto" style="{estilo}"><img src="{src}" alt="" style="object-position:{pos}">'
            f'<figcaption>{E(legenda)}</figcaption></figure>')


FACHADAS = EBOOK / "visual" / "openart" / "fachadas"
VISTAS3D = EBOOK / "visual" / "3d"  # planta 3D mobiliada, do nosso motor (ferramentas/planta3d.py + video/render-planta.cjs)


def fachada_bloco(p):
    """Vista da rua (foto ilustrativa do OpenArt, ou o desenho) ao lado da planta 3D mobiliada da casa.
    As duas molduras têm o mesmo tamanho e crescem até o fim da página (CSS .vistas); a foto e o 3D aparecem inteiros."""
    if arquivo_foto(FACHADAS, p['id']).exists():
        rua = (f'<h4>Vista da rua</h4>'
               f'{foto(p["id"], None, "Imagem ilustrativa gerada a partir da vista da rua desta planta.", "center 22%", FACHADAS, largura=1100)}')
        tipo = " com-foto"  # foto em pé (4:5): moldura com altura mínima para a fachada aparecer inteira (CSS)
    else:
        rua = f'<h4>Vista da rua (simplificada)</h4><div class="rua-svg">{svg_fachada(p)}</div>'
        tipo = ""
    v3d = foto(p["id"], None, "Ilustração do modelo 3D, sem telhado.", "center", VISTAS3D, largura=900, fundo=True)
    if not v3d:
        return f'<div class="fachada">{rua}</div>'
    return f'<div class="fachada vistas{tipo}"><div class="v-rua">{rua}</div><div class="v-3d"><h4>A casa em 3D</h4>{v3d}</div></div>'


def capa_fundo():
    """Fundo da capa: o papel azul de projeto (OpenArt), escurecido para o título ler bem.
    Cortado na proporção da página A4 (o que o "cover" mostrava) e com 1600 px de largura: uns 190 dpi
    debaixo do véu azul, sem diferença visível e bem mais leve."""
    origem = arquivo_foto(FOTOS, "06-papel-azul")
    if not origem.exists():
        return ""
    src = os.path.relpath(_jpeg(origem, 1600, 210 / 297), SAIDA)
    return f"background: linear-gradient(rgba(6,40,90,.45), rgba(6,40,90,.25)), url('{src}') center/cover, var(--azul-escuro)"


def svg_no_lote(p, k):
    """A casa (planta simples, cores de sempre) no lote comercial, com o recuo de referência, na escala k mm/m.
    A frente fica para baixo, na rua (a rua e a fita são da página). Cota do fundo do lote ao lado."""
    r = p["_r"].metricas
    LW, LD = r["lote_comercial"]
    rec = r["recuos"]
    fut = [c for c in p["comodos"] if c["tipo"] == "futuro"]
    Dm = max([p["D"]] + [c["y1"] for c in fut])
    Wm = max([p["W"]] + [c["x1"] for c in fut])
    planta = svg_planta(p, nomes=False, cotas=False, pad=0, moveis=True).replace(
        "<svg ", f'<svg x="{f3(rec["esq"])}" y="{f3(LD - rec["frente"] - Dm)}" width="{f3(Wm)}" height="{f3(Dm)}" ', 1)
    vw, vh = LW + .1, LD + .1  # só o lote: a cota do fundo sai para a esquerda, no vão entre as colunas (overflow visível)
    return (f'<svg viewBox="-.05 -.05 {f3(vw)} {f3(vh)}" style="width:{vw * k:.1f}mm;height:{vh * k:.1f}mm;overflow:visible" xmlns="http://www.w3.org/2000/svg" '
            f'role="img" aria-label="{E(p["nome"])} no lote de {LW} x {LD} m">'
            f'<rect x="0" y="0" width="{LW}" height="{LD}" fill="#F3E6C4" stroke="#17202B" stroke-width=".06" stroke-dasharray=".3 .15"/>'
            f'{planta}'
            f'<g stroke="#4F5B69" stroke-width=".04"><line x1="-.25" y1="0" x2="-.25" y2="{LD}"/><line x1="-.37" y1="0" x2="-.13" y2="0"/><line x1="-.37" y1="{LD}" x2="-.13" y2="{LD}"/></g>'
            f'<text x="-.4" y="{LD / 2}" text-anchor="middle" font-size=".5" class="mono" font-weight="700" fill="#4F5B69" '
            f'transform="rotate(-90 -.4 {LD / 2})">{LD} m de fundo</text></svg>')


def galeria(plantas, ids, legenda=""):
    """Faixa decorativa de plantas em miniatura (sem nomes), para fechar páginas de texto."""
    por_id = {p["id"]: p for p in plantas}
    itens = "".join(f'<figure>{svg_planta(por_id[i], nomes=False, cotas=False, pad=.2)}<figcaption>{i}</figcaption></figure>' for i in ids)
    return f'<div class="galeria">{itens}</div>' + (f'<p class="galeria-leg">{E(legenda)}</p>' if legenda else "")


# ------------------------------------------------------------------ páginas
class Livro:
    def __init__(self, plantas, config):
        self.plantas = plantas
        self.config = config
        self.paginas = []
        self.inicio = {}
        self.bloco = ""    # o bloco da página que está sendo escrita (montar); a ordem do modo duas partes sai dele
        self.fichas = []   # (bloco, argumentos) de cada página, para reordenar e numerar de novo
        self.folhas = {}   # casa -> quantas páginas ela ocupa

    def pagina(self, conteudo, classe="", orelha=None, rodape=True, aviso=False, estilo=""):
        n = len(self.paginas) + 1
        self.fichas.append((self.bloco, (conteudo, classe, orelha, rodape, aviso, estilo)))
        self.paginas.append(self._folha(n, conteudo, classe, orelha, rodape, aviso, estilo))
        return n

    def _folha(self, n, conteudo, classe, orelha, rodape, aviso, estilo):
        """orelha: a frente do lote (aba amarela), uma lista de frentes (várias abas) ou "geral" (aba azul da parte 2)."""
        par = n % 2 == 0
        lado = "esq" if par else "dir"
        tab = ""
        if orelha == "geral":
            tab = f'<div class="orelha geral {lado}" style="top:{aba_geral_mm(self.plantas)}mm">{E(TX.DUAS_PARTES["aba_geral"])}</div>'
        elif isinstance(orelha, (list, tuple)):
            tab = "".join(f'<div class="orelha {lado}" style="top:{30 + (f - 5) * 24}mm">frente {f} m</div>' for f in orelha)
        elif orelha is not None:
            top = 30 + (orelha - 5) * 24
            tab = f'<div class="orelha {lado}" style="top:{top}mm">frente {orelha} m</div>'
        rod = ""
        if rodape:
            rod = (f'<div class="rodape {"par" if par else "impar"}"><span class="num">{n}</span>'
                   f'<span>{AVISO if aviso else E(self.config.get("titulo_curto") or titulo_do(self.config))}</span></div>')
        atributo_estilo = f' style="{estilo}"' if estilo else ""
        return f'<section class="pagina {classe}"{atributo_estilo}>{tab}<div class="miolo">{conteudo}</div>{rod}</section>'

    def reordenar(self, ordem):
        """Põe os blocos na ordem dada e numera tudo de novo: rodapé, lado da aba e L.inicio (os números citados nos
        textos saem de L.inicio na passada seguinte do gerador)."""
        fora = sorted({b for b, _ in self.fichas} - set(ordem))
        if fora:
            sys.exit(f"bloco de página fora da ordem das duas partes: {', '.join(fora)}")
        pos = sorted(range(len(self.fichas)), key=lambda i: ordem.index(self.fichas[i][0]))  # estável: dentro do bloco, como estava
        novo = {velho + 1: k + 1 for k, velho in enumerate(pos)}
        self.fichas = [self.fichas[i] for i in pos]
        self.paginas = [self._folha(k + 1, *args) for k, (_, args) in enumerate(self.fichas)]
        self.inicio = {chave: novo[n] for chave, n in self.inicio.items()}


def titulo_do(config):
    """O título do e-book (config.json); enquanto for espaço reservado, o título de trabalho."""
    t = config.get("titulo", "")
    return t if t and not t.startswith("[") else "Que casa cabe no seu lote?"


def lote_frente(p):
    return p["_r"].metricas["lote_comercial"][0]


def casas_txt(n):
    """"1 casa" / "3 casas"."""
    return f"{n} casa{'s' if n != 1 else ''}"


def recuos_da_edicao(plantas):
    """Os recuos de referência das casas desta edição, do validador.
    Devolve (frente, fundos, lateral da casa com parede na divisa ou None, frases de corredor e de esquina):
    o trecho de corredor e o de esquina só entram se a edição tiver casa desse tipo, no singular ou no plural."""
    v = lambda x: f"{x:g}".replace(".", ",")
    tipos = {"divisa": [], "corredor": [], "esquina": []}
    for p in plantas:
        rec = p["_r"].metricas["recuos"]
        lat = (rec["esq"], rec["dir"])
        tipos["divisa" if min(lat) == 0 else "esquina" if max(lat) >= rec["frente"] else "corredor"].append(max(lat))
    r0 = plantas[0]["_r"].metricas["recuos"]
    na = lambda n: "Nas casas" if n > 1 else "Na casa"
    extras = []
    if tipos["corredor"]:
        extras.append(f"{na(len(tipos['corredor']))} de corredor, {v(tipos['corredor'][0])} m nas duas laterais.")
    if tipos["esquina"]:
        extras.append(f"{na(len(tipos['esquina']))} de esquina, {v(tipos['esquina'][0])} m também na rua do lado.")
    lateral = v(tipos["divisa"][0]) if tipos["divisa"] else None
    return v(r0["frente"]), v(r0["fundos"]), lateral, " ".join(extras)


GRUPOS = [
    ("Mora sozinho ou vai alugar", ["C02"]),
    ("Quer sair do aluguel e crescer depois", ["C03"]),
    ("Casal com 1 ou 2 filhos", ["C01", "C04", "C05", "C06", "E02", "E03", "E04", "E05"]),
    ("Família de 4 ou mais", ["F01", "F02", "F03", "F04", "E07", "S09"]),
    ("Trabalha em casa", ["S04"]),
    ("Gosta de receber", ["S07", "E06", "F05"]),
    ("Casa para a vida toda, pensada para ser sem degrau", ["S03"]),
    ("Casa de praia ou de fim de semana", ["S05", "C07"]),
]  # o jeito de morar de cada casa (páginas "Ache pelo jeito da sua família" e "Ache a sua casa")


# Bônus (achado do Revisor, 24/11/2026; CDC, arts. 30 e 37): o config.json diz o que o dono quer dar (decisão dele), mas
# o PDF só anuncia o bônus que tem página de verdade aqui. Para um bônus entrar: escreva a função que acrescenta a
# página dele, com data-bonus="<nome>" na página, e registre-a abaixo. Hoje nenhum tem página (os rascunhos estão em
# pedidos/anexos/bonus-*.md). O checar.py falha se o "O que vem junto" listar bônus sem página.
PAGINAS_BONUS = {}  # nome do bônus, igual ao do config.json -> função(L) que acrescenta a página dele


def bonus_com_conteudo(config):
    """Os bônus do config.json que o PDF pode anunciar: só os que têm página registrada em PAGINAS_BONUS."""
    return [b for b in config.get("bonus", []) if not b.startswith("[") and b in PAGINAS_BONUS]


def montar(plantas, config, numeros, duas_partes=False):
    """As páginas do e-book. Cada página nasce num bloco (L.bloco); com duas_partes=True (só prévia, D17) os blocos
    são reordenados no fim como no mapa: abertura; parte 1, cada casa; parte 2, casas em geral (aba azul); fecho."""
    L = Livro(plantas, config)
    geral = "geral" if duas_partes else None  # a aba lateral das páginas da parte 2
    contagem = {}
    for p in plantas:
        contagem[lote_frente(p)] = contagem.get(lote_frente(p), 0) + 1
    titulo = titulo_do(config)
    pequena = len(plantas) <= POUCAS  # edição pequena: "Ache a sua casa" no lugar de "pelo lote", "pela família" e índice
    pag_frente = {}
    for p in plantas:
        pag_frente.setdefault(lote_frente(p), []).append(numeros[p["id"]])
    qtd = "1 PLANTA DE CASA TÉRREA" if len(plantas) == 1 else f"{len(plantas)} PLANTAS DE CASAS TÉRREAS"

    # 1. capa
    L.bloco = "capa"
    L.pagina(f"""
      <div class="capa-topo"><span class="eti">{qtd} · {E(config.get('ano', '2026'))}</span>
        <h1 class="capa-titulo">{E(titulo)}</h1>
        <p class="capa-sub">Casas organizadas pela frente do terreno. Meça a frente do seu lote, ache a medida na régua abaixo e abra a página.</p></div>
      <div class="capa-planta maquete">{svg_planta(next((p for p in plantas if p['id'] == config.get('planta_da_capa', 'C01')), plantas[0]), humanizada=True, estilo="maquete")}</div>
      {svg_fita(contagem, pag_frente)}""", "capa", rodape=False, estilo=capa_fundo())

    # 2. aviso e como usar (no modo duas partes, o sumário entra e a foto encolhe)
    L.bloco = "usar"
    L.pagina(f"""
      {cab("usar")}
      <ol class="passos3">
        <li><b>Meça a frente do seu lote.</b><span>Com a trena, do muro de um vizinho ao do outro. Essa medida é a porta de entrada do e-book.</span></li>
        <li><b>Ache as casas que cabem.</b><span>Na página {numeros['lote']}, cada largura de lote leva às casas que cabem nela. A aba amarela na borda das páginas faz o mesmo quando você folheia.</span></li>
        <li><b>Leve a escolhida ao seu engenheiro.</b><span>Cada casa explica por que foi desenhada assim e traz as perguntas certas. Você chega na primeira conversa sabendo o que quer e o que perguntar.</span></li>
      </ol>
      {sumario(plantas, numeros) if duas_partes else foto("02-maos-medindo", 66, pos="center 72%")}
      <div class="caixa amarela"><h3>Planta de referência</h3>{TX.AVISO_COMPLETO}</div>""", "usar2" if duas_partes else "")
    L.inicio["usar"] = len(L.paginas)

    # 3. ache pelo lote (no modo duas partes é a porta da parte 1: mostra as abas de todas as frentes)
    L.bloco = "ache"
    linhas = []
    for f in sorted(contagem):
        casas = [p for p in plantas if lote_frente(p) == f]
        itens = "".join(f'<li><b>{p["id"]}</b> {E(p["nome"])} <span>{n0(p["_r"].metricas["area_fechada"])} m² · {E(p["quartos_txt"].replace(" (+1 depois)", ""))}</span><i>p. {numeros[p["id"]]}</i></li>' for p in casas)
        linhas.append(f'<div class="faixa"><div class="faixa-m">{f} m</div><ul>{itens}</ul></div>')
    rf, rfu, rlat, rext = recuos_da_edicao(plantas)
    recuos_txt = (f"Recuos de referência: {rf} m na frente, {rfu} m nos fundos"
                  + (f" e {rlat} m num dos lados; a outra parede fica na divisa, se a prefeitura deixar." if rlat else ".")
                  + (f" {rext}" if rext else "")
                  # as 3 ressalvas do lote maior: frente e fundo mínimos, recuos da cidade, taxa de ocupação (não cortar)
                  + " Lote maior também serve, se tiver pelo menos a frente e o fundo pedidos pela casa, se a prefeitura"
                    " não exigir recuos maiores e se a taxa de ocupação (quanto do lote a casa pode cobrir) deixar.")
    por_id = {p["id"]: p for p in plantas}
    if pequena:
        L.pagina(ache_a_sua_casa(plantas, numeros, recuos_txt), "acha", orelha=sorted(contagem) if duas_partes else None)
    else:
        L.pagina(f"""
      <span class="sobre">{TX.SOBRE["ache"]}</span><h2>Ache pelo seu lote</h2>
      <p class="abertura">Ache a frente do seu lote: ao lado estão as casas desenhadas num lote comum dessa frente, já com os recuos de referência. O fundo mínimo e a medida exata de cada casa estão na página dela.</p>
      <p class="pequeno">{recuos_txt}</p>
      <div class="faixas">{''.join(linhas)}</div>""", "lote", orelha=sorted(contagem) if duas_partes else None)
    L.inicio["lote"] = len(L.paginas)

    # 4. ache pelo jeito da família
    grupos = GRUPOS
    grupos = [(t, [i for i in ids if i in por_id]) for t, ids in grupos]
    grupos = [(t, ids) for t, ids in grupos if ids]  # edição de lançamento: grupo sem casa da edição sai
    mostra = [i for i in ["C02", "C03", "C06", "F01", "S03", "S07"] if i in por_id]
    if len(mostra) < min(6, len(plantas)):
        mostra = [p["id"] for p in plantas][:6]
    blocos = "".join(f'<div class="grupo"><h3>{E(t)}</h3><p>' + " · ".join(f'<b>{i}</b> {E(por_id[i]["nome"])} <i>p. {numeros[i]}</i>' for i in ids) + "</p></div>" for t, ids in grupos)
    L.bloco = "familia"
    if not pequena:
        L.pagina(f"""<span class="sobre">{TX.SOBRE["familia"]}</span><h2>Ache pelo jeito da sua família</h2>
      <p class="abertura">Se ainda não tem o lote, escolha pelo jeito de morar. Depois confira na página {numeros['lote']} se cabe.</p>
      <div class="grupos">{blocos}</div>
      {galeria(plantas, mostra, f"Algumas das {len(plantas)} casas, cada uma para um jeito de morar." if len(mostra) < len(plantas)
               else "A casa do e-book." if len(plantas) == 1 else f"As {len(plantas)} casas do e-book, cada uma para um lote e um jeito de morar.")}""")

    # 5–6. como ler + glossário
    L.bloco = "ler"
    c01 = por_id.get("C01") or por_id.get(config.get("planta_da_capa")) or plantas[0]
    legenda = "".join(f"<li><b>{E(t)}.</b> {E(d)}</li>" for t, d in TX.LEGENDA_LEITURA)
    L.inicio["ler"] = L.pagina(f"""{cab("ler")}
      <p class="abertura">Todas as casas deste e-book são desenhadas do mesmo jeito: a <b>rua fica embaixo</b>, cada cômodo tem nome e área, as janelas são azuis, a porta de entrada é amarela e as outras portas para fora têm a soleira cinza.</p>
      <div class="leitura"><div class="leitura-fig">{svg_planta(c01, humanizada=True)}</div><ul class="legenda">{legenda}</ul></div>
      <div class="caixa azul"><b>Dica:</b> a área do cômodo é a área por dentro das paredes. A "área fechada" da ficha soma a parte da casa com paredes e telhado, sem contar varanda nem garagem.</div>""", orelha=geral)
    termos = "".join(f"<div><dt>{E(t)}</dt><dd>{E(d)}</dd></div>" for t, d in TX.GLOSSARIO)
    L.inicio["palavras"] = L.pagina(f"""{cab("palavras")}
      <p class="abertura">As palavras que aparecem nas plantas, na prefeitura e na conversa com o engenheiro.</p>
      <dl class="glossario">{termos}</dl>""", orelha=geral)

    # 7–8. os 7 erros
    L.bloco = "erros"
    def erro(i, t, porque, certo):
        return f'<div class="erro"><div class="erro-n">{i}</div><div><h3>{"O mais caro: " + E(t[0].lower() + t[1:]) if i == 7 else E(t)}</h3><p>{E(porque)}</p><p class="certo"><b>O jeito certo:</b> {certo[0].lower() + certo[1:]}</p></div></div>'
    bl = [erro(i, *e) for i, e in enumerate(TX.ERROS, start=1)]
    L.inicio["erros"] = L.pagina(f'{cab("erros")}<p class="abertura">Cada casa deste e-book mostra quais desses erros ela evita. Use como lista de conferência antes de fechar a sua planta.</p>{"".join(bl[:4])}', orelha=geral)
    L.pagina(f'<span class="sobre">{TX.SOBRE["erros"]}</span>{"".join(bl[4:])}<div class="caixa amarela"><b>Cada item que você confere agora é uma parede que não vai ser quebrada depois.</b></div>', orelha=geral)

    # 9. índice
    L.bloco = "indice"
    linhas = "".join(
        f'<tr><td class="mono">{p["id"]}</td><td>{E(p["nome"])}</td><td class="n">{n0(p["_r"].metricas["area_fechada"])} m²</td>'
        f'<td>{E(p["quartos_txt"])}</td><td class="n">{p["banheiros"]}</td>'
        f'<td class="n">{lote_frente(p)} x {p["_r"].metricas["lote_comercial"][1]}</td><td class="n">{numeros[p["id"]]}</td></tr>'
        for p in plantas)
    if not pequena:
        L.pagina(f"""<span class="sobre">{TX.SOBRE["indice"]}</span><h2>As {len(plantas)} casas</h2>
      <table class="indice"><thead><tr><th>ID</th><th>Casa</th><th>Área</th><th>Quartos</th><th>Banh.</th><th>Lote mín.</th><th>Pág.</th></tr></thead><tbody>{linhas}</tbody></table>""")

    # as casas (no modo duas partes, cada uma ganha as 2 páginas do cômodo a cômodo, D20: paginas_comodo)
    L.bloco = "casas"
    for p in plantas:
        dupla(L, p, por_id, numeros)
        if duas_partes:
            L.inicio["comodo-" + p["id"]] = paginas_comodo(L, p)
        L.folhas[p["id"]] = len(L.paginas) + 1 - L.inicio[p["id"]]

    # terreno
    L.bloco = "terreno"
    # cada coluna com a largura do desenho do lote: os 3 saem na mesma escala (o de 5 m parece mesmo mais estreito)
    import re
    largura_vb = lambda svg: float(re.search(r'viewBox="([^"]+)"', svg).group(1).split()[2])
    lotes_ex = [i for i in ["E03", "C01", "F02"] if i in por_id]
    if len(lotes_ex) < min(3, len(plantas)):
        uma_por_largura = {}
        for p in sorted(plantas, key=lambda p: (lote_frente(p), p["id"])):
            uma_por_largura.setdefault(lote_frente(p), p["id"])
        lotes_ex = list(uma_por_largura.values())
        lotes_ex = [lotes_ex[0], lotes_ex[len(lotes_ex) // 2], lotes_ex[-1]] if len(lotes_ex) > 3 else lotes_ex
    colunas_lotes = " ".join(f"{largura_vb(svg_lote(por_id[i])):.2f}fr" for i in lotes_ex)
    # o lote mais fundo manda na altura: a fileira estreita até ele caber em 100 mm (a E03 de 2 quartos pede lote de 20,6 m)
    _vb = [[float(v) for v in re.search(r'viewBox="([^"]+)"', svg_lote(por_id[i])).group(1).split()[2:]] for i in lotes_ex]
    largura_lotes = min(170.0, 100.0 * sum(w for w, _ in _vb) / max(h for _, h in _vb))
    L.inicio["terreno"] = L.pagina(f"""{cab("terreno")}
      <p class="abertura">Confira com a conta abaixo <b>antes</b> de pagar qualquer projeto: a planta só serve se couber nas regras do seu lote.</p>
      <div class="duas">
        <div><h3>O que a prefeitura define</h3><ul class="lista">
          <li><b>Recuos:</b> distância mínima da casa até a rua, os vizinhos e os fundos.</li>
          <li><b>Taxa de ocupação:</b> quanto do lote a casa pode cobrir.</li>
          <li><b>Coeficiente de aproveitamento:</b> quanto se pode construir no total.</li>
          <li><b>Permeabilidade:</b> quanto do lote fica sem piso.</li></ul>
          <h3>Onde descobrir</h3><ul class="lista">
          <li>No Plano Diretor, na lei de zoneamento e no código de obras da sua cidade.</li>
          <li>Melhor: peça na prefeitura a consulta prévia do seu lote (leve a matrícula ou o IPTU).</li>
          <li>Em condomínio, leia também o regulamento.</li>
          <li>Em área urbana, o Código Civil (art. 1.301) não deixa abrir janela a menos de 1,5 m do terreno vizinho (o engenheiro confirma).</li></ul></div>
        <div class="caixa azul"><h3>A conta que você faz em casa</h3><p>(frente − recuos laterais) × (fundo − recuo da frente − recuo dos fundos) = espaço para a casa.</p>
          <p>Lote 10 x 20 com recuo de 3 m na frente, 1,5 m numa lateral e 1,5 m nos fundos: sobram 8,5 x 15,5 m. Cabem as casas de até 8,50 m de largura e 15,50 m de comprimento, se a taxa de ocupação da sua cidade deixar. A lateral sem recuo só vale se a prefeitura permitir encostar na divisa, e essa parede fica sem janela.</p>
          <p class="pequeno">Exemplo com recuos de referência. Os do seu lote são os da sua prefeitura.</p></div></div>
      <div class="lotes-ex" style="grid-template-columns:{colunas_lotes};width:{largura_lotes:.0f}mm;margin:0 auto">{''.join(f'<figure>{svg_lote(por_id[i])}<figcaption>{i} no lote de {lote_frente(por_id[i])} m</figcaption></figure>' for i in lotes_ex)}</div>""", "texto", orelha=geral)
    if duas_partes:  # a página "A parede que não pode ter janela" (D21): só no e-book em duas partes, ao lado de "Terreno e recuos"
        L.bloco = "parede"
        L.inicio["parede"] = pagina_parede(L, por_id, orelha=geral)
    L.bloco = "ficha"
    campos = ["Endereço do lote", "Frente (m)", "Fundo (m)", "Recuo da frente (m)", "Recuos laterais (m)",
              "Recuo dos fundos (m)", "Taxa de ocupação (%)", "Permeabilidade (%)", "Lado do nascente (leste)", "Para que lado fica a rua (bússola do celular)",
              "Regras do condomínio", "Casas que cabem (IDs)"]
    L.inicio["ficha"] = L.pagina(f'{cab("ficha")}<p class="abertura">Preencha com os dados da prefeitura e leve junto na primeira conversa com o engenheiro.</p><div class="preencher">{"".join(f"<div>{c}</div>" for c in campos)}</div>{foto("01-lote-trena", 60, pos="center 60%")}', orelha=geral)

    # próximos passos
    L.bloco = "passos"
    passos = [
        # "2 ou 3" só num livro com mais de 3 casas
        ("Escolha 2 ou 3 casas", "Pela frente do lote e pelo jeito da família. Anote os IDs.") if len(plantas) > 3 else
        ("Escolha a sua casa", "Pela frente do lote e pelo jeito da família. Se couber mais de uma, anote os IDs.") if len(plantas) > 1 else
        ("Confira se a casa cabe no seu lote", f"Pela frente e pelo fundo, com a conta da página {numeros['lote']}."),
        ("Confira as regras do seu lote", "Faça a consulta prévia na prefeitura e preencha a ficha do terreno."),
        ("Contrate um profissional habilitado", "Arquiteto (CAU) ou engenheiro civil (CREA). Ele adapta a planta ao terreno, ao sol e às regras da cidade e emite a RRT ou a ART."),
        ("Aprove o projeto na prefeitura", "Com o projeto legal aprovado, sai o alvará de construção."),
        ("Os outros projetos e o orçamento", "Estrutura, elétrica e hidráulica. Com eles o orçamento deixa de ser chute."),
        ("Construa com acompanhamento", "A obra precisa de responsável técnico, com ART ou RRT. Se for financiar, pergunte ao banco quais documentos ele pede."),
        ("Regularize a casa pronta", "Habite-se na prefeitura e registro da casa na matrícula do lote, no cartório."),
    ]
    L.inicio["passos"] = L.pagina(f'{cab("passos")}<ol class="passos">{"".join(f"<li><b>{t}</b><span>{d}</span></li>" for t, d in passos)}</ol>{foto("03-planta-canteiro", 74, pos="center 28%")}', "texto", orelha=geral)

    # bônus e contato
    L.bloco = "bonus"
    bonus = bonus_com_conteudo(config)
    for b in bonus:
        PAGINAS_BONUS[b](L)
    L.bloco = "fim"
    contato = config.get("contato", "")
    gerais = FICHAS.PADRAO + ["O meu lote tem matrícula e está regular na prefeitura?",
                              "Quanto custa o projeto completo e o que está incluído nele?"]
    L.pagina(f"""{cab("fim")}
      <p class="abertura">Você já tem o mais difícil: o lote e uma casa que deve caber nele (confirme os recuos na prefeitura), com o porquê de cada parede. O próximo passo é a primeira conversa com o engenheiro ou o arquiteto.</p>
      <div class="duas"><div><h3>Pergunte em qualquer casa</h3><ul class="lista">{''.join(f'<li>{E(q)}</li>' for q in gerais)}</ul>
          <p class="pequeno">Leve também a ficha do terreno preenchida e as perguntas da página da casa escolhida.</p></div>
        {'<div><h3>O que vem junto</h3><ul class="lista">' + ''.join(f'<li>{E(b)}</li>' for b in bonus) + '</ul>' if bonus else '<div>'}
          {('<h3>Novas casas</h3><p>' + E(config['promessa_atualizacao']) + '</p>') if config.get('promessa_atualizacao') else ''}
          <h3>Ficou em dúvida sobre qual casa cabe?</h3><p>Mande a frente e o fundo do seu lote e receba as casas que devem caber, como referência (não substitui o profissional): {E(contato) if contato and not contato.startswith('[') else '<span class="pendente">[contato do parceiro]</span>'}</p>
          <h3>Conhece alguém que vai construir?</h3><p>Mostre este e-book para quem também tem um lote esperando.</p></div></div>
      {foto("05-familia-lote", 78, pos="center 22%")}
      {svg_fita(contagem, pag_frente)}""", "fim")
    if duas_partes:
        L.reordenar(ORDEM_DUAS_PARTES)
    return L


# E-book em duas partes (decisão do dono, 24/11/2026; mapa do Designer em
# pedidos/anexos/mapa-duas-partes-do-ebook-2026-11-24.md). Só em prévia: python3 ebook/gerador/livro.py --previa DIR --duas-partes
ORDEM_DUAS_PARTES = ["capa", "usar",                                   # abertura (sem aba)
                     "ache", "familia", "indice", "casas",             # parte 1, cada casa (aba amarela da frente)
                     "ler", "erros", "terreno", "parede", "ficha", "passos", "bonus",  # parte 2, casas em geral (aba azul)
                     "fim"]                                            # fecho (sem aba)
GERAL_MM = 200     # altura da aba azul "geral", do topo da folha; desce se a edição tiver frente cuja aba passe daqui


def aba_geral_mm(plantas):
    """A aba azul fica sempre na mesma altura, abaixo da última aba de frente (cada aba tem 20 mm)."""
    ultima = 30 + (max(lote_frente(p) for p in plantas) - 5) * 24
    return max(GERAL_MM, ultima + 26)


def cab(chave):
    """Sobretítulo e título de uma página fixa, do lugar único (paginas.py: SOBRE e TITULOS)."""
    return f'<span class="sobre">{TX.SOBRE[chave]}</span><h2>{TX.TITULOS[chave]}</h2>'


def reservada(L, titulo, casa=None, lado="", orelha=None):
    """Página reservada do modo duas partes: só o quadro "página em preparo", para a contagem e a numeração baterem
    com o mapa enquanto a página de verdade é rascunho em outro script (cômodo a cômodo: D20)."""
    quadro = (f'<div class="reservada" data-reservada="1"><b>{E(TX.DUAS_PARTES["em_preparo"])}</b>'
              f'<span>{E(titulo)}</span></div>')
    if casa:
        return L.pagina(f'<div class="cab"><span class="mono id">{casa["id"]} · {E(casa["nome"].upper())}</span></div>{quadro}',
                        f"casa {lado} q", orelha=lote_frente(casa), aviso=True)
    return L.pagina(quadro, orelha=orelha)


def sumario(plantas, numeros):
    """O sumário da página 2 no modo duas partes (desenho do esboço ebook/plantas/rascunhos/sumario-duas-partes.py).
    Todo número de página vem de `numeros` (a passada anterior do gerador), nunca digitado."""
    pag = lambda chave: numeros.get(chave) or "—"
    folhas = numeros.get("folhas", {})
    linha = lambda titulo, chave, marca="": (f'<li><span>{E(titulo)}'
                                             + (f'<span class="sum-marca">{E(marca)}</span>' if marca else "")
                                             + f'</span><em>{pag(chave)}</em></li>')
    casas = "".join(
        f'<li class="sum-casa"><span class="sum-aba am">frente {lote_frente(p)} m</span><span>{E(p["nome"])}'
        f'<small>{n0(p["_r"].metricas["area_fechada"])} m² · {E(p["quartos_txt"].replace(" (+1 depois)", ""))}'
        + (f' · {folhas[p["id"]]} páginas' if folhas.get(p["id"]) else "")
        + (f'<br>{E(TX.DUAS_PARTES["sum_comodo"].format(numeros["comodo-" + p["id"]]))}' if numeros.get("comodo-" + p["id"]) else "")
        + f'</small></span><em>{pag(p["id"])}</em></li>'
        for p in sorted(plantas, key=lambda p: (lote_frente(p), p["id"])))
    geral = ("".join(linha(TX.TITULOS[c], c) for c in ("ler", "palavras", "erros", "terreno"))
             + linha(TX.PAREDE["titulo"], "parede")
             + "".join(linha(TX.TITULOS[c], c) for c in ("ficha", "passos")))
    (e1, n1, s1), (e2, n2, s2) = TX.DUAS_PARTES["parte1"], TX.DUAS_PARTES["parte2"]
    topo = lambda cor, e, n, s: (f'<div class="sum-cab"><span class="sum-aba {cor}">{E(e)}</span>'
                                 f'<div><b>{E(n)}</b><i>{E(s)}</i></div></div>')
    return (f'<div class="sum"><div class="sum-parte">{topo("am", e1, n1, s1)}'
            f'<ul>{linha(TX.TITULOS["ache"], "lote")}{casas}</ul></div>'
            f'<div class="sum-parte">{topo("az", e2, n2, s2)}<ul>{geral}</ul></div></div>')


# ------------------------------------------------------------------ página "A parede que não pode ter janela" (D21)
# Parte 2 (casas em geral) do modo --duas-partes, só prévia. O desenho é o do rascunho do Designer
# (ebook/plantas/rascunhos/parede_sem_janela.py, D19): a parede da divisa desce a folha pela esquerda e os 4 croquis
# encostam nela. Texto e rótulos: paginas.py (PAREDE). Medidas dos croquis em mm; nada aqui é gerado por IA.
PSJ_TINTA, PSJ_AZUL, PSJ_FITA, PSJ_CINZA, PSJ_BEGE = "#17202B", "#0B4FA8", "#FFC857", "#4F5B69", "#B08A4E"
PSJ_CW, PSJ_CH, PSJ_PD = 47.0, 36.0, 2.6     # croqui: largura, altura, grossura da parede da divisa (mm)
PSJ_CASA = "F01"                              # o croqui 1 é o quarto casal da Família Compacta, do desenho do e-book


def _psj_pilula(x, y, txt, fs=2.25, cor=PSJ_TINTA, ancora="middle", fundo="#fff", borda=None):
    w, h = len(txt) * fs * .6 + fs * .9, fs * 1.55
    x0 = x - w / 2 if ancora == "middle" else (x if ancora == "start" else x - w)
    return (f'<rect x="{x0:.2f}" y="{y - h / 2:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{h / 2:.2f}" fill="{fundo}" stroke="{borda or cor}" stroke-width=".22"/>'
            f'<text x="{x0 + w / 2:.2f}" y="{y + fs * .36:.2f}" text-anchor="middle" font-size="{fs}" font-weight="700" class="mono" fill="{cor}">{E(txt)}</text>')


def _psj_sugestao(x, y):
    return _psj_pilula(x, y, TX.PAREDE["rotulos"]["sugestao"], 2.2, cor="#8A5A00", ancora="start", fundo="#FFF4DA", borda=PSJ_BEGE)


def _psj_rot(x, y, txt, cor=PSJ_TINTA, fs=2.3, anc="start"):
    return f'<text x="{x:.2f}" y="{y:.2f}" text-anchor="{anc}" font-size="{fs}" font-weight="700" class="mono" fill="{cor}">{E(txt)}</text>'


def _psj_chamada(x0, y0, x1, y1, cor=PSJ_TINTA):
    return (f'<line x1="{x0:.2f}" y1="{y0:.2f}" x2="{x1:.2f}" y2="{y1:.2f}" stroke="{cor}" stroke-width=".22"/>'
            f'<circle cx="{x0:.2f}" cy="{y0:.2f}" r=".55" fill="{cor}"/>')


def _psj_seta(pts, cor=PSJ_FITA, larg=1.1, borda=PSJ_TINTA):
    """Seta grossa (sol ou água) por uma polilinha em mm; a ponta no último ponto."""
    d = "M" + " L".join(f"{x:.2f} {y:.2f}" for x, y in pts)
    (xa, ya), (xb, yb) = pts[-2], pts[-1]
    a = math.atan2(yb - ya, xb - xa)
    c, s = math.cos(a), math.sin(a)
    p1, p2, p3 = (xb + c * 1.3, yb + s * 1.3), (xb - s * 1.5, yb + c * 1.5), (xb + s * 1.5, yb - c * 1.5)
    ponta = f'<path d="M{p1[0]:.2f} {p1[1]:.2f} L{p2[0]:.2f} {p2[1]:.2f} L{p3[0]:.2f} {p3[1]:.2f} Z" fill="{cor}" stroke="{borda}" stroke-width=".25" stroke-linejoin="round"/>'
    return (f'<path d="{d}" fill="none" stroke="{borda}" stroke-width="{larg + .5:.2f}" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="{cor}" stroke-width="{larg:.2f}" stroke-linecap="round" stroke-linejoin="round"/>' + ponta)


def _psj_parede(y, h):
    """A parede da divisa em cada croqui: o mesmo tijolo escuro da parede da página (a mesma marca nos 4)."""
    return f'<rect x="0" y="{y:.2f}" width="{PSJ_PD:.2f}" height="{h:.2f}" fill="url(#psj-tijolo)"/>'


def _psj_svg(corpo, legenda=None):
    w, h = PSJ_CW, PSJ_CH
    defs = (f'<defs><pattern id="psj-tijolo" width="8" height="3.2" patternUnits="userSpaceOnUse">'
            f'<rect width="8" height="3.2" fill="{PSJ_TINTA}"/><path d="M0 .1H8M0 1.7H8M2 .1V1.7M6 1.7V3.2" stroke="#2C3846" stroke-width=".35"/></pattern>'
            f'<pattern id="psj-porc" width="2.4" height="2.4" patternUnits="userSpaceOnUse"><rect width="2.4" height="2.4" fill="{PISO_REAL["porc"]}"/>'
            f'<path d="M0 0H2.4M0 0V2.4" stroke="{PISO_REAL["porc_l"]}" stroke-width=".12"/></pattern>'
            f'<pattern id="psj-grama" width="3" height="3" patternUnits="userSpaceOnUse"><rect width="3" height="3" fill="{PISO_REAL["grama"]}"/>'
            f'<path d="M.6 .9l.15 -.45M2 2.2l.15 -.45" stroke="{PISO_REAL["grama_l"]}" stroke-width=".18"/></pattern>'
            f'<pattern id="psj-terra" width="2.2" height="2.2" patternUnits="userSpaceOnUse"><path d="M0 2.2L2.2 0" stroke="#B5AFA4" stroke-width=".22"/></pattern></defs>')
    leg = ""
    if legenda:  # fundo branco atrás das letras: a hachura do chão não passa por cima delas (Revisor, 24/11)
        lw = len(legenda) * 2.1 * .6 + 1.6
        leg = (f'<rect x="{w - 1.6 - lw + .8:.2f}" y="{h - 4.0:.2f}" width="{lw:.2f}" height="3.3" rx=".6" fill="#fff"/>'
               + _psj_rot(w - 1.6, h - 1.6, legenda, PSJ_CINZA, 2.1, "end"))
    return (f'<svg viewBox="0 0 {w:.2f} {h:.2f}" width="{w:.2f}mm" height="{h:.2f}mm" xmlns="http://www.w3.org/2000/svg">{defs}'
            f'<rect x="0" y="0" width="{w:.2f}" height="{h:.2f}" fill="#fff"/>{corpo}{leg}</svg>')


def psj_croqui_quarto(p):
    """Croqui 1: o quarto casal da Família Compacta, recortado da planta humanizada do e-book (o mesmo desenho)."""
    R = TX.PAREDE["rotulos"]
    CW, CH = PSJ_CW, PSJ_CH
    _, janelas, _, _ = _geometria(p)
    q = next(c for c in p["comodos"] if c["id"] == "quarto1")
    cama = next(m for m in q["moveis"] if m["tipo"] == "camaCasal")
    criados = [m for m in q["moveis"] if m["tipo"] == "criado"]
    jq = [j for j in janelas if j["id"] == "quarto1"]
    # o que o texto diz tem de estar no dado: cabeceira e 2 criados na divisa, janela no fundo
    ok = (q["x0"] == 0 and p["_r"].metricas["recuos"]["esq"] == 0 and len(criados) == 2
          and all(abs(c["x"] - .35) < .05 for c in criados) and abs(cama["rot"] - math.pi / 2) < .01
          and jq and p["janelas"]["quarto1"][0][0] == "fundos")
    if not ok:
        AVISOS.append("parede sem janela")
        print(f'AVISO: {p["id"]}: o quarto casal não bate mais com a página da parede sem janela '
              "(cabeceira e 2 criados na divisa, janela no fundo)")
    jan = jq[0]["seg"]
    Dm = max([p["D"]] + [c["y1"] for c in p["comodos"] if c["tipo"] == "futuro"])
    interno = svg_humanizada(p).split(">", 1)[1].rsplit("</svg>", 1)[0]
    # recorte: da face de fora da divisa (x=0) até a parede do quarto ao lado; do quintal do fundo à porta
    x0, x1 = 0.0, q["x1"] + .12
    ys0, ys1 = Dm - p["D"] - .55, Dm - (q["y0"] - .07)
    k = CH / (ys1 - ys0)
    wq = (x1 - x0) * k
    X = lambda x: (x - x0) * k
    Ys = lambda y: (Dm - y - ys0) * k
    s = [f'<svg x="0" y="0" width="{wq:.2f}" height="{CH:.2f}" viewBox="{x0:.3f} {ys0:.3f} {x1 - x0:.3f} {ys1 - ys0:.3f}" overflow="hidden">{interno}</svg>']
    # a prateleira sobre a cabeceira: sugestão (não está no desenho da casa), tracejado bege
    pr_y0, pr_y1 = q["y0"] + cama["y"] - cama["w"] / 2, q["y0"] + cama["y"] + cama["w"] / 2
    s.append(f'<rect x="{X(.17):.2f}" y="{Ys(pr_y1):.2f}" width="{.25 * k:.2f}" height="{(pr_y1 - pr_y0) * k:.2f}" fill="{PSJ_FITA}" fill-opacity=".35" stroke="{PSJ_BEGE}" stroke-width=".4" stroke-dasharray="1 .7"/>')
    s.append(_psj_parede(0, CH))
    xr = wq + 2.0   # rótulos à direita do desenho
    rot = lambda y, txt, cor=PSJ_TINTA: _psj_rot(xr + .8, y, txt, cor)
    s.append(_psj_chamada(X((jan[0] + jan[2]) / 2 + .55), Ys(jan[1]), xr, 4.0, PSJ_AZUL) + rot(4.8, R["janela_livre"], PSJ_AZUL))
    s.append(_psj_chamada(X(.29), Ys(pr_y1 - .3), xr, 12.5) + rot(13.3, R["prateleira"]) + _psj_sugestao(xr + .6, 16.4))
    s.append(_psj_chamada(X(.62), Ys(pr_y0 + .35), xr, 22.5) + rot(23.3, R["cabeceira"][0]) + rot(26.2, R["cabeceira"][1]))
    s.append(_psj_rot(xr + .8, CH - 4.6, R["casa_quarto"][0], PSJ_CINZA, 1.8) + _psj_rot(xr + .8, CH - 2.0, R["casa_quarto"][1], PSJ_CINZA, 1.8))
    return _psj_svg("".join(s))


def psj_croqui_cozinha():
    """Croqui 2: uma cozinha qualquer, vista de cima, em faixa, sem nome de casa (o aéreo é sugestão)."""
    R = TX.PAREDE["rotulos"]
    CW, CH = PSJ_CW, PSJ_CH
    k = 12.5
    S = EST_REVISTA
    xin, xpar, xrec = .21, 2.95, 3.10          # face da divisa, parede do recuo (de/até), em metros
    y0, y1 = .12, 2.70                          # a faixa de cozinha (cortada em cima e embaixo)
    X = lambda x: x * k
    Y = lambda y: y * k + .6
    s = [f'<rect x="{X(xin):.2f}" y="{Y(y0):.2f}" width="{X(xpar - xin):.2f}" height="{(y1 - y0) * k:.2f}" fill="url(#psj-porc)"/>']
    s.append(f'<rect x="{X(xrec):.2f}" y="0" width="{CW - X(xrec):.2f}" height="{CH:.2f}" fill="url(#psj-grama)"/>')
    jy0, jy1 = .6, 1.6                          # parede do recuo com a janela em cima da pia
    s.append(f'<rect x="{X(xpar):.2f}" y="0" width="{X(xrec - xpar):.2f}" height="{Y(jy0):.2f}" fill="{S["parede"]}"/>'
             f'<rect x="{X(xpar):.2f}" y="{Y(jy1):.2f}" width="{X(xrec - xpar):.2f}" height="{CH - Y(jy1):.2f}" fill="{S["parede"]}"/>'
             f'<rect x="{X(xpar):.2f}" y="{Y(jy0):.2f}" width="{X(xrec - xpar):.2f}" height="{(jy1 - jy0) * k:.2f}" fill="#fff" stroke="{S["parede"]}" stroke-width=".25"/>'
             f'<line x1="{X((xpar + xrec) / 2):.2f}" y1="{Y(jy0):.2f}" x2="{X((xpar + xrec) / 2):.2f}" y2="{Y(jy1):.2f}" stroke="{S["vidro"]}" stroke-width=".6"/>')
    for yy in (y0, y1):
        s.append(f'<line x1="{X(xin):.2f}" y1="{Y(yy):.2f}" x2="{X(xpar):.2f}" y2="{Y(yy):.2f}" stroke="{PSJ_CINZA}" stroke-width=".25" stroke-dasharray="1.2 .8"/>')
    # móveis do e-book (o mesmo desenho das plantas), em metros; o grupo escala para mm
    mv = lambda m, x, y, rot: f'<g transform="translate({X(x):.2f} {Y(y):.2f}) scale({k}) rotate({rot})">{_movel(m)}</g>'
    s.append(mv({"tipo": "bancada", "w": 1.8, "d": .6}, xpar - .3, 1.45, 90))   # pia em cima, embaixo da janela
    s.append(mv({"tipo": "geladeira", "w": .72, "d": .7}, xin + .35, .58, -90))
    ay0, ay1 = 1.1, 2.6                          # o armário aéreo na parede da divisa: sugestão
    s.append(f'<rect x="{X(xin) + .2:.2f}" y="{Y(ay0):.2f}" width="{.35 * k:.2f}" height="{(ay1 - ay0) * k:.2f}" fill="{PSJ_FITA}" fill-opacity=".35" stroke="{PSJ_BEGE}" stroke-width=".4" stroke-dasharray="1 .7"/>')
    s.append(_psj_parede(0, CH))
    s.append(_psj_rot(X(xin + .78), Y(.62), R["geladeira"]))
    s.append(_psj_rot(X(xin + .5), Y(1.72), R["aereo"]) + _psj_sugestao(X(xin + .5), Y(1.72) + 3.0))
    s.append(_psj_rot(X(xpar - .66), Y(1.13), R["pia"], anc="end"))
    xj = X(xrec) + (CW - X(xrec)) / 2
    em_pe = lambda y, txt, cor: (f'<text x="{xj:.2f}" y="{Y(y):.2f}" text-anchor="middle" font-size="2.2" font-weight="700" class="mono" '
                                 f'fill="{cor}" transform="rotate(-90 {xj:.2f} {Y(y):.2f})">{E(txt)}</text>')
    s.append(em_pe(1.1, R["janela"], PSJ_AZUL) + em_pe(2.2, R["recuo"], "#3F6E35"))
    return _psj_svg("".join(s))


def psj_corte(tipo):
    """Croquis 3 e 4: a casa como uma fatia. Esquema: a planta não tem telhado, forro nem laje nos dados."""
    R = TX.PAREDE["rotulos"]
    CW, CH, PD = PSJ_CW, PSJ_CH, PSJ_PD
    AZUL, TINTA, CINZA = PSJ_AZUL, PSJ_TINTA, PSJ_CINZA
    k = 7.0
    chao = CH - 5.0                                  # linha do piso, em mm
    X = lambda x: PD + x * k
    Y = lambda h: chao - h * k
    larg = 5.0                                       # casa do esquema, em metros (não é das 3 casas)
    VID = EST_REVISTA["vidro"]
    s = [f'<rect x="0" y="{chao:.2f}" width="{CW:.2f}" height="{CH - chao:.2f}" fill="url(#psj-terra)"/>'
         f'<line x1="0" y1="{chao:.2f}" x2="{CW:.2f}" y2="{chao:.2f}" stroke="{TINTA}" stroke-width=".35"/>']
    pare = lambda x, h0, h1, w=.15: f'<rect x="{X(x):.2f}" y="{Y(h1):.2f}" width="{w * k:.2f}" height="{(h1 - h0) * k:.2f}" fill="#8F887C"/>'
    telha = lambda pts: ('<path d="M' + " L".join(f"{X(a):.2f} {Y(b):.2f}" for a, b in pts) + '" fill="none" stroke="#9C5B3B" stroke-width="1.1" stroke-linecap="square"/>')
    rot = _psj_rot
    jan_baixa = lambda h0, h1: f'<line x1="{X(larg - .08):.2f}" y1="{Y(h1):.2f}" x2="{X(larg - .08):.2f}" y2="{Y(h0):.2f}" stroke="{VID}" stroke-width=".8"/>'
    if tipo == 3:
        hb, ha = 2.8, 3.55                           # telhado baixo e o do meio, mais alto
        xa0, xa1 = 1.6, 3.4
        s.append(f'<rect x="{X(0):.2f}" y="{Y(2.7):.2f}" width="{larg * k:.2f}" height="{2.7 * k:.2f}" fill="#FBF7EF"/>'
                 f'<rect x="{X(xa0):.2f}" y="{Y(3.45):.2f}" width="{(xa1 - xa0) * k:.2f}" height="{.75 * k:.2f}" fill="#FBF7EF"/>')
        s.append(pare(xa1 - .07, 2.7, 2.85, .14) + pare(xa1 - .07, 3.35, 3.5, .14) + pare(xa0 - .07, 2.7, 3.5, .14) + pare(larg - .15, 0, 2.7))
        s.append(jan_baixa(1.0, 2.1))
        s.append(telha([(0, hb), (xa0, hb)]) + telha([(xa0 - .1, ha), (xa1 + .2, ha)]) + telha([(xa1, hb), (larg + .3, hb - .2)]))
        # rufo no encontro do telhado baixo com a parede da faixa de janela
        s.append(f'<path d="M{X(xa1) - .1:.2f} {Y(3.0):.2f} V{Y(2.8) - .2:.2f} H{X(xa1) + 2.2:.2f}" fill="none" stroke="{AZUL}" stroke-width=".6"/>')
        s.append(_psj_chamada(X(xa1) + 1.6, Y(2.8), X(larg) + .8, Y(2.8) + 5.0, AZUL) + rot(X(larg) + 1.2, Y(2.8) + 5.8, R["rufo"], AZUL))
        # o sol: entra pela faixa de janela e desce no cômodo escuro
        s.append(_psj_seta([(CW - 1.8, Y(3.1) - 2.2), (X(xa1) + .3, Y(3.1)), (X(2.65), Y(.35))]))
        # a faixa de janela por cima da seta (a seta passa por ela), com o nome
        s.append(f'<rect x="{X(xa1) - .7:.2f}" y="{Y(3.35):.2f}" width="1.4" height="{.5 * k:.2f}" fill="#fff" stroke="{TINTA}" stroke-width=".25"/>'
                 f'<line x1="{X(xa1):.2f}" y1="{Y(3.35):.2f}" x2="{X(xa1):.2f}" y2="{Y(2.85):.2f}" stroke="{VID}" stroke-width=".8"/>')
        yc = Y(ha) - 3.0
        s.append(f'<g stroke="{AZUL}" stroke-width=".3"><line x1="{X(0):.2f}" y1="{yc:.2f}" x2="{X(xa1):.2f}" y2="{yc:.2f}"/>'
                 f'<line x1="{X(0):.2f}" y1="{yc - 1:.2f}" x2="{X(0):.2f}" y2="{yc + 1:.2f}"/><line x1="{X(xa1):.2f}" y1="{yc - 1:.2f}" x2="{X(xa1):.2f}" y2="{yc + 1:.2f}"/></g>')
        s.append(_psj_pilula((X(0) + X(xa1)) / 2, yc, R["distancia"], 2.2, cor=AZUL))
        s.append(rot(X(xa1) + 2.0, yc + .8, R["janela_alta"], AZUL) + _psj_chamada(X(xa1) + .5, Y(3.25), X(xa1) + 2.6, yc + 1.6, AZUL))
        s.append(rot(X(1.3), Y(1.3), R["comodo_escuro"][0], CINZA, 2.1) + rot(X(1.3), Y(1.3) + 2.6, R["comodo_escuro"][1], CINZA, 2.1))
    else:
        hd, hr, hf = 2.85, 3.6, 2.55                 # telhado de uma água: baixo na divisa (calha), alto no recuo; forro
        xt0, xt1 = 1.3, 2.1                          # a telha clara, longe da janela
        alt = lambda x: hd + (hr - hd) * x / larg
        xm = (xt0 + xt1) / 2
        s.append(f'<rect x="{X(0):.2f}" y="{Y(hf):.2f}" width="{larg * k:.2f}" height="{hf * k:.2f}" fill="#FBF7EF"/>')
        s.append(pare(larg - .15, 0, alt(larg)) + jan_baixa(1.2, 2.2))
        s.append(f'<g stroke="#8F887C" stroke-width=".7"><line x1="{X(0):.2f}" y1="{Y(hf):.2f}" x2="{X(xt0):.2f}" y2="{Y(hf):.2f}"/>'
                 f'<line x1="{X(xt1):.2f}" y1="{Y(hf):.2f}" x2="{X(larg - .15):.2f}" y2="{Y(hf):.2f}"/></g>'
                 f'<g stroke="#8F887C" stroke-width=".35"><line x1="{X(xt0):.2f}" y1="{Y(hf):.2f}" x2="{X(xt0):.2f}" y2="{Y(alt(xt0)):.2f}"/>'
                 f'<line x1="{X(xt1):.2f}" y1="{Y(hf):.2f}" x2="{X(xt1):.2f}" y2="{Y(alt(xt1)):.2f}"/></g>')
        s.append(telha([(.1, hd), (xt0, alt(xt0))]) + telha([(xt1, alt(xt1)), (larg + .3, alt(larg + .3))]))
        s.append(f'<line x1="{X(xt0):.2f}" y1="{Y(alt(xt0)):.2f}" x2="{X(xt1):.2f}" y2="{Y(alt(xt1)):.2f}" stroke="#BFE3FA" stroke-width="1.1"/>'
                 f'<line x1="{X(xt0):.2f}" y1="{Y(alt(xt0)) - .55:.2f}" x2="{X(xt1):.2f}" y2="{Y(alt(xt1)) - .55:.2f}" stroke="{AZUL}" stroke-width=".25"/>')
        s.append(f'<ellipse cx="{X(xm):.2f}" cy="{chao - .5:.2f}" rx="{(xt1 - xt0) * k * .75:.2f}" ry=".9" fill="{PSJ_FITA}" opacity=".6"/>')
        s.append(_psj_seta([(X(xm) + 8.0, Y(alt(xm)) - 7.0), (X(xm), Y(alt(xm)) - .3), (X(xm), chao - 2.4)]))
        # a calha do lado da divisa, o cano descendo do lado de dentro e a água seguindo para o lote
        cx = X(.0)
        s.append(f'<path d="M{cx:.2f} {Y(hd) - .3:.2f} v1.5 h2.4 v-1.5" fill="#fff" stroke="{AZUL}" stroke-width=".45"/>')
        s.append(f'<line x1="{cx + 1.2:.2f}" y1="{Y(hd) + 1.2:.2f}" x2="{cx + 1.2:.2f}" y2="{chao - 1.0:.2f}" stroke="{AZUL}" stroke-width=".6"/>')
        s.append(_psj_seta([(cx + 1.2, chao - 1.0), (X(.95), chao - 1.0)], cor="#7FC3E8", larg=.7, borda=AZUL))
        s.append(_psj_chamada(X(xt0) + .6, Y(alt(xt0)) - .8, X(.6), Y(hd) - 5.2, AZUL) + rot(X(.1) - 1.0, Y(hd) - 8.2, R["telha"][0], AZUL, 2.1) + rot(X(.1) - 1.0, Y(hd) - 5.7, R["telha"][1], AZUL, 2.1))  # em 2 linhas: não encosta na seta do sol
        s.append(_psj_chamada(X(xt1) - .2, Y(hf) + .3, X(2.3), Y(hf) + 3.2) + rot(X(2.3) + .5, Y(hf) + 4.0, R["vao"], fs=2.1))
        s.append(rot(cx + 2.4, Y(hf) + 4.0, R["calha"], AZUL))
        s.append(rot(X(2.35), Y(.75), R["agua"][0], AZUL, 2.1) + rot(X(2.35), Y(.75) + 2.6, R["agua"][1], AZUL, 2.1))
    topo = 3.0 if tipo == 3 else 5.0
    s.append(_psj_parede(topo, chao - topo))
    return _psj_svg("".join(s), R["esquema"])


def pagina_parede(L, por_id, orelha=None):
    """A página inteira: cabeçalho (título, subtítulo, abertura), as 4 ideias com o croqui e o número na parede,
    a caixa "Leve ao engenheiro" e o aviso legal no rodapé."""
    import re
    P = TX.PAREDE
    R = P["rotulos"]
    casa = por_id.get(PSJ_CASA) or next(p for p in PL.carregar() if p["id"] == PSJ_CASA)
    # número e unidade, "art." e o número, e "10 x 20 cm" não se separam na quebra de linha
    nb = lambda t: re.sub(r"\(art\. ([\d.]+)", "(art.\u00a0\\1", re.sub(r"(\d) (m²|m|cm)\b", "\\1\u00a0\\2", E(t))).replace("10 x 20\u00a0cm", "10\u00a0x\u00a020\u00a0cm")
    figs = [psj_croqui_quarto(casa), psj_croqui_cozinha(), psj_corte(3), psj_corte(4)]
    classes = ("faz", "cuid", "casas")
    ideias = "".join(
        f'<article class="ideia"><span class="nm">{i}</span><figure>{fig}</figure><div><h3>{E(it["nome"])}</h3>'
        + "".join(f'<p class="{c}"><b>{E(r)}</b>{nb(it[c])}</p>' for c, r in zip(classes, P["campos"])) + "</div></article>"
        for i, (it, fig) in enumerate(zip(P["ideias"], figs), 1))
    muro = f'<div class="muro"><span class="rot">{E(R["muro"])}</span></div><span class="vizinho">{E(R["vizinho"])}</span>'
    cabecalho = (f'<header class="cab-psj"><div><span class="sobre">{E(P["sobre"])}</span><h2>{E(P["titulo"])}</h2>'
                 f'<p class="sub">{E(P["sub"])}</p></div><p class="abre">{nb(P["abre"])}</p></header>')
    eng = (f'<section class="eng"><h3>{E(P["engenheiro"])}<span class="selo-psj"><span>{E(R["selo"][0])}</span>{E(R["selo"][1])}</span></h3>'
           f'<ol>{"".join(f"<li>{nb(q)}</li>" for q in P["perguntas"])}</ol></section>')
    return L.pagina(f"{muro}{cabecalho}{ideias}{eng}", "q psj", orelha=orelha, aviso=True)


# ------------------------------------------------------------------ páginas "cômodo a cômodo" de cada casa (D20)
# Parte 1 (cada casa) do modo --duas-partes, só prévia: 2 páginas depois da dupla da casa. O desenho é o do rascunho do
# Designer (ebook/plantas/rascunhos/comodo_a_comodo.py, A9 e D31): a planta do e-book (svg_humanizada) com a parede de
# cada número pintada de amarelo. Texto e rótulos: paginas.py (COMODOS e COMODO). Toda medida desenhada sai dos dados
# e do validador e é conferida contra o texto: se não bater, o gerador avisa e falha (_ca_aviso).
CA_TINTA, CA_AZUL, CA_FITA, CA_CINZA = "#17202B", "#0B4FA8", "#FFC857", "#4F5B69"
CA_VERDE = "#1B6E35"   # F01: área aberta (faixa livre, fundo); o tracejado azul é a veneziana da C01
CA_LARG = 176          # largura do miolo da folha, em mm (210 menos as margens de 17)


def _ca_aviso(txt):
    """Dado que não bate com o texto aprovado: avisa e impede a entrega (gerar() falha com AVISOS)."""
    txt = "cômodo a cômodo: " + txt
    if txt not in AVISOS:
        AVISOS.append(txt)
        print("AVISO:", txt)


def _ca_nb(txt):
    """Número e unidade não se separam na quebra de linha ("1,86 m", "46 e 51 cm", "12,5 m²")."""
    return re.sub(r"(\d) (m²|m|cm)\b", "\\1\u00a0\\2", txt)


class _CaGeo:
    """Paredes, portas e móveis do desenho do e-book (a mesma geometria do svg_humanizada e do 3D), em metros."""

    def __init__(self, p):
        self.p = p
        self.caixas, _, self.portas, moveis = _geometria(p)
        self.mov = _moveis_sem_choque(p["id"], moveis)
        self.com = {c["id"]: c for c in p["comodos"]}
        fut = [c for c in p["comodos"] if c["tipo"] == "futuro"]
        self.Dm = max([p["D"]] + [c["y1"] for c in fut])

    def caixa(self, mv, cad=True):
        """Caixa do móvel em metros (x0, y0, x1, y1), y para o fundo; com as cadeiras da mesa e da escrivaninha."""
        t, w, d = mv["tipo"], mv.get("w", .45), mv.get("d", .4)
        if t == "criado":
            w, d = .44, .4
        if t == "vaso":
            w, d = .4, .62
        if t == "mesaJantar" and cad:
            w += .62
        if t == "escrivaninha" and cad:
            d += .84
        r = mv.get("rot", 0) or 0
        c, s = abs(math.cos(r)), abs(math.sin(r))
        hw, hd = c * w / 2 + s * d / 2, s * w / 2 + c * d / 2
        return (mv["x"] - hw, mv["y"] - hd, mv["x"] + hw, mv["y"] + hd)

    def mv(self, tipo, amb, i=0, cad=True):
        achados = sorted((m for m in self.mov if m["tipo"] == tipo and m.get("amb") == amb), key=lambda m: (m["x"], m["y"]))
        return self.caixa(achados[i], cad)

    def face(self, cid, lado):
        """Face de dentro da parede do cômodo (as paredes de verdade, P3.paredes_reais); sem parede, a linha do cômodo."""
        c = self.com[cid]
        ov = lambda a0, a1, b0, b1: min(a1, b1) - max(a0, b0)
        if lado in ("x0", "x1"):
            v = c[lado]
            ws = [b for b in self.caixas if b[0] - 1e-6 <= v <= b[2] + 1e-6 and ov(b[1], b[3], c["y0"], c["y1"]) > .3]
            return (max(b[2] for b in ws) if lado == "x0" else min(b[0] for b in ws)) if ws else v
        v = c[lado]
        ws = [b for b in self.caixas if b[1] - 1e-6 <= v <= b[3] + 1e-6 and ov(b[0], b[2], c["x0"], c["x1"]) > .3]
        return (max(b[3] for b in ws) if lado == "y0" else min(b[1] for b in ws)) if ws else v

    def obstaculos(self):
        """Móveis (sem o tapete) e giros de porta, em metros (y para o fundo)."""
        obs = [self.caixa(m) for m in self.mov if m["tipo"] != "tapete"]
        giros = []
        for d in self.portas:
            H, A, B = PL.porta_dobradica(self.p, d)
            giros.append((H, d["r"], (min(H[0], A[0], B[0]), min(H[1], A[1], B[1]), max(H[0], A[0], B[0]), max(H[1], A[1], B[1]))))
        return obs, giros


def _ca_etiquetas(svg, Dm):
    """As pílulas com o nome do cômodo que o svg_humanizada escolheu, em metros (y para o fundo)."""
    r = []
    for cx, cy, k, x, y, w, h in re.findall(r'<g transform="translate\(([-\d.]+) ([-\d.]+)\) scale\(([\d.]+)\) translate\([^)]*\)"><rect x="([-\d.]+)" y="([-\d.]+)" width="([\d.]+)" height="([\d.]+)"', svg):
        cx, cy, k, x, y, w, h = map(float, (cx, cy, k, x, y, w, h))
        sx0, sy0 = cx + (x - .03 - cx) * k, cy + (y - .05 - cy) * k
        sx1, sy1 = cx + (x + w - cx) * k, cy + (y + h - cy) * k
        r.append((sx0, Dm - sy1, sx1, Dm - sy0))
    return r


def _ca_num(v):
    """10.0 -> "10"; 12.8 -> "12,8" (lote e recuo, como no texto)."""
    return f"{v:g}".replace(".", ",")


def _ca_cm(v):
    """Metros em centímetros, como no texto ("91 cm"; "22,5 cm")."""
    return f"{v * 100:.1f}".replace(".", ",").removesuffix(",0") + " cm"


def _ca_conferir_util(p, T, por_n):
    U = p["_r"].metricas["util"]
    for it in T["itens"]:
        if it["n"] in por_n:
            w, d, _ = U[por_n[it["n"]]]
            if it["dim"] != f"{m(w)} x {m(d)} m":
                _ca_aviso(f"lugar {it['n']}: texto {it['dim']}, validador {m(w)} x {m(d)} m")


def _ca_no_texto(txt, *onde):
    """A medida do desenho está no texto? Se não, avisa e a cota não sai."""
    if any(txt in o for o in onde):
        return True
    _ca_aviso(f"o desenho mede {txt}; o texto não traz esse número (cota não desenhada)")
    return False


# ------------------------------------------------------------------ a planta com as marcas (tudo em metros, por cima do desenho)
class _CaPlanta:
    """O desenho do e-book (svg_humanizada) com o recuo da direita inteiro, as paredes marcadas e os números.
    O que muda de casa para casa (marcas, números, cotas) está em self.casa (classes E03, F01, C01 abaixo)."""

    def __init__(self, p, T, casa):
        self.p, self.T, self.casa = p, T, casa
        self.g = _CaGeo(p)
        self.Dm = self.g.Dm
        self.W, self.D = p["W"], p["D"]
        self.n = len(T["itens"])
        self.rec = p["_r"].metricas["recuos"]["dir"]
        casa.conferir(self)
        svg = svg_humanizada(p)
        com_item = casa.com_item
        Dm = self.Dm

        def tira(mt):  # o nome do cômodo com número sai: o nome está na linha do número (mesma regra do mobiliar.py)
            cx, cy = map(float, re.match(r'<g transform="translate\(([-\d.]+) ([-\d.]+)\)', mt.group(0)).groups())
            dentro = [c["id"] for c in p["comodos"] if c["x0"] <= cx <= c["x1"] and c["y0"] <= Dm - cy <= c["y1"]]
            return "" if dentro and dentro[0] in com_item else mt.group(0)
        svg = re.sub(r'<g transform="translate\([-\d.]+ [-\d.]+\) scale\([\d.]+\) translate\([^)]*\)">.*?</g>', tira, svg)
        self.etq = _ca_etiquetas(svg, Dm)
        # o desenho do livro mostra só 0,70 m do recuo da direita; aqui ele vai inteiro (1,50 m), com a divisa do lote
        K = ESTILOS["revista"]["piso"]
        S = ESTILOS["revista"]
        W, xr = self.W, self.W + self.rec
        fundo = (
            _piso("grama", W, -.7, self.rec, Dm + 1.95, K)
            + _piso("calcada", W, Dm + 1.25, self.rec + 1, .42, K)
            + f'<rect x="{W}" y="{Dm + 1.67:.3f}" width="{self.rec + 1}" height="1" fill="{S["rua"]}"/>')
        hach = "".join(f"M{xr:.3f} {yy + .12:.3f}l.12 -.12" for yy in [-.7 + k * .12 for k in range(int((Dm + 1.95) / .12))])
        muro = (f'<rect x="{xr:.3f}" y="-.7" width=".12" height="{Dm + 1.95:.3f}" fill="#E4E1DA" stroke="#8F887C" stroke-width=".01"/>'
                f'<path d="{hach}" stroke="#B5AFA4" stroke-width=".02"/>')
        # F01: o fundo do lote entra até o recuo de fundos do lote mínimo (1,5 m), por cima da cota "casa" do livro
        ef = casa.fundo_extra(self)
        if ef:
            y0 = -ef
            hach_e = lambda x: "".join(f"M{x:.3f} {yy + .12:.3f}l.12 -.12" for yy in [y0 + k * .12 for k in range(int((ef - .7) / .12) + 1)])
            muro += (_piso("grama", 0, y0, xr, ef - .7 + .02, K)
                     + f'<rect x="-.08" y="{y0:.3f}" width=".08" height="{ef - .7:.3f}" fill="#fff"/>'
                     + f'<rect x="-.2" y="{y0:.3f}" width=".12" height="{ef - .7:.3f}" fill="#E4E1DA" stroke="#8F887C" stroke-width=".01"/>'
                     + f'<path d="{hach_e(-.2)}" stroke="#B5AFA4" stroke-width=".02"/>'
                     + f'<rect x="{xr:.3f}" y="{y0:.3f}" width=".12" height="{ef - .7:.3f}" fill="#E4E1DA" stroke="#8F887C" stroke-width=".01"/>'
                     + f'<path d="{hach_e(xr)}" stroke="#B5AFA4" stroke-width=".02"/>')
        i = svg.index(">") + 1
        self.base = svg[:i] + fundo + svg[i:].rsplit("</svg>", 1)[0] + muro

    # coordenadas: x do validador; y da tela = Dm - y (frente embaixo)
    def Y(self, y):
        return self.Dm - y

    def parede(self, eixo, v, a, b):
        """Retângulos (tela) da parede que passa em x=v (eixo 'x') ou y=v (eixo 'y'), entre a e b."""
        r = []
        for b0, b1, b2, b3 in self.g.caixas:
            if eixo == "x" and b0 <= v <= b2 and min(b, b3) - max(a, b1) > .02:
                r.append((b0, self.Y(min(b, b3)), b2 - b0, min(b, b3) - max(a, b1)))
            if eixo == "y" and b1 <= v <= b3 and min(b, b2) - max(a, b0) > .02:
                r.append((max(a, b0), self.Y(b3), min(b, b2) - max(a, b0), b3 - b1))
        return r

    def par(self, eixo, v, a, b):
        """Como parede(), só com as paredes que correm na direção do eixo pedido (parede() também pega a parede
        que cruza a linha; na Casa Fita isso não acontece nos trechos marcados, e ela fica como está)."""
        return [r for r, c in zip(self.parede(eixo, v, a, b), [c for c in self.g.caixas if self._cruza(c, eixo, v, a, b)])
                if (c[3] - c[1] >= c[2] - c[0]) == (eixo == "x")]

    @staticmethod
    def _cruza(c, eixo, v, a, b):
        b0, b1, b2, b3 = c
        if eixo == "x":
            return b0 <= v <= b2 and min(b, b3) - max(a, b1) > .02
        return b1 <= v <= b3 and min(b, b2) - max(a, b0) > .02

    # --- as tintas: parede inteira, meia parede (o lado de um cômodo), faixa por fora (parede com janela), sem parede
    @staticmethod
    def pinta(rs):
        return "".join(f'<rect x="{x + .02:.3f}" y="{y:.3f}" width="{max(.02, w - .04):.3f}" height="{h:.3f}" fill="{CA_FITA}" stroke="{CA_TINTA}" stroke-width=".018"/>' for x, y, w, h in rs)

    @staticmethod
    def pinta_h(rs):
        return "".join(f'<rect x="{x:.3f}" y="{y + .02:.3f}" width="{w:.3f}" height="{max(.02, h - .04):.3f}" fill="{CA_FITA}" stroke="{CA_TINTA}" stroke-width=".018"/>' for x, y, w, h in rs)

    def meia(self, eixo, v, a, b, lado):
        """A metade da espessura da parede do lado de um cômodo (lado '+' = x maior ou mais para o fundo):
        quando dois números apontam a mesma parede, cada um pinta a sua face."""
        s = []
        for x, y, w, h in self.par(eixo, v, a, b):
            if eixo == "x":
                x, w = (x + w / 2, w / 2) if lado == "+" else (x, w / 2)
            else:
                y, h = (y, h / 2) if lado == "+" else (y + h / 2, h / 2)
            s.append(f'<rect x="{x:.3f}" y="{y:.3f}" width="{w:.3f}" height="{h:.3f}" fill="{CA_FITA}" stroke="{CA_TINTA}" stroke-width=".008"/>')
        return "".join(s)

    def fora_v(self, y0, y1, x=None, lado="+"):
        """Faixa amarela rente à parede vertical em x, por fora dela (lado '+': à direita), entre y0 e y1."""
        x = self.W if x is None else x
        xx = x + .03 if lado == "+" else x - .14
        return f'<rect x="{xx:.3f}" y="{self.Y(y1):.3f}" width=".11" height="{y1 - y0:.3f}" fill="{CA_FITA}" stroke="{CA_TINTA}" stroke-width=".018"/>'

    def fora_h(self, x0, x1, y):
        return f'<rect x="{x0:.3f}" y="{self.Y(y) - .14:.3f}" width="{x1 - x0:.3f}" height=".11" fill="{CA_FITA}" stroke="{CA_TINTA}" stroke-width=".018"/>'

    def sem_parede(self, eixo, v, a, b):
        """Pontilhado amarelo na linha onde o desenho não tem parede (o lado aberto, a divisa sem muro)."""
        n = max(2, int(abs(b - a) / .2))
        pts = [(v, a + (b - a) * k / n) if eixo == "x" else (a + (b - a) * k / n, v) for k in range(n + 1)]
        return "".join(f'<circle cx="{x:.3f}" cy="{self.Y(y):.3f}" r=".055" fill="{CA_FITA}" stroke="{CA_TINTA}" stroke-width=".016"/>' for x, y in pts)

    def por_cima(self, x0, y0, x1, y1):
        """Tracejado bege: o que fica por cima (maleiro)."""
        return f'<rect x="{x0:.3f}" y="{self.Y(y1):.3f}" width="{x1 - x0:.3f}" height="{y1 - y0:.3f}" fill="{CA_FITA}" fill-opacity=".28" stroke="{CA_TINTA}" stroke-width=".025" stroke-dasharray=".12 .08"/>'

    def area_aberta(self, x0, y0, x1, y1, cor=CA_AZUL, aberto_em_cima=False):
        """Tracejado (azul na Casa Fita; verde na F01): área aberta. aberto_em_cima: o lote continua além do desenho,
        o lado de cima fica sem tracejado e leva a marca de corte."""
        if not aberto_em_cima:
            return f'<rect x="{x0:.3f}" y="{self.Y(y1):.3f}" width="{x1 - x0:.3f}" height="{y1 - y0:.3f}" fill="none" stroke="{cor}" stroke-width=".035" stroke-dasharray=".2 .12"/>'
        Y = self.Y
        return f'<path d="M{x0:.3f} {Y(y1):.3f}V{Y(y0):.3f}H{x1:.3f}V{Y(y1):.3f}" fill="none" stroke="{cor}" stroke-width=".035" stroke-dasharray=".2 .12"/>' + self.corte(x0, x1, y1)

    def corte(self, x0, x1, y):
        """Marca de corte (linha de interrupção com o zigue-zague no meio): o terreno continua além do desenho."""
        Y, xm = self.Y(y), (x0 + x1) / 2
        return (f'<path d="M{x0 - .05:.3f} {Y:.3f}H{xm - .18:.3f}L{xm - .08:.3f} {Y - .16:.3f}L{xm + .08:.3f} {Y + .16:.3f}L{xm + .18:.3f} {Y:.3f}H{x1 + .05:.3f}" '
                f'fill="none" stroke="{CA_TINTA}" stroke-width=".025" stroke-linejoin="round"/>')

    def marcas(self, so=None):
        m = self.casa.marcas(self)
        return "".join(v for n, v in m.items() if so is None or n in so)

    def obstaculos(self, k):
        obs, giros = self.g.obstaculos()
        return obs + [gb for _, _, gb in giros] + list(self.etq)

    def lugar(self, cid, pref, r, extra=()):
        """Ponto do número no chão livre do cômodo, o mais perto possível de pref (metros, y do validador)."""
        g = self.g
        x0, x1, y0, y1 = g.face(cid, "x0"), g.face(cid, "x1"), g.face(cid, "y0"), g.face(cid, "y1")
        obs, giros = g.obstaculos()
        ocup = obs + list(extra) + [(a, self.Dm - d, c, self.Dm - b) for a, b, c, d in self.etq]
        melhor = None
        for i in range(41):
            for j in range(41):
                x = x0 + r + .05 + (x1 - x0 - 2 * r - .1) * i / 40
                y = y0 + r + .05 + (y1 - y0 - 2 * r - .1) * j / 40
                bb = (x - r - .04, y - r - .04, x + r + .04, y + r + .04)
                duro = sum(_inter(bb, o) for o in ocup)
                for (hx, hy), rr, gb in giros:
                    if _inter(bb, gb) > 0 and math.hypot(x - hx, y - hy) < rr + r + .03:
                        duro += .05
                sc = duro * 1000 + math.hypot(x - pref[0], y - pref[1])
                if melhor is None or sc < melhor[0]:
                    melhor = (sc, x, y, duro)
        if melhor[3] > 0:
            _ca_aviso(f"número em {cid}: encosta em móvel, porta ou etiqueta ({melhor[3]:.3f} m²)")
        return melhor[1], melhor[2]

    def numero(self, x, y, n, r, grande=False):
        Y = self.Y(y)
        anel = f'<circle cx="{x:.3f}" cy="{Y:.3f}" r="{r * 1.32:.3f}" fill="none" stroke="{CA_TINTA}" stroke-width="{r * .07:.3f}" stroke-dasharray="{r * .2:.3f} {r * .14:.3f}"/>' if grande else ""
        return (f'{anel}<circle cx="{x:.3f}" cy="{Y + r * .13:.3f}" r="{r:.3f}" fill="{CA_TINTA}" opacity=".25"/>'
                f'<circle cx="{x:.3f}" cy="{Y:.3f}" r="{r:.3f}" fill="{CA_FITA}" stroke="{CA_TINTA}" stroke-width="{r * .15:.3f}"/>'
                f'<text x="{x:.3f}" y="{Y + r * .45:.3f}" text-anchor="middle" font-size="{r * 1.33:.3f}" font-weight="800" class="tit" fill="{CA_TINTA}">{n}</text>')

    def pilula(self, x, y, txt, fs, rot=0, cor=CA_AZUL):
        w, h = len(txt) * fs * .62 + fs * .7, fs * 1.45
        return (f'<g transform="translate({x:.3f} {self.Y(y):.3f}) rotate({rot})"><rect x="{-w / 2:.3f}" y="{-h / 2:.3f}" width="{w:.3f}" height="{h:.3f}" rx="{h / 2:.3f}" fill="#fff" stroke="{cor}" stroke-width="{fs * .09:.3f}"/>'
                f'<text x="0" y="{fs * .36:.3f}" text-anchor="middle" font-size="{fs:.3f}" font-weight="700" class="mono" fill="{cor}">{E(txt)}</text></g>')

    @staticmethod
    def caixa_pilula(x, y, txt, fs, rot=0):
        """A caixa (metros, y do validador) que a pílula ocupa: os números não sentam nela."""
        w, h = len(txt) * fs * .62 + fs * .7, fs * 1.45
        if rot:
            w, h = h, w
        return (x - w / 2, y - h / 2, x + w / 2, y + h / 2)

    def cota(self, ax, bx, y, txt, fs, px=None):
        Y, t = self.Y(y), fs * .35
        return (f'<g stroke="{CA_AZUL}" stroke-width="{fs * .1:.3f}" fill="none"><line x1="{ax:.3f}" y1="{Y:.3f}" x2="{bx:.3f}" y2="{Y:.3f}"/>'
                f'<line x1="{ax:.3f}" y1="{Y - t:.3f}" x2="{ax:.3f}" y2="{Y + t:.3f}"/><line x1="{bx:.3f}" y1="{Y - t:.3f}" x2="{bx:.3f}" y2="{Y + t:.3f}"/></g>'
                + self.pilula((ax + bx) / 2 if px is None else px, y, txt, fs))

    def cota_v(self, x, ay, by, txt, fs, py=None):
        t = fs * .35
        return (f'<g stroke="{CA_AZUL}" stroke-width="{fs * .1:.3f}"><line x1="{x:.3f}" y1="{self.Y(ay):.3f}" x2="{x:.3f}" y2="{self.Y(by):.3f}"/>'
                f'<line x1="{x - t:.3f}" y1="{self.Y(ay):.3f}" x2="{x + t:.3f}" y2="{self.Y(ay):.3f}"/><line x1="{x - t:.3f}" y1="{self.Y(by):.3f}" x2="{x + t:.3f}" y2="{self.Y(by):.3f}"/></g>'
                + self.pilula(x, (ay + by) / 2 if py is None else py, txt, fs, rot=-90))

    def svg(self, k, recorte, so=None, rn=2.6, rn3=3.6, fs_mm=2.5, zoom=False):
        """SVG em mm. recorte = (x0, x1, y_fundo, y_frente) em metros do validador. k = mm por metro."""
        x0, x1, yf, yr = recorte
        vx, vy, vw, vh = x0, self.Y(yf), x1 - x0, yf - yr
        r, r3, fs = rn / k, rn3 / k, fs_mm / k
        so = set(so or range(1, self.n + 1))
        s = [self.base]
        s += self.casa.chao(self, so, zoom)
        s.append(self.marcas(so))
        extra = []
        s += self.casa.medidas(self, so, zoom, fs, extra)
        s += self.casa.numeros(self, so, zoom, r, r3, fs, extra, s)
        s.append("</svg>")
        out = "".join(s)
        out = re.sub(r'^<svg viewBox="[^"]*"', f'<svg viewBox="{vx:.3f} {vy:.3f} {vw:.3f} {vh:.3f}" width="{vw * k:.2f}mm" height="{vh * k:.2f}mm"', out)
        return out, vw * k, vh * k

    def numeros_em(self, so, zoom, r, r3, fs, extra, prefs, destaque):
        """Os números no chão livre de cada cômodo (prefs: n -> (cômodo, ponto preferido))."""
        nums = []
        for n in sorted(so):
            if n not in prefs:
                continue
            cid, pref = prefs[n]
            rr = r3 if n == destaque else r
            if cid is None:   # ponto fixo, fora de cômodo (recuo, fundo)
                x, y = pref
            else:
                x, y = self.lugar(cid, pref, rr * (1.32 if n == destaque else 1), extra)
            extra.append((x - rr, y - rr, x + rr, y + rr))
            nums.append(self.numero(x, y, n, rr, grande=(n == destaque)))
        return nums


# ------------------------------------------------------------------ Casa Fita (E03): o desenho da prova de 24/11, sem mudança
class _CaE03:
    id, destaque = "E03", 3
    com_item = {"quarto2", "sala", "cozinha", "circ", "banho", "quarto1"}

    def fundo_extra(self, P):
        return 0

    def conferir(self, P):
        p, T = P.p, P.T
        _ca_conferir_util(p, T, {1: "quarto2", 2: "sala", 3: "cozinha", 4: "banho", 5: "circ", 6: "quarto1"})
        rec = p["_r"].metricas["recuos"]["dir"]
        if T["itens"][6]["dim"] != f"{m1(rec)} x {m1(p['D'])} m":
            _ca_aviso(f"lugar 7: texto {T['itens'][6]['dim']}, dados {m1(rec)} x {m1(p['D'])} m")
        _, jan, portas, _ = _geometria(p)
        jc = next(j for j in jan if j["id"] == "cozinha")["seg"]
        if f"{m(abs(jc[3] - jc[1]))} m" not in T["itens"][2]["ideia"]:
            _ca_aviso(f"janela da cozinha: desenho {m(abs(jc[3] - jc[1]))} m, não está no texto")
        pc = PL.porta_dobradica(p, next(d for d in portas if d["id"] == "ext-cozinha"))
        vao = min(pc[0][1], pc[1][1]) - jc[3]
        # 22,5 cm: o número exato dos dados, sem arredondar (decisão do Maestro, 24/11, veto-pagina-prova-E03-2026-11-24.md)
        if _ca_cm(vao) not in T["itens"][2]["ideia"]:
            _ca_aviso(f"cozinha: entre a janela e a porta, o desenho tem {vao * 100:.1f} cm; o texto não traz esse número")
        P.jc, P.pc = jc, pc

    def marcas(self, P):
        """As paredes de cada número, pintadas de amarelo (a parede inteira de espessura, ou uma faixa por fora
        quando a parede tem janela, para não esconder a janela). Lugares e paredes: campo "Aponta" do texto."""
        Y, W, jc = P.Y, P.W, P.jc
        pinta, pinta_h, fora_v, fora_h = P.pinta, P.pinta_h, P.fora_v, P.fora_h
        return {
            # 1: tomada nas duas cabeceiras (divisa e recuo); nicho na divisa
            1: pinta(P.parede("x", .07, .75, 2.05)) + pinta(P.parede("x", 3.43, .3, 1.35)),
            # 2: o vão de 1,92 m é a cota (em medidas()); o cuidado é a porta do quarto da frente, no canto da divisa
            2: pinta_h([(.25, Y(3.16), .8, .12)]),
            # 3: a janela da pia (por fora, para não esconder a janela) e os 22,5 cm até a porta de fora
            3: fora_v(jc[1], jc[3]) + f'<rect x="{W + .03:.3f}" y="{Y(P.pc[1][1]):.3f}" width=".11" height="{P.pc[1][1] - jc[3]:.3f}" fill="{CA_TINTA}"/>',
            # 4: a parede do serviço (vaso e pia) e a janela dentro do box
            4: pinta_h(P.parede("y", 11.2, 1.16, 2.5)) + fora_v(11.5, 12.6),
            # 5: o maleiro por cima do hall (tracejado = por cima) e a parede da divisa do hall
            5: (f'<rect x=".2" y="{Y(12.84):.3f}" width=".8" height="{12.84 - 9.96:.3f}" fill="{CA_FITA}" fill-opacity=".28" stroke="{CA_TINTA}" stroke-width=".025" stroke-dasharray=".12 .08"/>'
                + pinta(P.parede("x", .07, 9.96, 12.84))),
            # 6: o interruptor na cabeceira (parede do recuo, ao lado do criado) e a janela do fundo
            6: pinta(P.parede("x", 3.43, 13.15, 13.9)) + fora_h(.8, 2.7, 16.1 + .14 + .03),
            # 7: o recuo inteiro (tracejado azul)
            7: (f'<rect x="{W + .2:.3f}" y="{Y(P.D):.3f}" width="{P.rec - .3:.3f}" height="{P.D:.3f}" fill="none" stroke="{CA_AZUL}" stroke-width=".035" stroke-dasharray=".2 .12"/>'),
        }

    def chao(self, P, so, zoom):
        if not zoom and 3 in so:   # a cozinha, destaque da página: o chão em amarelo claro
            g = P.g
            return [f'<rect x="{g.face("cozinha", "x0"):.3f}" y="{P.Y(g.face("cozinha", "y1")):.3f}" width="{g.face("cozinha", "x1") - g.face("cozinha", "x0"):.3f}" height="{g.face("cozinha", "y1") - g.face("cozinha", "y0"):.3f}" fill="{CA_FITA}" fill-opacity=".2"/>']
        return []

    def medidas(self, P, so, zoom, fs, extra):
        s, Wc = [], P.W
        if 2 in so:  # o vão de 1,92 m entre o rack e o sofá, medido no desenho; só sai se bater com o texto
            rk, sf = P.g.mv("rack", "sala"), P.g.mv("sofa", "sala")
            txt = m(sf[0] - rk[2])
            if txt + " m" in P.T["itens"][1]["ideia"]:
                yc = 4.55
                s.append(P.cota(rk[2], sf[0], yc, txt, fs))
                extra.append((rk[2], yc - fs, sf[0], yc + fs))
            else:
                _ca_aviso(f"sala: o desenho mede {txt} m entre o rack e o sofá; o texto não traz esse número (cota não desenhada)")
        if 3 in so:   # 1,70 da janela e os 22,5 cm, por fora, no recuo (os números saem do texto, conferidos em conferir())
            jc = P.jc
            m170 = re.search(r"(\d,\d\d) m", P.T["itens"][2]["ideia"]).group(1)
            m22 = re.search(r"(\d+(?:,\d+)? cm)", P.T["itens"][2]["ideia"]).group(1)
            xm = Wc + .42 if zoom else Wc + .55
            s.append(f'<g stroke="{CA_AZUL}" stroke-width="{fs * .1:.3f}"><line x1="{xm:.3f}" y1="{P.Y(jc[1]):.3f}" x2="{xm:.3f}" y2="{P.Y(jc[3]):.3f}"/>'
                     f'<line x1="{xm - fs * .35:.3f}" y1="{P.Y(jc[1]):.3f}" x2="{xm + fs * .35:.3f}" y2="{P.Y(jc[1]):.3f}"/><line x1="{xm - fs * .35:.3f}" y1="{P.Y(jc[3]):.3f}" x2="{xm + fs * .35:.3f}" y2="{P.Y(jc[3]):.3f}"/></g>')
            s.append(P.pilula(xm, (jc[1] + jc[3]) / 2, m170, fs, rot=-90))
            if zoom:  # os 22,5 cm, com linha de chamada até a faixa preta
                ym = (jc[3] + P.pc[1][1]) / 2
                s.append(f'<line x1="{Wc + .14:.3f}" y1="{P.Y(ym):.3f}" x2="{Wc + .9:.3f}" y2="{P.Y(ym + .45):.3f}" stroke="{CA_TINTA}" stroke-width="{fs * .08:.3f}"/>')
                s.append(P.pilula(Wc + 1.0, ym + .45, m22, fs, cor=CA_TINTA))
        return s

    def numeros(self, P, so, zoom, r, r3, fs, extra, s):
        nums, Wc = [], P.W
        prefs = {1: ("quarto2", (1.85, 1.75)), 2: ("sala", (1.8, 3.75)), 3: ("cozinha", (2.0, 8.0)),
                 4: ("banho", (2.0, 12.55)), 5: ("circ", (.6, 11.2)), 6: ("quarto1", (2.3, 13.35))}
        for n in sorted(so):
            if n == 7:
                if not zoom:
                    nums.append(P.numero(Wc + P.rec / 2 + .1, 11.5, 7, r))
                    s.append(f'<text x="{Wc + P.rec / 2 + .1:.3f}" y="{P.Y(10.6):.3f}" text-anchor="end" font-size="{fs * .95:.3f}" font-weight="700" class="mono" fill="{CA_AZUL}" transform="rotate(-90 {Wc + P.rec / 2 + .1:.3f} {P.Y(10.6):.3f})">{E(TX.COMODO["desenho"]["recuo"].format(P.T["itens"][6]["dim"].split(" x ")[0]))}</text>')
                continue
            cid, pref = prefs[n]
            rr = r3 if n == 3 else r
            x, y = P.lugar(cid, pref, rr * (1.32 if n == 3 else 1), extra)
            extra.append((x - rr, y - rr, x + rr, y + rr))
            nums.append(P.numero(x, y, n, rr, grande=(n == 3)))
        return nums

    def legenda(self):
        return _ca_legenda(self.id)


# ------------------------------------------------------------------ Casa Família Compacta (F01), 8,50 x 8,30
class _CaF01:
    id, destaque = "F01", 1
    com_item = {"sala", "cozinha", "servico", "banho", "circ", "quarto1", "quarto3"}

    def fundo_extra(self, P):
        # o desenho do livro mostra 0,70 m do fundo; aqui vai o recuo de fundos do lote mínimo (dados: recuos.fundos)
        return P.p["_r"].metricas["recuos"]["fundos"] + .1

    def conferir(self, P):
        p, T, g = P.p, P.T, P.g
        it = {i["n"]: i for i in T["itens"]}
        _ca_conferir_util(p, T, {1: "sala", 2: "cozinha", 3: "servico", 4: "banho", 5: "circ", 6: "quarto1", 7: "quarto3"})
        # 1: o ponto de luz no meio da mesa, medido por dentro das paredes da divisa e da frente
        mesa = g.mv("mesaJantar", "sala", cad=False)
        P.luz = ((mesa[0] + mesa[2]) / 2, (mesa[1] + mesa[3]) / 2)
        P.fx0, P.fy0 = g.face("sala", "x0"), g.face("sala", "y0")
        P.m_luz_x, P.m_luz_y = m(P.luz[0] - P.fx0), m(P.luz[1] - P.fy0)
        rk, sf = g.mv("rack", "sala"), g.mv("sofa", "sala")
        P.rk, P.sf, P.m_tv = rk, sf, m(sf[0] - rk[2])
        # o vão livre da sala, por dentro (D32, Arquiteto): da face de dentro da divisa até o lado aberto para a cozinha
        P.vao = p["_r"].metricas["util"]["sala"][0]
        if abs(P.fx0 + P.vao - g.com["sala"]["x1"]) > .005:
            _ca_aviso("sala: o vão livre não chega ao lado aberto para a cozinha (o pontilhado)")
        assert p["_r"].info, "o validador não avisa mais o vão da sala"
        ok = [_ca_no_texto(f"{P.m_luz_x} m da parede da divisa", it[1]["ideia"]), _ca_no_texto(f"{P.m_luz_y} m da parede da frente", it[1]["ideia"]),
              _ca_no_texto(f"({P.m_tv} m)", it[1]["cuid"])]
        P.cotas_sala = all(ok)
        P.m_vao = m(P.vao)
        P.tem_vao = _ca_no_texto(f"{P.m_vao} x ", it[1]["dim"])
        # 2: os 2,59 m de parede depois da porta do serviço
        _, jan, portas, _ = _geometria(p)
        pcs = PL.porta_dobradica(p, next(d for d in portas if d["id"] == "cozinha-servico"))
        P.porta_cs = max(pcs[0][1], pcs[1][1], pcs[2][1] if abs(pcs[2][0] - 6.7) < .01 else 0)
        P.fy1_coz = g.face("cozinha", "y1")
        P.m_259 = m(P.fy1_coz - P.porta_cs)
        P.tem_259 = _ca_no_texto(f"{P.m_259} m depois da porta do serviço", it[2]["ideia"])
        # 3: uns 91 cm entre o tanque e a máquina
        tq, mq = g.mv("tanque", "servico"), g.mv("maquina", "servico")
        P.tq, P.mq, P.m_91 = tq, mq, _ca_cm(round(mq[1] - tq[3], 2))
        P.tem_91 = _ca_no_texto(f"uns {P.m_91}", it[3]["cuid"])
        P.jan = {j["id"]: j["seg"] for j in jan}
        pe = PL.porta_dobradica(p, next(d for d in portas if d["id"] == "ext-sala"))
        P.porta_ent = max(pe[0][0], pe[1][0], pe[2][0])     # a parede da frente começa depois da porta de entrada
        rec = p["_r"].metricas["recuos"]
        lote = p["_r"].metricas["lote_comercial"]
        fundo_com = lote[1] - rec["frente"] - P.D
        lmin = p["_r"].metricas["lote"]
        d8 = f"{m1(lote[0])} x {m1(fundo_com)} m"
        r8 = f"no lote de {lote[0]} x {lote[1]} ({m1(rec['fundos'])} m no lote mínimo, de {_ca_num(lmin[0])} x {_ca_num(lmin[1])})"
        if it[8]["dim"] != d8 or it[8]["resto"] != r8:
            _ca_aviso(f"lugar 8: texto {it[8]['dim']} {it[8]['resto']}, dados {d8} {r8}")
        # as legendas do fundo e da frente, no desenho (D32)
        P.txt_fundo = (TX.COMODO["desenho"]["fundo"][0].format(m1(fundo_com), lote[0], lote[1]),
                       TX.COMODO["desenho"]["fundo"][1].format(m1(rec['fundos']), _ca_num(lmin[0]), _ca_num(lmin[1])))
        P.txt_frente = TX.COMODO["desenho"]["frente"].format(_ca_num(rec['frente']))
        if f"{m1(rec['dir'])} m" not in it[3]["ideia"]:
            _ca_aviso("lugar 3: a faixa livre do texto não é o recuo da direita dos dados")

    def marcas(self, P):
        W, D, g = P.W, P.D, P.g
        q1 = g.mv("armario", "quarto1")
        cama = g.mv("camaCasal", "quarto1")
        esc_ = g.mv("escrivaninha", "quarto3", cad=False)
        pia = g.mv("pia", "banho")
        box = g.mv("box", "banho")
        return {
            # 1: "medida a partir da parede da divisa (esquerda) e da parede da frente": a parede da divisa da sala
            #    inteira e a faixa por fora da parede da frente (ela tem a janela de 2,40 m); o caminho entre o rack e
            #    o sofá é a cota de 1,45 m (em medidas())
            1: P.pinta(P.par("x", .07, .15, 3.64)) + P.fora_h(P.porta_ent, 4.54, -.17),
            # 2: "parede da direita (a do banheiro e do serviço), em cima da pia e do fogão": a face da cozinha, da porta
            #    do serviço ao fundo da cozinha; "o lado sem parede que dá para a sala": pontilhado
            2: P.meia("x", 6.7, P.porta_cs, P.fy1_coz, "-") + P.sem_parede("x", 4.6, .15, 3.6),
            # 3: "do lado de fora da porta do serviço, na parede da direita (a faixa livre)": por fora, da janela do
            #    serviço ao fim do serviço (a porta no meio); o cuidado (entre tanque e máquina) é a cota de 91 cm
            3: P.fora_v(P.jan["servico"][3], 2.24),
            # 4: "no canto do box, nas paredes da cozinha e do serviço": a face do banheiro nas duas paredes, no
            #    comprimento do box; "na pia, na parede de fora, embaixo da janela": faixa por fora, no trecho da pia
            4: P.meia("x", 6.7, box[1], box[3], "+") + P.meia("y", 2.3, 6.76, box[2], "+") + P.fora_v(pia[1], pia[3]),
            # 5: "nas duas pontas: junto da sala e perto da porta do banheiro": a divisa na ponta do corredor e a parede
            #    da cozinha antes da porta do banheiro; "ao longo da parede dos quartos": a face do corredor
            5: P.pinta(P.par("x", .07, 3.76, 4.74)) + P.meia("y", 3.7, 6.0, 6.64, "+") + P.meia("y", 4.8, .15, 6.64, "-"),
            # 6: "na parede do corredor (guarda-roupa e maleiro)": a face do quarto atrás do guarda-roupa, com o maleiro
            #    tracejado por cima; "entre o pé da cama e a parede do quarto do meio": a face do quarto no pé da cama
            6: P.meia("y", 4.8, q1[0], q1[2], "+") + P.por_cima(q1[0], q1[1], q1[2], q1[3]) + P.meia("x", 2.833, cama[1], cama[3], "-"),
            # 7: "na parede da esquerda (a do quarto do meio), no canto da escrivaninha, embaixo da janela"; "na parede
            #    do corredor, no trecho que é o fundo do banheiro"
            7: P.meia("x", 5.667, esc_[1], esc_[3], "+") + P.meia("y", 4.8, 6.76, 8.35, "+"),
            # 8: "a faixa do fundo inteira, ao longo da parede do fundo; o cuidado marca as 3 janelas dos quartos"
            8: (P.area_aberta(.1, D + .2, W + P.rec - .12, D + P.p["_r"].metricas["recuos"]["fundos"] - .1, cor=CA_VERDE, aberto_em_cima=True)
                + "".join(P.fora_h(P.jan[q][0], P.jan[q][2], D + .17) for q in ("quarto1", "quarto2", "quarto3"))),
        }

    def chao(self, P, so, zoom):
        s = []
        if 3 in so and not zoom:   # a faixa livre de 1,5 m do item 3 (tracejado verde: área aberta)
            s.append(P.area_aberta(P.W + .2, .05, P.W + P.rec - .12, P.D - .05, cor=CA_VERDE))
        if 1 in so and not zoom:   # a sala, destaque da página: o chão em amarelo claro
            g = P.g
            s.append(f'<rect x="{g.face("sala", "x0"):.3f}" y="{P.Y(g.face("sala", "y1")):.3f}" width="{4.54 - g.face("sala", "x0"):.3f}" height="{g.face("sala", "y1") - g.face("sala", "y0"):.3f}" fill="{CA_FITA}" fill-opacity=".2"/>')
        return s

    def medidas(self, P, so, zoom, fs, extra):
        s = []
        if 1 in so:
            lx, ly = P.luz
            if P.tem_vao:   # o vão livre da sala, da face de dentro da divisa até o pontilhado (D32)
                yv = 3.33
                s.append(P.cota(P.fx0, P.fx0 + P.vao, yv, TX.COMODO["desenho"]["vao"].format(P.m_vao), fs, px=1.5))
                extra.append(P.caixa_pilula(1.5, yv, TX.COMODO["desenho"]["vao"].format(P.m_vao), fs))
            if P.cotas_sala:
                # o ponto de luz: 3,75 m da divisa e 1,70 m da frente, por dentro
                s.append(P.cota(P.fx0, lx, ly, P.m_luz_x, fs, px=1.3))
                s.append(P.cota_v(lx, P.fy0, ly, P.m_luz_y, fs, py=.62))
                extra += [P.caixa_pilula(1.3, ly, P.m_luz_x, fs), P.caixa_pilula(lx, .62, P.m_luz_y, fs, rot=1)]
                # o caminho entre a TV e o sofá
                yt = 2.5
                s.append(P.cota(P.rk[2], P.sf[0], yt, P.m_tv, fs, px=1.3))
                extra.append(P.caixa_pilula(1.3, yt, P.m_tv, fs))
                rl = fs * .62
                s.append(f'<g transform="translate({lx:.3f} {P.Y(ly):.3f})"><circle r="{rl:.3f}" fill="{CA_FITA}" stroke="{CA_TINTA}" stroke-width="{fs * .1:.3f}"/>'
                         f'<path d="M{-rl * .7:.3f} {-rl * .7:.3f}L{rl * .7:.3f} {rl * .7:.3f}M{rl * .7:.3f} {-rl * .7:.3f}L{-rl * .7:.3f} {rl * .7:.3f}" stroke="{CA_TINTA}" stroke-width="{fs * .1:.3f}"/></g>')
                s.append(P.pilula(lx, ly + fs * 1.55, TX.COMODO["desenho"]["luz"], fs * .8, cor=CA_TINTA))
                extra.append(P.caixa_pilula(lx, ly + fs * 1.55, TX.COMODO["desenho"]["luz"], fs * .8))
        if 2 in so and P.tem_259 and not zoom:
            xc = 5.72
            s.append(P.cota_v(xc, P.porta_cs, P.fy1_coz, P.m_259, fs, py=1.75))
            extra.append(P.caixa_pilula(xc, 1.75, P.m_259, fs, rot=1))
        if 3 in so and P.tem_91 and not zoom:
            xc = 7.64
            s.append(P.cota_v(xc, P.tq[3], P.mq[1], P.m_91, fs * .85))
            extra.append(P.caixa_pilula(xc, (P.tq[3] + P.mq[1]) / 2, P.m_91, fs * .85, rot=1))
        if 3 in so and not zoom:   # a faixa livre (texto do item 3)
            xt, yt = P.W + P.rec / 2 + .12, 5.0
            s.append(f'<text x="{xt:.3f}" y="{P.Y(yt):.3f}" text-anchor="middle" font-size="{fs * .95:.3f}" font-weight="700" class="mono" fill="{CA_VERDE}" transform="rotate(-90 {xt:.3f} {P.Y(yt):.3f})">{E(TX.COMODO["desenho"]["faixa"].format(m1(P.rec)))}</text>')
        if 8 in so and not zoom:
            rf = P.p["_r"].metricas["recuos"]["fundos"]
            yt = P.Y(P.D + rf / 2 + .02)
            s.append(f'<text x="2.75" y="{yt - fs * .3:.3f}" font-size="{fs * .95:.3f}" font-weight="700" class="mono" fill="{CA_VERDE}">{E(P.txt_fundo[0])}'
                     f'<tspan x="2.75" dy="{fs * 1.25:.3f}">{E(P.txt_fundo[1])}</tspan></text>')
        if 1 in so and not zoom:   # a frente: o desenho corta o recuo da frente
            ff = fs * .8
            w = len(P.txt_frente) * ff * .62 + ff * .7
            s.append(P.pilula(1.4 + w / 2, -.86, P.txt_frente, ff, cor=CA_TINTA))
        return s

    def numeros(self, P, so, zoom, r, r3, fs, extra, s):
        rf = P.p["_r"].metricas["recuos"]["fundos"]
        prefs = {1: ("sala", (1.55, .55)), 2: ("cozinha", (5.1, 2.6)), 3: ("servico", (7.1, 1.32)), 4: ("banho", (7.45, 3.55)),
                 5: ("circ", (3.4, 4.25)), 6: ("quarto1", (2.42, 6.84)), 7: ("quarto3", (6.75, 6.3)),
                 8: (None, (2.3, P.D + rf / 2 + .02))}
        return P.numeros_em(so, zoom, r, r3, fs, extra, prefs, self.destaque)

    def legenda(self):
        return _ca_legenda(self.id)


# ------------------------------------------------------------------ Casa Compacta (C01), 6,50 x 8,50
class _CaC01:
    id, destaque = "C01", 4
    com_item = {"varanda", "quarto2", "sala", "circ", "banho", "quarto1", "cozinha", "servico"}

    def fundo_extra(self, P):
        return 0

    def conferir(self, P):
        p, T, g = P.p, P.T, P.g
        it = {i["n"]: i for i in T["itens"]}
        _ca_conferir_util(p, T, {1: "varanda", 2: "quarto2", 3: "sala", 4: "circ", 5: "banho", 6: "quarto1", 7: "cozinha", 8: "servico"})
        # o hall só tem pedaços de parede entre as 3 portas: a face de dentro vem desses pedaços (a mesma do validador)
        c = g.com["circ"]
        toca = lambda v: [b for b in g.caixas if b[1] - 1e-6 <= v <= b[3] + 1e-6 and min(b[2], c["x1"]) - max(b[0], c["x0"]) > .05 and b[2] - b[0] > b[3] - b[1]]
        P.hall = (g.face("circ", "x0"), max(b[3] for b in toca(c["y0"])), g.face("circ", "x1"), min(b[1] for b in toca(c["y1"])))
        P.m_hx, P.m_hy = m(P.hall[2] - P.hall[0]), m(P.hall[3] - P.hall[1])
        P.tem_hall = _ca_no_texto(f"{P.m_hx} x {P.m_hy} m", it[4]["ideia"])
        # 7: a bancada em L de 1,21 m, da parede do serviço até a bancada de hoje
        bc = g.mv("bancada", "cozinha")
        P.bc, P.fx0_coz = bc, g.face("cozinha", "x0")
        P.m_121 = m(bc[0] - P.fx0_coz)
        P.tem_121 = _ca_no_texto(f"{P.m_121} m", it[7]["ideia"])
        # 2 e 5: os 95 cm do guarda-roupa atrás do box
        box, arm = g.mv("box", "banho"), g.mv("armario", "quarto2")
        P.box, P.arm2 = box, arm
        if _ca_cm(round(min(box[2], arm[2]) - max(box[0], arm[0]), 2)) not in it[2]["cuid"]:
            _ca_aviso("quarto da frente: o trecho do guarda-roupa atrás do box não bate com o texto")
        _, jan, portas, _ = _geometria(p)
        P.jan = {j["id"]: j for j in jan}
        ven = P.jan["servico"]
        if ven.get("tipo") != "veneziana":
            _ca_aviso("o serviço não tem a veneziana nos dados")
        if T.get("veneziana") not in p["_r"].avisos:
            _ca_aviso("a nota da veneziana do texto não é igual ao aviso dos dados")
        vp = PL.porta_dobradica(p, next(d for d in portas if d["id"] == "varanda-sala"))
        P.folha_porta = max(vp[0][1], vp[1][1], vp[2][1])
        P.mesa = g.mv("mesaJantar", "sala")

    def marcas(self, P):
        W, D, g = P.W, P.D, P.g
        js, jq1, jc = P.jan["sala"]["seg"], P.jan["quarto1"]["seg"], P.jan["cozinha"]["seg"]
        pia = g.mv("pia", "banho")
        mq = g.mv("maquina", "servico")
        h = P.hall
        return {
            # 1: "entre a divisa (esquerda; o desenho não mostra parede ali) e a parede do quarto da frente (direita)":
            #    pontilhado na linha da divisa (nada de parede desenhada) e a parede do quarto; "na janela da sala, na
            #    parede entre a sala e a varanda": faixa do lado da varanda, rente à janela
            1: P.sem_parede("x", .05, .08, 1.15) + P.pinta(P.par("x", 3.42, 0, 1.2)) + P.fora_h(js[0], js[2], 1.2 - .17),
            # 2: "na parede da rua (frente, sem janela)"; "na parede do fundo do quarto, no trecho do banheiro, do lado
            #    da janela do recuo": a face do quarto no trecho do box (os 95 cm)
            2: P.pinta_h(P.par("y", .07, 3.5, 6.35)) + P.meia("y", 3.3, P.box[0], P.box[2], "-"),
            # 3: "na parede da divisa (esquerda, o rack) e na parede do quarto da frente (direita, o sofá, antes da
            #    abertura do hall)"; o cuidado é a mesma parede do quarto. As duas paredes marcadas, os móveis do
            #    desenho como estão (a troca é sugestão do texto, não vai ao desenho): a divisa entre a folha da porta
            #    e a cadeira da mesa, e a parede do quarto até a abertura do hall
            3: P.pinta(P.par("x", .07, P.folha_porta, P.mesa[1])) + P.pinta(P.par("x", 3.35, 1.35, 3.38)),
            # 4: "no teto do hall inteiro, por cima das portas": o maleiro tracejado; "nas paredes do hall onde ele
            #    apoia": os pedaços de parede do hall (o lado da sala é aberto e fica sem tinta)
            4: (P.por_cima(h[0] + .03, h[1], h[2], h[3])
                + P.pinta_h(P.par("y", 3.3, 3.42, 4.45)) + P.pinta(P.par("x", 4.45, 3.36, 5.04)) + P.pinta_h(P.par("y", 5.1, 3.42, 4.45))),
            # 5: "na pia, no fundo do banheiro, ao lado da porta"; "na parede do box que dá para o quarto da frente":
            #    a face do banheiro na mesma parede que o 2 marca do lado do quarto
            5: P.meia("y", 5.1, pia[0], pia[2], "-") + P.meia("y", 3.3, P.box[0], P.box[2], "+"),
            # 6: "na parede do fundo (a da janela)": faixa por fora; o cuidado (o lado da cama junto da janela) é o
            #    lugar do número
            6: P.fora_h(g.face("quarto1", "x0"), g.face("quarto1", "x1"), D + .17),
            # 7: "na parede do fundo, embaixo da janela": faixa por fora; "na parede da direita (a do quarto casal),
            #    atrás da pia e da bancada"
            7: P.fora_h(jc[0], jc[2], D + .17) + P.meia("x", 3.35, P.bc[1], P.bc[3], "-"),
            # 8: "na parede da divisa (esquerda), acima da máquina"; o cuidado é a veneziana em cima da porta de fora,
            #    que o desenho do livro já traz tracejada em azul
            8: P.pinta(P.par("x", .07, mq[1], mq[3])),
        }

    def chao(self, P, so, zoom):
        if 4 in so and not zoom:   # o hall, destaque da página: o chão em amarelo claro
            h = P.hall
            return [f'<rect x="{h[0]:.3f}" y="{P.Y(h[3]):.3f}" width="{h[2] - h[0]:.3f}" height="{h[3] - h[1]:.3f}" fill="{CA_FITA}" fill-opacity=".2"/>']
        return []

    def medidas(self, P, so, zoom, fs, extra):
        s = []
        if 4 in so and zoom and P.tem_hall:
            h = P.hall
            yc, xc = h[1] + .2, h[0] + .17
            s.append(P.cota(h[0], h[2], yc, P.m_hx, fs, px=(h[0] + h[2]) / 2 + .12))
            s.append(P.cota_v(xc, h[1], h[3], P.m_hy, fs, py=4.55))
            extra += [P.caixa_pilula((h[0] + h[2]) / 2 + .12, yc, P.m_hx, fs), P.caixa_pilula(xc, 4.55, P.m_hy, fs, rot=1)]
        if 7 in so and P.tem_121 and not zoom:
            yc = 8.12
            s.append(P.cota(P.fx0_coz, P.bc[0], yc, P.m_121, fs))
            extra.append(P.caixa_pilula((P.fx0_coz + P.bc[0]) / 2, yc, P.m_121, fs))
        return s

    def numeros(self, P, so, zoom, r, r3, fs, extra, s):
        prefs = {1: ("varanda", (1.7, .6)), 2: ("quarto2", (4.92, 1.4)), 3: ("sala", (1.8, 3.35)),
                 4: ("circ", (3.97, 4.0) if zoom else (3.9, 4.2)), 5: ("banho", (4.95, 3.55)), 6: ("quarto1", (4.6, 8.08)),
                 7: ("cozinha", (2.0, 7.2)), 8: ("servico", (1.05, 7.0))}
        return P.numeros_em(so, zoom, r, r3, fs, extra, prefs, self.destaque)

    def legenda(self):
        return _ca_legenda(self.id)


def _ca_esc(t):
    return E(_ca_nb(t))


def _ca_cab_item(it):
    resto = f'<span class="ca-sub2">{_ca_esc(it["resto"])}</span>' if it.get("resto") else ""
    return f'<span class="nn">{it["n"]}</span><h3>{_ca_esc(it["nome"])} <span class="mono">{_ca_esc(it["dim"])}</span>{resto}</h3>'


def _ca_linha(it, ref=False):
    cab = _ca_cab_item(it)
    if ref:
        return f'<article class="ln ref">{cab}<p class="ao">{E(TX.COMODO["ref"])}</p></article>'
    return (f'<article class="ln">{cab}<p class="ca-id"><b>{E(TX.COMODO["ideia"])}</b> {_ca_esc(it["ideia"])}</p>'
            f'<p class="cuid"><b>{E(TX.COMODO["cuidado"])}</b> {_ca_esc(it["cuid"])}</p></article>')


def _ca_cartao(it):
    return (f'<article class="cd">{_ca_cab_item(it)}<p class="ca-id"><b>{E(TX.COMODO["ideia"])}</b> {_ca_esc(it["ideia"])}</p>'
            f'<p class="cuid"><b>{E(TX.COMODO["cuidado"])}</b> {_ca_esc(it["cuid"])}</p></article>')


def _ca_heroi(it, largo=False, estreito=False, leg=""):
    cls = "heroi" + (" largo" if largo else "") + (" estreito" if estreito else "")
    lg = f'<span class="leg-h">{E(leg)}</span>' if leg else ""
    return (f'<div class="{cls}">{lg}{_ca_cab_item(it)}'
            f'<p class="ca-id"><b>{E(TX.COMODO["ideia"])}</b> {_ca_esc(it["ideia"])}</p><p class="cuid"><b>{E(TX.COMODO["cuidado"])}</b> {_ca_esc(it["cuid"])}</p></div>')


def _ca_legenda(cid):
    """A legenda da planta: o desenho de cada marca e a frase dela (paginas.py, COMODO["legenda"])."""
    d = {}
    d["amarelo"] = f'<svg viewBox="0 0 9 4"><rect x=".3" y="1.2" width="8.4" height="1.6" fill="{CA_FITA}" stroke="{CA_TINTA}" stroke-width=".25"/></svg>'
    d["ponto"] = f'<svg viewBox="0 0 9 4">' + "".join(f'<circle cx="{x}" cy="2" r=".7" fill="{CA_FITA}" stroke="{CA_TINTA}" stroke-width=".22"/>' for x in (1, 3.33, 5.67, 8)) + "</svg>"
    d["trac"] = f'<svg viewBox="0 0 9 4"><rect x=".4" y=".5" width="8.2" height="3" fill="{CA_FITA}" fill-opacity=".28" stroke="{CA_TINTA}" stroke-width=".3" stroke-dasharray="1 .7"/></svg>'
    d["medida"] = f'<svg viewBox="0 0 9 4"><line x1=".5" y1="2" x2="8.5" y2="2" stroke="{CA_AZUL}" stroke-width=".35"/><line x1=".5" y1="1" x2=".5" y2="3" stroke="{CA_AZUL}" stroke-width=".35"/><line x1="8.5" y1="1" x2="8.5" y2="3" stroke="{CA_AZUL}" stroke-width=".35"/></svg>'
    d["recuo"] = f'<svg viewBox="0 0 9 4"><rect x=".4" y=".5" width="8.2" height="3" fill="none" stroke="{CA_AZUL}" stroke-width=".3" stroke-dasharray="1.2 .7"/></svg>'
    d["verde"] = f'<svg viewBox="0 0 9 4"><rect x=".4" y=".5" width="8.2" height="3" fill="#BFDDA0" stroke="{CA_VERDE}" stroke-width=".3" stroke-dasharray="1.2 .7"/></svg>'
    d["ven"] = f'<svg viewBox="0 0 9 4"><rect x=".4" y="1.3" width="8.2" height="1.4" fill="#9AA0A6" stroke="none"/><rect x=".4" y="1.1" width="8.2" height="1.8" fill="none" stroke="{CA_AZUL}" stroke-width=".35" stroke-dasharray="1 .6"/></svg>'
    d["porta"] = (f'<svg viewBox="0 0 9 4"><path d="M2.6 3.3 A3.2 3.2 0 0 1 5.8 .1" fill="none" stroke="{CA_CINZA}" stroke-width=".18" stroke-dasharray=".5 .35"/>'
             f'<rect x="2.3" y="3" width="4.4" height=".7" fill="{CA_FITA}" stroke="{CA_TINTA}" stroke-width=".2"/>'
             f'<line x1="2.6" y1="3.1" x2="2.6" y2=".1" stroke="{CA_FITA}" stroke-width=".55" stroke-linecap="round"/>'
             f'<line x1="2.6" y1="3.1" x2="2.6" y2=".1" stroke="{CA_TINTA}" stroke-width=".12"/></svg>')
    return '<div class="legenda-ca">' + "".join(f'<div>{d[m]}<span>{E(txt)}</span></div>' for m, txt in TX.COMODO["legenda"][cid]) + "</div>"


def _ca_perguntas(T):
    li = "".join(f'<li><b>{_ca_esc(a)}</b> {_ca_esc(b)}{"".join(f"<span class=ref>{n}</span>" for n in ns)}</li>' for a, b, ns in T["perguntas"])
    return f'<div class="perg"><h3>{E(TX.COMODO["perguntas"])}</h3><ol>{li}</ol></div>'


def _ca_cabeca(p, T, sub=True):
    r = p["_r"].metricas
    lote = r["lote_comercial"]
    return (f'<div><div class="ca-eti"><span>{E(TX.COMODO["eti"])}</span><i>{E(p["id"])}</i>'
            f'<span class="f">{E(p["nome"])}, {PL.n0(r["area_fechada"])} m², {E(p["quartos_txt"])}, lote de {lote[0]} x {lote[1]} m</span></div>'
            f'<h2>{E(T["titulo"])}</h2>' + (f'<p class="ca-sub">{E(T["sub"])}</p>' if sub else "")
            + f'<p class="ca-abre">{_ca_esc(T["abre"])}</p></div>')


def _ca_selo(cid):
    return f'<span class="selo">{E(TX.COMODO["selo"][cid])}</span>'


def _ca_eti2(p, T):
    return f'<div class="ca-eti"><span>{E(TX.COMODO["eti"])}</span><i>{E(p["id"])}</i><span class="f">{E(T["sub"])}</span></div>'


def _ca_paginas_E03(L, p, T, casa, orelha):
    """Casa comprida (5 x 16): planta em pé encostada no meio do livro, detalhe da cozinha à esquerda; lista em linhas."""
    PLT = _CaPlanta(p, T, casa)
    D, W, rec = PLT.D, PLT.W, PLT.rec
    rec_main = (-.42, W + rec + .32, D + .55, -1.05)      # a casa inteira, do fundo à calçada
    rec_zoom = (-.05, W + rec + .15, 9.94, 5.87)          # a cozinha e o recuo ao lado dela
    it = T["itens"]
    nota = f'<p class="nota-ca"><b>{E(TX.COMODO["tomadas"])}</b> {_ca_esc(T["nota"])}</p>'
    alv = f'<p class="alv">{_ca_esc(T["alvenaria"])}</p>'
    svg_m, wm, hm = PLT.svg(11.6, rec_main)
    kz = (CA_LARG - (wm + 3) - 6 - 3) / (rec_zoom[1] - rec_zoom[0])   # coluna da esquerda menos a moldura
    svg_z, wz, hz = PLT.svg(kz, rec_zoom, so={3}, rn3=5.2, fs_mm=3.0, zoom=True)
    n = L.pagina(f"""{_ca_cabeca(p, T)}
      <div class="ca-corpo">
        <div class="ca-esq">
          {casa.legenda()}
          <div class="cozinha-bloco"><figure class="ca-zoom"><span class="leg">{E(TX.COMODO["detalhe"]["E03"])}</span><div class="moldura">{svg_z}</div></figure>
          {_ca_heroi(it[2])}</div>
          {nota}
          {alv}
        </div>
        <div class="ca-planta" style="width:{wm + 3:.2f}mm"><div class="moldura">{svg_m}</div>{_ca_selo("E03")}</div>
      </div>""", "q ca", orelha=orelha, aviso=True)
    linhas = "".join(_ca_linha(i, ref=(i["n"] == 3)) for i in it)
    L.pagina(f"""{_ca_eti2(p, T)}
      <div class="linhas">{linhas}</div>
      {_ca_perguntas(T)}
      {nota}
      {alv}""", "q ca", orelha=orelha, aviso=True)
    return n


def _ca_paginas_F01(L, p, T, casa, orelha):
    """Casa quase quadrada (8,50 x 8,30): a planta na largura da página 1, com o destaque (a sala) nela; na página 2,
    o destaque em texto grande e os outros 7 lugares em cartões de 2 colunas."""
    PLT = _CaPlanta(p, T, casa)
    D, W, rec = PLT.D, PLT.W, PLT.rec
    rf = p["_r"].metricas["recuos"]["fundos"]
    rec_main = (-.52, W + rec + .3, D + rf + .1, -1.05)   # -.52: o rótulo "divisa" inteiro
    it = T["itens"]
    nota = f'<p class="nota-ca"><b>{E(TX.COMODO["tomadas"])}</b> {_ca_esc(T["nota"])}</p>'
    alv = f'<p class="alv">{_ca_esc(T["alvenaria"])}</p>'
    svg_m, wm, hm = PLT.svg(15.2, rec_main, rn=2.7, rn3=3.9, fs_mm=2.5)
    n = L.pagina(f"""{_ca_cabeca(p, T)}
      <div class="ca-planta larga"><div class="moldura">{svg_m}</div></div>
      <div class="ca-pe">{casa.legenda()}<div class="ca-pe-dir">{_ca_selo("F01")}{alv}</div></div>""", "q ca", orelha=orelha, aviso=True)
    cartoes = "".join(_ca_cartao(i) for i in it if i["n"] != 1)
    L.pagina(f"""{_ca_eti2(p, T)}
      {_ca_heroi(it[0], largo=True, leg=TX.COMODO["destaque"]["F01"])}
      <div class="cartoes">{cartoes}{_ca_perguntas(T)}</div>
      {nota}
      {alv}""", "q ca", orelha=orelha, aviso=True)
    return n


def _ca_paginas_C01(L, p, T, casa, orelha):
    """Casa de 6,50 x 8,50: planta grande encostada no meio do livro; ao lado, numa coluna estreita, o hall ampliado;
    embaixo, o destaque na largura da página. Na página 2, os outros 7 em cartões e a nota da veneziana junto do 8."""
    PLT = _CaPlanta(p, T, casa)
    D, W, rec = PLT.D, PLT.W, PLT.rec
    rec_main = (-.52, W + rec + .3, D + .55, -1.05)   # -.52: o rótulo "divisa" inteiro
    rec_hall = (3.05, 4.75, 5.55, 2.85)               # o hall e um pedaço das 3 portas
    it = T["itens"]
    nota = f'<p class="nota-ca"><b>{E(TX.COMODO["tomadas"])}</b> {_ca_esc(T["nota"])}</p>'
    ven = f'<p class="nota-ca ven"><b>{E(TX.COMODO["atencao"])}</b> {_ca_esc(T["veneziana"])}</p>'
    alv = f'<p class="alv">{_ca_esc(T["alvenaria"])}</p>'
    col = 40
    k = (CA_LARG - col - 5 - 3) / (rec_main[1] - rec_main[0])
    svg_m, wm, hm = PLT.svg(k, rec_main, rn=2.7, rn3=3.9, fs_mm=2.5)
    kz = (col - 3) / (rec_hall[1] - rec_hall[0])
    svg_z, _, _ = PLT.svg(kz, rec_hall, so={4}, rn3=4.4, fs_mm=2.6, zoom=True)
    n = L.pagina(f"""{_ca_cabeca(p, T)}
      <div class="ca-corpo">
        <div class="ca-esq estreita" style="width:{col}mm;flex:none">
          <figure class="ca-zoom"><span class="leg">{E(TX.COMODO["detalhe"]["C01"])}</span><div class="moldura">{svg_z}</div></figure>
          {casa.legenda()}
        </div>
        <div class="ca-planta" style="width:{wm + 3:.2f}mm"><div class="moldura">{svg_m}</div>{_ca_selo("C01")}</div>
      </div>
      {_ca_heroi(it[3], largo=True, leg=TX.COMODO["destaque"]["C01"])}
      {alv}""", "q ca", orelha=orelha, aviso=True)
    cartoes = "".join(_ca_cartao(i) if i["n"] != 4 else "" for i in it) + f'<div class="cd nota-cd">{ven}{nota}</div>'
    L.pagina(f"""{_ca_eti2(p, T)}
      <div class="cartoes">{cartoes}</div>
      {_ca_perguntas(T)}
      {alv}""", "q ca c01", orelha=orelha, aviso=True)
    return n


CA_CASAS = {"E03": (_CaE03, _ca_paginas_E03), "F01": (_CaF01, _ca_paginas_F01), "C01": (_CaC01, _ca_paginas_C01)}
FOLHAS_COMODO = 2  # folhas do cômodo a cômodo em cada casa (o mapa: a casa tem 4 páginas, 2 pares abertos)


def paginas_comodo(L, p):
    """As 2 páginas "cômodo a cômodo" da casa p, depois da dupla dela. Devolve o número da primeira. Casa sem texto
    aprovado (paginas.py, COMODOS) fica com as páginas reservadas, para a numeração do mapa não mudar."""
    if p["id"] not in CA_CASAS or p["id"] not in TX.COMODOS:
        n = [reservada(L, f'{TX.DUAS_PARTES["comodo"]} ({i} de {FOLHAS_COMODO})', casa=p, lado=lado)
             for i, lado in enumerate(("esq", "dir")[:FOLHAS_COMODO], start=1)]
        return n[0]
    T = TX.COMODOS[p["id"]]
    assert [i["n"] for i in T["itens"]] == list(range(1, len(T["itens"]) + 1)) and len(T["itens"]) >= 7 and len(T["perguntas"]) == 3
    classe, paginas = CA_CASAS[p["id"]]
    antes = len(L.paginas)
    n = paginas(L, p, T, classe(), lote_frente(p))
    assert len(L.paginas) - antes == FOLHAS_COMODO
    return n


def ache_a_sua_casa(plantas, numeros, recuos_txt):
    """Edição pequena (até POUCAS casas): as casas lado a lado, cada uma no seu lote comercial e todas na mesma escala,
    pela frente do lote (a rua embaixo, a fita com a frente), com área, quartos, jeito de morar e página."""
    casas = sorted(plantas, key=lambda p: (lote_frente(p), p["id"]))
    filas = [casas] if len(casas) <= 3 else [casas[:(len(casas) + 1) // 2], casas[(len(casas) + 1) // 2:]]
    lote = lambda p: p["_r"].metricas["lote_comercial"]
    gap, alto = 9.0, (144.0 if len(filas) == 1 else 54.0)  # mm; "alto" = lote mais fundo de cada fila
    col_min = min(49.0, (176.0 - gap * (max(len(fl) for fl in filas) - 1)) / max(len(fl) for fl in filas))  # o texto cabe
    k = min(alto / max(lote(p)[1] for p in casas),
            *[(176.0 - 12 - gap * (len(fila) - 1)) / sum(lote(p)[0] + .1 for p in fila) for fila in filas])
    jeito = {i: t for t, ids in GRUPOS for i in ids}
    html = []
    for fila in filas:
        cols = " ".join(f"{max(col_min, (lote(p)[0] + .1) * k):.1f}mm" for p in fila)
        lotes = "".join(f'<div class="ac-lote">{svg_no_lote(p, k)}</div>' for p in fila)
        fitas = "".join(f'<div class="ac-fita" style="width:{lote(p)[0] * k:.1f}mm;--m:{k:.2f}mm">{lote(p)[0]} m</div>' for p in fila)
        txt = "".join(
            f'<div class="ac-txt"><span class="mono id">{p["id"]}</span><h3>{E(p["nome"])}</h3>'
            f'<p>{n0(p["_r"].metricas["area_fechada"])} m² · {E(p["quartos_txt"].replace(" (+1 depois)", ""))} · {p["banheiros"]} banheiro{"s" if p["banheiros"] > 1 else ""}</p>'
            + (f'<p class="ac-jeito">{E(jeito[p["id"]])}</p>' if p["id"] in jeito else "")
            + '</div>' for p in fila)
        pags = "".join(f'<b class="ac-pag">pág. {numeros[p["id"]]}</b>' for p in fila)  # fileira própria: as páginas alinhadas
        html.append(f'<div class="ac-fila{" ac-2" if len(filas) > 1 else ""}" style="grid-template-columns:{cols};column-gap:{gap:.0f}mm">{lotes}'
                    f'<div class="ac-rua">RUA</div>{fitas}{txt}{pags}</div>')
    return (cab("ache") +
            f'<p class="abertura">Procure a frente do seu lote na fita amarela: em cima dela está a casa desenhada num lote comum dessa frente, já com os recuos de referência. '
            f'O fundo mínimo e a medida exata estão na página da casa.</p>'
            + "".join(html)
            + f'<p class="pequeno ac-recuos">{recuos_txt}</p>')


AVISOS = []  # o que impede a entrega: gancho que não bate com o validador
n0 = PL.n0  # o mesmo arredondamento em todo número que vai ao público


def melhor_lado(o):
    """Melhor lado da rua; quando o segundo lado empata quase, diz os dois."""
    pts = o.get("pontos", {})
    seg = o.get("segunda")
    if seg and pts and pts[o["melhor"]] - pts[seg] <= 0.05 * abs(pts[o["melhor"]]):
        return f"{ORI[o['melhor']]} ou {ORI[seg]}"
    return ORI[o["melhor"]]


def avisos_juntos(p):
    """Junta avisos repetidos do validador ("Sala tem vão de 4.6 m...", "Quarto tem vão...") numa frase só."""
    import re
    grupos, outros = {}, []
    for a in p["_r"].avisos + p["_r"].info:
        m = re.match(r"(.+?) tem vão de ([\d.]+) m: (.+)", a)
        if m:
            grupos.setdefault((m.group(2), m.group(3)), []).append(m.group(1))
        else:
            outros.append(a)
    for (vao, resto), nomes in grupos.items():
        art = [("a " if n.split()[0].lower().endswith("a") else "o ") + n.lower() for n in nomes]
        lista = art[0] if len(art) == 1 else ", ".join(art[:-1]) + " e " + art[-1]
        lista = lista[0].upper() + lista[1:]
        outros.append(f"{lista} {'tem' if len(nomes) == 1 else 'têm'} vão livre (sem parede no meio) de {vao.replace('.', ',')} m: {resto}")
    return outros


def dupla(L, p, por_id, numeros):
    r = p["_r"].metricas
    t = FICHAS.TEXTOS.get(p["id"], {})
    f = lote_frente(p)
    quartos = p["quartos_txt"].replace(" (+1 depois)", "")
    pens = PL.pensou(p)
    g = t.get("gancho", "")
    if g and (f"{f} m de frente" not in g or (f"{n0(r['area_fechada'])} m²" not in g and "m²" in g)):
        AVISOS.append(p["id"])
        print(f"AVISO: gancho de {p['id']} não bate com o validador ({f} m, {n0(r['area_fechada'])} m²): {g}")
    gancho = t.get('gancho', f'{f} m de frente. {quartos}. {n0(r["area_fechada"])} m².')
    erros = list(t.get("erros", [1, 2, 4]))
    # "corredor comprido" só conta como evitado se a casa não tiver corredor de fora a fora
    circs = [c for c in p["comodos"] if c["tipo"] == "circ"]
    if 2 in erros and (r["circulacao"] > 0.12 or any(max(c["x1"] - c["x0"], c["y1"] - c["y0"]) > 6.0 for c in circs)):
        erros.remove(2)  # sem pôr outro no lugar: só entra o que foi conferido
    # o número é o do capítulo dos 7 erros (1, 2, 4...), e o título diz onde ele está: o leitor acha o erro pelo número
    erros_html = "".join(f'<li><span class="erro-mini">{n}</span>{E(TX.ERROS[n - 1][0])}</li>' for n in erros)
    ne = numeros.get("erros")
    erros_tit = f"Dos {len(TX.ERROS)} erros " + (f"da pág. {ne}" if isinstance(ne, int) and ne else "do e-book") + ", esta casa evita"
    cat = CATEGORIAS[p["id"][0]]
    L.inicio[p["id"]] = L.pagina(f"""
      <div class="cab"><span class="mono id">{p['id']} · {cat.upper()}</span><h2 class="nome">{E(p['nome'])}</h2>
        <p class="gancho">{E(gancho)}</p>{chips(p, gancho)}</div>
      <div class="planta-grande moldura">{svg_planta(p, humanizada=True)}</div>
      <div class="selo-tec">Planta de referência humanizada · medidas em metros · móveis para dar escala</div>
      <div class="duas"><div><h4>Para quem é</h4><p>{E(t.get('para_quem', ''))}</p></div>
        <div><h4>{erros_tit}</h4><ul class="erros-mini">{erros_html}</ul></div></div>""",
             "casa esq q", orelha=f, aviso=True)
    nao = t.get("nao_serve")
    nao_html = ""
    if nao:
        alvo = nao[1]
        # a alternativa só é citada se estiver nesta edição (no lançamento, as outras casas não estão no PDF)
        veja = f' Veja a <b>{alvo} {E(por_id[alvo]["nome"])}</b>, {"p. " + str(numeros[alvo]) if isinstance(numeros[alvo], int) else "no e-book"}.' if alvo in por_id else ""
        # sem a alternativa na edição: só diz que falta suíte se nenhuma casa da edição tiver (conferido no validador)
        if not veja and "suíte" in nao[0] and not any("suíte" in q["quartos_txt"] for q in por_id.values()):
            veja = " O e-book completo não tem casa com suíte." if numeros.get("erros") == "e-book" else " Este e-book não tem casa com suíte."
        nao_html = f'<div><h4>Para quem não serve</h4><p>{E(nao[0])}{veja}</p></div>'
    perg = [q for q in t.get("perguntas", []) if q not in FICHAS.PADRAO] or ["As perguntas que valem para toda casa estão em \"Pergunte em qualquer casa\", no fim do e-book" + (" completo" if numeros.get("erros") == "e-book" else "") + "."]
    linha = lambda a, b, c="": f'<div class="r-l"><span>{a}</span><b>{b}</b><span>{c}</span></div>'
    L.pagina(f"""
      <div class="cab"><span class="mono id">{p['id']} · A CASA NO SEU LOTE</span><h2 class="nome">Cabe num lote de {f} x {r['lote_comercial'][1]} m.</h2></div>
      <div class="lado"><div class="lote-fig">{svg_lote(p)}</div>
        <div class="rotulo"><div class="r-tit">INFORMAÇÃO DA CASA</div>
          <div class="r-por">Lote comum {f} x {r['lote_comercial'][1]} m · mínimo {m(r['lote'][0])} x {m(r['lote'][1])} m</div>
          <div class="r-cab"><span></span><span>nesta casa</span><span>referência</span></div>
          {linha('Área fechada', f"{n0(r['area_fechada'])} m²")}
          {linha('Medidas por fora', f"{m(p['W'])} x {m(p['D'])} m")}
          {linha('Varanda e garagem', f"{n0(r['area_coberta_aberta'])} m²" if r['area_coberta_aberta'] else '—')}
          {linha('Área coberta total', f"{n0(r['area_fechada'] + r['area_coberta_aberta'])} m²", 'conta no orçamento') if r['area_coberta_aberta'] else ''}
          {linha('Quartos', E(quartos))}
          {linha('Banheiros', p['banheiros'])}
          {linha('Corredor', f"{n0(r['circulacao'] * 100)}% da casa" if r['circulacao'] else ('externo' if any(c['id'] == 'corr' for c in p['comodos']) else 'não tem'), 'bom: até 14%')}
          {linha('Janela nos quartos' if any(c['tipo'] in ('dorm', 'casal') for c in p['comodos']) else 'Janela no ambiente', '✓', 'mín. 1/6 do piso')}
          {linha('Melhor lado da rua', melhor_lado(r['orientacao']))}
          {linha('Pode espelhar', 'sim', 'troca o lado')}
          <div class="r-nota">Conferido medida por medida pelo X1-Plantas, com recuos de referência. Não substitui o profissional: confira os da sua cidade.</div></div></div>
      {('<div class="atencao"><h4>Atenção: leve ao engenheiro</h4><ul>' + ''.join(f'<li>{E(a)}</li>' for a in avisos_juntos(p)) + '</ul></div>') if (p['_r'].avisos or p['_r'].info) else ''}
      {fachada_bloco(p)}
      <div><h4>Por que esta planta é assim</h4><div class="pensou">
        {''.join(f'<div>{icone(ic)}<p>{E(x)}</p></div>' for ic, x in zip(['sol', 'ar', 'agua', 'seta'], pens))}</div></div>
      <div class="duas">{nao_html}<div><h4>Leve ao seu engenheiro</h4><ul class="perg">{''.join(f'<li>{E(q)}</li>' for q in perg)}</ul></div></div>""",
             "casa dir q", orelha=f, aviso=True)


# ------------------------------------------------------------------ saída
CSS = (AQUI / "livro.css").read_text(encoding="utf-8")


def sem_quebra(doc):
    """Não deixa "e-book" quebrar no hífen no fim da linha (só no texto do corpo, fora das tags)."""
    import re
    cab, corpo = doc.split("<body>", 1)
    corpo = re.sub(r"(?<![\w/.-])([Ee])-book(?![^<]*>)", r'<span class="nq">\1-book</span>', corpo)
    return cab + "<body>" + corpo


def montar_gratis(plantas, config, pid):
    """Planta grátis do funil: a página dupla de uma casa e uma página que mostra o que mais existe (ímã)."""
    L = Livro(plantas, config)
    por_id = {p["id"]: p for p in plantas}
    numeros = {p["id"]: "e-book" for p in plantas}
    numeros["lote"] = 3
    numeros["erros"] = "e-book"  # a planta grátis não tem o capítulo: "dos 7 erros do e-book"
    L.paginas = []
    dupla(L, por_id[pid], por_id, numeros)
    contagem = {}
    for p in plantas:
        contagem[lote_frente(p)] = contagem.get(lote_frente(p), 0) + 1
    p = por_id[pid]
    f = lote_frente(p)
    fundo = p["_r"].metricas["lote_comercial"][1]
    mesmas = [q for q in plantas if lote_frente(q) <= f and q["_r"].metricas["lote_comercial"][1] <= fundo and q["id"] != pid]
    titulo_ima = "No seu lote cabem mais casas"
    frase_ima = (f"Num lote de {f} x {fundo} m, com os recuos de referência, {'cabem outras' if len(mesmas) > 1 else 'cabe outra'} "
                 f"{casas_txt(len(mesmas)) if len(mesmas) > 1 else 'casa'} do e-book, "
                 "cada uma com a casa no lote, a \"Informação da casa\" e o porquê de cada escolha.")
    legenda_ima = (f"Algumas das casas que também cabem num lote de {f} x {fundo} m." if len(mesmas) > 6
                   else f"{'As casas que também cabem' if len(mesmas) > 1 else 'A casa que também cabe'} num lote de {f} x {fundo} m.")
    if not mesmas:
        # casa do menor lote: mostra o que cabe com um pouco mais de terreno
        # só as de frente maior: a frase fala em "um pouco mais de frente" (na edição de 3, a E03 é mais estreita e mais funda)
        maiores = sorted([q for q in plantas if q["id"] != pid and lote_frente(q) > f], key=lambda q: (lote_frente(q), q["_r"].metricas["area_fechada"]))
        mesmas = maiores[:6]
        titulo_ima = "E se o lote for um pouco maior?"
        if len(maiores) > 1:
            frase_ima = (f"Com um pouco mais de frente, as opções crescem: {casas_txt(len(maiores))} do e-book pedem lote mais largo, "
                         "cada uma com o lote mínimo calculado.")
            legenda_ima = "Algumas das casas dos próximos tamanhos de lote." if len(maiores) > 6 else "As casas dos próximos tamanhos de lote."
        elif maiores:
            q = maiores[0]
            lq = f"{lote_frente(q)} x {q['_r'].metricas['lote_comercial'][1]} m"
            frase_ima = (f"Num lote de {lq} cabe a {q['nome']}, com {q['quartos_txt'].replace(' (+1 depois)', '')}. "
                         "Ela também vem com a casa no lote e o porquê de cada escolha.")
            legenda_ima = f"A {q['nome']}, para o lote de {lq}."
        else:
            # a casa grátis é a de frente maior: mostra as outras do e-book
            mesmas = [q for q in plantas if q["id"] != pid][:6]
            outras = len(plantas) - 1
            titulo_ima = "As outras casas do e-book" if outras > 1 else "A outra casa do e-book" if outras else "A casa no seu lote"
            frase_ima = (f"O e-book tem mais {casas_txt(outras)}, cada uma com o lote mínimo calculado." if outras > 1
                         else f"O e-book tem mais {casas_txt(outras)}, também com o lote mínimo calculado." if outras else "")
            legenda_ima = ""
    L.pagina(f"""<span class="sobre">Essa foi 1 de {len(plantas)}</span><h2>{titulo_ima}</h2>
      <p class="abertura">A {E(p['nome'])} cabe num lote de {f} m de frente. {E(frase_ima)}</p>
      {galeria(plantas, [q['id'] for q in mesmas[:6]], legenda_ima)}
      <div class="caixa amarela"><h3>Me fala a frente do seu lote</h3><p>Responde aqui no WhatsApp com a medida que eu te digo quais casas cabem nele com os recuos de referência. Os da sua cidade, você confirma na prefeitura.</p></div>
      <p class="pequeno"><b>Planta de referência:</b> não é projeto executivo nem legal, não serve para aprovar nem para construir direto. Leve a um arquiteto ou engenheiro.</p>
      {svg_fita(contagem)}""", "fim")
    return L


def gerar(previa=None, duas_partes=False):
    if duas_partes and (not previa or SAIDA == EBOOK / "saida"):
        sys.exit(RECUSA_DUAS_PARTES)
    config = json.loads((EBOOK / "config.json").read_text(encoding="utf-8"))
    plantas = PL.carregar()
    for p in plantas:
        if p["_r"].erros:
            sys.exit(f"{p['id']} tem erro no validador: corrija antes de gerar o e-book")
    ordem = "CEFS"
    plantas.sort(key=lambda p: (ordem.index(p["id"][0]), p["id"]))
    plantas = edicao(plantas, config)
    if duas_partes:  # as casas pela frente do lote (decisão do Maestro, 24/11/2026): quem folheia vai para a frente quando o lote cresce
        plantas.sort(key=lambda p: (lote_frente(p), p["id"]))
    # 1ª passada descobre as páginas; a 2ª escreve os números certos
    numeros = {"lote": 3, **{p["id"]: 0 for p in plantas}}
    for _ in range(2):
        L = montar(plantas, config, numeros, duas_partes)
        numeros = {**L.inicio, "folhas": dict(L.folhas)}
    if duas_partes:
        print("modo duas partes (só prévia): " + ", ".join(f"{p['id']} pág. {numeros[p['id']]}" for p in plantas)
              + f"; casas em geral a partir da pág. {numeros['ler']}")
        for p in plantas:  # a casa abre em página par: planta à esquerda, lote à direita, a dupla junta
            if numeros[p["id"]] % 2:
                print(f"AVISO: {p['id']} começa na página {numeros[p['id']]} (ímpar): a dupla da casa não fica lado a lado")
    SAIDA.mkdir(exist_ok=True)
    doc = (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{E(config.get("titulo", "E-book"))}</title>'
           f'<style>{CSS}</style></head><body>{"".join(L.paginas)}</body></html>')
    doc = sem_quebra(doc)
    arq = SAIDA / "ebook.html"
    arq.write_text(doc, encoding="utf-8")
    env = dict(os.environ)
    try:
        env["NODE_PATH"] = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()
    except FileNotFoundError:
        pass
    cmd = ["node", str(AQUI / "pdf.cjs"), str(arq), str(SAIDA / "ebook.pdf")] + ([str(previa)] if previa else [])
    r = subprocess.run(cmd, env=env, capture_output=True, text=True)
    print(r.stdout.strip(), r.stderr.strip())
    falhou = r.returncode != 0
    print(f"{len(L.paginas)} páginas, {len(plantas)} casas")
    atualizar_calculadora(plantas, numeros, gravar=SAIDA == EBOOK / "saida")
    gratis = config.get("plantas_gratis") or [config.get("planta_gratis", "C01")]
    if SAIDA == EBOOK / "saida":  # planta grátis de casa que saiu da lista (ou da edição) não fica para trás
        for velho in SAIDA.glob("planta-gratis-*.*"):
            if velho.stem.removeprefix("planta-gratis-") not in gratis:
                velho.unlink()
                print(f"apagada: {velho.name} (fora de plantas_gratis)")
    for pid in gratis:
        G = montar_gratis(plantas, config, pid)
        arq = SAIDA / f"planta-gratis-{pid}.html"
        arq.write_text(sem_quebra(doc.split("<body>")[0] + "<body>" + "".join(G.paginas) + "</body></html>"), encoding="utf-8")
        r = subprocess.run(["node", str(AQUI / "pdf.cjs"), str(arq), str(SAIDA / f"planta-gratis-{pid}.pdf")], env=env, capture_output=True, text=True)
        print(r.stdout.strip(), r.stderr.strip())
        falhou = falhou or r.returncode != 0
    if falhou or AVISOS:
        sys.exit("ERRO: página estourada, gancho que não bate com o validador ou falha ao gerar o PDF (veja os avisos acima)")


RECUSA_DUAS_PARTES = ("ERRO: --duas-partes só roda junto com --previa <pasta> nesta etapa (D17). O e-book em duas partes "
                      "ainda é prévia: o PDF oficial em ebook/saida/ e a calculadora não podem mudar agora.\n"
                      "Use: python3 ebook/gerador/livro.py --previa <pasta> --duas-partes")


def edicao(plantas, config):
    """As casas desta edição (config.json, "casas_lancamento"; vazia ou ausente = todas), na ordem do e-book.
    Casa da lista que não existe, planta grátis ou da capa fora da edição: erro (o PDF não sai)."""
    ids = config.get("casas_lancamento") or []
    if not ids:
        return plantas
    existem = {p["id"] for p in plantas}
    faltam = [i for i in ids if i not in existem]
    if faltam:
        sys.exit(f"casas_lancamento cita casa que não existe: {', '.join(faltam)}")
    gratis = config.get("plantas_gratis") or [config.get("planta_gratis", "C01")]
    fora = [i for i in gratis + [config.get("planta_da_capa", "C01")] if i not in ids]
    if fora:
        sys.exit(f"planta grátis ou da capa fora da edição de lançamento: {', '.join(fora)}")
    return [p for p in plantas if p["id"] in ids]


def atualizar_calculadora(plantas, numeros, gravar=True):
    """Reescreve a lista de casas da calculadora do parceiro a partir do validador (nunca à mão).
    Com gravar=False (--previa e --conferir) não toca no arquivo: só avisa se ele está desatualizado."""
    arq = EBOOK / "vendas" / "calculadora-lote.html"
    casas = [{"id": p["id"], "nome": p["nome"], "area": int(n0(p["_r"].metricas["area_fechada"])), "q": p["quartos_txt"],
              "b": p["banheiros"], "fr": p["_r"].metricas["lote"][0], "fu": p["_r"].metricas["lote"][1],
              "pag": numeros[p["id"]], "dest": p.get("destaque", "")} for p in plantas]
    txt = arq.read_text(encoding="utf-8")
    ini = txt.index("const CASAS = ")
    fim = txt.index("];", ini) + 2
    txt = txt[:ini] + "const CASAS = " + json.dumps(casas, ensure_ascii=False) + ";" + txt[fim:]
    # a nota dos recuos também sai das casas da edição (corredor e esquina só se houver)
    rf, rfu, rlat, rext = recuos_da_edicao(plantas)
    nota = (f"Conta feita com os recuos de referência do e-book: {rf} m na frente, {rfu} m nos fundos"
            + (f" e {rlat} m numa lateral, com a outra parede na divisa, se a prefeitura deixar." if rlat else ".")
            + (f" {rext}" if rext else "")
            + " A prefeitura do cliente pode pedir recuos maiores. A lista de casas sai do validador a cada geração do e-book."
              " É uma indicação de referência e não substitui o profissional.")
    ini = txt.index('<p class="nota">') + len('<p class="nota">')
    fim = txt.index("</p>", ini)
    novo = txt[:ini] + html.escape(nota, quote=False) + txt[fim:]
    if gravar:
        arq.write_text(novo, encoding="utf-8")
    elif novo != arq.read_text(encoding="utf-8"):
        print("AVISO: a calculadora do parceiro está desatualizada; ela só é regravada na geração oficial"
              " (python3 ebook/gerador/livro.py, sem --previa e sem --conferir)")


if __name__ == "__main__":
    prev = None
    if "--conferir" in sys.argv or "--previa" in sys.argv:
        # conferência e prévia: gera numa pasta temporária e não mexe em ebook/saida nem na calculadora.
        # O PDF oficial só é gravado sem --previa e sem --conferir.
        import tempfile
        SAIDA = Path(tempfile.mkdtemp(prefix="ebook-conferir-"))
    if "--previa" in sys.argv:
        prev = Path(sys.argv[sys.argv.index("--previa") + 1]).resolve()
    if "--duas-partes" in sys.argv and not prev:
        sys.exit(RECUSA_DUAS_PARTES)
    gerar(prev, duas_partes="--duas-partes" in sys.argv)
