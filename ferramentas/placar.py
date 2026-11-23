"""Placar do veto: quanto cada agente acerta quando veta (fila da noite, tarefa A3; condições do Fable).

  python3 ferramentas/placar.py             gera contexto/PLACAR.md
  python3 ferramentas/placar.py --conferir  falha se o PLACAR.md estiver velho (roda no checar.py)

Só lê o que já existe, sem inventar nota:
- tabelas de veto das fichas de 23/11/2026 em diante, no formato fixo
  | Rodada | Agente | Nota | Ponto que caiu | Por quê |   (pedidos/LEIA-ME.md, "Plano vetado antes de fazer");
- provas com erro plantado (pedidos/PROVAS.md, tabelas "| Agente | Achados (de N) | Parciais | Alarmes falsos (de M) | ...");
- lições gravadas (pedidos/LICOES.md, pelo pedido.py licao e pelo fechar).
Toda média sai com o n ao lado; nenhuma regra muda com n menor que 5.
"""
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "contexto" / "PLACAR.md"
DESDE = "2026-11-23"
CAB_VETO = "| Rodada | Agente | Nota | Ponto que caiu | Por quê |"
N_MINIMO = 5


def nome(agente):
    """'Revisor de risco', '`revisor-de-risco`' e 'revisor-de-risco (Fable)' viram o mesmo nome."""
    a = re.sub(r"\(.*?\)|`|\*", "", agente).strip().lower()
    a = unicodedata.normalize("NFKD", re.sub(r"\s+", "-", a)).encode("ascii", "ignore").decode()
    agentes = RAIZ / ".claude" / "agents"
    sem_de = re.sub(r"-d[aeo]s?-", "-", a)  # 'editor-de-video' -> 'editor-video', se só esse existir
    return sem_de if not (agentes / f"{a}.md").exists() and (agentes / f"{sem_de}.md").exists() else a


def numero(txt):
    m = re.search(r"\d+(?:[.,]\d+)?", txt or "")
    return float(m.group().replace(",", ".")) if m else None


def linhas_de_tabela(texto, cabecalho_re):
    """Linhas de dados de toda tabela cujo cabeçalho casa com o regex (pula a linha |---|)."""
    linhas, dentro = [], False
    for l in texto.splitlines():
        if re.match(cabecalho_re, l.strip()):
            dentro = True
            continue
        if dentro and l.strip().startswith("|"):
            if not re.match(r"^\|[\s:|-]+\|$", l.strip()):
                linhas.append([c.strip() for c in l.strip().strip("|").split("|")])
        else:
            dentro = False
    return linhas


def vetos():
    notas, pontos = defaultdict(list), defaultdict(lambda: defaultdict(int))
    for f in sorted((RAIZ / "pedidos").glob("20*/*.md")):
        if f.name[:10] < DESDE:
            continue
        for c in linhas_de_tabela(f.read_text(encoding="utf-8"), re.escape(CAB_VETO)):
            if len(c) < 4 or numero(c[2]) is None:
                continue
            a = nome(c[1])
            notas[a].append(numero(c[2]))
            if c[3] and c[3] not in ("-", "—", "nenhum"):
                pontos[a][c[3].lower()] += 1
    return notas, pontos


def provas():
    """Por agente: achados, plantados, alarmes falsos, limpos e quantas provas fez."""
    arq = RAIZ / "pedidos" / "PROVAS.md"
    soma = defaultdict(lambda: [0.0, 0, 0.0, 0, 0])
    if not arq.exists():
        return soma
    texto = arq.read_text(encoding="utf-8")
    for cab in re.findall(r"^\| Agente \| Achados \(de \d+\) \|.*$", texto, re.M):
        plantados = int(re.search(r"Achados \(de (\d+)\)", cab).group(1))
        limpos = int(m.group(1)) if (m := re.search(r"Alarmes falsos \(de (\d+)\)", cab)) else 0
        for c in linhas_de_tabela(texto, re.escape(cab)):
            if len(c) < 4:
                continue
            s = soma[nome(c[0])]
            s[0] += (numero(c[1]) or 0) + 0.5 * (numero(c[2]) or 0)  # parcial vale meio
            s[1] += plantados
            s[2] += numero(c[3]) or 0
            s[3] += limpos
            s[4] += 1
    return soma


def licoes():
    arq = RAIZ / "pedidos" / "LICOES.md"
    cont = defaultdict(lambda: defaultdict(int))
    if arq.exists():
        for c in linhas_de_tabela(arq.read_text(encoding="utf-8"), r"^\| Data \| Papel \| Origem \|"):
            if len(c) >= 3:
                cont[nome(c[1])][c[2]] += 1
    return cont


def br(x):
    return f"{x:.1f}".replace(".", ",").replace(",0", "")


def gerar():
    notas, pontos = vetos()
    pv, lc = provas(), licoes()
    agentes = sorted(set(notas) | set(pv) | set(lc))
    out = ["# Placar do veto (gerado: não edite)", "",
           "> Saída de `python3 ferramentas/placar.py`. Leia a sua linha antes de vetar. n = quantas vezes foi medido; "
           f"com n menor que {N_MINIMO}, nenhuma regra muda por causa deste número. Fontes: tabelas de veto das fichas "
           "de 23/11 em diante, `pedidos/PROVAS.md` e `pedidos/LICOES.md`.", "",
           "| Agente | Nota do veto (n) | Ponto que mais cai | Provas: achados (alarmes falsos) | Lições (origem) |",
           "|---|---|---|---|---|"]
    for a in agentes:
        nv = notas.get(a, [])
        nota = f"{br(sum(nv) / len(nv))} (n = {len(nv)})" if nv else "n = 0, sem nota ainda"
        cai = max(pontos[a].items(), key=lambda kv: (kv[1], kv[0]))[0] if pontos.get(a) else "-"
        if a in pv:
            ach, plant, alarme, limpos, n = pv[a]
            prova = f"{br(ach)} de {plant} ({br(alarme)} de {limpos}), n = {n}"
        else:
            prova = "-"
        lic = ", ".join(f"{o} {k}" for o, k in sorted(lc[a].items())) if a in lc else "-"
        out.append(f"| {a} | {nota} | {cai} | {prova} | {lic} |")
    if not agentes:
        out.append("| (ninguém) | n = 0, sem nota ainda | - | - | - |")
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    novo = gerar()
    if "--conferir" in sys.argv[1:]:
        atual = SAIDA.read_text(encoding="utf-8") if SAIDA.exists() else ""
        if atual != novo:
            sys.exit("contexto/PLACAR.md está velho: rode `python3 ferramentas/placar.py`")
        print("placar em dia")
    else:
        SAIDA.write_text(novo, encoding="utf-8")
        print(f"contexto/PLACAR.md gerado ({len(novo)} caracteres)")
