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
PONTOS = ["objetivo", "lugar", "prova", "correção", "novo e do papel"]  # a régua, pedidos/LEIA-ME.md
APELIDOS = {"fable": "supervisor", "opus": "maestro", "minoai-frontier": "diretor"}
SEM_ARQUIVO = {"maestro", "diretor", "haiku"}  # medidos, mas sem .claude/agents/<nome>.md


def nome(agente):
    """'Revisor de risco', '`revisor-de-risco`' e 'revisor-de-risco (Fable)' viram o mesmo nome."""
    a = re.sub(r"\(.*?\)|`|\*", "", agente).strip().lower()
    a = unicodedata.normalize("NFKD", re.sub(r"\s+", "-", a)).encode("ascii", "ignore").decode()
    agentes = RAIZ / ".claude" / "agents"
    sem_de = re.sub(r"-d[aeo]s?-", "-", a)  # 'editor-de-video' -> 'editor-video', se só esse existir
    a = sem_de if not (agentes / f"{a}.md").exists() and (agentes / f"{sem_de}.md").exists() else a
    return APELIDOS.get(a, a)


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
    """Notas e pontos por agente, e os erros de formato (o --conferir falha com eles: nada é pulado em silêncio)."""
    notas, pontos, erros = defaultdict(list), defaultdict(lambda: defaultdict(int)), []
    conhecidos = {p.stem for p in (RAIZ / ".claude" / "agents").glob("*.md")} | SEM_ARQUIVO
    for f in sorted((RAIZ / "pedidos").glob("20*/*.md")):
        if not re.match(r"\d{4}-\d\d-\d\d", f.name) or f.name[:10] < DESDE:
            continue
        texto = f.read_text(encoding="utf-8")
        for l in texto.splitlines():
            cab = [c.strip().lower() for c in l.strip().strip("|").split("|")]
            if l.strip().startswith("|") and "agente" in cab and any(c.startswith("nota") for c in cab) and l.strip() != CAB_VETO:
                erros.append(f"{f.name}: tabela de veto fora do formato fixo: {l.strip()}")
        for c in linhas_de_tabela(texto, re.escape(CAB_VETO)):
            a, n = nome(c[1]) if len(c) > 1 else "", numero(c[2]) if len(c) > 2 else None
            if len(c) < 5 or n is None or not 0 <= n <= 5 or a not in conhecidos:
                erros.append(f"{f.name}: linha de veto sem agente conhecido ou sem nota de 0 a 5: {' | '.join(c)}")
                continue
            notas[a].append(n)
            for p in re.split(r"[,;+]", c[3].lower()):
                p = p.strip()
                p = PONTOS[int(p) - 1] if p in list("12345") else p
                if p in PONTOS:
                    pontos[a][p] += 1
                elif p not in ("", "-", "—", "nenhum"):
                    erros.append(f"{f.name}: ponto fora da régua ({', '.join(PONTOS)}, ou 1 a 5): {p}")
    return notas, pontos, erros


def provas():
    """Por agente: achados, plantados, alarmes falsos, limpos e quantas provas fez. Uma passada: tabela repetida não soma duas vezes."""
    arq = RAIZ / "pedidos" / "PROVAS.md"
    soma, plantados, limpos = defaultdict(lambda: [0.0, 0, 0.0, 0, 0]), None, 0
    for l in arq.read_text(encoding="utf-8").splitlines() if arq.exists() else []:
        l = l.strip()
        if m := re.match(r"\| Agente \| Achados \(de (\d+)\) \|", l):
            plantados = int(m.group(1))
            limpos = int(a.group(1)) if (a := re.search(r"Alarmes falsos \(de (\d+)\)", l)) else 0
        elif plantados is not None and l.startswith("|"):
            c = [x.strip() for x in l.strip("|").split("|")]
            if len(c) >= 4 and not re.match(r"^\|[\s:|-]+\|$", l):
                s = soma[nome(c[0])]
                s[0] += (numero(c[1]) or 0) + 0.5 * (numero(c[2]) or 0)  # parcial vale meio: escolha nossa, dita no topo do placar
                s[1] += plantados
                s[2] += numero(c[3]) or 0
                s[3] += limpos
                s[4] += 1
        else:
            plantados = None
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
    return f"{x:.2f}".rstrip("0").rstrip(".").replace(".", ",")  # duas casas: 3,95 não vira 4


def gerar():
    notas, pontos, erros = vetos()
    pv, lc = provas(), licoes()
    agentes = sorted(set(notas) | set(pv) | set(lc))
    out = ["# Placar do veto (gerado: não edite)", "",
           "> Saída de `python3 ferramentas/placar.py`. Quem chama um veto cola no pedido a linha do agente. "
           "Nota = a que o Maestro deu ao veto pela régua, de 0 a 5 (a do maestro é dele para si mesmo); "
           f"n = quantas vezes foi medido; com n menor que {N_MINIMO}, nenhuma regra muda por causa do número. "
           "Prova = erros plantados achados; parcial vale meio achado (escolha nossa); o que cada um deixou passar "
           "(omissões) não entra no número e está em `pedidos/PROVAS.md`. Fontes: tabelas de veto das fichas de 23/11 "
           "em diante, `pedidos/PROVAS.md` e `pedidos/LICOES.md`.", "",
           "| Agente | Nota do veto, de 0 a 5 (n) | Ponto que mais cai (vezes) | Provas: plantados achados; alarmes falsos | Lições (origem) |",
           "|---|---|---|---|---|"]
    for a in agentes:
        nv = notas.get(a, [])
        pouco = ", pouco para mudar regra" if len(nv) < N_MINIMO else ""
        nota = f"{br(sum(nv) / len(nv))} (n = {len(nv)}{pouco})" if nv else "n = 0, sem nota ainda"
        topo = max(pontos[a].values()) if pontos.get(a) else 0
        cai = ", ".join(f"{p} ({k} de {len(nv)})" for p, k in sorted(pontos[a].items()) if k == topo) if topo else "-"
        if a in pv:
            ach, plant, alarme, limpos, n = pv[a]
            falso = f"{br(alarme)} de {limpos}" if limpos else "alarme falso não medido"
            prova = f"{br(ach)} de {plant}; {falso}; n = {n}"
        else:
            prova = "-"
        lic = ", ".join(f"{o} {k}" for o, k in sorted(lc[a].items())) if a in lc else "-"
        out.append(f"| {a} | {nota} | {cai} | {prova} | {lic} |")
    if not agentes:
        out.append("| (ninguém) | n = 0, sem nota ainda | - | - | - |")
    return "\n".join(out) + "\n", erros


if __name__ == "__main__":
    novo, erros = gerar()
    if len(novo) > 3500:  # fica em contexto/: o mesmo limite do checar.py
        erros.append(f"contexto/PLACAR.md passaria de 3500 caracteres ({len(novo)}): encurte o topo, nunca suba o limite")
    if erros:
        sys.exit("tabela de veto fora do formato (pedidos/LEIA-ME.md, a régua do veto):\n  " + "\n  ".join(erros))
    if "--conferir" in sys.argv[1:]:
        atual = SAIDA.read_text(encoding="utf-8") if SAIDA.exists() else ""
        if atual != novo:
            sys.exit("contexto/PLACAR.md está velho: rode `python3 ferramentas/placar.py`")
        print("placar em dia")
    else:
        SAIDA.write_text(novo, encoding="utf-8")
        print(f"contexto/PLACAR.md gerado ({len(novo)} caracteres)")
