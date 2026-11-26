"""Rascunho C01V: a parede cheia da lateral esquerda da varanda da C01, na divisa, até a cobertura (Nilo, 26/11/2026).

Por quê: o Código Civil (art. 1.301) proíbe varanda a menos de 1,5 m do terreno vizinho; a varanda da C01 encosta na
divisa da esquerda (recuo 0), então essa lateral é parede cheia, sem vista para o vizinho. O validador já avisa isso,
mas o motor (planta3d.construir) só levanta parede de cômodo fechado e a lateral aparecia aberta (só o beiral tracejado).
Pendência do quadro de 26/11 ("desenhar a parede da varanda da C01, planta e 3D, e avisar a Vera").

O que muda na planta: UMA coisa. A varanda ganha `parede_cheia=("esq",)`: parede externa de 15 cm em x = 0, de y = 0
(face da frente) a y = 1,20 (onde ela já encontra a parede da sala), emendada na parede da divisa que já existe.
Nada mais muda: medidas, cômodos, portas, janelas, móveis, área fechada e lote são os da oficial.

Por que vem um protótipo do motor aqui dentro: o motor oficial não lê `parede_cheia`. Para a parede aparecer na prévia,
no desenho do e-book e no 3D DESTE rascunho (e para o conferir-rascunho.py rodar as conferências do 3D com ela), o
rascunho troca, só neste processo, duas peças do planta3d: `mobiliar` (que recebe a lista de paredes; a parede nova entra
nela antes dos móveis, então o arranjo e as conferências já a enxergam) e `_classe` (que diz se a parede é externa: o
lado da varanda com parede cheia conta como fechado). O protótipo só age em cômodo com `parede_cheia`: as outras 23 casas
não mudam. Aplicar na oficial é outro passo: levar estas duas mudanças para ferramentas/planta3d.py, a chave para o
F("varanda", ...) da C01 em projetos.py e o protótipo do aviso (abaixo) para o validar de plantas.py.

A frase do aviso (art. 1.301) já sai certa DESTE rascunho: o protótipo do aviso troca "precisa ser fechada com parede
cheia ... (no desenho ela aparece tracejada)" por "é parede cheia até a cobertura, como está no desenho" só quando prova,
nas paredes de verdade do construir (as da planta 2D e do 3D), que há parede externa de 15 cm cobrindo a lateral inteira;
declarada e não desenhada vira erro. As outras casas com varanda na divisa seguem com "tracejada" (verdade para elas).
Ao aplicar, o comentário de plantas.py (linha 563) passa a dizer o mesmo que esta frase (pedido da Vera, 26/11/2026).

Uso: python3 ferramentas/conferir-rascunho.py ebook/plantas/rascunhos/C01V.py
"""
import copy
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(RAIZ / "ferramentas"), str(RAIZ / "ebook" / "plantas")]
import planta3d as P3  # noqa: E402
import plantas as PL  # noqa: E402

LADOS = ("esq", "dir", "frente", "fundos")


# ---------------------------------------------------------------- protótipo do motor (vai para planta3d.py ao aplicar)
def _paredes_cheias(planta):
    """[(o, fixo, a, b, cômodo, lado)] das laterais com parede cheia de cômodos abertos (varanda na divisa)."""
    out = []
    for c in planta["comodos"]:
        for lado in c.get("parede_cheia", ()):
            assert lado in LADOS, f"{c['id']}: parede_cheia com lado {lado!r}"
            _, o, fixo, a, b = next(x for x in P3.arestas(c) if x[0] == lado)
            out.append((o, P3.R(fixo), a, b, c, lado))
    return out


if not getattr(P3, "_c01v", False):  # o conferir e o antes-depois podem rodar o rascunho mais de uma vez
    P3._c01v = True
    _mobiliar, _classe = P3.mobiliar, P3._classe

    def mobiliar(planta, vaos_por_comodo, jan_por_comodo, paredes=(), portas=()):
        """Antes dos móveis, a parede cheia entra na lista de paredes do construir (a mesma lista que ele devolve)."""
        if isinstance(paredes, list):
            for (o, fixo, a, b, _, _) in _paredes_cheias(planta):
                ivs = [(min(p[0], p[2]), max(p[0], p[2])) if o == "h" else (min(p[1], p[3]), max(p[1], p[3]))
                       for p in paredes if (p[1] == p[3]) == (o == "h") and abs((p[1] if o == "h" else p[0]) - fixo) < 1e-6]
                resto = [p for p in paredes if not ((p[1] == p[3]) == (o == "h") and abs((p[1] if o == "h" else p[0]) - fixo) < 1e-6)]
                juntos = P3.unir(ivs + [(a, b)])
                paredes[:] = resto + [[P3.R(i), fixo, P3.R(j), fixo] if o == "h" else [fixo, P3.R(i), fixo, P3.R(j)]
                                      for (i, j) in juntos]
        return _mobiliar(planta, vaos_por_comodo, jan_por_comodo, paredes, portas)

    def classe(planta, o, fixo, s):
        """Parede cheia de varanda conta como externa, com a varanda do lado de dentro (15 cm para dentro dela)."""
        k = _classe(planta, o, fixo, s)
        if k is None:
            for (o2, f2, a, b, c, lado) in _paredes_cheias(planta):
                if o2 == o and abs(f2 - fixo) < 1e-6 and a - 1e-6 <= s <= b + 1e-6:
                    return 1 if lado in ("esq", "frente") else -1
        return k

    P3.mobiliar, P3._classe = mobiliar, classe


# ---------------------------------------------------------------- protótipo do aviso (vai para plantas.py ao aplicar)
# A frase do art. 1.301 que vai ao comprador tem de dizer o que o desenho mostra. Ela só troca de "tracejada" para
# "como está no desenho" quando o programa PROVA que a parede existe: uma parede externa (classe ±1, 15 cm) que cobre a
# lateral inteira da varanda (de a até b) na linha da divisa, nas paredes de verdade do construir (as mesmas da planta 2D
# e do 3D). Se a parede_cheia estiver declarada e não sair desenhada, vira ERRO, não aviso bonito. As outras casas com
# varanda na divisa (C02, C03 e as demais sem parede_cheia) seguem com "tracejada", que continua verdadeiro para elas.
TRACEJADA = ("precisa ser fechada com parede cheia até a cobertura, sem vista para o vizinho "
             "(no desenho ela aparece tracejada)")
DESENHADA = "é parede cheia até a cobertura, como está no desenho, sem vista para o vizinho"


def parede_desenhada(planta, c, lado):
    """True se a lateral `lado` da varanda `c` sai como parede externa inteira nas paredes de verdade (2D e 3D)."""
    alvo = [x for x in _paredes_cheias(planta) if x[4]["id"] == c["id"] and x[5] == lado]
    if not alvo:
        return False
    o, fixo, a, b, _, _ = alvo[0]
    reais = P3.paredes_reais(planta, P3.construir(planta)[0])
    return any(q[0] == o and abs(q[6] - fixo) < 1e-6 and q[4] >= 0.15 - 1e-6 and q[5] in (1, -1)
               and q[2] <= a + 1e-6 and q[3] >= b - 1e-6 for q in reais)


if not getattr(PL, "_c01v", False):
    PL._c01v = True
    _validar = PL.validar

    def validar(planta):
        r = _validar(planta)
        for c in planta["comodos"]:
            for lado in c.get("parede_cheia", ()):
                frase = f"{c['nome']} encosta na divisa da {PL.NOMES_LADO[lado]}: essa lateral "
                i = next((k for k, a in enumerate(r.avisos) if a.startswith(frase) and TRACEJADA in a), None)
                if i is None:
                    continue  # sem aviso do art. 1.301 para esse lado: nada a trocar
                if parede_desenhada(planta, c, lado):
                    r.avisos[i] = r.avisos[i].replace(TRACEJADA, DESENHADA)
                else:
                    r.erro(f"{c['nome']}: parede_cheia na {PL.NOMES_LADO[lado]} declarada, mas não sai desenhada")
        return r

    PL.validar = validar


# ---------------------------------------------------------------- a planta: a oficial + a parede cheia
p = copy.deepcopy(next(x for x in PL.carregar() if x["id"] == "C01"))
p.pop("_r", None)
varanda = next(c for c in p["comodos"] if c["id"] == "varanda")
varanda["parede_cheia"] = ("esq",)  # ao aplicar: F("varanda", "Varanda", "varanda", parede_cheia=("esq",)) em projetos.py

if __name__ == "__main__":
    r = PL.validar(p)
    paredes = P3.construir(p)[0]
    reais = P3.paredes_reais(p, paredes)
    print("erros:", r.erros)
    print("avisos:", *r.avisos, sep="\n  ")
    print("parede da divisa (x = 0):", [q for q in reais if q[0] == "v" and abs(q[6]) < 1e-6])
