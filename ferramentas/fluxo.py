"""Fluxos fixos (dono, 26/11/2026: "ultra max"): a conferência mais barata que pega o erro, primeiro por programa.

Plano: pedidos/anexos/plano-fluxos-2026-11-26.md; mapa: pedidos/anexos/mapa-conferencias-2026-11-26.md.
Os fluxos salvos (.claude/workflows/) chamam estes comandos por um agente barato e só depois gastam juízo.

Uso:
  python3 ferramentas/fluxo.py texto <arquivo> [--json]   frases vetadas, promessas proibidas e números da casa contra o
                                                          PLANTAS.md (erro); lote sem prefeitura, nota interna, hora futura (aviso)
  python3 ferramentas/fluxo.py pagina <pdf> <n> [--json]   o mesmo que "texto", no texto da página n de um PDF de prévia
  python3 ferramentas/fluxo.py passe <arq.json|-> [--publico]   passe entre agentes com forma fixa; arquivo citado existe e o
                                                          git acompanha; --publico exige a ideia do Diretor com a fonte
  python3 ferramentas/fluxo.py juri <arq.json|->           recusa rodada de júri incompleta (CONSELHO.md 5b) e calcula o resultado
  python3 ferramentas/fluxo.py registrar <arq.json|->      grava a rodada e o gasto em pedidos/fluxos/ e colhe as lições sozinho
  python3 ferramentas/fluxo.py relatorio                   gasto por fluxo e conferidor sem achado próprio (candidato a corte)
  python3 ferramentas/fluxo.py prova-estado                nível de cada papel na prova de entrada e os casos que voltam
  python3 ferramentas/fluxo.py prova-nota <arq.json|->     dá a nota (por programa), sobe o nível de quem passou, grava lição de quem errou
  python3 ferramentas/fluxo.py testar                      prova que cada conferência pega o erro (o checar.py roda)

Saída 1 quando há erro (texto, passe, júri incompleto, registro fora da forma).
"""
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
FLUXOS = RAIZ / "pedidos" / "fluxos"
PROVAS = RAIZ / "pedidos" / "provas"
PASSE = ("feito", "suposicoes", "faltando", "arquivos", "perguntas_ao_dono")
ANGULOS = ("comprador", "dinheiro", "risco")
LICOES_POR_RODADA = 3  # por autor; as outras ficam no registro da rodada

# --- 1. Texto que vai ao público -------------------------------------------------------------------------------------
# Frases vetadas pela Vera que não voltam (contexto/redator.md) e as promessas que o CLAUDE.md proíbe.
VETADAS = [
    (r"todas as casas cabem", "frase vetada: 'todas as casas cabem' (contexto/redator.md)"),
    (r"banheiro com giro", "frase vetada: 'banheiro com giro' sem conferência (contexto/redator.md)"),
    (r"recebe(?:r[áa])? as pr[óo]ximas plantas", "frase vetada: 'recebe as próximas plantas' sem o sim do dono (contexto/redator.md)"),
    (r"\bem breve\b", "futuro que o dono não prometeu: 'em breve' (contexto/redator.md)"),
]
PROMESSAS = [
    (r"dispens\w*\s+(?:o |a |de |do |da )?(?:pedreiro|engenheiro|arquiteto|profissional|projeto)",
     "promessa proibida: dispensar pedreiro, engenheiro ou arquiteto (CLAUDE.md)"),
    (r"\bsem (?:precisar de |contratar )?(?:pedreiro|engenheiro|arquiteto)\b", "promessa proibida: obra sem profissional (CLAUDE.md)"),
    (r"aprova[çc][ãa]o (?:garantida|certa)|garant\w+ (?:a )?aprova[çc]|aprova(?:da|do)? na prefeitura com certeza|j[áa] aprovad[ao]",
     "promessa proibida: aprovação na prefeitura (CLAUDE.md)"),
    (r"(?:custo|pre[çc]o|valor) (?:exato|certo|fechado) (?:da|de) obra|obra (?:sai|custa|fica) (?:por )?(?:exatamente |s[óo] )?R\$",
     "promessa proibida: custo exato de obra (CLAUDE.md)"),
    (r"prazo (?:garantido|exato|certo) (?:da|de) obra|(?:fica|fica pronta|termina) em \d+ (?:dias|meses) com certeza",
     "promessa proibida: prazo de obra (CLAUDE.md)"),
]
NEGA = re.compile(r"\b(n[ãa]o|nunca|nem|jamais|nenhum|nenhuma|sem que)\b", re.I)  # negação antes, na mesma linha: "nunca prometer..."
AVISOS = [
    (r"\bventila[çc][ãa]o cruzada\b", "'ventilação cruzada': só com janelas opostas, conferidas no PLANTAS.md (contexto/redator.md)"),
    (r"\bainda n[ãa]o (?:temos|tem|tenho)\b", "'ainda não': soa como promessa de futuro (contexto/redator.md)"),
    (r"o dono decide|\bnota (?:interna|ao s[óo]cio)\b|\(a preencher\)|\bTODO\b", "nota interna no texto ao cliente (Vera, 26/11)"),
]
DIRECOES = ("norte", "sul", "leste", "oeste")


def casas():
    """Ficha de cada casa tirada do PLANTAS.md (gerado pelo validador): área fechada, lote, lote mínimo e frente."""
    txt = (RAIZ / "ebook" / "plantas" / "PLANTAS.md").read_text(encoding="utf-8")
    num = lambda s: float(s.replace(",", "."))
    out = {}
    for m in re.finditer(r"^## (\w\d\d) · (.+)\n(?:.*\n){0,3}?\*\*(\d+) m² fechados\*\*.*?lote de \*\*([\d,]+) x ([\d,]+) m\*\* "
                         r"\(no mínimo ([\d,]+) x ([\d,]+) m\) · frente para o \*\*(\w+)\*\*", txt, re.M):
        out[m.group(1)] = {"nome": m.group(2).strip(), "area": int(m.group(3)), "lote": (num(m.group(4)), num(m.group(5))),
                           "minimo": (num(m.group(6)), num(m.group(7))), "frente": m.group(8)}
    return out


def conferir_texto(txt, agora=None):
    """[(linha, 'erro'|'aviso', mensagem)] para um texto que vai ao público."""
    achados, base = [], casas()
    agora = agora or datetime.now(timezone.utc)
    num = lambda s: float(s.replace(",", "."))
    for i, linha in enumerate(txt.splitlines(), 1):
        low = linha.lower()
        for rx, msg in VETADAS:
            for m in re.finditer(rx, low):
                if not NEGA.search(low[:m.start()]):
                    achados.append((i, "erro", msg))
        for rx, msg in PROMESSAS:
            for m in re.finditer(rx, low):
                if not NEGA.search(low[:m.start()]):
                    achados.append((i, "erro", msg))
        for rx, msg in AVISOS:
            if re.search(rx, linha, re.I):
                achados.append((i, "aviso", msg))
        if re.search(r"\b(lote|recuo)s?\b", low) and "prefeitura" not in low and re.search(r"\d", low):
            achados.append((i, "aviso", "lote ou recuo com medida sem 'a prefeitura confirma' (Vera, 26/11)"))
        # números da casa: só quando a linha fala de UMA casa (código ou nome)
        citadas = [c for c, d in base.items() if re.search(rf"\b{c}\b", linha) or d["nome"].lower() in low]
        if len(citadas) == 1:
            d = base[citadas[0]]
            for m in re.finditer(r"(\d+(?:,\d+)?) ?m²(?: fechados| constru[íi]dos| de (?:casa|área))", low):
                if round(num(m.group(1))) != d["area"]:
                    achados.append((i, "erro", f"{citadas[0]}: {m.group(1)} m² no texto, {d['area']} m² fechados no PLANTAS.md"))
            for m in re.finditer(r"lote (?:de )?(\d+(?:,\d+)?) ?x ?(\d+(?:,\d+)?)", low):
                par = (num(m.group(1)), num(m.group(2)))
                if par not in (d["lote"], d["minimo"]):
                    achados.append((i, "erro", f"{citadas[0]}: lote {m.group(1)} x {m.group(2)} no texto; no PLANTAS.md, "
                                               f"{d['lote'][0]:g} x {d['lote'][1]:g} (mínimo {d['minimo'][0]:g} x {d['minimo'][1]:g})"))
            for m in re.finditer(r"(?:frente para o|melhor com a rua a[o]?) (" + "|".join(DIRECOES) + r")\b", low):
                if m.group(1) != d["frente"] and not NEGA.search(low[:m.start()]):
                    achados.append((i, "erro", f"{citadas[0]}: rua ao {m.group(1)} no texto, ao {d['frente']} no PLANTAS.md (o lado vem do PLANTAS.md)"))
        hoje = f"{agora:%d/%m}"
        if hoje in linha:
            for m in re.finditer(r"\b([01]?\d|2[0-3]):([0-5]\d)\b", linha):
                if (int(m.group(1)), int(m.group(2))) > (agora.hour, agora.minute):
                    achados.append((i, "aviso", f"hora {m.group(0)} de hoje passa da hora real ({agora:%H:%M} UTC): rode date -u"))
    return achados


# --- 2. Passe entre agentes --------------------------------------------------------------------------------------------
def conferir_passe(p, publico=False):
    erros = []
    if not isinstance(p, dict):
        return ["o passe não é um objeto JSON"]
    for k in PASSE:
        if not isinstance(p.get(k), list):
            erros.append(f"falta o campo '{k}' (lista; vazia se não houver nada)")
    if isinstance(p.get("feito"), list) and not p["feito"]:
        erros.append("'feito' vazio: o passo não diz o que fez")
    if publico and not str(p.get("fonte_diretor") or "").strip():
        erros.append("conteúdo público sem a ideia do Diretor com a fonte ('fonte_diretor'; provas 1 e 2)")
    for a in p.get("arquivos") or []:
        rel = str(a).split(":")[0].strip()
        arq = RAIZ / rel
        if rel.startswith("ebook/saida"):
            erros.append(f"{rel}: ebook/saida/ é só com o dono")
        elif not arq.exists():
            erros.append(f"{rel}: o arquivo citado não existe")
        elif subprocess.run(["git", "check-ignore", "-q", rel], cwd=RAIZ).returncode == 0:
            erros.append(f"{rel}: está numa pasta que o git ignora (não fica salvo; auditoria 0116)")
    return erros


# --- 3. Júri (CONSELHO.md, seção 5b) -----------------------------------------------------------------------------------
def _cita(c, onde):
    arq, linha = str((c or {}).get("arquivo", "")).strip(), (c or {}).get("linha")
    if not arq:
        return f"{onde}: sem arquivo"
    f = RAIZ / arq
    if not f.is_file():
        return f"{onde}: {arq} não existe"
    if not isinstance(linha, int) or linha < 1:
        return f"{onde}: sem número de linha"
    n = len(f.read_text(encoding="utf-8", errors="replace").splitlines())
    return None if linha <= n else f"{onde}: {arq} tem {n} linhas, a citação diz {linha}"


def conferir_juri(r):
    """Recusa a rodada que fura uma regra da 5b e calcula o resultado (piso 7, média 8,5, jurado de fato falso perde a nota)."""
    erros = []
    regua = r.get("regua") or {}
    if not all(str(regua.get(k) or "").strip() for k in ("3", "6", "9")):
        erros.append("sem régua com o que vale 3, 6 e 9 (regra 0)")
    if not str(r.get("motivo") or "").strip():
        erros.append("sem o motivo de ir ao júri (custa dinheiro, vai ao público ou não se desfaz)")
    jur = r.get("jurados") or []
    if len(jur) != 3:
        erros.append(f"{len(jur)} jurados; a regra 1 pede 3")
    if sorted(str(j.get("angulo")) for j in jur) != sorted(ANGULOS):
        erros.append("cada jurado com um ângulo diferente: comprador, dinheiro e risco (regra 1)")
    modelos = [str(j.get("modelo", "")).lower() for j in jur]
    if len(set(modelos)) != len(modelos):
        erros.append("dois jurados no mesmo modelo (regra 1: 3 modelos)")
    for n, j in enumerate(jur):
        if not isinstance(j.get("nota"), (int, float)) or not 0 <= j["nota"] <= 10:
            erros.append(f"jurado {n + 1}: nota fora de 0 a 10")
        defs = j.get("defeitos") or []
        if len(defs) < 2:
            erros.append(f"jurado {n + 1}: {len(defs)} defeito(s); a regra pede pelo menos 2 com arquivo e linha")
        erros += [e for e in (_cita(d, f"jurado {n + 1}, defeito {k + 1}") for k, d in enumerate(defs)) if e]
    rev = r.get("revisao_anonima") or []
    if len(rev) != len(jur) or any(len(x.get("ordem") or []) != len(jur) - 1 for x in rev):
        erros.append("revisão anônima incompleta: cada jurado ordena as outras opiniões (regra 2)")
    pres = r.get("presidente") or {}
    if str(pres.get("modelo", "")).lower() in modelos or not pres.get("modelo"):
        erros.append("o presidente tem de ser o modelo que não opinou (regra 3)")
    fatos = pres.get("fatos") or []
    if len(fatos) < 5:
        erros.append(f"presidente conferiu {len(fatos)} fato(s); a regra 3 pede 5")
    erros += [e for e in (_cita(f, f"fato {k + 1}") for k, f in enumerate(fatos)) if e]
    if not isinstance((r.get("gasto") or {}).get("tokens_saida"), int) or r["gasto"]["tokens_saida"] <= 0:
        erros.append("rodada sem o gasto anotado (tokens de saída do budget.spent())")
    falsos = {f.get("de") for f in fatos if f.get("confirmado") is False and isinstance(f.get("de"), int)}
    notas = [None if n + 1 in falsos else j.get("nota") for n, j in enumerate(jur)]
    validas = [x for x in notas if isinstance(x, (int, float))]
    media = round(sum(validas) / len(validas), 2) if validas else None
    # o piso olha TODAS as notas dadas: perder a nota por fato falso tira o jurado da média, nunca abre o piso
    # (rodada real de 26/11: o jurado do 5 errou um fato e a média ficou só com o 8); e passar pede 2 notas válidas
    dadas = [j.get("nota") for j in jur if isinstance(j.get("nota"), (int, float))]
    piso = bool(dadas) and min(dadas) >= 7
    passa = not erros and media is not None and media >= 8.5 and piso and len(validas) >= 2
    rodada = r.get("rodada", 1)
    proximo = "aprovada" if passa else ("recusada: complete a rodada" if erros else ("reescrever uma vez" if rodada < 2 else "vai ao dono com as duas notas"))
    return {"completa": not erros, "erros": erros, "notas": notas, "perderam_a_nota": sorted(falsos), "media": media,
            "piso_ok": piso, "passa": passa, "proximo": proximo}


# --- 4. Registro da rodada e colheita das lições -----------------------------------------------------------------------
def _carrega(caminho):
    return json.loads(sys.stdin.read() if caminho == "-" else Path(caminho).read_text(encoding="utf-8"))


def _papeis():
    return {f.stem for f in (RAIZ / "contexto").glob("*.md") if f.stem.islower()}


def _json(arq, padrao):
    return json.loads(arq.read_text(encoding="utf-8")) if arq.exists() else padrao


def _grava_json(arq, obj):
    arq.parent.mkdir(parents=True, exist_ok=True)
    arq.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def _licao(papel, texto, origem):
    """Grava pelo pedido.py (o mesmo registro único), consolidando as antigas se o arquivo encher."""
    import importlib.util as iu
    e = iu.spec_from_file_location("pedido", Path(__file__).resolve().parent / "pedido.py"); p = iu.module_from_spec(e); e.loader.exec_module(p)
    p.RAIZ, p.PEDIDOS = RAIZ, RAIZ / "pedidos"
    import contextlib
    try:
        with contextlib.redirect_stdout(sys.stderr):  # a saída do registrar é só o JSON (o fluxo lê o stdout)
            p.licao(papel, texto, origem=origem, consolidar_cheio=True)
        return True
    except SystemExit as x:
        print(f"lição de {papel} não gravada: {x}")
        return False


def conferir_registro(r):
    erros = []
    for k in ("fluxo", "peca", "resultado"):
        if not str(r.get(k) or "").strip():
            erros.append(f"falta '{k}'")
    if not isinstance((r.get("gasto") or {}).get("tokens_saida"), int):
        erros.append("falta o gasto (gasto.tokens_saida, do budget.spent())")
    confs = r.get("conferidores")
    if not isinstance(confs, list) or not confs:
        erros.append("falta a lista de conferidores (nome, tipo P ou A, achados_proprios)")
    for c in confs or []:
        if c.get("tipo") not in ("P", "A") or not isinstance(c.get("achados_proprios"), int) or not c.get("nome"):
            erros.append(f"conferidor fora da forma: {c}")
    for a in r.get("achados") or []:
        if not all(str(a.get(k) or "").strip() for k in ("autor", "chave", "texto")):
            erros.append(f"achado sem autor, chave ou texto: {a}")
    return erros


def registrar(r, agora=None):
    erros = conferir_registro(r)
    if erros:
        return {"gravado": False, "erros": erros}
    agora = agora or datetime.now(timezone.utc)
    marca = f"{agora:%Y-%m-%d-%H%M%S}"
    r = dict(r, registrado_em=f"{agora:%Y-%m-%dT%H:%M:%SZ}")
    _grava_json(FLUXOS / "rodadas" / f"{marca}-{r['fluxo']}.json", r)
    colhidas = _json(FLUXOS / "licoes-colhidas.json", {})
    voltam = _json(PROVAS / "voltam.json", [])
    papeis, novas, repetidas, por_autor = _papeis(), [], [], {}
    ordem = {"vera": 0, "presidente": 1}  # a leitura final pesa mais; as de programa por último (o programa já as pega sozinho)
    for a in sorted(r.get("achados") or [], key=lambda a: ordem.get(a.get("achado_por"), 2 if not str(a.get("achado_por", "")).startswith("programa") else 3)):
        chave = f"{a['autor']}|{re.sub(r'[^a-z0-9-]', '-', a['chave'].lower())}"
        if a["autor"] not in papeis or not str(a.get("licao") or "").strip():
            continue
        if chave in colhidas:  # a lição já estava no arquivo e o erro voltou: o caso vai para a próxima prova
            colhidas[chave]["vezes"] += 1
            voltam.append({"papel": a["autor"], "chave": a["chave"], "texto": a["texto"], "rodada": marca})
            repetidas.append(chave)
        elif por_autor.get(a["autor"], 0) >= LICOES_POR_RODADA:  # o resto fica no registro da rodada, para não encher o arquivo de uma vez
            continue
        elif _licao(a["autor"], f"({r['fluxo']}) {a['licao']}", "fluxo"):
            por_autor[a["autor"]] = por_autor.get(a["autor"], 0) + 1
            colhidas[chave] = {"desde": f"{agora:%Y-%m-%d}", "vezes": 1, "rodada": marca}
            novas.append(chave)
    _grava_json(FLUXOS / "licoes-colhidas.json", colhidas)
    if repetidas:
        _grava_json(PROVAS / "voltam.json", voltam)
    tabela = FLUXOS / "RODADAS.md"
    if not tabela.exists():
        tabela.write_text("# Rodadas dos fluxos fixos\n\n> Gravado por `python3 ferramentas/fluxo.py registrar` no fim de cada fluxo "
                          "(`.claude/workflows/`). Não edite à mão; o detalhe de cada rodada está em `rodadas/`.\n\n"
                          "| Quando (UTC) | Fluxo | Peça | Resultado | Voltas | Tokens de saída | Achados | Lições novas | Erro que voltou |\n"
                          "|---|---|---|---|---|---|---|---|---|\n", encoding="utf-8")
    with open(tabela, "a", encoding="utf-8") as h:
        h.write(f"| {agora:%d/%m %H:%M} | {r['fluxo']} | `{r['peca']}` | {r['resultado']} | {r.get('voltas', 0)} | "
                f"{r['gasto']['tokens_saida']} | {len(r.get('achados') or [])} | {len(novas)} | {len(repetidas)} |\n")
    return {"gravado": True, "arquivo": f"pedidos/fluxos/rodadas/{marca}-{r['fluxo']}.json", "licoes_novas": novas, "voltaram": repetidas}


def relatorio():
    rod = [json.loads(f.read_text(encoding="utf-8")) for f in sorted((FLUXOS / "rodadas").glob("*.json"))] if (FLUXOS / "rodadas").exists() else []
    por_fluxo, por_conf = {}, {}
    for r in rod:
        f = por_fluxo.setdefault(r["fluxo"], {"rodadas": 0, "tokens_saida": 0})
        f["rodadas"] += 1; f["tokens_saida"] += r["gasto"]["tokens_saida"]
        for c in r.get("conferidores") or []:
            k = por_conf.setdefault(c["nome"], {"rodadas": 0, "achados_proprios": 0, "tokens": 0, "tipo": c["tipo"]})
            k["rodadas"] += 1; k["achados_proprios"] += c["achados_proprios"]
            k["tokens"] += c.get("tokens") or (r["gasto"].get("por_conferidor") or {}).get(c["nome"], 0)
    corte = [n for n, k in por_conf.items() if k["tipo"] == "A" and k["rodadas"] >= 5 and k["achados_proprios"] == 0]
    return {"rodadas": len(rod), "por_fluxo": por_fluxo, "por_conferidor": por_conf, "candidatos_a_corte": corte}


# --- 5. Prova de entrada que fica mais difícil ------------------------------------------------------------------------
NIVEIS = {
    1: "erro escrito: uma frase fere uma regra escrita (promessa proibida, frase vetada)",
    2: "número errado contra o arquivo (área, lote, lado da rua, preço): só quem abre o PLANTAS.md ou o CONTEXTO.md pega",
    3: "omissão: falta o passo ou o aviso que a regra exige (Diretor, 'a prefeitura confirma', Revisor, sim do dono)",
    4: "decisão do dono contrariada ou suposição tratada como sim (pedidos/anexos/decisoes-do-dono-2026-11-23.md)",
    5: "dois problemas no mesmo caso, um óbvio e um sutil, e uma isca que parece erro e não é",
    6: "casos refeitos dos erros que voltaram (pedidos/provas/voltam.json), com outras palavras, mais iscas",
}


def nivel_desc(n):
    return NIVEIS.get(n) or f"{NIVEIS[6]}; {n - 5} iscas por caso e o problema no meio de um texto mais longo"


def prova_estado():
    est = _json(PROVAS / "NIVEIS.json", {})
    voltam = _json(PROVAS / "voltam.json", [])
    return {p: {"nivel": d["nivel"], "o_que_vale": nivel_desc(d["nivel"]), "voltam": [v for v in voltam if v["papel"] == p][-5:]}
            for p, d in est.items()} | {"_niveis": {str(k): v for k, v in NIVEIS.items()}}


def _acertou(gab, resp):
    """Problema plantado achado: a resposta aponta a mesma linha (1 de folga)."""
    return any(isinstance(x.get("linha"), int) and abs(x["linha"] - gab["linha"]) <= 1 for x in resp)


def prova_nota(d, agora=None, gravar=True):
    """d = {casos: [{id, texto, problemas: [{linha, categoria, porque}]}], respostas: {papel: [{id, problemas: [{linha, categoria}]}]},
    nivel_por_papel opcional}. Nota por programa; quem acerta tudo sem alarme falso sobe de nível."""
    agora = agora or datetime.now(timezone.utc)
    est = _json(PROVAS / "NIVEIS.json", {})
    if "gabarito_arquivo" in d:  # o gabarito fica fora do repositório até a nota (provas 1 e 2); depois entra aqui, revelado
        d = dict(d, casos=json.loads(Path(d["gabarito_arquivo"]).read_text(encoding="utf-8"))["casos"])
    casos = {c["id"]: c for c in json.loads(json.dumps(d["casos"]))}  # cópia: quem chama não perde o gabarito
    # item que TODOS os papéis (2 ou mais) deixaram passar fica em disputa: na prova 1 o gabarito errou em 3 planos.
    # Não conta nem vira lição até o árbitro decidir ("confirmados" volta a contar; "anulados" sai do gabarito).
    chave = lambda cid, g: f"{cid}:{g['linha']}"
    conf, anul = set(d.get("confirmados") or []), set(d.get("anulados") or [])
    for c in casos.values():
        c["problemas"] = [g for g in c["problemas"] if chave(c["id"], g) not in anul]
    resp_de = {p: {x["id"]: x.get("problemas") or [] for x in rs or []} for p, rs in d["respostas"].items()}
    disputa = [chave(cid, g) for cid, c in casos.items() for g in c["problemas"]
               if len(resp_de) >= 2 and chave(cid, g) not in conf and not any(_acertou(g, r.get(cid, [])) for r in resp_de.values())]
    for c in casos.values():
        c["problemas"] = [g for g in c["problemas"] if chave(c["id"], g) not in disputa]
    out = {"_em_disputa": disputa} if disputa else {}
    if disputa and gravar:  # a nota só é gravada depois do árbitro
        return out
    for papel, resps in d["respostas"].items():
        r = {x["id"]: x.get("problemas") or [] for x in resps or []}
        achou, perdeu, falso = 0, [], []
        for cid, c in casos.items():
            dada = r.get(cid, [])
            if c["problemas"]:
                for g in c["problemas"]:
                    if _acertou(g, dada):
                        achou += 1
                    else:
                        perdeu.append({"caso": cid, **g})
            elif dada:
                falso.append(cid)
        total = sum(len(c["problemas"]) for c in casos.values())
        nivel = est.get(papel, {}).get("nivel", 1)
        passou = not perdeu and not falso
        out[papel] = {"nivel": nivel, "achou": achou, "de": total, "alarmes_falsos": falso, "perdeu": perdeu, "passou": passou,
                      "proximo_nivel": nivel + 1 if passou else nivel}
        if gravar:
            h = est.setdefault(papel, {"nivel": 1, "historico": []})
            h["historico"].append({"em": f"{agora:%Y-%m-%d %H:%M}", "nivel": nivel, "achou": achou, "de": total, "falsos": len(falso), "gasto_tokens": d.get("gasto_tokens")})
            h["nivel"] = out[papel]["proximo_nivel"]
            if papel in _papeis():
                for p in perdeu[:2]:  # no máximo 2 lições por prova, para o arquivo não encher de uma vez
                    _licao(papel, f"Prova de entrada, nível {nivel}: deixei passar {p['categoria']} ({p['porque']}).", "prova")
                if falso:
                    _licao(papel, f"Prova de entrada, nível {nivel}: apontei problema em {len(falso)} caso(s) limpo(s); "
                                  "só aponto o que a regra escrita sustenta, com arquivo e linha.", "prova")
    if gravar:
        rel = PROVAS / f"rodada-{agora:%Y-%m-%d-%H%M}.md"
        linhas = [f"# Prova de entrada, {agora:%d/%m/%Y %H:%M} UTC", "",
                  "> Gravado por `python3 ferramentas/fluxo.py prova-nota` (fluxo `.claude/workflows/prova-de-entrada.js`). "
                  "Nota por programa: problema achado = linha certa (1 de folga); caso limpo apontado = alarme falso. "
                  "Passou (tudo achado, nenhum alarme falso): o próximo nível fica mais difícil.", "",
                  f"**Gasto:** {d.get('gasto_tokens', 'não anotado')} tokens de saída (budget.spent() do fluxo, sem a nota).", "",
                  "| Papel | Nível | Achou | Alarmes falsos | Passou | Próximo nível |", "|---|---|---|---|---|---|"]
        linhas += ([f"**Árbitro:** confirmou {sorted(conf) or 'nada'}; anulou {sorted(anul) or 'nada'}.", ""] if conf or anul else [])
        linhas += [f"| {p} | {o['nivel']} | {o['achou']} de {o['de']} | {len(o['alarmes_falsos'])} | {'sim' if o['passou'] else 'não'} | {o['proximo_nivel']} |"
                   for p, o in out.items() if not p.startswith("_")]
        linhas += ["", "## Gabarito (revelado depois da nota)", ""]
        for cid, c in casos.items():
            prob = "; ".join(f"linha {g['linha']}: {g['categoria']} ({g['porque']})" for g in c["problemas"]) or "limpo"
            linhas += [f"### Caso {cid}", "", "```", c["texto"].strip(), "```", "", f"**Gabarito:** {prob}", ""]
        rel.parent.mkdir(parents=True, exist_ok=True)
        rel.write_text("\n".join(linhas) + "\n", encoding="utf-8")
        _grava_json(PROVAS / "NIVEIS.json", est)
        voltam = _json(PROVAS / "voltam.json", [])
        voltam += [{"papel": p, "chave": x["categoria"], "texto": casos[x["caso"]]["texto"][:600], "rodada": f"prova {agora:%Y-%m-%d}"}
                   for p, o in out.items() if not p.startswith("_") for x in o["perdeu"]]
        _grava_json(PROVAS / "voltam.json", voltam)
    return out


# --- 6. Prova de que cada conferência pega o erro ----------------------------------------------------------------------
def testar():
    falhas = []
    base = casas()
    if not {"C01", "E03", "F01"} <= set(base):
        falhas.append(f"PLANTAS.md não foi lido: {sorted(base)[:5]}")
    c = base.get("C01", {"area": 0, "lote": (0, 0), "frente": "x"})
    ruim = (f"A Casa Compacta tem {c['area'] + 3} m² fechados.\nTodas as casas cabem no seu lote.\nA planta dispensa o engenheiro.\n"
            f"C01: frente para o {'norte' if c['frente'] != 'norte' else 'sul'}.\nC01 cabe num lote de 9 x 20 m.\n")
    bom = (f"A Casa Compacta tem {c['area']} m² fechados.\nA planta não dispensa o engenheiro.\nNunca: 'todas as casas cabem'; obra sem pedreiro.\n"
           f"C01: frente para o {c['frente']}.\nC01 cabe num lote de {c['lote'][0]:g} x {c['lote'][1]:g} m, e a prefeitura confirma o recuo.\n")
    linhas_ruins = sorted({i for i, t, _ in conferir_texto(ruim) if t == "erro"})
    if linhas_ruins != [1, 2, 3, 4, 5]:
        falhas.append(f"texto plantado: erros nas linhas {linhas_ruins}, esperado 1 a 5")
    if [x for x in conferir_texto(bom) if x[1] == "erro"]:
        falhas.append(f"texto limpo acusado: {conferir_texto(bom)}")
    tarde = datetime(2026, 11, 26, 6, 16, tzinfo=timezone.utc)
    if not any("hora" in m for _, _, m in conferir_texto("26/11 06:45 feito", tarde)) or conferir_texto("26/11 06:10 feito", tarde):
        falhas.append("hora futura não foi pega (ou a certa foi acusada)")
    if conferir_passe({"feito": ["x"], "suposicoes": [], "faltando": [], "arquivos": ["CLAUDE.md"], "perguntas_ao_dono": []}):
        falhas.append("passe certo foi recusado")
    if len(conferir_passe({"feito": [], "arquivos": ["nao-existe.md", "ebook/saida/x.pdf"]}, publico=True)) < 6:
        falhas.append("passe errado passou")
    cita = lambda k: {"arquivo": "CLAUDE.md", "linha": k}
    bom_j = {"motivo": "vai ao público", "regua": {"3": "a", "6": "b", "9": "c"}, "rodada": 1, "gasto": {"tokens_saida": 10},
             "jurados": [{"modelo": m, "angulo": a, "nota": 9, "defeitos": [cita(1), cita(2)]} for m, a in zip(("haiku", "sonnet", "opus"), ANGULOS)],
             "revisao_anonima": [{"ordem": [1, 2]}] * 3,
             "presidente": {"modelo": "fable", "fatos": [dict(cita(k), confirmado=True) for k in range(1, 6)]}}
    v = conferir_juri(bom_j)
    if not v["passa"]:
        falhas.append(f"rodada de júri certa recusada: {v['erros']}")
    ruim_j = json.loads(json.dumps(bom_j))
    ruim_j["jurados"][0]["defeitos"] = [{"arquivo": "CLAUDE.md", "linha": 99999}]
    ruim_j["presidente"]["modelo"] = "haiku"; ruim_j["presidente"]["fatos"] = ruim_j["presidente"]["fatos"][:3]
    ruim_j["regua"] = {}; ruim_j["gasto"] = {}; ruim_j["revisao_anonima"] = []
    if len(conferir_juri(ruim_j)["erros"]) < 7:
        falhas.append(f"rodada de júri incompleta passou: {conferir_juri(ruim_j)['erros']}")
    piso = json.loads(json.dumps(bom_j)); piso["jurados"][2]["nota"] = 6.5
    falso = json.loads(json.dumps(bom_j)); falso["presidente"]["fatos"][0].update(confirmado=False, de=1); falso["jurados"][1]["nota"] = 6
    baixo_falso = json.loads(json.dumps(bom_j)); baixo_falso["jurados"][0]["nota"] = 5
    baixo_falso["presidente"]["fatos"][0].update(confirmado=False, de=1)
    if conferir_juri(baixo_falso)["passa"] or conferir_juri(baixo_falso)["piso_ok"]:
        falhas.append("jurado de nota baixa que errou um fato abriu o piso")
    um_so = json.loads(json.dumps(bom_j))
    for k in (0, 1):
        um_so["presidente"]["fatos"][k].update(confirmado=False, de=k + 1)
    if conferir_juri(um_so)["passa"]:
        falhas.append("passou com uma nota válida só")
    if conferir_juri(piso)["passa"] or conferir_juri(falso)["notas"][0] is not None or conferir_juri(dict(piso, rodada=2))["proximo"] != "vai ao dono com as duas notas":
        falhas.append("piso 7, nota perdida por fato falso ou ida ao dono na 2ª rodada não funcionou")
    if not conferir_registro({}) or conferir_registro({"fluxo": "x", "peca": "y", "resultado": "z", "gasto": {"tokens_saida": 1},
                                                       "conferidores": [{"nome": "p", "tipo": "P", "achados_proprios": 0}]}):
        falhas.append("registro: forma não conferida")
    casos = [{"id": 1, "texto": "a", "problemas": [{"linha": 3, "categoria": "x", "porque": "y"}]}, {"id": 2, "texto": "b", "problemas": []}]
    n = prova_nota({"casos": casos, "respostas": {"a": [{"id": 1, "problemas": [{"linha": 4}]}], "b": [{"id": 2, "problemas": [{"linha": 1}]}]}},
                   gravar=False)
    todos_perdem = prova_nota({"casos": casos, "respostas": {"a": [], "b": []}}, gravar=False)
    if todos_perdem.get("_em_disputa") != ["1:3"] or not todos_perdem["a"]["passou"]:
        falhas.append(f"item que todos perderam não ficou em disputa: {todos_perdem}")
    if prova_nota({"casos": json.loads(json.dumps(casos)), "respostas": {"a": [], "b": []}, "confirmados": ["1:3"]}, gravar=False)["a"]["passou"]:
        falhas.append("item confirmado pelo árbitro não voltou a contar")
    if not n["a"]["passou"] or n["b"]["passou"] or n["b"]["alarmes_falsos"] != [2] or n["b"]["perdeu"][0]["caso"] != 1:
        falhas.append(f"nota da prova errada: {n}")
    falhas += _testar_colheita()
    return falhas


def _testar_colheita():
    """De ponta a ponta numa pasta temporária: lição nova grava, a repetida vai à prova, o arquivo cheio consolida sem perder nada."""
    import tempfile
    global RAIZ, FLUXOS, PROVAS
    velhos, falhas = (RAIZ, FLUXOS, PROVAS), []
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        RAIZ, FLUXOS, PROVAS = d, d / "pedidos" / "fluxos", d / "pedidos" / "provas"
        try:
            (d / "contexto").mkdir(parents=True)
            (d / "contexto" / "redator.md").write_text("# r\n\n## Lições\n\n" + "".join(f"- **2{k}/11:** lição antiga {k} {'x' * 300}\n" for k in range(15)), encoding="utf-8")
            antigas = (d / "contexto" / "redator.md").read_text(encoding="utf-8")
            rodada = {"fluxo": "texto-publico", "peca": "a.md", "resultado": "aprovado", "gasto": {"tokens_saida": 5},
                      "conferidores": [{"nome": "vera", "tipo": "A", "achados_proprios": 1}],
                      "achados": [{"autor": "redator", "chave": "Número sem fonte", "texto": "t", "licao": "número só do PLANTAS.md"},
                                  {"autor": "ninguem", "chave": "x", "texto": "t", "licao": "não grava"}]}
            import contextlib, io
            with contextlib.redirect_stdout(io.StringIO()):
                r1 = registrar(rodada)
                r2 = registrar(rodada)
            ctx = (d / "contexto" / "redator.md").read_text(encoding="utf-8")
            hist = (d / "pedidos" / "historico" / "licoes-redator.md")
            movidas = hist.read_text(encoding="utf-8") if hist.exists() else ""
            todas = all(l in ctx or l in movidas for l in antigas.splitlines() if l.startswith("- **"))
            if not (r1["gravado"] and len(r1["licoes_novas"]) == 1 and r2["voltaram"] and "número só do PLANTAS.md" in ctx
                    and len(ctx) <= 5000 and todas and "Lições antigas" in ctx and len(_json(PROVAS / "voltam.json", [])) == 1
                    and (FLUXOS / "RODADAS.md").read_text(encoding="utf-8").count("texto-publico") == 2
                    and len(list((FLUXOS / "rodadas").glob("*.json"))) >= 1):
                falhas.append(f"colheita de lições: {r1} {r2} tamanho {len(ctx)} todas {todas}")
            if registrar({"fluxo": "x"})["gravado"]:
                falhas.append("registro fora da forma foi gravado")
        finally:
            RAIZ, FLUXOS, PROVAS = velhos
    return falhas


def main(a):
    if not a:
        sys.exit(__doc__)
    cmd = a[0]
    if cmd == "texto" and len(a) >= 2:
        achados = conferir_texto(Path(a[1]).read_text(encoding="utf-8"))
        if "--json" in a:
            print(json.dumps([{"linha": i, "tipo": t, "msg": m} for i, t, m in achados], ensure_ascii=False))
        else:
            for i, t, m in achados:
                print(f"[{t.upper()}] linha {i}: {m}")
            print(f"{sum(t == 'erro' for _, t, _ in achados)} erro(s), {sum(t == 'aviso' for _, t, _ in achados)} aviso(s)")
        sys.exit(1 if any(t == "erro" for _, t, _ in achados) else 0)
    if cmd == "pagina" and len(a) >= 3:
        from pypdf import PdfReader
        txt = PdfReader(a[1]).pages[int(a[2]) - 1].extract_text() or ""
        achados = conferir_texto(txt)
        print(json.dumps({"texto": txt, "achados": [{"linha": i, "tipo": t, "msg": m} for i, t, m in achados]}, ensure_ascii=False)
              if "--json" in a else "\n".join(f"[{t.upper()}] linha {i}: {m}" for i, t, m in achados) or "nada achado")
        sys.exit(1 if any(t == "erro" for _, t, _ in achados) else 0)
    if cmd == "passe" and len(a) >= 2:
        erros = conferir_passe(_carrega(a[1]), "--publico" in a)
        print(json.dumps({"ok": not erros, "erros": erros}, ensure_ascii=False))
        sys.exit(1 if erros else 0)
    if cmd == "juri" and len(a) == 2:
        v = conferir_juri(_carrega(a[1]))
        print(json.dumps(v, ensure_ascii=False))
        sys.exit(0 if v["completa"] else 1)
    if cmd == "registrar" and len(a) == 2:
        v = registrar(_carrega(a[1]))
        print(json.dumps(v, ensure_ascii=False))
        sys.exit(0 if v["gravado"] else 1)
    if cmd == "relatorio":
        print(json.dumps(relatorio(), ensure_ascii=False, indent=1))
        return
    if cmd == "prova-estado":
        print(json.dumps(prova_estado(), ensure_ascii=False, indent=1))
        return
    if cmd == "prova-nota" and len(a) == 2:
        print(json.dumps(prova_nota(_carrega(a[1])), ensure_ascii=False, indent=1))
        return
    if cmd == "testar":
        f = testar()
        print("\n".join(f) if f else "fluxo.py: as conferências pegam os erros plantados e deixam os limpos")
        sys.exit(1 if f else 0)
    sys.exit(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
