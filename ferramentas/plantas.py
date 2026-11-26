"""Biblioteca e validador de plantas: as regras de projeto do X1-Plantas, em código.

Cada planta é um conjunto de cômodos retangulares em metros (x para a direita, y da frente
da casa, na rua, para os fundos), mais portas e janelas. O validador confere, pelas regras de
projeto do X1-Plantas (não é revisão de arquiteto), antes de uma planta entrar no e-book:

  Geometria       cômodos dentro da casa, sem sobreposição e sem vãos soltos
  Dimensões       área e lado mínimos de cada tipo de cômodo (acima do mínimo legal)
  Luz e ar        janela de pelo menos 1/6 do piso nos cômodos de permanência (1/8 em
                  cozinha, serviço e banheiro) e janela só em parede que dá para fora
  Circulação      toda parte alcançável a partir da entrada; circulação até 14% da área
  Privacidade     quarto e banheiro social nunca ficam no caminho de outro quarto
  Áreas molhadas  banheiro encostado em cozinha, serviço ou outro banheiro (uma prumada só)
  Vãos            cômodos com lado acima de 4,5 m pedem conferência da estrutura
  Lote            lote mínimo calculado a partir dos recuos de referência
  Orientação      melhor lado da rua para a frente da casa (critério simplificado)

IMPORTANTE: são regras de referência. Recuos, taxa de ocupação, aberturas e áreas mínimas
variam por município e por zona bioclimática (NBR 15220). Nenhuma planta aqui substitui
projeto legal assinado por arquiteto ou engenheiro habilitado.

Uso:
    python3 ferramentas/plantas.py validar          confere todas as plantas
    python3 ferramentas/plantas.py previa [ID ...]  rascunho em ebook/plantas/rascunhos/ (prévia em alta: imagens2d.py --previas)
    python3 ferramentas/plantas.py exportar         grava um JSON por planta em ebook/plantas/dados/
    python3 ferramentas/plantas.py fichas           regrava ebook/plantas/PLANTAS.md (a ficha de cada planta)
    python3 ferramentas/plantas.py resumo           mostra a tabela com os números calculados
    python3 ferramentas/plantas.py referencias      casa x regra das referências: grava ebook/plantas/CONSERTOS.md
"""
import json
import math
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PASTA = RAIZ / "ebook" / "plantas"
sys.path.insert(0, str(PASTA))

EXTERNOS = {"externo", "patio", "futuro"}          # fora da casa fechada
SEMIEXTERNOS = {"varanda", "garagem"}              # cobertos, abertos nas laterais
MOLHADOS = {"banho", "lavabo", "cozinha", "servico"}
PERMANENCIA = {"sala", "estar", "jantar", "dorm", "casal", "escritorio"}
# Paredes: as medidas da casa (W x D) são pela face de fora; cada cômodo perde a parede por dentro.
PAREDE_EXT, PAREDE_INT = 0.15, 0.12
# (área útil mínima m², menor lado livre m), medidos por dentro das paredes. Valores de referência do
# X1-Plantas, perto dos códigos de obras comuns; o código da cidade manda.
MINIMOS_UTIL = {
    "sala": (8.0, 2.3), "estar": (12.0, 2.8), "jantar": (5.0, 2.0), "dorm": (6.0, 2.0), "casal": (7.0, 2.3),
    "escritorio": (4.0, 1.6), "cozinha": (4.0, 1.5), "servico": (1.5, 0.95), "banho": (1.8, 1.0),
    "lavabo": (1.0, 0.8), "circ": (0.0, 0.8), "varanda": (0.0, 0.9), "garagem": (0.0, 2.5), "deposito": (0.8, 0.7),
}
# abaixo disto (por dentro) o cômodo funciona, mas é apertado: vira aviso para o engenheiro
CONFORTO_UTIL = {"sala": (9.0, 2.5), "casal": (8.0, 2.4)}
# (área mínima m², menor lado m) de eixo: usados só para as janelas automáticas
MINIMOS = {
    "sala": (10.0, 2.6), "estar": (14.0, 3.0), "jantar": (6.0, 2.2),
    "dorm": (7.0, 2.4), "casal": (8.5, 2.6), "escritorio": (4.5, 1.8),
    "cozinha": (4.5, 1.7), "servico": (2.0, 1.2), "banho": (2.4, 1.2),
    "lavabo": (1.2, 0.9), "circ": (0.0, 0.9), "varanda": (0.0, 0.9),
    "garagem": (0.0, 2.6), "deposito": (1.0, 0.8),
}
ALTURA_JANELA = {"sala": 1.4, "estar": 1.4, "jantar": 1.2, "dorm": 1.2, "casal": 1.2,
                 "escritorio": 1.2, "cozinha": 1.0, "servico": 1.0, "banho": 0.6, "lavabo": 0.6}
RAZAO_JANELA = {"sala": 1 / 6, "estar": 1 / 6, "jantar": 1 / 6, "dorm": 1 / 6, "casal": 1 / 6,
                "escritorio": 1 / 6, "cozinha": 1 / 8, "servico": 1 / 8, "banho": 1 / 8, "lavabo": 1 / 8}
# Veneziana em cima da porta de fora (F(..., veneziana_sobre_porta="fundos"); decisão do dono para a C01, 24/11/2026):
# na largura do vão da porta de fora (0,90 m), da verga da porta (2,10 m) até 2,60 m; sobram 20 cm de verga até o teto
# de 2,80 m do desenho 3D. Só em cômodo de 1/8 (cozinha, serviço, banheiro) e só onde há porta de fora embaixo.
VENEZIANA_PORTA = {"largura": 0.9, "base": 2.1, "topo": 2.6}
CIRC_MAX = 0.14
VAO_MAX = 4.5
RECUOS_PADRAO = {"frente": 3.0, "fundos": 1.5, "esq": 0.0, "dir": 1.5}  # esq = parede na divisa

NOMES_LADO = {"frente": "frente", "fundos": "fundos", "esq": "esquerda", "dir": "direita"}
# Para cada orientação da frente da casa, o ponto cardeal de cada lado da planta.
# O desenho põe a rua embaixo; quem está na rua olha para dentro do lote, e a direita do desenho é a direita dele.
# Rua ao norte = ele olha para o sul = a direita é o oeste. Até 26/11/2026 a tabela estava espelhada nos lados
# (achado do Nilo, o Arquiteto, na passada do e-book); o checar.py agora confere pela regra: direita = o ponto
# anterior a "frente" na volta N, L, S, O.
ORIENTACAO = {
    "norte": {"frente": "N", "dir": "W", "fundos": "S", "esq": "E"},
    "leste": {"frente": "E", "dir": "N", "fundos": "W", "esq": "S"},
    "sul": {"frente": "S", "dir": "E", "fundos": "N", "esq": "W"},
    "oeste": {"frente": "W", "dir": "S", "fundos": "E", "esq": "N"},
}
PESO_SOL = {  # por metro de janela: manhã (L) vale muito nos quartos, tarde (O) pesa contra
    "dorm": {"N": 2, "E": 3, "S": 1, "W": -3}, "casal": {"N": 2, "E": 3, "S": 1, "W": -3},
    "sala": {"N": 3, "E": 2, "S": 1, "W": -1}, "estar": {"N": 3, "E": 2, "S": 1, "W": -1},
    "jantar": {"N": 3, "E": 2, "S": 1, "W": -1},
    "cozinha": {"N": 0, "E": 1, "S": 2, "W": 0}, "servico": {"N": 0, "E": 0, "S": 1, "W": 2},
    "banho": {"N": 0.5, "E": 0.5, "S": 0.5, "W": 0.5}, "lavabo": {"N": 0.5, "E": 0.5, "S": 0.5, "W": 0.5},
    "escritorio": {"N": 3, "E": 1, "S": 3, "W": -1},
}


# --------------------------------------------------------------------------------------
# Construção das plantas
# --------------------------------------------------------------------------------------
def R(id, nome, tipo, x0, y0, x1, y1, **extra):
    d = {"id": id, "nome": nome, "tipo": tipo, "x0": round(x0, 3), "y0": round(y0, 3),
         "x1": round(x1, 3), "y1": round(y1, 3)}
    d.update(extra)
    return d


def linha(y0, y1, x0, itens):
    """Cômodos lado a lado. itens: (id, nome, tipo, largura[, extra])."""
    out, x = [], x0
    for it in itens:
        id, nome, tipo, w = it[:4]
        extra = it[4] if len(it) > 4 else {}
        out.append(R(id, nome, tipo, x, y0, x + w, y1, **extra))
        x += w
    return out


def coluna(x0, x1, y0, itens):
    """Cômodos empilhados. itens: (id, nome, tipo, altura[, extra])."""
    out, y = [], y0
    for it in itens:
        id, nome, tipo, h = it[:4]
        extra = it[4] if len(it) > 4 else {}
        out.append(R(id, nome, tipo, x0, y, x1, y + h, **extra))
        y += h
    return out


def area(c):
    return (c["x1"] - c["x0"]) * (c["y1"] - c["y0"])


def lados(c):
    return c["x1"] - c["x0"], c["y1"] - c["y0"]


def _desconto(planta, c, lado):
    """Quanto o cômodo perde de parede naquele lado: parede externa inteira, metade da interna."""
    abertos = SEMIEXTERNOS | EXTERNOS  # varanda, garagem, pátio, jardim e ampliação: a parede para eles é externa
    passagens = {frozenset(pt[:2]) for pt in planta.get("portas", []) if len(pt) > 2 and pt[2] == "aberto"}
    aberto = c["tipo"] in abertos
    borda = {"esq": abs(c["x0"]) < 1e-6, "dir": abs(c["x1"] - planta["W"]) < 1e-6,
             "frente": abs(c["y0"]) < 1e-6, "fundos": abs(c["y1"] - planta["D"]) < 1e-6}[lado]
    d = 0.0 if aberto else (PAREDE_EXT if borda else 0.0)
    eixo = {"esq": ("v", c["x0"]), "dir": ("v", c["x1"]), "frente": ("h", c["y0"]), "fundos": ("h", c["y1"])}[lado]
    for o in planta["comodos"]:
        if o is c or o["tipo"] == "futuro":
            continue
        pc = parede_comum(c, o)
        if not pc or pc[0] != eixo[0] or abs(pc[1] - eixo[1]) > 1e-6:
            continue
        if frozenset((c["id"], o["id"])) in passagens:
            continue  # passagem aberta: não há parede entre os dois
        o_aberto = o["tipo"] in abertos
        dd = 0.0 if aberto else (PAREDE_EXT if o_aberto else PAREDE_INT / 2)
        d = max(d, dd)
    return d


def util(planta, c):
    """Medidas livres do cômodo, por dentro das paredes: (largura, profundidade, área)."""
    lx = c["x1"] - c["x0"] - _desconto(planta, c, "esq") - _desconto(planta, c, "dir")
    ly = c["y1"] - c["y0"] - _desconto(planta, c, "frente") - _desconto(planta, c, "fundos")
    return lx, ly, lx * ly


def _intervalo(a0, a1, b0, b1):
    lo, hi = max(a0, b0), min(a1, b1)
    return (lo, hi) if hi - lo > 1e-6 else None


def parede_comum(a, b):
    """Trecho de parede entre dois cômodos: (orientação, posição fixa, início, fim)."""
    for (p, q) in ((a, b), (b, a)):
        if abs(p["x1"] - q["x0"]) < 1e-6:
            iv = _intervalo(p["y0"], p["y1"], q["y0"], q["y1"])
            if iv:
                return ("v", p["x1"], iv[0], iv[1])
        if abs(p["y1"] - q["y0"]) < 1e-6:
            iv = _intervalo(p["x0"], p["x1"], q["x0"], q["x1"])
            if iv:
                return ("h", p["y1"], iv[0], iv[1])
    return None


def _dentro(planta, x, y, ignorar=()):
    for c in planta["comodos"]:
        if c["id"] in ignorar:
            continue
        if c["x0"] - 1e-9 <= x <= c["x1"] + 1e-9 and c["y0"] - 1e-9 <= y <= c["y1"] + 1e-9:
            return c
    return None


def trecho_externo(planta, c, lado):
    """Comprimento da parede do lado 'lado' do cômodo que dá para fora (m)."""
    if lado in ("frente", "fundos"):
        y = c["y0"] if lado == "frente" else c["y1"]
        d = -0.05 if lado == "frente" else 0.05
        a, b = c["x0"], c["x1"]
        pts = [(x, y + d) for x in _passos(a, b)]
    else:
        x = c["x0"] if lado == "esq" else c["x1"]
        d = -0.05 if lado == "esq" else 0.05
        a, b = c["y0"], c["y1"]
        pts = [(x + d, y) for y in _passos(a, b)]
    total, n = 0.0, 0
    for (px, py) in pts:
        viz = _dentro(planta, px, py, ignorar=(c["id"],))
        n += 1
        if viz is None or (viz["tipo"] in EXTERNOS and viz["tipo"] != "futuro") or viz["tipo"] in SEMIEXTERNOS and c["tipo"] not in SEMIEXTERNOS:
            total += 1
    return (b - a) * total / max(n, 1)


def _passos(a, b, passo=0.1):
    n = max(int(round((b - a) / passo)), 1)
    return [a + (i + 0.5) * (b - a) / n for i in range(n)]


def _rec(planta):
    rec = dict(RECUOS_PADRAO)
    rec.update(planta.get("recuos", {}))
    return rec


def _na_borda(planta, c, lado):
    """A parede está na lateral da casa (e não virada para um pátio interno)?"""
    return abs(c["x0"]) < 1e-6 if lado == "esq" else abs(c["x1"] - planta["W"]) < 1e-6


def _vizinho_coberto(planta, c, lado):
    x = c["x0"] - 0.05 if lado == "esq" else c["x1"] + 0.05
    y = (c["y0"] + c["y1"]) / 2
    v = _dentro(planta, x, y, ignorar=(c["id"],))
    return v is not None and (v["tipo"] in SEMIEXTERNOS or v["tipo"] in EXTERNOS)


def F(id, nome, tipo, **kw):
    return ("folha", dict(id=id, nome=nome, tipo=tipo, **kw))


def movel(tipo, lado, x0, y0, x1, y1, **kw):
    """Móvel posto à mão pelo Arquiteto: F(..., moveis=[movel(...), ...]) troca o arranjo automático do motor 3D naquele cômodo.

    (x0, y0, x1, y1) é o retângulo que ele ocupa no chão, em metros a partir do canto (x0, y0) do cômodo; a parede é a de
    verdade, a mesma do 3D e da planta 2D (P3.paredes_reais): a face de dentro fica a 15 cm da face de fora na parede
    externa e a 6 cm do eixo na interna, então móvel encostado começa aí. A mesa de jantar conta as cadeiras.
    lado: a parede para a qual ele dá as costas (cabeceira da cama, encosto do sofá, fundo do armário e da escrivaninha)."""
    w, d = (x1 - x0, y1 - y0) if lado in ("frente", "fundos") else (y1 - y0, x1 - x0)
    if tipo == "mesaJantar":
        w -= 0.9  # o motor soma as cadeiras (0,45 m de cada lado) à largura
    rot = {"frente": 0.0, "fundos": math.pi, "esq": math.pi / 2, "dir": -math.pi / 2}[lado]
    return dict(tipo=tipo, x=round((x0 + x1) / 2, 3), y=round((y0 + y1) / 2, 3), rot=rot, w=round(w, 3), d=round(d, 3), **kw)


def H(*itens):
    return ("H", list(itens))


def V(*itens):
    return ("V", list(itens))


def monta(W, D, no):
    out = []

    def rec(no, x0, y0, x1, y1):
        if no[0] == "folha":
            d = dict(no[1])
            d.update(x0=round(x0, 3), y0=round(y0, 3), x1=round(x1, 3), y1=round(y1, 3))
            out.append(d)
            return
        modo, itens = no
        total = (y1 - y0) if modo == "H" else (x1 - x0)
        fixo = sum(t for t, _ in itens if t is not None)
        livres = [i for i, (t, _) in enumerate(itens) if t is None]
        if len(livres) > 1 or (not livres and abs(fixo - total) > 0.011):
            raise ValueError(f"divisão inválida: soma {fixo:.2f} de {total:.2f} em {itens[0][1][1].get('id', '?') if itens[0][1][0] == 'folha' else modo}")
        pos = y0 if modo == "H" else x0
        for t, filho in itens:
            t = t if t is not None else total - fixo
            if modo == "H":
                rec(filho, x0, pos, x1, pos + t)
            else:
                rec(filho, pos, y0, pos + t, y1)
            pos += t
    rec(no, 0.0, 0.0, W, D)
    return out


def casa(id, nome, W, D, arvore, portas, quartos_txt, banheiros, extra=(), **kw):
    p = dict(id=id, nome=nome, W=W, D=D, comodos=monta(W, D, arvore) + list(extra),
             portas=portas, quartos_txt=quartos_txt, banheiros=banheiros, janelas={})
    p.update(kw)
    return p


def _livre_para_fora(planta, c, lado):
    """Comprimento da parede que dá para fora e pode ter janela (respeita divisas)."""
    ext = trecho_externo(planta, c, lado)
    if ext <= 0:
        return 0.0
    if lado in ("esq", "dir") and _na_borda(planta, c, lado) and _rec(planta)[lado] < 1.4 and not _vizinho_coberto(planta, c, lado):
        return 0.0
    return ext


PREFERENCIA = {"sala": ("frente", "dir", "esq", "fundos"), "estar": ("frente", "dir", "esq", "fundos"),
               "jantar": ("dir", "esq", "frente", "fundos"), "cozinha": ("fundos", "dir", "esq", "frente"),
               "servico": ("dir", "esq", "fundos", "frente"), "banho": ("dir", "esq", "fundos", "frente"),
               "lavabo": ("dir", "esq", "fundos", "frente"), "dorm": ("fundos", "dir", "esq", "frente"),
               "casal": ("fundos", "dir", "esq", "frente"), "escritorio": ("frente", "dir", "esq", "fundos")}


def auto_janelas(planta):
    """Põe janelas onde a parede dá para fora, na ordem de preferência das regras de projeto do X1-Plantas."""
    planta["janelas"] = {}
    for c in planta["comodos"]:
        t = c["tipo"]
        if t not in RAZAO_JANELA or c.get("sem_janela"):
            continue
        falta = RAZAO_JANELA[t] * area(c) * 1.18 / ALTURA_JANELA[t]
        lista = []
        for lado in c.get("pref", PREFERENCIA[t]):
            if falta <= 0.01:
                break
            if lado == c.get("veneziana_sobre_porta"):  # a parede da porta já tem a veneziana: janela ali cairia na porta
                continue
            ext = _livre_para_fora(planta, c, lado)
            if ext < 1.0 - 1e-6 and not (t in ("banho", "lavabo") and ext >= 0.9):
                continue
            largura = min(ext - 0.4 if ext >= 1.4 else ext - 0.3, max(falta, 0.6))
            largura = math.ceil(largura * 10 - 1e-9) / 10
            largura = min(largura, math.floor((ext - 0.3) * 10) / 10)
            if largura < 0.5:
                continue
            lista.append((lado, largura))
            falta -= largura
        if lista:
            planta["janelas"][c["id"]] = lista


# --------------------------------------------------------------------------------------
# Validação
# --------------------------------------------------------------------------------------
class Relatorio:
    def __init__(self, planta):
        self.p = planta
        self.erros, self.avisos, self.info = [], [], []
        self.referencias, self.ref_info = [], []  # régua das referências: lista de conserto, não vai ao comprador
        self.metricas = {}

    def erro(self, m):
        self.erros.append(m)

    def aviso(self, m):
        self.avisos.append(m)


def casa_fechada(planta):
    return [c for c in planta["comodos"] if c["tipo"] not in EXTERNOS and c["tipo"] not in SEMIEXTERNOS]


def validar(planta):
    r = Relatorio(planta)
    W, D = planta["W"], planta["D"]
    cs = planta["comodos"]
    por_id = {c["id"]: c for c in cs}
    if len(por_id) != len(cs):
        r.erro("ids de cômodos repetidos")

    # Geometria
    for c in cs:
        if c["x0"] < -1e-6 or c["y0"] < -1e-6 or c["x1"] > W + 1e-6 or c["y1"] > D + 1e-6:
            if c["tipo"] != "futuro":
                r.erro(f"{c['nome']} fora da área da casa")
    base = [c for c in cs if c["tipo"] != "futuro"]
    for i, a in enumerate(base):
        for b in base[i + 1:]:
            ix = _intervalo(a["x0"], a["x1"], b["x0"], b["x1"])
            iy = _intervalo(a["y0"], a["y1"], b["y0"], b["y1"])
            if ix and iy:
                r.erro(f"{a['nome']} e {b['nome']} se sobrepõem")
    soma = sum(area(c) for c in base)
    if abs(soma - W * D) > 0.05:
        r.erro(f"cômodos somam {soma:.2f} m², mas a casa tem {W * D:.2f} m² (vão solto ou sobreposição)")
    for f in [c for c in cs if c["tipo"] == "futuro"]:
        for b in base:
            if _intervalo(f["x0"], f["x1"], b["x0"], b["x1"]) and _intervalo(f["y0"], f["y1"], b["y0"], b["y1"]):
                r.erro(f"ampliação {f['nome']} invade {b['nome']}")

    fechada = casa_fechada(planta)
    a_fechada = sum(area(c) for c in fechada)
    r.metricas["area_fechada"] = round(a_fechada, 1)
    r.metricas["area_total"] = round(W * D, 1)
    r.metricas["area_coberta_aberta"] = round(sum(area(c) for c in cs if c["tipo"] in SEMIEXTERNOS), 1)

    # Dimensões mínimas, por dentro das paredes
    r.metricas["util"] = {}
    for c in cs:
        t = c["tipo"]
        lx, ly, a = util(planta, c)
        r.metricas["util"][c["id"]] = [round(lx, 2), round(ly, 2), round(a, 1)]
        if t in MINIMOS_UTIL:
            amin, lmin = MINIMOS_UTIL[t]
            if a < amin - 1e-6:
                r.erro(f"{c['nome']}: {a:.1f} m² livres (mínimo de referência {amin:.1f} m²)")
            if min(lx, ly) < lmin - 1e-6:
                r.erro(f"{c['nome']}: menor lado livre {min(lx, ly):.2f} m (mínimo de referência {lmin:.2f} m)")
            if t in CONFORTO_UTIL:
                ac, lc = CONFORTO_UTIL[t]
                if a < ac - 1e-6 or min(lx, ly) < lc - 1e-6:
                    r.aviso(f"{c['nome']} fica com {lx:.2f} x {ly:.2f} m livres ({_f(a)} m²)".replace(".", ",") + ": funciona, mas é apertado; o engenheiro confere a mobília")
        if t in PERMANENCIA or t == "cozinha":
            if max(lados(c)) > VAO_MAX + 1e-6:
                r.info.append(f"{c['nome']} tem vão de {max(lados(c)):.1f} m: o engenheiro confere laje e vigas")

    # Janelas
    janelas = planta.get("janelas", {})
    for id, lista in janelas.items():
        if id not in por_id:
            r.erro(f"janela em cômodo que não existe: {id}")
    soma_luz = {}
    for c in cs:
        t = c["tipo"]
        if t not in RAZAO_JANELA:
            continue
        lista = janelas.get(c["id"], [])
        a_jan = 0.0
        for (lado, larg) in lista:
            ext = trecho_externo(planta, c, lado)
            if lado in ("esq", "dir") and _na_borda(planta, c, lado) and _rec(planta)[lado] < 1.4 and not _vizinho_coberto(planta, c, lado):
                r.erro(f"{c['nome']}: janela na {NOMES_LADO[lado]}, que é divisa (recuo {_rec(planta)[lado]:.1f} m)")
            if ext < larg + 0.3 - 1e-6:
                r.erro(f"{c['nome']}: janela de {larg:.1f} m na {NOMES_LADO[lado]} não cabe "
                       f"(parede que dá para fora: {ext:.1f} m)")
            a_jan += larg * ALTURA_JANELA[t]
        ven = c.get("veneziana_sobre_porta")
        if ven:
            # declarada, nunca automática: tem de ter porta de fora embaixo, não divide a parede com janela e, contando o vão
            # inteiro, chega a 1/8 do piso livre; mesmo assim vira aviso (passa menos ar e quase nenhuma luz, e só com o
            # pé-direito de 2,80 m do desenho: com 2,50 ou 2,55 m ela fica mais baixa e dá uns 9 a 11%; veto do Revisor, 24/11)
            vl, vh = VENEZIANA_PORTA["largura"], VENEZIANA_PORTA["topo"] - VENEZIANA_PORTA["base"]
            a_ven, livre = vl * vh, util(planta, c)[2]
            if RAZAO_JANELA[t] != 1 / 8:
                r.erro(f"{c['nome']}: veneziana em cima da porta só em cozinha, serviço ou banheiro, não em cômodo de permanência")
            if not any(pt[0] == "ext" and pt[1] == c["id"] and len(pt) > 2 and pt[2] == ven for pt in planta.get("portas", [])):
                r.erro(f"{c['nome']}: veneziana na {NOMES_LADO[ven]}, mas não há porta de fora embaixo dela")
            if any(l == ven for (l, _) in lista):
                r.erro(f"{c['nome']}: janela e veneziana na mesma parede ({NOMES_LADO[ven]})")
            if (a_jan + a_ven) / livre + 1e-9 < RAZAO_JANELA[t]:
                r.erro(f"{c['nome']}: janela e veneziana somam {(a_jan + a_ven) / livre * 100:.0f}% do piso livre (mínimo de referência 12,5%)")
            m2 = lambda v: f"{v:.2f}".replace(".", ",")
            de = {"servico": "do serviço", "cozinha": "da cozinha", "banho": "do banheiro", "lavabo": "do lavabo"}.get(t, "do cômodo")
            pd = VENEZIANA_PORTA["topo"] + 0.2  # 20 cm de verga até o teto (ver VENEZIANA_PORTA)
            r.aviso(f"{c['nome']}: {'não tem janela. A ventilação vem de' if not lista else 'além da janela, a ventilação conta com'} uma veneziana de "
                    f"{m2(vl)} x {m2(vh)} m em cima da porta de fora, que só cabe com pé-direito de uns {m2(pd)} m. Ela deixa passar menos ar e "
                    f"quase nenhuma luz: o engenheiro confere se a ventilação e a luz {de} bastam no código de obras da sua cidade.")
            a_jan += a_ven
        razao = a_jan / area(c) if area(c) else 0
        soma_luz[c["id"]] = razao
        if razao + 1e-9 < RAZAO_JANELA[t] and not ven:  # com veneziana, a conta é a de cima (piso livre) e o aviso
            if t in ("banho", "lavabo") and c.get("exaustao"):
                r.aviso(f"{c['nome']}: sem janela suficiente, ventilação por exaustão mecânica (confira o código)")
            else:
                r.erro(f"{c['nome']}: janela de {razao * 100:.0f}% do piso "
                       f"(mínimo de referência {RAZAO_JANELA[t] * 100:.0f}%)")
    r.metricas["luz"] = {k: round(v, 4) for k, v in soma_luz.items()}

    # Conexões e circulação
    g = {}
    def liga(a, b):
        g.setdefault(a, set()).add(b)
        g.setdefault(b, set()).add(a)
    for porta in planta.get("portas", []):
        a, b = porta[0], porta[1]
        if a != "ext" and a not in por_id or b not in por_id:
            r.erro(f"porta com cômodo desconhecido: {porta[:2]}")
            continue
        if a == "ext":
            liga("ext", b)
            continue
        pc = parede_comum(por_id[a], por_id[b])
        if not pc:
            r.erro(f"porta entre {a} e {b}, mas os cômodos não dividem parede")
            continue
        comp = pc[3] - pc[2]
        aberta = len(porta) > 2 and porta[2] == "aberto"
        if comp < (1.0 if aberta else 0.9) - 1e-6:
            r.erro(f"{por_id[a]['nome']}–{por_id[b]['nome']}: parede em comum de {comp:.2f} m é curta para a ligação")
        liga(a, b)
    entrou = {a for a in g if "ext" in g.get(a, ())}
    if "ext" not in g:
        r.erro("a casa não tem porta de entrada")
    alcancados, fila = {"ext"}, ["ext"]
    while fila:
        n = fila.pop()
        for m in g.get(n, ()):
            if m not in alcancados:
                alcancados.add(m)
                fila.append(m)
    for c in fechada:
        if c["id"] not in alcancados:
            r.erro(f"{c['nome']} não é alcançável a partir da entrada")
    circ = sum(area(c) for c in cs if c["tipo"] == "circ")
    r.metricas["circulacao"] = round(circ / a_fechada, 3) if a_fechada else 0
    if a_fechada and circ / a_fechada > CIRC_MAX:
        r.erro(f"circulação ocupa {circ / a_fechada * 100:.0f}% da casa (máximo de referência {CIRC_MAX * 100:.0f}%)")

    # Privacidade: o caminho até um quarto ou banho não passa por outro quarto
    def caminho_sem(alvo, proibidos, permitido=()):
        vistos, fila = {"ext"}, ["ext"]
        while fila:
            n = fila.pop()
            for m in g.get(n, ()):
                if m in vistos:
                    continue
                if m == alvo:
                    return True
                if m in proibidos and m not in permitido:
                    continue
                vistos.add(m)
                fila.append(m)
        return False
    privados = {c["id"] for c in cs if c["tipo"] in ("dorm", "casal")}
    banhos = {c["id"] for c in cs if c["tipo"] == "banho"}
    for c in cs:
        if c["tipo"] in ("dorm", "casal"):
            if not caminho_sem(c["id"], privados | banhos):
                r.erro(f"{c['nome']} só se alcança passando por outro quarto ou banheiro")
        if c["tipo"] == "banho":
            dono = c.get("privativo")
            perm = (dono,) if dono else ()
            if not caminho_sem(c["id"], privados | banhos, perm):
                r.erro(f"{c['nome']} só se alcança passando por um quarto")
            if not dono:
                # o banheiro social não deve abrir direto para a cozinha
                if "cozinha" in g.get(c["id"], ()) or any(por_id[x]["tipo"] == "cozinha" for x in g.get(c["id"], ()) if x != "ext"):
                    r.erro(f"{c['nome']} abre direto para a cozinha")

    # Ampliação: não pode tapar janela nem ficar presa atrás de quarto sem saída para o quintal
    for f in [c for c in cs if c["tipo"] == "futuro"]:
        for b in cs:
            pc = parede_comum(f, b) if b is not f and b["tipo"] != "futuro" else None
            if not pc:
                continue
            lado_b = ("fundos" if abs(pc[1] - b["y1"]) < 1e-6 else "frente") if pc[0] == "h" else ("dir" if abs(pc[1] - b["x1"]) < 1e-6 else "esq")
            if any(l == lado_b for (l, _) in janelas.get(b["id"], [])):
                r.erro(f"ampliação {f['nome']} tapa a janela de {b['nome']}")
        if not any(trecho_externo(planta, f, l) >= 0.9 for l in ("esq", "dir", "fundos", "frente")):
            r.erro(f"ampliação {f['nome']} não tem parede livre para a porta")

    # Casa acessível: banheiro e circulação com o giro de 1,50 m da cadeira de rodas (por dentro das paredes)
    if planta.get("acessivel"):
        for c in cs:
            if c["tipo"] in ("banho", "circ"):
                lx, ly, _ = util(planta, c)
                if min(lx, ly) < 1.5 - 1e-6:
                    r.erro(f"{c['nome']}: {min(lx, ly):.2f} m livres, não cabe o giro de 1,50 m da cadeira de rodas")
        r.info.append("Casa acessível: o engenheiro confere o resto da NBR 9050 (barras, portas, área de transferência, entrada sem degrau)")

    # Varanda encostada numa divisa: a lateral dela fica fechada (Código Civil, art. 1.301)
    for c in cs:
        if c["tipo"] == "varanda" and c["id"] != "corr":
            for lado in ("esq", "dir"):
                if _na_borda(planta, c, lado) and _rec(planta)[lado] < 1.4:
                    r.aviso(f"{c['nome']} encosta na divisa da {NOMES_LADO[lado]}: essa lateral fica fechada, sem abertura para o vizinho (o Código Civil, art. 1.301, não deixa fazer varanda a menos de 1,5 m do terreno vizinho: o engenheiro confirma)")
                    break

    # Áreas molhadas juntas
    for c in cs:
        if c["tipo"] == "banho":
            viz = [o for o in cs if o["id"] != c["id"] and o["tipo"] in MOLHADOS and parede_comum(c, o)]
            if not viz:
                r.aviso(f"{c['nome']} não encosta em cozinha, serviço ou outro banheiro: prumada própria, um cano que desce só para esse banheiro (custa mais)")
    coz = [c for c in cs if c["tipo"] == "cozinha"]
    serv = [c for c in cs if c["tipo"] == "servico"]
    if not serv:
        r.erro("a casa não tem área de serviço")
    for c in coz:
        if serv and not planta.get("servico_externo") and not any(parede_comum(c, s) for s in serv):
            r.aviso("a cozinha não encosta na área de serviço")

    if planta.get("acessivel"):
        for c in cs:
            if c["tipo"] == "circ" and min(lados(c)) < 1.2 - 1e-6:
                r.erro(f"{c['nome']}: circulação de {min(lados(c)):.2f} m (casa acessível pede 1,20 m)")
            if c["tipo"] == "banho" and min(lados(c)) < 1.5 - 1e-6:
                r.erro(f"{c['nome']}: banheiro sem giro de 1,50 m")

    # Lote mínimo de referência
    rec = dict(RECUOS_PADRAO)
    rec.update(planta.get("recuos", {}))
    xs = [c["x0"] for c in base] + [c["x1"] for c in base]
    ys = [c["y0"] for c in base] + [c["y1"] for c in base]
    fut = [c for c in cs if c["tipo"] == "futuro"]
    ymax = max([c["y1"] for c in base + fut])
    xmax = max([c["x1"] for c in base + fut])
    lote_frente = round(xmax + rec["esq"] + rec["dir"] + 0.0, 1)
    lote_fundo = round(ymax + rec["frente"] + rec["fundos"], 1)
    r.metricas["lote"] = (lote_frente, lote_fundo)
    r.metricas["recuos"] = rec
    r.metricas["lote_comercial"] = (math.ceil(lote_frente), math.ceil(lote_fundo / 5) * 5)
    ocupacao = (W * D) / (lote_frente * lote_fundo)
    r.metricas["taxa_ocupacao"] = round(ocupacao, 2)
    if lote_frente < 5.0:
        r.erro(f"lote de {lote_frente:.1f} m de frente é menor que o mínimo da Lei 6.766 (5 m)")

    # Régua das 51 plantas de referência (aviso, não erro; dono, 23/11/2026)
    referencias(planta, r, g)

    # Orientação
    r.metricas["orientacao"] = melhor_orientacao(planta)
    return r


# As 5 regras tiradas das 51 plantas de referência (ebook/referencias/plantas-ref/REFERENCIAS.md), aprovadas
# pelo dono em 23/11/2026 como AVISO: viram a lista de conserto, não barram a planta. Medidas por dentro.
FONTE_REF = "ebook/referencias/plantas-ref/REFERENCIAS.md"
REF = {
    "circ_max": 0.06, "circ_ate_m2": 60.0, "lote_corredor": 4.5,  # 1: circulação; exceção: lote de 4 a 4,5 m
    "banho": 1.50,                                                # 2: os dois lados do banheiro
    "quarto": 2.85, "quarto_2camas": 2.60,                        # 3: largura do quarto
    "servico": 1.15,                                              # 4: "cerca de 1,20" (5 cm de folga)
    "cozinha": 1.80,                                              # 5b: menor lado da cozinha
    "frente_estreita": 6.0,                                       # informação: lote de até 6 m de frente
}
REGRAS_REF = [("1", "Circulação"), ("2", "Banheiro"), ("3", "Quarto"), ("4", "Serviço"), ("5a", "Por dentro"), ("5b", "Cozinha")]


def _m(v):
    return f"{v:.2f}".replace(".", ",")


def referencias(planta, r, g):
    """Grava em r.referencias [(regra, medida curta, frase)] e em r.metricas["frente_estreita"] a informação do lote.
    Fica fora de r.avisos de propósito: os avisos vão ao PDF e às fichas do comprador; estes são a lista de conserto."""
    r.referencias, r.ref_info = [], []  # fora de r.info também: o info vai ao PDF
    cs = planta["comodos"]
    u = r.metricas["util"]
    def fora(regra, curta, frase):
        r.referencias.append((regra, curta, f"{frase} (regra {regra}, {FONTE_REF})"))
    a_f = r.metricas["area_fechada"]
    frente = r.metricas["lote"][0]
    # 1. Circulação: o corredor coberto de fora a fora (id "corr") também é caminho, e entra na conta
    circ = sum(area(c) for c in cs if c["tipo"] == "circ" or c["id"] == "corr")
    pc = circ / a_f if a_f else 0
    r.metricas["circulacao_ref"] = round(pc, 3)
    if a_f <= REF["circ_ate_m2"] + 1e-6 and pc > REF["circ_max"] + 1e-6:
        qual = "corredor coberto lateral" if any(c["id"] == "corr" for c in cs) else "circulação"
        if frente <= REF["lote_corredor"] + 1e-6:
            r.ref_info.append(f"referência: {qual} de {pc * 100:.0f}% da casa, aceito como exceção (lote de {_m(frente)} m de frente; "
                          f"as referências de 4 a 4,5 m usam corredor lateral; regra 1, {FONTE_REF})")
        else:
            fora("1", f"{pc * 100:.0f}%", f"{qual} ocupa {pc * 100:.0f}% da casa de {_f(a_f)} m²; nas referências de até 60 m² "
                 f"fica em até 6% (corredor lateral só em lote de 4 a 4,5 m de frente)")
    # 2. Banheiro, 3. Quarto, 4. Serviço, 5b. Cozinha: o menor lado livre
    for c in cs:
        t = c["tipo"]
        lx, ly = u[c["id"]][:2]
        menor = min(lx, ly)
        if t == "banho" and menor < REF["banho"] - 1e-6:
            fora("2", _m(menor), f"{c['nome']} com {_m(lx)} x {_m(ly)} m livres; nas referências o banheiro tem os dois lados com 1,50 m ou mais")
        if t == "dorm" and menor < REF["quarto_2camas"] - 1e-6:
            fora("3", _m(menor), f"{c['nome']} com {_m(menor)} m de largura livre: abaixo de 2,60 m não cabem as duas camas; "
                 "nas referências o quarto tem 2,85 a 3,00 m")
        elif t in ("dorm", "casal") and menor < REF["quarto"] - 1e-6:
            fora("3", _m(menor), f"{c['nome']} com {_m(menor)} m de largura livre; nas referências o quarto tem 2,85 a 3,00 m")
        if t == "servico":
            saida = any(c["id"] in (pt[0], pt[1]) and ({pt[0], pt[1]} - {c["id"]}) & ({"ext"} | {o["id"] for o in cs if o["tipo"] in EXTERNOS | SEMIEXTERNOS})
                        for pt in planta.get("portas", []))
            falta = []
            if menor < REF["servico"] - 1e-6:
                falta.append(f"{_m(menor)} m de largura livre")
            if not saida:
                falta.append("sem porta para o quintal")
            if falta:
                fora("4", " e ".join(([_m(menor)] if menor < REF["servico"] - 1e-6 else []) + (["sem saída"] if not saida else [])),
                     f"{c['nome']}: " + "; ".join(falta) + "; nas referências o serviço tem cerca de 1,20 m e sai para o quintal")
        if t == "cozinha" and menor < REF["cozinha"] - 1e-6:
            fora("5b", _m(menor), f"{c['nome']} com {_m(menor)} m no menor lado livre; nas referências e na régua federal, pelo menos 1,80 m")
    # 5a. Banheiro e quartos alcançados por dentro: a partir da sala, sem sair para varanda, corredor coberto ou quintal
    dentro = {c["id"] for c in casa_fechada(planta)}
    vistos = {c["id"] for c in cs if c["tipo"] in ("sala", "estar", "jantar")}
    fila = list(vistos)
    while fila:
        n = fila.pop()
        for m in g.get(n, ()):
            if m in dentro and m not in vistos:
                vistos.add(m)
                fila.append(m)
    por_fora = [c["nome"] for c in cs if c["tipo"] in ("banho", "dorm", "casal") and c["id"] not in vistos]
    if por_fora:
        fora("5a", f"{len(por_fora)} por fora", f"{', '.join(por_fora)}: da sala só se chega saindo de casa (corredor coberto, varanda ou quintal); "
             "nas referências banheiro e quartos se alcançam por dentro")
    # Informação: frente estreita
    r.metricas["frente_estreita"] = frente <= REF["frente_estreita"] + 1e-6
    if r.metricas["frente_estreita"]:
        r.ref_info.append(f"referência (informação): casa de frente estreita, lote de {_m(frente)} m de frente; "
                      f"as referências de São José dos Campos chegam a lote de 4 a 5 m ({FONTE_REF}, padrão 1)")


def melhor_orientacao(planta):
    por_id = {c["id"]: c for c in planta["comodos"]}
    pontos = {}
    for ori, mapa in ORIENTACAO.items():
        total = 0.0
        for id, lista in planta.get("janelas", {}).items():
            c = por_id.get(id)
            if not c or c["tipo"] not in PESO_SOL:
                continue
            for (lado, larg) in lista:
                total += larg * PESO_SOL[c["tipo"]][mapa[lado]]
        pontos[ori] = round(total, 1)
    ordem = sorted(pontos, key=lambda k: -pontos[k])
    return {"melhor": ordem[0], "segunda": ordem[1], "pior": ordem[-1], "pontos": pontos}


# --------------------------------------------------------------------------------------
# Previa (desenho 2D)
# --------------------------------------------------------------------------------------
def porta_dobradica(planta, d):
    """Dobradiça, ponta da folha fechada e ponta da folha aberta de uma porta do motor 3D (coordenadas da planta).

    O arco() do motor gira sempre no mesmo sentido, então metade das portas saía com a dobradiça no lado
    errado (a folha abria para o meio do cômodo, espelhada). Aqui a dobradiça vai para a ponta do vão mais
    perto do canto da parede, onde a folha aberta encosta, e a folha continua abrindo para o mesmo cômodo.
    Decide pela geometria (não inverte nada), então continua certo se o motor for corrigido."""
    hx, hy, r = d["x"], d["y"], d["r"]
    px, py = hx + r * math.cos(d["a0"]), hy + r * math.sin(d["a0"])
    ux, uy = math.cos(d["a1"]), math.sin(d["a1"])
    horiz = abs(math.sin(d["a0"])) < 1e-6
    por_id = {c["id"]: c for c in planta["comodos"]}
    ids = str(d["id"])
    ponta = None
    if ids.startswith("ext-") and ids[4:] in por_id:
        c = por_id[ids[4:]]
        ponta = (c["x0"], c["x1"]) if horiz else (c["y0"], c["y1"])
    else:
        for porta in planta.get("portas", []):
            if f"{porta[0]}-{porta[1]}" == ids and porta[0] in por_id and porta[1] in por_id:
                pc = parede_comum(por_id[porta[0]], por_id[porta[1]])
                if pc:
                    ponta = (pc[2], pc[3])
                break
    if ponta:
        dist = lambda v: min(abs(v - ponta[0]), abs(v - ponta[1]))
        e0, e1 = (hx, px) if horiz else (hy, py)
        if dist(e1) < dist(e0) - 1e-6:
            hx, hy, px, py = px, py, hx, hy
    return (hx, hy), (px, py), (hx + r * ux, hy + r * uy)


CORES = {"sala": "#E8D7BC", "estar": "#E8D7BC", "jantar": "#E8D7BC", "cozinha": "#D5E0CF",
         "dorm": "#EADCC6", "casal": "#E6D0B0", "banho": "#CFE0E6", "lavabo": "#CFE0E6",
         "servico": "#D8E4D0", "circ": "#F1EBE0", "escritorio": "#E3DDF0", "varanda": "#EDEFE2",
         "garagem": "#DADDE2", "patio": "#DDEBCF", "externo": "#FFFFFF", "futuro": "#FFF1D0",
         "deposito": "#E9E2D6"}


def previa(planta, caminho, escala=80):
    from PIL import Image, ImageDraw, ImageFont
    W, D = planta["W"], planta["D"]
    fut = [c for c in planta["comodos"] if c["tipo"] == "futuro"]
    Dm = max([D] + [c["y1"] for c in fut])
    Wm = max([W] + [c["x1"] for c in fut])
    m = 90
    larg, alt = int(Wm * escala + 2 * m), int(Dm * escala + 2 * m + 70)
    im = Image.new("RGB", (larg, alt), "#0B4FA8")
    d = ImageDraw.Draw(im)
    for i in range(0, larg, escala // 2):
        d.line([(i, 0), (i, alt)], fill="#1860B8", width=1)
    for j in range(0, alt, escala // 2):
        d.line([(0, j), (larg, j)], fill="#1860B8", width=1)
    try:
        f = ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-SemiBold.otf", 15)
        fg = ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-Bold.otf", 22)
        fp = ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-Regular.otf", 12)
    except OSError:
        f = fg = fp = ImageFont.load_default()
    X = lambda x: m + x * escala
    Y = lambda y: m + y * escala + 40
    d.text((m, 14), f"{planta['id']} · {planta['nome']}", font=fg, fill="white")
    for c in planta["comodos"]:
        if c["tipo"] == "externo":
            continue
        box = [X(c["x0"]), Y(c["y0"]), X(c["x1"]), Y(c["y1"])]
        if c["tipo"] == "futuro":
            d.rectangle(box, outline="#FFC857", width=3)
            d.text((box[0] + 6, box[1] + 6), "ampliação", font=fp, fill="#FFC857")
            continue
        d.rectangle(box, fill=CORES.get(c["tipo"], "#EEE"), outline="#222", width=2)
        if c["tipo"] == "patio":
            d.text((box[0] + 6, box[1] + 6), "pátio", font=fp, fill="#355")
            continue
        cx, cy = (box[0] + box[2]) / 2, (box[1] + box[3]) / 2
        nome = c["nome"].upper()
        a = f"{area(c):.1f} m²"
        wn = d.textlength(nome, font=f)
        if wn > (box[2] - box[0]) - 6:
            nome = nome.split()[0]
            wn = d.textlength(nome, font=f)
        d.text((cx - wn / 2, cy - 14), nome, font=f, fill="#1B2430")
        d.text((cx - d.textlength(a, font=fp) / 2, cy + 4), a, font=fp, fill="#4A5463")
    # contorno externo
    d.rectangle([X(0), Y(0), X(W), Y(D)], outline="#111", width=5) if all(c["tipo"] not in EXTERNOS for c in planta["comodos"] if c["tipo"] != "futuro") else None
    por_id = {c["id"]: c for c in planta["comodos"]}
    # portas: vão e giro nas mesmas posições do motor 3D (o mesmo do e-book), com a dobradiça no canto
    try:
        import planta3d as P3
        portas3d = {str(q["id"]): q for q in P3.construir(planta)[2]}
    except Exception:  # sem o motor (ex.: import circular), fica o desenho simples de antes
        portas3d = {}
    # portas e ligações
    for porta in planta.get("portas", []):
        a, b = porta[0], porta[1]
        if a == "ext":
            c = por_id[b]
            lado = porta[2]
            pos = porta[3] if len(porta) > 3 else None
            _porta_ext(d, c, lado, pos, X, Y, escala)
            if c.get("veneziana_sobre_porta") == lado:  # veneziana em cima da porta: só o contorno azul (fica acima do corte)
                _porta_ext(d, c, lado, pos, X, Y, escala, veneziana=True)
            continue
        pc = parede_comum(por_id[a], por_id[b])
        if not pc:
            continue
        o, p, i0, i1 = pc
        aberta = len(porta) > 2 and porta[2] == "aberto"
        centro = (i0 + i1) / 2
        meia = ((i1 - i0) / 2 - 0.05) if aberta else 0.4
        q = portas3d.get(f"{a}-{b}")
        if q and not aberta:
            (hx, hy), (fx, fy), (ox, oy) = porta_dobradica(planta, q)
            r = q["r"]
            lo, hi = (min(hx, fx), max(hx, fx)) if o == "h" else (min(hy, fy), max(hy, fy))
            if o == "v":
                d.rectangle([X(p) - 4, Y(lo), X(p) + 4, Y(hi)], fill=CORES.get(por_id[a]["tipo"], "#EEE"))
            else:
                d.rectangle([X(lo), Y(p) - 4, X(hi), Y(p) + 4], fill=CORES.get(por_id[a]["tipo"], "#EEE"))
            # Y desta prévia não inverte o eixo: o ângulo na tela é o mesmo da planta (PIL gira no sentido horário)
            af = math.degrees(math.atan2(fy - hy, fx - hx)) % 360
            ao = math.degrees(math.atan2(oy - hy, ox - hx)) % 360
            ini = af if round((ao - af) % 360) == 90 else ao
            d.arc([X(hx - r), Y(hy - r), X(hx + r), Y(hy + r)], ini, ini + 90, fill="#C2683F", width=2)
            d.line([X(hx), Y(hy), X(ox), Y(oy)], fill="#C2683F", width=2)
            continue
        if o == "v":
            d.rectangle([X(p) - 4, Y(centro - meia), X(p) + 4, Y(centro + meia)], fill=CORES.get(por_id[a]["tipo"], "#EEE"))
            if not aberta:
                d.arc([X(p) - 0.8 * escala, Y(centro - meia), X(p) + 0.8 * escala, Y(centro - meia) + 1.6 * escala], 270, 360, fill="#C2683F", width=2)
        else:
            d.rectangle([X(centro - meia), Y(p) - 4, X(centro + meia), Y(p) + 4], fill=CORES.get(por_id[a]["tipo"], "#EEE"))
            if not aberta:
                d.arc([X(centro - meia), Y(p) - 0.8 * escala, X(centro - meia) + 1.6 * escala, Y(p) + 0.8 * escala], 0, 90, fill="#C2683F", width=2)
    # janelas
    for id, lista in planta.get("janelas", {}).items():
        c = por_id.get(id)
        if not c:
            continue
        for (lado, larg) in lista:
            if lado in ("frente", "fundos"):
                y = c["y0"] if lado == "frente" else c["y1"]
                cx = (c["x0"] + c["x1"]) / 2
                d.rectangle([X(cx - larg / 2), Y(y) - 4, X(cx + larg / 2), Y(y) + 4], fill="#7FD0FF", outline="#0B4FA8")
            else:
                x = c["x0"] if lado == "esq" else c["x1"]
                cy = (c["y0"] + c["y1"]) / 2
                d.rectangle([X(x) - 4, Y(cy - larg / 2), X(x) + 4, Y(cy + larg / 2)], fill="#7FD0FF", outline="#0B4FA8")
    # cotas
    d.line([(X(0), Y(0) - 22), (X(W), Y(0) - 22)], fill="white", width=2)
    t = f"{W:.2f} m".replace(".", ",")
    d.text(((X(0) + X(W)) / 2 - d.textlength(t, font=fp) / 2, Y(0) - 40), t, font=fp, fill="white")
    d.line([(X(0) - 22, Y(0)), (X(0) - 22, Y(D))], fill="white", width=2)
    t = f"{D:.2f} m".replace(".", ",")
    d.text((X(0) - 70, (Y(0) + Y(D)) / 2 - 6), t, font=fp, fill="white")
    # rodapé
    mt = {}
    fe = f"{n0(planta['_r'].metricas['area_fechada'])} m² fechados" if "_r" in planta else ""
    rod = f"{fe} · {planta['quartos_txt']} · lote ref. {_f(planta['_r'].metricas['lote'][0])} x {_f(planta['_r'].metricas['lote'][1])} m · frente para o {planta['_r'].metricas['orientacao']['melhor']}" if "_r" in planta else ""
    d.text((m, alt - 36), rod, font=fp, fill="white")
    im.save(caminho)


def n0(x):
    """Arredonda como na escola (90,5 vira 91). Use em todo número inteiro que vai ao público."""
    import decimal
    return str(decimal.Decimal(str(round(x, 6))).quantize(decimal.Decimal("1"), rounding=decimal.ROUND_HALF_UP))


def _f(v):
    return f"{v:.1f}".replace(".", ",")


def _porta_ext(d, c, lado, pos, X, Y, escala, veneziana=False):
    larg, e = 0.9, (9 if veneziana else 5)
    cor = dict(fill=None, outline="#0B4FA8", width=3) if veneziana else dict(fill="#FFC857", outline="#111")
    if lado in ("frente", "fundos"):
        y = c["y0"] if lado == "frente" else c["y1"]
        cx = pos if pos is not None else (c["x0"] + c["x1"]) / 2
        d.rectangle([X(cx - larg / 2), Y(y) - e, X(cx + larg / 2), Y(y) + e], **cor)
    else:
        x = c["x0"] if lado == "esq" else c["x1"]
        cy = pos if pos is not None else (c["y0"] + c["y1"]) / 2
        d.rectangle([X(x) - e, Y(cy - larg / 2), X(x) + e, Y(cy + larg / 2)], **cor)


ORI_NOME = {"norte": "norte", "sul": "sul", "leste": "leste", "oeste": "oeste"}
ORI_AO = {"norte": "ao norte", "sul": "ao sul", "leste": "a leste", "oeste": "a oeste"}


def pensou(planta):
    """Por que a planta é assim: três decisões, em português, a partir do que o validador mediu."""
    r = planta["_r"]
    m = r.metricas
    cs = planta["comodos"]
    tipos = [c["tipo"] for c in cs]
    out = []
    o = m["orientacao"]
    out.append(f"Sol: melhor com a rua {ORI_AO[o['melhor']]}; evite a rua {ORI_AO[o['pior']]}. "
               "Se o seu lote for diferente, a planta pode ser espelhada ou as janelas mudadas.")
    portas_ext = [pt[1] for pt in planta.get("portas", []) if pt[0] == "ext"]
    if any(t == "patio" for t in tipos):
        com = [c["nome"].lower() for c in cs for (l, _) in planta.get("janelas", {}).get(c["id"], [])
               if any(o["tipo"] == "patio" and parede_comum(c, o) and parede_comum(c, o)[0] == ("h" if l in ("frente", "fundos") else "v") for o in cs)]
        quem = " e ".join(dict.fromkeys(com)) if com else "a casa"
        out.append(f"Pátio de luz: {'o ' + quem if com else quem} abre janela para o pátio, com luz e ar sem dar para o vizinho.")
    elif any(c["id"] == "corr" for c in cs):
        out.append("Corredor coberto ao lado: todos os cômodos abrem para ele e ganham janela, mesmo num lote estreito. Da sala para o banheiro "
                   "e os quartos se passa por ele, então vale fechar a frente com portão. O código de obras da sua cidade diz se janela para "
                   "área coberta conta como ventilação.")
    elif any(c["tipo"] == "varanda" and c["id"] in portas_ext for c in cs):
        out.append("Varanda: a porta da sala fica coberta, protegida da chuva e do sol direto.")
    else:
        luz = m.get("luz", {})
        ok = lambda ts, lim: all(luz.get(c["id"], 0) + 1e-9 >= lim for c in cs if c["tipo"] in ts)
        grupo = [n for n, ts in (("sala", {"sala", "estar", "jantar"}), ("cozinha", {"cozinha"}), ("quartos", {"dorm", "casal"})) if any(c["tipo"] in ts for c in cs)]
        if sum(1 for c in cs if c["tipo"] in ("dorm", "casal")) == 1:
            grupo = ["quarto" if g == "quartos" else g for g in grupo]
        lista = grupo[0] if len(grupo) == 1 else ", ".join(grupo[:-1]) + " e " + grupo[-1]
        if ok(PERMANENCIA, 1 / 6) and ok({"cozinha"}, 1 / 8):
            out.append(f"Luz e ar: {lista} {'tem' if len(grupo) == 1 else 'têm'} janela para fora. Nos cômodos onde a família fica (sala e quartos), "
                       "a janela tem pelo menos um sexto do piso; na cozinha, pelo menos um oitavo (valores de referência; "
                       "o código de obras da sua cidade pode pedir outro).")
        else:
            out.append(f"Luz e ar: {lista} {'tem' if len(grupo) == 1 else 'têm'} janela para fora (o tamanho de cada uma o código de obras da sua cidade confere).")
    prumada = any("prumada própria" in a for a in r.avisos)
    if prumada:
        qual = "o banheiro da suíte" if any(c.get("privativo") for c in cs if c["tipo"] == "banho") else "o banheiro"
        out.append(f"Áreas molhadas: {qual} fica longe da cozinha e pede tubulação própria. Pergunte ao engenheiro quanto isso pesa no orçamento.")
    else:
        viz = []
        for b in (c for c in cs if c["tipo"] == "banho" and not c.get("privativo")):
            for o2 in cs:
                if o2["id"] != b["id"] and o2["tipo"] in MOLHADOS and parede_comum(b, o2) and o2["tipo"] not in viz:
                    viz.append(o2["tipo"])
        nome_viz = {"cozinha": "na cozinha", "servico": "na área de serviço", "banho": "no outro banheiro", "lavabo": "no lavabo"}
        onde = " e ".join(nome_viz[v] for v in viz[:2]) if viz else "em outra área molhada"
        out.append(f"Banheiro colado {onde}: os canos ficam juntos, num trecho só, com menos parede para abrir. O traçado final é do engenheiro.")
    if planta.get("servico_externo") or planta["id"] in ("C03",):
        fut = [c for c in cs if c["tipo"] == "futuro"]
        atras = [b["nome"].lower() for f in fut for b in cs if b["tipo"] != "futuro" and parede_comum(f, b)]
        onde = f", atrás de: {', '.join(atras)}" if atras else ""
        out.append(f"A casa cresce: o quarto 2 entra nos fundos{onde}, com porta para o quintal. Não quebra o que foi construído e não tapa nenhuma janela.")
    elif m["circulacao"]:
        out.append(f"Circulação: só {n0(m['circulacao'] * 100)}% da área é corredor. O resto é cômodo que você usa.")
    else:
        out.append("Corredor coberto: todos os cômodos abrem para ele, então não existe corredor interno comendo metro quadrado.")
    return out[:3] if len(out) > 3 else out


def cmd_fichas():
    L = ["# As 24 plantas: ficha de cada uma", "",
         "> Gerado por `python3 ferramentas/plantas.py fichas`. Parte da pasta E-book ([`../EBOOK.md`](../EBOOK.md)). "
         "Regras: [`../referencias/ARQUITETO.md`](../referencias/ARQUITETO.md). "
         "**Plantas de referência**: o projeto para a prefeitura é assinado por arquiteto ou engenheiro habilitado.", ""]
    for p in carregar():
        m = p["_r"].metricas
        L += [f"## {p['id']} · {p['nome']}", "",
              f"![{p['id']}](previas/{p['id']}.png)", "",
              f"**{n0(m['area_fechada'])} m² fechados** · {p['quartos_txt']} · {p['banheiros']} banheiro(s) · cabe num lote de "
              f"**{m['lote_comercial'][0]} x {m['lote_comercial'][1]} m** (no mínimo {_f(m['lote'][0])} x {_f(m['lote'][1])} m) · frente para o **{m['orientacao']['melhor']}**", ""]
        if p.get("destaque"):
            L += [f"*{p['destaque']}*", ""]
        L += ["**Por que esta planta é assim**", ""] + [f"- {t}" for t in pensou(p)]
        if p["_r"].avisos:
            L += ["", "**Atenção**", ""] + [f"- {a}" for a in p["_r"].avisos]
        if p["_r"].info:
            L += [""] + [f"- {a}" for a in p["_r"].info]
        L += [""]
    (PASTA / "PLANTAS.md").write_text("\n".join(L), encoding="utf-8")
    print("ebook/plantas/PLANTAS.md gerado")


# --------------------------------------------------------------------------------------
# Linha de comando
# --------------------------------------------------------------------------------------
def carregar():
    import projetos
    plantas = projetos.todas()
    for p in plantas:
        auto_janelas(p)
        p["_r"] = validar(p)
    return plantas


def cmd_validar(ids):
    plantas = [p for p in carregar() if not ids or p["id"] in ids]
    ruim = 0
    for p in plantas:
        r = p["_r"]
        marca = "OK " if not r.erros else "ERRO"
        print(f"[{marca}] {p['id']} {p['nome']:<26} {r.metricas['area_fechada']:>5} m² · lote ref {r.metricas['lote'][0]}x{r.metricas['lote'][1]} "
              f"· circ {r.metricas['circulacao'] * 100:.0f}% · frente p/ {r.metricas['orientacao']['melhor']}")
        for e in r.erros:
            print("      ✗", e)
        for a in r.avisos:
            print("      !", a)
        for _, _, a in r.referencias:
            print("      ! referência:", a)
        for a in r.ref_info:
            print("      ·", a)
        ruim += bool(r.erros)
    print(f"\n{len(plantas)} plantas, {ruim} com erro.")
    return 1 if ruim else 0


def cmd_previa(ids):
    """Rascunho rápido em ebook/plantas/rascunhos/. As prévias em alta saem de: python3 ferramentas/imagens2d.py --previas"""
    saida = PASTA / "rascunhos"
    saida.mkdir(parents=True, exist_ok=True)
    plantas = [p for p in carregar() if not ids or p["id"] in ids]
    for p in plantas:
        previa(p, saida / f"{p['id']}.png")
    print(f"{len(plantas)} prévias em {saida}")


def cmd_exportar():
    saida = PASTA / "dados"
    saida.mkdir(parents=True, exist_ok=True)
    plantas = carregar()
    for p in plantas:
        r = p["_r"]
        dado = {k: v for k, v in p.items() if k != "_r"}
        dado["pensou"] = pensou(p)
        dado["validacao"] = {"erros": r.erros, "avisos": r.avisos, "info": r.info, "metricas": r.metricas,
                             "referencias": [a for _, _, a in r.referencias] + r.ref_info}
        (saida / f"{p['id']}.json").write_text(json.dumps(dado, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(plantas)} arquivos em {saida}")


def cmd_resumo():
    for p in carregar():
        r = p["_r"]
        m = r.metricas
        q = p["quartos_txt"]
        print(f"| {p['id']} | {p['nome']} | {n0(m['area_fechada'])} m² | {q} | {p['banheiros']} | "
              f"{m['lote_comercial'][0]} x {m['lote_comercial'][1]} | {m['orientacao']['melhor']} |")


def cmd_referencias():
    """Casa x regra das 51 plantas de referência: o que está fora em cada casa (a lista de conserto)."""
    plantas = carregar()
    cab = "| Casa | m² | Frente do lote | " + " | ".join(f"{n} {t}" for n, t in REGRAS_REF) + " | Fora |"
    L = ["# Lista de conserto: as 24 casas contra as plantas de referência", "",
         "> Gerado por `python3 ferramentas/plantas.py referencias`; não edite. Régua: as 5 regras tiradas das 51 plantas de "
         "[`../referencias/plantas-ref/REFERENCIAS.md`](../referencias/plantas-ref/REFERENCIAS.md), aprovadas pelo dono em 23/11/2026 "
         "como aviso (não barram a planta e não vão ao PDF). Medidas livres, por dentro das paredes; `-` = dentro da regra.", "",
         "Regras: **1** circulação (com o corredor coberto lateral) até 6% em casa de até 60 m² (corredor lateral só em lote de 4 a 4,5 m) · "
         "**2** banheiro com os dois lados de 1,50 m ou mais · **3** quarto de 2,85 a 3,00 m de largura, nunca abaixo de 2,60 m se for de duas camas · "
         "**4** serviço com cerca de 1,20 m e saída para o quintal · **5a** banheiro e quartos alcançados por dentro de casa · **5b** cozinha com pelo menos 1,80 m. "
         "Frente do lote: o lote mínimo de referência; *estreita* = até 6 m.", "",
         cab, "|" + "---|" * (cab.count("|") - 1)]
    conta = {n: 0 for n, _ in REGRAS_REF}
    for p in plantas:
        r, m = p["_r"], p["_r"].metricas
        celula = {}
        for regra, curta, _ in r.referencias:
            celula.setdefault(regra, []).append(curta)
        for n in celula:
            conta[n] += 1
        fr = _m(m["lote"][0]).rstrip("0").rstrip(",") + " m" + (" *estreita*" if m["frente_estreita"] else "")
        L.append(f"| {p['id']} | {n0(m['area_fechada'])} | {fr} | " + " | ".join(", ".join(celula.get(n, ["-"])) for n, _ in REGRAS_REF) + f" | {len(celula)} |")
    L.append("| **Casas fora** | | " + str(sum(p["_r"].metricas["frente_estreita"] for p in plantas)) + " estreitas | "
             + " | ".join(f"**{conta[n]}**" for n, _ in REGRAS_REF) + " | |")
    L += ["", "O detalhe de cada casa (medida e frase): `python3 ferramentas/plantas.py validar ID`, linhas \"! referência\".", ""]
    (PASTA / "CONSERTOS.md").write_text("\n".join(L), encoding="utf-8")
    print("\n".join(L[6:-2]))
    print("\nebook/plantas/CONSERTOS.md gerado")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "validar"
    args = sys.argv[2:]
    if cmd == "validar":
        sys.exit(cmd_validar(args))
    elif cmd == "previa":
        cmd_previa(args)
    elif cmd == "exportar":
        cmd_exportar()
    elif cmd == "fichas":
        cmd_fichas()
    elif cmd == "resumo":
        cmd_resumo()
    elif cmd == "referencias":
        cmd_referencias()
    else:
        sys.exit(__doc__)
