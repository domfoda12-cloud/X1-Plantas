"""As 24 plantas do 1º e do 2º lançamento, desenhadas como um arquiteto organiza a casa.

Convenção: x cresce para a direita, y cresce da rua (frente, y=0) para os fundos.
A parede da esquerda é a divisa (sem janela) salvo quando a planta diz o contrário.
Tudo em metros. Rode `python3 ferramentas/plantas.py validar` depois de qualquer mudança.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "ferramentas"))
from plantas import F, H, V, casa, R  # noqa: E402

CENTRO = None


def _compacta(id, nome, W, D, sala, coz, varanda=0.0, h1=3.4, h3=3.4, **kw):
    """Casa compacta de 2 quartos: sala e cozinha na frente, circulação e banho no meio, quartos nos fundos."""
    serv = W - sala - coz
    linhas = []
    portas = []
    if varanda:
        linhas.append((varanda, F("varanda", "Varanda", "varanda")))
        portas += [("ext", "varanda", "frente"), ("varanda", "sala")]
    else:
        portas += [("ext", "sala", "frente")]
    linhas += [
        (h1, V((sala, F("sala", "Sala", "sala")), (coz, F("cozinha", "Cozinha", "cozinha")),
                (None, F("servico", "Serviço", "servico")))),
        (1.2, V((W - 2.1, F("circ", "Circulação", "circ")), (None, F("banho", "Banheiro", "banho")))),
        (None, V((W / 2, F("quarto1", "Quarto casal", "casal")), (None, F("quarto2", "Quarto", "dorm")))),
    ]
    portas += [("sala", "cozinha", "aberto"), ("cozinha", "servico"), ("sala", "circ", "aberto"),
               ("circ", "banho"), ("circ", "quarto1"), ("circ", "quarto2")]
    d = h1 + 1.2 + h3 + varanda
    return casa(id, nome, W, d, H(*linhas), portas, kw.pop("q", "2 quartos"), kw.pop("b", 1), **kw)


def _estreita(id, nome, Wq, linhas_h, portas, q, b, recuos=None, antes=(), fundos=None, corr=1.0, **kw):
    """Casa de corredor lateral: os cômodos em fila e um corredor coberto ao lado, como numa casa de vila."""
    W = Wq + corr
    corpo = V((Wq, H(*linhas_h)), (None, F("corr", "Corredor coberto", "varanda")))
    D = sum(t for t, _ in antes) + sum(t for t, _ in linhas_h)
    partes = list(antes) + [(sum(t for t, _ in linhas_h), corpo)]
    if fundos:
        partes.append(fundos)
        D += fundos[0]
    return casa(id, nome, W, D, H(*partes), portas, q, b, recuos=recuos or {}, **kw)


def _fila(Wq, sala, coz, serv_w, banho_w, h_wet, quartos):
    """Fila de cômodos de uma casa estreita: sala, cozinha, serviço+banho, quartos. Tudo encosta no corredor."""
    linhas = [(sala, F("sala", "Sala", "sala")), (coz, F("cozinha", "Cozinha", "cozinha")),
              (h_wet, V((serv_w, F("servico", "Serviço", "servico")), (None, F("banho", "Banheiro", "banho"))))]
    return linhas + quartos


PORTAS_FILA = [("ext", "corr", "frente"), ("corr", "sala"), ("sala", "cozinha", "aberto"), ("corr", "cozinha"),
               ("cozinha", "servico"), ("corr", "banho")]


def todas():
    P = []

    # ---------------------------------------------------------------- Casas compactas (C)
    P.append(_compacta("C01", "Casa Compacta", 6.5, 0, 3.3, 2.0, h1=3.4, h3=3.9,
                       destaque="A casa mais enxuta que ainda tem 2 quartos separados e serviço coberto"))
    P.append(casa("C02", "Casa Studio", 4.5, 7.2,
                  H((4.0, F("estar", "Sala e cama", "estar")),
                    (None, V((2.7, F("cozinha", "Cozinha", "cozinha")),
                             (None, H((1.6, F("banho", "Banheiro", "banho")), (None, F("servico", "Serviço", "servico"))))))),
                  [("ext", "estar", "frente"), ("estar", "cozinha", "aberto"), ("estar", "banho"), ("cozinha", "servico")],
                  "studio", 1))
    P.append(casa("C03", "Casa Inicial", 5.5, 7.5,
                  H((3.4, V((3.2, F("sala", "Sala", "sala")), (None, F("cozinha", "Cozinha", "cozinha")))),
                    (1.2, V((3.2, F("circ", "Circulação", "circ")), (None, F("banho", "Banheiro", "banho")))),
                    (None, V((3.2, F("quarto1", "Quarto casal", "casal")), (None, F("servico", "Serviço", "servico"))))),
                  [("ext", "sala", "frente"), ("sala", "cozinha", "aberto"), ("sala", "circ", "aberto"), ("circ", "banho"),
                   ("circ", "quarto1"), ("ext", "servico", "dir")],
                  "1 quarto (+1 depois)", 1, servico_externo=True,
                  extra=[R("futuro1", "Quarto 2 (ampliação)", "futuro", 3.2, 7.5, 5.5, 10.9)]))
    P.append(_compacta("C04", "Casa Duo", 6.0, 0, 3.0, 1.8, varanda=1.6, h1=3.4, h3=3.4,
                       destaque="Varanda na frente e dois quartos do mesmo tamanho"))
    P.append(_compacta("C05", "Casa Popular", 6.0, 0, 3.0, 1.8, h1=3.4, h3=3.2,
                       destaque="A casa de 2 quartos mais enxuta, sem desperdiçar um metro"))
    P.append(casa("C06", "Casa Compacta Suíte", 7.5, 7.6,
                  H((3.4, V((3.8, F("sala", "Sala", "sala")), (2.3, F("cozinha", "Cozinha", "cozinha")),
                            (None, F("servico", "Serviço", "servico")))),
                    (1.2, V((5.0, F("circ", "Circulação", "circ")), (None, F("banho", "Banheiro", "banho")))),
                    (None, V((2.8, F("quarto2", "Quarto", "dorm")), (3.0, F("quarto1", "Suíte", "casal")),
                             (None, F("bsuite", "Banho da suíte", "banho", privativo="quarto1"))))),
                  [("ext", "sala", "frente"), ("sala", "cozinha", "aberto"), ("cozinha", "servico"), ("sala", "circ", "aberto"),
                   ("circ", "banho"), ("circ", "quarto2"), ("circ", "quarto1"), ("quarto1", "bsuite")],
                  "2 quartos (1 suíte)", 2))
    P.append(_compacta("C07", "Casa Compacta Varanda", 6.5, 0, 3.3, 2.0, varanda=1.8, h1=3.4, h3=3.9,
                       destaque="Varanda larga para a rede e a cadeira de fim de tarde"))

    # ---------------------------------------------------------------- Estreitas (E)
    suite = lambda w1, w2, h: (h, V((w1, F("bsuite", "Banho da suíte", "banho", privativo="quarto1")), (None, F("quarto1", "Suíte", "casal"))))
    P.append(_estreita("E01", "Casa Estreita", 4.0,
                       _fila(4.0, 3.6, 2.8, 1.8, 0, 2.0, [suite(1.3, 2.7, 3.2), (3.0, F("quarto2", "Quarto", "dorm"))]),
                       PORTAS_FILA + [("corr", "quarto1"), ("quarto1", "bsuite"), ("corr", "quarto2")],
                       "2 quartos (1 suíte)", 2, recuos={"esq": 1.5},
                       antes=[(4.6, V((3.0, F("garagem", "Garagem", "garagem")), (None, F("jardim", "Jardim", "externo"))))],
                       destaque="Garagem na frente e todos os cômodos abrindo para o corredor"))
    P.append(_estreita("E02", "Casa Corredor", 2.6,
                       [(3.9, F("sala", "Sala", "sala")), (2.8, F("cozinha", "Cozinha", "cozinha")),
                        (2.0, V((1.3, F("servico", "Serviço", "servico")), (None, F("banho", "Banheiro", "banho")))),
                        (3.3, F("quarto1", "Quarto casal", "casal")), (3.3, F("quarto2", "Quarto", "dorm"))],
                       PORTAS_FILA + [("corr", "quarto1"), ("corr", "quarto2")],
                       "2 quartos", 1, recuos={"esq": 1.5}))
    P.append(_estreita("E03", "Casa Fita", 2.6,
                       [(3.9, F("sala", "Sala", "sala")), (2.8, F("cozinha", "Cozinha", "cozinha")),
                        (1.3, F("servico", "Serviço", "servico")), (1.8, F("banho", "Banheiro", "banho")),
                        (3.4, F("quarto1", "Quarto casal", "casal"))],
                       [("ext", "corr", "frente"), ("corr", "sala"), ("sala", "cozinha", "aberto"), ("corr", "cozinha"),
                        ("cozinha", "servico"), ("corr", "servico"), ("corr", "banho"), ("corr", "quarto1")],
                       "1 quarto", 1, recuos={"esq": 0.0}, corr=0.9,
                       destaque="Cabe em lote de 5 m de frente: todas as janelas dão para o corredor"))
    P.append(casa("E04", "Casa Pátio", 7.5, 8.0,
                  H((3.4, V((4.0, F("sala", "Sala", "sala")), (2.3, F("cozinha", "Cozinha", "cozinha")), (None, F("servico", "Serviço", "servico")))),
                    (1.2, V((5.5, F("circ", "Circulação", "circ")), (None, F("banho", "Banheiro", "banho")))),
                    (None, V((3.0, F("quarto1", "Quarto casal", "casal", pref=("dir", "fundos"))), (1.5, F("patio", "Pátio de luz", "patio")),
                             (None, F("quarto2", "Quarto", "dorm", pref=("esq", "fundos")))))),
                  [("ext", "sala", "frente"), ("sala", "cozinha", "aberto"), ("cozinha", "servico"), ("sala", "circ", "aberto"),
                   ("circ", "banho"), ("circ", "quarto1"), ("circ", "quarto2")],
                  "2 quartos", 1, destaque="Pátio de luz entre os quartos: os dois abrem janela para ele"))
    P.append(_estreita("E05", "Casa Estreita Suíte", 3.9,
                       _fila(3.9, 3.8, 2.8, 1.8, 0, 2.0, [suite(1.3, 2.6, 3.4), (3.0, F("quarto2", "Quarto", "dorm"))]),
                       PORTAS_FILA + [("corr", "quarto1"), ("quarto1", "bsuite"), ("corr", "quarto2")],
                       "2 quartos (1 suíte)", 2, recuos={"esq": 1.5}))
    P.append(_estreita("E06", "Casa Estreita Gourmet", 4.6,
                       _fila(4.6, 3.8, 2.8, 2.0, 0, 2.0, [suite(1.4, 3.2, 3.2), (3.0, F("quarto2", "Quarto", "dorm"))]),
                       PORTAS_FILA + [("corr", "quarto1"), ("quarto1", "bsuite"), ("corr", "quarto2"), ("corr", "gourmet", "aberto"),
                                      ("quarto2", "gourmet", "aberto")],
                       "2 quartos (1 suíte)", 2, recuos={"esq": 1.5},
                       fundos=(3.2, F("gourmet", "Área gourmet", "varanda")),
                       destaque="Área gourmet nos fundos, aberta para o corredor"))
    P.append(_estreita("E07", "Casa Estreita 3 Quartos", 4.0,
                       _fila(4.0, 3.8, 2.8, 1.8, 0, 2.0,
                             [(3.0, F("quarto2", "Quarto", "dorm")), (3.0, F("quarto3", "Quarto", "dorm")),
                              (3.3, V((1.3, F("bsuite", "Banho da suíte", "banho", privativo="quarto1")), (None, F("quarto1", "Suíte", "casal"))))]),
                       PORTAS_FILA + [("corr", "quarto1"), ("quarto1", "bsuite"), ("corr", "quarto2"), ("corr", "quarto3")],
                       "3 quartos (1 suíte)", 2, recuos={"esq": 1.5},
                       destaque="3 quartos, um deles suíte, num lote de 8 m de frente"))

    # ---------------------------------------------------------------- Família (F)
    P.append(_familia("F01", "Casa Família Compacta", 8.4, sala=4.2, coz=2.4, col=1.8, h1=3.6, h3=3.4, suite=False))
    P.append(casa("F02", "Casa Integrada", 10.0, 8.6,
                  H((3.8, V((4.0, F("sala", "Sala", "sala")), (2.4, F("jantar", "Jantar", "jantar")),
                            (2.4, F("cozinha", "Cozinha", "cozinha")), (None, F("servico", "Serviço", "servico")))),
                    (1.2, V((6.8, F("circ", "Circulação", "circ")), (None, F("banho", "Banheiro", "banho")))),
                    (None, V((2.8, F("quarto3", "Quarto", "dorm")), (2.8, F("quarto2", "Quarto", "dorm")),
                             (3.1, F("quarto1", "Suíte", "casal")), (None, F("bsuite", "Banho da suíte", "banho", privativo="quarto1"))))),
                  [("ext", "sala", "frente"), ("sala", "jantar", "aberto"), ("jantar", "cozinha", "aberto"), ("cozinha", "servico"),
                   ("sala", "circ", "aberto"), ("circ", "banho"), ("circ", "quarto3"), ("circ", "quarto2"), ("circ", "quarto1"), ("quarto1", "bsuite")],
                  "3 quartos (1 suíte)", 2))
    P.append(_familia("F03", "Casa Família", 9.4, sala=4.4, coz=2.8, col=2.2, h1=3.8, h3=3.4, suite=True, varanda=1.8))
    P.append(_familia("F04", "Casa Família Suíte", 9.4, sala=4.4, coz=2.8, col=2.2, h1=3.8, h3=3.6, suite=True, garagem=5.0))
    P.append(casa("F05", "Casa em L", 11.4, 8.6,
                  H((3.8, V((4.6, F("sala", "Sala", "sala")), (2.6, F("jantar", "Jantar", "jantar")),
                            (2.8, F("cozinha", "Cozinha", "cozinha")), (None, F("servico", "Serviço", "servico")))),
                    (1.2, V((7.4, F("circ", "Circulação", "circ")), (None, F("banho", "Banheiro", "banho")))),
                    (None, V((2.6, F("quarto2", "Quarto", "dorm")), (2.6, F("quarto3", "Quarto", "dorm")),
                             (2.8, F("quarto1", "Suíte", "casal")), (1.3, F("bsuite", "Banho da suíte", "banho", privativo="quarto1")),
                             (None, F("jardim", "Jardim", "externo"))))),
                  [("ext", "sala", "frente"), ("sala", "jantar", "aberto"), ("jantar", "cozinha", "aberto"), ("cozinha", "servico"),
                   ("sala", "circ", "aberto"), ("circ", "banho"), ("circ", "quarto2"), ("circ", "quarto3"), ("circ", "quarto1"), ("quarto1", "bsuite")],
                  "3 quartos (1 suíte)", 2))

    # ---------------------------------------------------------------- Especiais (S)
    P.append(casa("S03", "Casa Acessível", 8.8, 8.9,
                  H((3.6, V((4.0, F("sala", "Sala", "sala")), (3.2, F("cozinha", "Cozinha", "cozinha")), (None, F("servico", "Serviço", "servico")))),
                    (1.9, V((5.6, F("circ", "Circulação", "circ")), (None, F("banho", "Banheiro", "banho")))),
                    (None, V((4.4, F("quarto1", "Quarto casal", "casal")), (None, F("quarto2", "Quarto", "dorm"))))),
                  [("ext", "sala", "frente"), ("sala", "cozinha", "aberto"), ("cozinha", "servico"), ("sala", "circ", "aberto"),
                   ("circ", "banho"), ("circ", "quarto1"), ("circ", "quarto2")],
                  "2 quartos", 1, acessivel=True,
                  destaque="Circulação larga e banheiro com espaço livre para o giro de 1,50 m da cadeira de rodas"))
    P.append(casa("S04", "Casa Home Office", 7.8, 10.8,
                  H((3.2, V((2.0, F("escritorio", "Escritório", "escritorio")), (None, F("varanda", "Varanda", "varanda")))),
                    (3.2, V((4.8, F("sala", "Sala", "sala")), (1.8, F("cozinha", "Cozinha", "cozinha")), (None, F("servico", "Serviço", "servico")))),
                    (1.2, V((5.2, F("circ", "Circulação", "circ")), (None, F("banho", "Banheiro", "banho")))),
                    (None, V((3.9, F("quarto1", "Quarto casal", "casal")), (None, F("quarto2", "Quarto", "dorm"))))),
                  [("ext", "escritorio", "frente"), ("ext", "varanda", "frente"), ("varanda", "sala"), ("escritorio", "sala"),
                   ("sala", "cozinha", "aberto"), ("cozinha", "servico"), ("sala", "circ", "aberto"), ("circ", "banho"),
                   ("circ", "quarto1"), ("circ", "quarto2")],
                  "2 quartos + escritório", 1,
                  destaque="Escritório com porta para a rua: cliente entra sem passar pela casa"))
    P.append(casa("S05", "Casa de Praia", 7.4, 10.4,
                  H((2.4, F("varanda", "Varandão", "varanda")),
                    (3.6, V((3.8, F("sala", "Sala", "sala")), (2.4, F("cozinha", "Cozinha", "cozinha")), (None, F("servico", "Serviço", "servico")))),
                    (1.2, V((5.0, F("circ", "Circulação", "circ")), (None, F("banho", "Banheiro", "banho")))),
                    (None, V((3.0, F("quarto2", "Quarto", "dorm")), (3.0, F("quarto1", "Suíte", "casal")),
                             (None, F("bsuite", "Banho da suíte", "banho", privativo="quarto1"))))),
                  [("ext", "varanda", "frente"), ("varanda", "sala", "aberto"), ("sala", "cozinha", "aberto"), ("cozinha", "servico"),
                   ("sala", "circ", "aberto"), ("circ", "banho"), ("circ", "quarto2"), ("circ", "quarto1"), ("quarto1", "bsuite")],
                  "2 quartos (1 suíte)", 2,
                  destaque="Varandão na frente e suíte para o casal"))
    P.append(casa("S07", "Casa Gourmet", 9.4, 8.6,
                  H((3.8, V((3.6, F("sala", "Sala", "sala")), (2.8, F("cozinha", "Cozinha", "cozinha")),
                            (None, H((2.4, F("gourmet", "Área gourmet", "varanda")), (None, F("servico", "Serviço", "servico")))))),
                    (1.2, V((6.4, F("circ", "Circulação", "circ")), (None, F("banho", "Banheiro", "banho")))),
                    (None, V((2.6, F("quarto2", "Quarto", "dorm")), (2.6, F("quarto3", "Quarto", "dorm")), (2.9, F("quarto1", "Suíte", "casal")),
                             (None, F("bsuite", "Banho da suíte", "banho", privativo="quarto1"))))),
                  [("ext", "sala", "frente"), ("sala", "cozinha", "aberto"), ("cozinha", "gourmet", "aberto"), ("cozinha", "servico"),
                   ("sala", "circ", "aberto"), ("circ", "banho"), ("circ", "quarto2"), ("circ", "quarto1"), ("circ", "quarto3"), ("quarto1", "bsuite")],
                  "3 quartos (1 suíte)", 2,
                  destaque="Cozinha aberta para a área gourmet, a casa que recebe"))
    p = _familia("S09", "Casa de Esquina", 9.4, sala=4.4, coz=2.8, col=2.2, h1=3.8, h3=3.4, suite=True, varanda=1.8)
    p["recuos"] = {"esq": 3.0}
    for c in p["comodos"]:
        if abs(c["x0"]) < 1e-6 and c["tipo"] in ("dorm", "casal"):
            c["pref"] = ("esq", "fundos")  # na esquina, o quarto abre janela para a rua do lado
    P.append(p)
    return P


def _familia(id, nome, W, sala, coz, col, h1, h3, suite, varanda=0.0, garagem=0.0):
    """Casa de 3 quartos: social na frente, circulação de 1,10 m no meio, quartos nos fundos."""
    topo = V((sala, F("sala", "Sala", "sala")), (coz, F("cozinha", "Cozinha", "cozinha")),
             (None, H((2.0, F("servico", "Serviço", "servico")), (None, F("banho", "Banheiro", "banho")))))
    if suite:
        fundos = V((2.6, F("quarto2", "Quarto", "dorm")), (2.6, F("quarto3", "Quarto", "dorm")),
                   (W - 2.6 - 2.6 - 1.3, F("quarto1", "Suíte", "casal")),
                   (None, F("bsuite", "Banho da suíte", "banho", privativo="quarto1")))
    else:
        w = W / 3
        fundos = V((w, F("quarto1", "Quarto casal", "casal")), (w, F("quarto2", "Quarto", "dorm")), (None, F("quarto3", "Quarto", "dorm")))
    linhas = []
    portas = []
    if garagem:
        linhas.append((garagem, V((3.0, F("garagem", "Garagem", "garagem")), (None, F("jardim", "Jardim", "externo")))))
        portas.append(("ext", "sala", "frente", sala - 0.7))
    elif varanda:
        linhas.append((varanda, F("varanda", "Varanda", "varanda")))
        portas += [("ext", "varanda", "frente"), ("varanda", "sala")]
    else:
        portas.append(("ext", "sala", "frente"))
    linhas += [(h1, topo), (1.1, F("circ", "Circulação", "circ")), (None, fundos)]
    portas += [("sala", "cozinha", "aberto"), ("cozinha", "servico"), ("sala", "circ", "aberto"), ("circ", "banho"),
               ("circ", "quarto1"), ("circ", "quarto2"), ("circ", "quarto3")]
    if suite:
        portas.append(("quarto1", "bsuite"))
    D = sum(t for t, _ in linhas[:-1]) + h3
    q = "3 quartos (1 suíte)" if suite else "3 quartos"
    return casa(id, nome, W, D, H(*linhas), portas, q, 2 if suite else 1)
