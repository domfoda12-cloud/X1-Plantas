#!/usr/bin/env python3
"""O plano geral (pedidos/PLANO.md) em comandos: o que dá para fazer agora, o que cada decisão do dono destrava, e a conferência.

O plano é escrito pelo agente `planejador`; este programa só lê, marca e confere, para a resposta a "o que faço agora?" sair
de uma conta, não de memória.

Uso: python3 ferramentas/plano.py agora             passos que podem começar já (dependências feitas) e os que só esperam o dono
     python3 ferramentas/plano.py destrava          as decisões do dono, da que mais destrava passos para a que menos destrava
     python3 ferramentas/plano.py caminho <passo>   tudo o que falta, em ordem, para chegar a um passo (ex.: D12)
     python3 ferramentas/plano.py feito <passo> "o que virou"          marca o passo como feito, com a data
     python3 ferramentas/plano.py respondido <n> "o que o dono disse"  marca a decisão n como respondida (só com fala dele)
     python3 ferramentas/plano.py subir [passo...]  sobe passos livres para "Agora" (sem nome: os primeiros livres, até ficar com 3)
     python3 ferramentas/plano.py conferir          falha se o plano estiver quebrado (usado pelo checar.py)
"""
import datetime, re, sys
from pathlib import Path

PLANO = Path(__file__).resolve().parent.parent / "pedidos" / "PLANO.md"
JURI = PLANO.parent / "anexos" / "juri-decisoes-faceis-2026-11-24.md"  # as decisões que o júri tomou e mostra ao dono (cartão v6)
SECOES = ["## Agora", "## Depois", "## Esperando o dono", "## Não fazer"]
RE_PASSO = re.compile(r"^\| ([A-Z]\d+) \|")
RE_DEC = re.compile(r"^(\d+)\. ")
MAL = []  # linhas de passo com número errado de colunas, achadas em ler()


def ler():
    texto = PLANO.read_text(encoding="utf-8")
    linhas = texto.split("\n")
    passos, decisoes, secao = {}, {}, ""
    for i, l in enumerate(linhas):
        if l.startswith("## "):
            secao = l
        m = RE_PASSO.match(l)
        if m and (secao.startswith("## Agora") or secao.startswith("## Depois")):
            c = [x.strip() for x in l.strip().strip("|").split("|")]
            if len(c) != 6:
                MAL.append(f"{m.group(1)}: a linha tem {len(c)} colunas e precisa de 6 (um | dentro do texto desloca as colunas: escreva 'ou' no lugar)")
                continue
            passos[m.group(1)] = dict(id=m.group(1), linha=i, texto=c[1], quem=c[2], onde=c[3], pronto=c[4], dep=c[-1],
                                      feito=c[1].startswith("**Feito"),
                                      secao="agora" if secao.startswith("## Agora") else ("fila" if "fila da equipe" in secao.lower() else "depois"))
        m = RE_DEC.match(l)
        if m and secao.startswith("## Esperando o dono"):
            decisoes[int(m.group(1))] = dict(n=int(m.group(1)), linha=i, texto=l[len(m.group(0)):], respondida="**Respondido" in l)
    ordem = list(passos)
    for p in passos.values():
        p["passos"], p["decisoes"] = dependencias(p["dep"], ordem)
    return linhas, passos, decisoes


def dependencias(dep, ordem):
    """'decisões 1, 15 e 16; D6' -> (['D6'], [1, 15, 16]); 'D3 a D11' -> D3..D11."""
    ps, ds = [], []
    for a, b in re.findall(r"([A-Z]\d+) a ([A-Z]\d+)", dep):
        if a in ordem and b in ordem:
            ps += ordem[ordem.index(a): ordem.index(b) + 1]
    ps += re.findall(r"[A-Z]\d+", dep)
    for trecho in re.findall(r"decis(?:ão|ões)\s+([\d,\sea]+)", dep):
        for a, b in re.findall(r"(\d+)\s+a\s+(\d+)", trecho):      # "decisões 3 a 5" = 3, 4 e 5
            ds += list(range(int(a), int(b) + 1))
        ds += [int(n) for n in re.findall(r"\d+", trecho)]
    return list(dict.fromkeys(ps)), list(dict.fromkeys(ds))


def sobra(dep):
    """O que resta da coluna 'depende de' depois de tirar os códigos: tem de ser nada (texto livre não se calcula)."""
    t = re.sub(r"\*\*|`", "", dep)
    t = re.sub(r"decis(?:ão|ões)\s+[\d,\sea]+", " ", t)
    t = re.sub(r"[A-Z]\d+(\s+a\s+[A-Z]\d+)?", " ", t)
    t = re.sub(r"\bninguém\b|\be\b|[,;.]", " ", t)
    return t.strip()


def falta(p, passos, decisoes):
    """O que ainda trava um passo: (passos não feitos, decisões não respondidas)."""
    return ([x for x in p["passos"] if x in passos and not passos[x]["feito"]],
            [n for n in p["decisoes"] if n in decisoes and not decisoes[n]["respondida"]])


def curto(t, n=110):
    t = re.sub(r"\*\*|`", "", t)
    return t if len(t) <= n else t[: n - 1].rstrip() + "…"


def bloqueia(n, passos, decisoes):
    """Todos os passos que não saem sem a decisão n, direta ou indiretamente."""
    travados = {p["id"] for p in passos.values() if not p["feito"] and n in p["decisoes"]}
    mudou = True
    while mudou:
        mudou = False
        for p in passos.values():
            if not p["feito"] and p["id"] not in travados and travados & set(p["passos"]):
                travados.add(p["id"]); mudou = True
    return sorted(travados, key=list(passos).index)


def cmd_agora():
    _, passos, decisoes = ler()
    abertos = [p for p in passos.values() if not p["feito"]]
    livres = [p for p in abertos if falta(p, passos, decisoes) == ([], [])]
    print(f"Plano: {sum(p['feito'] for p in passos.values())} de {len(passos)} passos feitos; "
          f"{sum(not d['respondida'] for d in decisoes.values())} decisões do dono sem resposta.\n")
    agora = [p for p in livres if p["secao"] == "agora"]
    print("AGORA (abertos, podem começar já):" if agora else "AGORA: VAZIO. A regra do dono é nunca ficar vazio: suba um passo livre da fila ou chame o planejador.")
    for p in agora:
        print(f"  {p['id']}  {curto(p['texto'])}\n       quem: {curto(p['quem'], 60)} · pronto quando: {curto(p['pronto'], 90)}")
    fila = [p for p in livres if p["secao"] != "agora"]
    if fila:
        print("\nLIVRES PARA SUBIR (fila da equipe e Depois, na ordem do plano):")
        for p in fila:
            print(f"  {p['id']}  {curto(p['texto'], 95)}  [{curto(p['quem'], 40)}]")
    so_dono = [p for p in abertos if p not in livres and not falta(p, passos, decisoes)[0]]
    if so_dono:
        print("\nSÓ FALTA O DONO RESPONDER (o passo anterior já está feito):")
        for p in so_dono:
            ds = falta(p, passos, decisoes)[1]
            print(f"  {p['id']}  {curto(p['texto'], 80)}\n       falta a decisão " + ", ".join(f"{n} ({curto(decisoes[n]['texto'], 50)})" for n in ds))
    resto = [p for p in abertos if p not in livres and p not in so_dono]
    if resto:
        print("\nDEPOIS (espera passo anterior): " + ", ".join(p["id"] for p in resto))


def cmd_destrava():
    _, passos, decisoes = ler()
    conta = sorted(((len(bloqueia(n, passos, decisoes)), n) for n, d in decisoes.items() if not d["respondida"]), key=lambda x: (-x[0], x[1]))
    print("Decisões do dono, da que mais destrava passos para a que menos (contando o que vem em cadeia):\n")
    for k, n in conta:
        if k:
            print(f"  {k:2d} passos  decisão {n}: {curto(decisoes[n]['texto'], 90)}\n             trava: {', '.join(bloqueia(n, passos, decisoes))}")
    print(f"\n  Sem passo do plano preso a elas: {', '.join(str(n) for k, n in conta if not k) or 'nenhuma'}")


def cmd_caminho(alvo):
    _, passos, decisoes = ler()
    if alvo not in passos:
        sys.exit(f"Não existe o passo {alvo}. Passos: {', '.join(passos)}")
    vistos, ds = [], []
    def anda(i):
        for x in passos[i]["passos"]:
            if x in passos and x not in vistos:
                anda(x)
        if i not in vistos:
            vistos.append(i)
        for n in passos[i]["decisoes"]:
            if n in decisoes and not decisoes[n]["respondida"] and n not in ds:
                ds.append(n)
    anda(alvo)
    print(f"Para chegar a {alvo} ({curto(passos[alvo]['texto'], 70)}):\n")
    for i in vistos:
        print(f"  [{'x' if passos[i]['feito'] else ' '}] {i}  {curto(passos[i]['texto'], 95)}")
    print(f"\nDecisões do dono no caminho ({len(ds)}): " + "; ".join(f"{n} ({curto(decisoes[n]['texto'], 45)})" for n in sorted(ds)))


def gravar(linhas):
    PLANO.write_text("\n".join(linhas), encoding="utf-8")


def falta_no_juri(pid):
    """O que falta à decisão J<n> no arquivo do júri (seção '## J1' ou linha de tabela '| J1 |'); lista vazia = pode fechar (F24)."""
    t = JURI.read_text(encoding="utf-8") if JURI.exists() else ""
    # a seção vem primeiro: uma tabela de notas antes dela também tem a linha "| J1 |"
    m = re.search(rf"^## {pid}\b.*?(?=^## |\Z)", t, re.S | re.M) or re.search(rf"^\| {pid} \|[^\n]*", t, re.M)
    if not m:
        return [f"a seção '## {pid}' (ou a linha '| {pid} |')"]
    bloco = m.group(0).replace("*", "").replace("`", "").lower()
    return [nome for nome, r in (('"como desfazer"', r"como desfazer"), ('"mostrado ao dono: sim"', r"mostrado ao dono:\s*sim\b")) if not re.search(r, bloco)]


def cmd_feito(pid, nota):
    linhas, passos, _ = ler()
    if pid not in passos:
        sys.exit(f"Não existe o passo {pid}.")
    if passos[pid]["feito"]:
        sys.exit(f"{pid} já está marcado como feito.")
    if re.fullmatch(r"J\d+", pid) and falta_no_juri(pid):  # regra v6 do dono: o júri decide, mas mostra e diz como desfazer
        sys.exit(f"Não marca {pid}: em pedidos/anexos/{JURI.name} falta " + " e ".join(falta_no_juri(pid))
                 + ". Decisão do júri só fecha com o \"como desfazer\" escrito e \"mostrado ao dono: sim\".")
    hoje = datetime.date.today().strftime("%d/%m")
    i = passos[pid]["linha"]
    linhas[i] = linhas[i].replace(f"| {pid} | ", f"| {pid} | **Feito {hoje}:** {nota.rstrip('.')}. ", 1)
    gravar(linhas); print(f"{pid} marcado como feito."); cmd_agora()


def cmd_respondido(n, nota):
    linhas, _, decisoes = ler()
    n = int(n)
    if n not in decisoes:
        sys.exit(f"Não existe a decisão {n}.")
    hoje = datetime.date.today().strftime("%d/%m")
    i = decisoes[n]["linha"]
    linhas[i] = linhas[i].replace(f"{n}. ", f"{n}. **Respondido {hoje}:** {nota.rstrip('.')}. ", 1)
    gravar(linhas); print(f"Decisão {n} marcada como respondida."); cmd_agora()


def cmd_subir(ids):
    """Move a linha de cada passo para o fim da tabela de "Agora". Só passo livre (nada falta); sem argumento sobe um só (dono, 24/11: uma tarefa por vez), e o limite é 2 abertos (a principal e um apoio)."""
    linhas, passos, decisoes = ler()
    abertos = [p["id"] for p in passos.values() if p["secao"] == "agora" and not p["feito"]]
    livres = [p["id"] for p in passos.values() if p["secao"] != "agora" and not p["feito"] and falta(p, passos, decisoes) == ([], [])]
    if not ids:
        ids = livres[: max(0, 1 - len(abertos))]
    for i in ids:
        if i not in passos:
            sys.exit(f"Não existe o passo {i}.")
        if i not in livres:
            sys.exit(f"{i} não pode subir: já está em 'Agora', está feito, ou ainda depende de alguém.")
    if len(abertos) + len(ids) > 2:
        sys.exit(f"'Agora' ficaria com {len(abertos) + len(ids)} passos abertos; o máximo é 2 (a tarefa principal e um apoio).")
    if not ids:
        print("Nada para subir."); return
    textos = [linhas[passos[i]["linha"]] for i in ids]
    for n in sorted((passos[i]["linha"] for i in ids), reverse=True):
        del linhas[n]
    ini = next(k for k, l in enumerate(linhas) if l.startswith("## Agora"))
    fim = next((k for k in range(ini + 1, len(linhas)) if linhas[k].startswith("## ")), len(linhas))
    ult = max(k for k in range(ini, fim) if linhas[k].startswith("|"))
    linhas[ult + 1: ult + 1] = textos
    gravar(linhas); print("Subiram para 'Agora': " + ", ".join(ids)); cmd_agora()


def cmd_conferir():
    texto = PLANO.read_text(encoding="utf-8")
    _, passos, decisoes = ler()
    erros = [f"falta a seção '{s}'" for s in SECOES if s not in texto]
    erros += MAL
    pos = [texto.find(s) for s in SECOES if s in texto]
    if pos != sorted(pos):
        erros.append("as seções Agora, Depois, Esperando o dono e Não fazer estão fora de ordem")
    if not passos:
        erros.append("nenhum passo com número (A1, D1...) nas tabelas de Agora e Depois")
    # linha de passo mal escrita some calada: "|D7 |" ou "| D7|" (prova 4, 24/11)
    secao = ""
    vistos = {}
    for l in texto.split("\n"):
        if l.startswith("## "):
            secao = l
        if (secao.startswith("## Agora") or secao.startswith("## Depois")) and re.match(r"^\|\s*[A-Z]\d+\s*\|", l):
            cod = re.match(r"^\|\s*([A-Z]\d+)", l).group(1)
            if not RE_PASSO.match(l):
                erros.append(f"{cod}: a linha tem de começar com '| {cod} | ' (com os espaços), senão o passo some da conta")
            vistos[cod] = vistos.get(cod, 0) + 1
    erros += [f"{c}: o código aparece {n} vezes" for c, n in vistos.items() if n > 1]
    nd = [int(m.group(1)) for l in texto.split("\n") for m in [RE_DEC.match(l)] if m]
    erros += [f"decisão {n}: o número aparece mais de uma vez" for n in sorted(set(x for x in nd if nd.count(x) > 1))]
    for p in passos.values():
        resto = sobra(p["dep"])
        if resto:
            erros.append(f"{p['id']}: 'depende de' tem texto que não é código ('{resto[:50]}'): use só passos (D3, D3 a D11), 'decisão N' ou 'ninguém'")
        if p["feito"]:
            fp, _ = falta(p, passos, decisoes)
            if fp:
                erros.append(f"{p['id']} está feito, mas depende de {', '.join(fp)}, que não está feito")
    for p in passos.values():
        for campo in ("quem", "onde", "pronto", "dep"):
            if not p[campo]:
                erros.append(f"{p['id']}: coluna vazia ({campo})")
        for x in p["passos"]:
            if x not in passos:
                erros.append(f"{p['id']} depende de {x}, que não existe")
            elif x == p["id"]:
                erros.append(f"{p['id']} depende dele mesmo")
        for n in p["decisoes"]:
            if n not in decisoes:
                erros.append(f"{p['id']} depende da decisão {n}, que não está em 'Esperando o dono'")
        if p["secao"] == "agora" and not p["feito"] and (p["decisoes"] or [x for x in p["passos"] if x in passos and not passos[x]["feito"]]):
            erros.append(f"{p['id']} está em 'Agora' mas ainda depende de alguém: vai para 'Depois'")
    # uma coisa por vez (dono, 20/11 e 23/11): vídeo e animação só depois do primeiro Pix medido (D13)
    if not ("D13" in passos and passos["D13"]["feito"]):
        erros += [f"{p['id']} está em 'Agora' e mexe em '{p['onde']}': vídeo e animação só abrem depois do D13 feito (uma coisa por vez: primeiro o e-book vende)"
                  for p in passos.values() if p["secao"] == "agora" and not p["feito"] and re.search(r"video/|animacoes-3d/", p["onde"])]
    abertos_agora = [p["id"] for p in passos.values() if p["secao"] == "agora" and not p["feito"]]
    if len(abertos_agora) > 2:  # dono, 24/11, 20:45: uma tarefa principal e no máximo um apoio
        erros.append(f"'Agora' tem {len(abertos_agora)} passos abertos; o máximo é 2 (a tarefa principal e um apoio)")
    # regra do dono (24/11/2026): "Sempre coloque algo no Agora, nunca pare"
    if not abertos_agora:
        erros.append("'Agora' está vazio: suba um passo livre da fila da equipe ou de 'Depois' (regra do dono, 24/11: nunca vazio)")
    livres_fora = [p["id"] for p in passos.values() if p["secao"] != "agora" and not p["feito"] and falta(p, passos, decisoes) == ([], [])]
    if len(livres_fora) < 6:
        erros.append(f"só há {len(livres_fora)} passos livres fora de 'Agora' (mínimo 6): chame o planejador para encher a fila da equipe")
    # ciclo de dependência
    def ciclo(i, pilha):
        if i in pilha:
            return True
        return any(ciclo(x, pilha | {i}) for x in passos[i]["passos"] if x in passos and x != i)
    for i in passos:
        if ciclo(i, frozenset()):
            erros.append(f"{i} está num ciclo de dependência"); break
    nums = sorted(decisoes)
    if nums and nums != list(range(1, len(nums) + 1)):
        erros.append("as decisões de 'Esperando o dono' não estão numeradas em sequência a partir de 1")
    if erros:
        print("Plano com problema:\n  " + "\n  ".join(erros)); sys.exit(1)
    print(f"Plano em ordem: {len(passos)} passos, {len(decisoes)} decisões, dependências fechadas.")


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help"):
        print(__doc__)
    elif a[0] == "agora": cmd_agora()
    elif a[0] == "destrava": cmd_destrava()
    elif a[0] == "caminho" and len(a) == 2: cmd_caminho(a[1])
    elif a[0] == "feito" and len(a) == 3: cmd_feito(a[1], a[2])
    elif a[0] == "respondido" and len(a) == 3: cmd_respondido(a[1], a[2])
    elif a[0] == "subir": cmd_subir(a[1:])
    elif a[0] == "conferir": cmd_conferir()
    else: sys.exit(__doc__)
