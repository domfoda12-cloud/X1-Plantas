"""Confere um rascunho de planta antes de alguém dizer "pronto para aplicar" (lição do A6, 24/11/2026).

O conserto da janela da C01 (rascunho C01J, variante c) passou no validador e mesmo assim a porta batia na bancada.
Este programa roda no rascunho TODAS as conferências que a planta oficial passa: as do validador
(`plantas.py validar`) e as do 3D que o `checar.py` usa (`planta3d.py`). Só lê: não grava prévia, dado,
módulo 3D nem imagem, e não toca em `ebook/plantas/projetos.py`.

Uso:
    python3 ferramentas/conferir-rascunho.py ebook/plantas/rascunhos/C01J.py c    rascunho (variante opcional)
    python3 ferramentas/conferir-rascunho.py C01                                  planta oficial, para comparar

O rascunho é um .py que monta a planta num dicionário (com "comodos" e "portas"); o programa roda o arquivo com a
variante em sys.argv[1], com a prévia desligada, e pega a planta pelo nome `p` ou `planta` (ou a única que achar).
Sai com 1 se houver erro do validador ou qualquer item nas listas; aviso do validador só é mostrado (aceito com motivo escrito).
"""
import contextlib
import copy
import io
import runpy
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "ferramentas"))
sys.path.insert(0, str(RAIZ / "ebook" / "plantas"))
import planta3d as P3  # noqa: E402
import plantas as PL  # noqa: E402


def carregar_rascunho(arquivo, variante=None):
    """Roda o rascunho com a prévia desligada e devolve a planta que ele montou."""
    previa, argv = PL.previa, sys.argv
    PL.previa = lambda *a, **k: None
    sys.argv = [str(arquivo)] + ([variante] if variante else [])
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            ns = runpy.run_path(str(arquivo), run_name="__rascunho__")
    finally:
        PL.previa, sys.argv = previa, argv
    eh = lambda v: isinstance(v, dict) and "comodos" in v and "portas" in v
    for nome in ("p", "planta"):
        if eh(ns.get(nome)):
            return ns[nome]
    achadas = [v for k, v in ns.items() if not k.startswith("_") and eh(v)]
    if len(achadas) != 1:
        sys.exit(f"não achei uma planta só em {arquivo} (achei {len(achadas)}): chame-a de `p`")
    return achadas[0]


def conferencias(p):
    """(nome, itens) de cada conferência; lista vazia = passou."""
    if "janelas" not in p:
        PL.auto_janelas(p)
    r = PL.validar(p)
    mv = P3.construir(p)[3]
    tipo = {c["id"]: c["tipo"] for c in p["comodos"]}
    nome = {c["id"]: c["nome"] for c in p["comodos"]}
    quartos = [f"{nome[q]} aberto para {nome[o]}" for pt in p.get("portas", [])
               if len(pt) > 2 and pt[2] == "aberto" and "ext" not in pt[:2]
               for q, o in ((pt[0], pt[1]), (pt[1], pt[0]))
               if tipo[q] in ("dorm", "casal") and (tipo[o] in PL.EXTERNOS | PL.SEMIEXTERNOS or "gourmet" in nome[o].lower())]
    zona = [f"{m['amb']}: {o['tipo']} na zona da cadeira" for m in mv if m["tipo"] == "escrivaninha" for o in mv
            if o["amb"] == m["amb"] and o["tipo"] not in P3.NAO_COLIDE + ("escrivaninha", "cadeira")
            and P3.sobrepoe(P3.pegada(o), P3.zona_da_cadeira(m), -0.005)]
    return r, [
        ("validador: erros", list(r.erros)),
        ("porta que bate em móvel fixo (tanque, pia, vaso, bancada, box, máquina)",
         [f"{amb}: a porta {porta} bate no {t} ({cm} cm)" for amb, porta, t, cm in P3.portas_em_fixos(p)]),
        ("móvel atravessando parede", [f"{amb}: {t} entra {cm} cm na parede {q}" for amb, t, q, cm in P3.moveis_na_parede(p)]),
        ("móvel sobre móvel", [f"{amb}: {a} sobre {b}" for amb, a, b in P3.sobrepostos(mv)]),
        ("móvel alto na frente de janela", [f"{amb}: {t} na frente da janela ({cm} cm)" for amb, t, cm in P3.altos_na_janela(p)]),
        ("janela em cima de porta", [f"{jan} sobre a porta {porta}" for porta, jan in P3.janelas_sobre_portas(p)]),
        ("cadeira de escrivaninha em cima de cama ou móvel", [f"{amb}: cadeira em cima de {t}" for amb, t in P3.cadeiras_sem_lugar(p)]),
        ("cadeira de escrivaninha sem 0,60 x 0,75 m para puxar", zona),
        (f"cadeira de jantar a menos de {round(100 * P3.CADEIRA_PAREDE)} cm da parede",
         [f"{amb}: {cm} cm até a parede" for amb, cm in P3.cadeiras_apertadas(p)]),
        (f"guarda-roupa sem {round(100 * P3.FRENTE_ARMARIO)} cm livres na frente",
         [f"{amb}: {cm} cm livres" for amb, cm in P3.armarios_sem_frente(p)]),
        ("quarto aberto para área externa ou gourmet", quartos),
    ]


def main(args):
    if not args:
        sys.exit(__doc__)
    alvo = args[0]
    if alvo.endswith(".py"):
        p, rotulo = carregar_rascunho(Path(alvo), args[1] if len(args) > 1 else None), f"rascunho {alvo}" + (f" variante {args[1]}" if len(args) > 1 else "")
    else:
        import projetos
        achou = [x for x in projetos.todas() if x["id"] == alvo]
        if not achou:
            sys.exit(f"planta {alvo} não existe em projetos.py")
        p, rotulo = copy.deepcopy(achou[0]), f"planta oficial {alvo} (só leitura)"
        PL.auto_janelas(p)  # como PL.carregar(); no rascunho, quem põe as janelas é o próprio arquivo
    r, lista = conferencias(p)
    m = r.metricas
    print(f"Conferência de {rotulo}: {p['id']} · {m['area_fechada']} m² fechados · lote ref {m['lote'][0]} x {m['lote'][1]}")
    ruins = 0
    for nome, itens in lista:
        print(f"[{'ERRO' if itens else 'OK '}] {nome}" + (f" ({len(itens)})" if itens else ""))
        for i in itens:
            print("      ✗", i)
        ruins += bool(itens)
    for a in r.avisos:
        print("      ! aviso do validador (aceito só com motivo escrito):", a)
    print(f"\n{'NÃO está pronto para aplicar' if ruins else 'Passou nas conferências'}: {ruins} de {len(lista)} com erro."
          + ("" if ruins else " Falta o olho: prévia, caminho do dia e as regras da apostila 2, que nenhum programa confere."))
    return 1 if ruins else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
