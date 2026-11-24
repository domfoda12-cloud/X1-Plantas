"""Fichas dos pedidos do dono: criar, listar, fechar e conferir (regras em pedidos/LEIA-ME.md).

Uso: python3 ferramentas/pedido.py nova "assunto curto"   cria a ficha com o último prompt da caixa de entrada, palavra por palavra
     python3 ferramentas/pedido.py nova "assunto" --juntar 3   junta os 3 últimos prompts (recados seguidos sobre o mesmo pedido)
     python3 ferramentas/pedido.py recado <ficha>          acrescenta o último prompt da entrada como recado numa ficha aberta
     (nova e recado aceitam --de AAAA-MM-DD-HHMMSS para escolher o prompt pela hora; os dois mostram o que copiaram)
     python3 ferramentas/pedido.py listar [--fechadas]     mostra as fichas abertas (ou as fechadas)
     python3 ferramentas/pedido.py fechar <ficha> "o que virou"   fecha a ficha e escreve a linha no CONTEXTO-HISTORICO.md
         (ficha de 23/11/2026 em diante precisa do campo "O que aprendi": "papel: lição", uma por linha, ou "nada novo";
          cada lição vai ao "Lições" do contexto/<papel>.md e a pedidos/LICOES.md;
          recusa se o contexto/QUADRO.md não tiver o aviso da ficha (o código 2026-11-24-1144 dela) com as 3 partes: "pediu:", "mudou:"
          e o que muda para cada papel; e avisa se o contexto/<papel>.md de quem está em "Papéis afetados" não mudou desde que ela abriu)
     python3 ferramentas/pedido.py licao <papel> "lição" [--ficha X] [--ponto 1-5] [--origem dono|prova|auditoria|juri|maestro]
                                                           grava uma lição no contexto/<papel>.md e em pedidos/LICOES.md
     python3 ferramentas/pedido.py quadro                  tira do contexto/QUADRO.md o aviso mais antigo se passar de 5 ou do tamanho
     python3 ferramentas/pedido.py indice                  regenera pedidos/FILA.md
     python3 ferramentas/pedido.py conferir                falha se alguma ficha estiver sem campo obrigatório; avisa (sem falhar) da auditoria atrasada
     python3 ferramentas/pedido.py auditar                 lista as fichas fechadas que nenhuma auditoria leu (pedidos/AUDITORIAS.md)

A ficha é a fonte única do pedido: o histórico e a fila saem dela, para ninguém escrever a mesma coisa três vezes.
"""
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PEDIDOS, ENTRADA = RAIZ / "pedidos", RAIZ / "pedidos" / "entrada"
CAMPOS = ["Estado", "Prompt (palavra por palavra)", "O que ele pediu, parte por parte", "Por que ele pediu, ou o que quer descobrir",
          "Objetivo dele", "Ligação com as ideias gerais do projeto", "Perguntas que me fiz", "Pronto quando", "Suposições (o dono não disse)",
          "Quem executa", "Conferência", "Resultado"]
FECHADA = ["Conferência", "Resultado"]  # só precisam estar preenchidos em ficha fechada
VAZIO = "(a preencher)"
APRENDI = "O que aprendi"  # obrigatório só em ficha fechada de 23/11/2026 em diante (as antigas não quebram)
DESDE_APRENDI = "2026-11-23"
AFETADOS = "Papéis afetados"  # a pergunta do fechar (F31): nomes de contexto/<papel>.md, ou "ninguém"
ORIGENS = ("dono", "prova", "auditoria", "juri", "maestro", "ficha")
LIMITE_CONTEXTO = 5000  # o mesmo do checar.py (subiu de 3500 em 24/11/2026, com o sim do dono: cartão p21)


def fichas():
    return sorted(p for p in PEDIDOS.glob("20*/*.md"))


def campo(txt, nome):
    m = re.search(rf"^\*\*{re.escape(nome)}:\*\*[ \t]*(.*?)(?=^\*\*[^*\n]+:\*\*|^## |\Z)", txt, re.S | re.M)
    return m.group(1).strip() if m else None


def trocar(txt, nome, valor):
    return re.sub(rf"(^\*\*{re.escape(nome)}:\*\*)[ \t]*.*?(?=^\*\*[^*\n]+:\*\*|^## |\Z)", lambda m: f"{m.group(1)} {valor}\n\n", txt, flags=re.S | re.M)


DE = None


def ultimos_prompts(n=1):
    arqs = sorted(ENTRADA.glob("*.md")) if ENTRADA.exists() else []
    if DE:  # prompt escolhido pela hora (auditoria do Fable, 22/11: o último nem sempre é o do pedido)
        arqs = [a for a in arqs if a.stem.startswith(DE)][:1]
    else:
        arqs = arqs[-n:]
    if not arqs:
        sys.exit("A caixa de entrada (pedidos/entrada/) está vazia ou sem esse prompt: escreva o prompt na ficha à mão.")
    texto = "\n\n".join(re.sub(r"^<!--.*?-->\n", "", a.read_text(encoding="utf-8")).strip() for a in arqs)
    # mostra o que foi copiado: quem atende confere que é o prompt certo
    print(f"prompt copiado ({', '.join(a.stem for a in arqs)}): {texto[:120]}{'…' if len(texto) > 120 else ''}")
    return texto


def achar(nome):
    achadas = [f for f in fichas() if nome in f.name]
    if len(achadas) != 1:
        sys.exit(f"'{nome}' bate com {len(achadas)} fichas; use um pedaço do nome que só uma tenha. Abertas:\n" + "\n".join(listar(False)))
    return achadas[0]


def nova(assunto, juntar=1):
    agora = datetime.now()
    nome = re.sub(r"[^a-z0-9]+", "-", assunto.lower().translate(str.maketrans("áàâãéêíóôõúç", "aaaaeeiooouc"))).strip("-")[:60]
    arq = PEDIDOS / f"{agora:%Y-%m}" / f"{agora:%Y-%m-%d-%H%M}-{nome}.md"
    arq.parent.mkdir(parents=True, exist_ok=True)
    corpo = f"# {assunto}\n\n" + "".join(
        f"**{c}:** " + ("aberta" if c == "Estado" else ultimos_prompts(juntar) if c.startswith("Prompt") else VAZIO) + "\n\n" for c in CAMPOS)
    corpo += f"**{APRENDI}:** {VAZIO}\n\n**{AFETADOS}:** {VAZIO}\n\n"
    arq.write_text(corpo, encoding="utf-8")
    print(arq.relative_to(RAIZ))


def recado(nome):
    arq = achar(nome)
    txt = arq.read_text(encoding="utf-8")
    novo = f"{campo(txt, CAMPOS[1])}\n\n*Recado de {datetime.now():%d/%m %H:%M}:* {ultimos_prompts()}"
    arq.write_text(trocar(txt, CAMPOS[1], novo), encoding="utf-8")
    print("recado acrescentado em", arq.relative_to(RAIZ))


def listar(mostrar=True, estado="aberta"):
    linhas = [f"{f.relative_to(RAIZ)} · {f.read_text(encoding='utf-8').splitlines()[0][2:]}"
              for f in fichas() if (campo(f.read_text(encoding="utf-8"), "Estado") or "").startswith(estado)]
    if mostrar:
        print("\n".join(linhas) or f"nenhuma ficha {estado}")
    return linhas


def sem_auditoria():
    """Fichas fechadas que nenhuma auditoria leu. Conta ficha, não linha (as 3 de 22/11 escaparam pela conta de totais):
    vale como auditada a ficha cujo começo do nome (15 caracteres, 2026-11-22-2237) está numa linha de tabela de
    pedidos/AUDITORIAS.md ou na linha "Fichas cobertas por auditorias anteriores". Citar a ficha no texto corrido não conta."""
    arq = PEDIDOS / "AUDITORIAS.md"
    lidas = "\n".join(l for l in (arq.read_text(encoding="utf-8") if arq.exists() else "").splitlines()
                      if l.startswith(("|", "Fichas cobertas por auditorias")))
    return [f for f in fichas() if (campo(f.read_text(encoding="utf-8"), "Estado") or "").startswith("fechada") and f.name[:15] not in lidas]


def aviso_auditoria():
    """A frase do aviso quando há 3 ou mais fichas fechadas sem auditoria; senão, vazio."""
    faltam = sem_auditoria()
    if len(faltam) < 3:
        return ""
    return (f"HORA DA AUDITORIA: {len(faltam)} fichas fechadas sem auditoria ({', '.join(f.name[:15] for f in faltam)}). Chame o agente "
            "`supervisor` (Fable) com elas (`python3 ferramentas/pedido.py auditar`); a auditoria escreve o código de cada uma na tabela de pedidos/AUDITORIAS.md.")


def auditar():
    faltam = sem_auditoria()
    print("\n".join(str(f.relative_to(RAIZ)) for f in faltam) or "nenhuma ficha fechada sem auditoria")
    print(f"{len(faltam)} sem auditoria" + (" (com 3 ou mais é hora da auditoria)" if len(faltam) < 3 else ": HORA DA AUDITORIA"))


def quadro():
    """Deixa no quadro o bloco "Agora" e os 5 avisos mais novos, dentro de 3.500 caracteres (o mais antigo sai: já está no histórico)."""
    q = RAIZ / "contexto" / "QUADRO.md"
    t = q.read_text(encoding="utf-8")
    while True:
        avisos = [m.start() for m in re.finditer(r"^## \d", t, re.M)]
        if len(avisos) <= 1 or (len(avisos) <= 5 and len(t) <= 6000):
            break
        print("saiu do quadro (já está no histórico):", t[avisos[-1]:].split("\n", 1)[0])
        t = t[:avisos[-1]].rstrip() + "\n"
    q.write_text(t, encoding="utf-8")


def quando(arq):
    """Hora da última mudança do arquivo: a do último commit se ele está salvo e igual no git; senão, a do disco
    (numa conversa nova a hora do disco é a do clone, por isso o git vem primeiro)."""
    try:
        git = lambda *c: subprocess.run(["git", *c, "--", str(arq)], cwd=RAIZ, capture_output=True, text=True, timeout=30)
        estado = git("status", "--porcelain")
        if estado.returncode == 0 and not estado.stdout.strip():
            return int(git("log", "-1", "--format=%ct").stdout.strip())
    except (OSError, ValueError, subprocess.SubprocessError):
        pass  # sem git, fora do git ou arquivo sem commit: vale o disco
    return arq.stat().st_mtime


def falta_no_quadro(cod):
    """O que falta ao aviso da ficha no contexto/QUADRO.md; lista vazia = aviso com as 3 partes (F27, auditoria R2).
    O aviso é o bloco "## ..." que cita o código da ficha (em "## Agora", a linha que cita); as partes: "pediu:", "mudou:"
    e o que muda para cada papel ("muda para", "Todos:" ou o nome de um papel antes de dois-pontos)."""
    q = RAIZ / "contexto" / "QUADRO.md"
    blocos = []
    for s in re.split(r"^(?=## )", q.read_text(encoding="utf-8") if q.exists() else "", flags=re.M):
        blocos += s.splitlines() if s.startswith("## Agora") else [s]
    blocos = [b for b in blocos if cod in b]
    if not blocos:
        return [f"o aviso inteiro (nenhum bloco do quadro cita `{cod}`)"]
    papeis = "|".join(re.escape(p.stem).replace("\\-", "[ -]") for p in (RAIZ / "contexto").glob("*.md") if p.stem.islower())
    partes = [('o que o dono pediu ("pediu:")', r"pediu:"), ('o que mudou ("mudou:")', r"mudou:"),
              ('o que muda para cada papel ("muda para ...", "Todos:" ou o nome do papel e dois-pontos)', rf"muda para|\b(?:todos|{papeis})\b[^\n:]*:")]
    return min(([nome for nome, r in partes if not re.search(r, b, re.I)] for b in blocos), key=len)


def contextos_parados(arq, txt):
    """Os avisos do fechar sobre os papéis afetados (F31, auditoria R3): a pergunta, se a ficha não responde, e cada
    contexto/<papel>.md que não mudou desde que a ficha abriu (a hora está no nome dela). Avisa, não recusa."""
    v = (campo(txt, AFETADOS) or "").lower()
    papeis = [p for p in dict.fromkeys(re.findall(r"[a-z][a-z-]*", v)) if (RAIZ / "contexto" / f"{p}.md").is_file()]
    if not papeis and not re.search(r"ningu[eé]m|nenhum", v):
        return [f"[AVISO] Quais papéis este pedido afetou? Escreva na ficha \"**{AFETADOS}:** arquiteto, redator\" (nomes de contexto/<papel>.md) "
                "ou \"ninguém\", e atualize o contexto de cada um."]
    try:
        abriu = datetime.strptime(arq.name[:15], "%Y-%m-%d-%H%M")
    except ValueError:
        return []
    return [f"[AVISO] contexto/{p}.md não mudou desde que a ficha abriu ({abriu:%d/%m %H:%M}): o pedido afetou o `{p}`; escreva nele o que muda, "
            "senão ele trabalha com o contexto de antes do pedido." for p in papeis if quando(RAIZ / "contexto" / f"{p}.md") < abriu.timestamp()]


def aviso_ultimo_velho():
    """A frase do aviso se o contexto/entregas/ULTIMO.md for mais velho que a última ficha fechada; senão, vazio (F30, auditoria R5)."""
    ult = RAIZ / "contexto" / "entregas" / "ULTIMO.md"
    fechadas = [f for f in fichas() if (campo(f.read_text(encoding="utf-8"), "Estado") or "").startswith("fechada")]
    if not ult.exists() or not fechadas:
        return ""
    t, f = max((quando(f), f) for f in fechadas)
    if quando(ult) >= t:
        return ""
    return (f"[AVISO] o contexto/entregas/ULTIMO.md ({datetime.fromtimestamp(quando(ult)):%d/%m %H:%M}) é mais velho que a última ficha fechada "
            f"({f.name[:15]}, {datetime.fromtimestamp(t):%d/%m %H:%M}): escreva o resumo de passagem no REGISTRO.md e copie para o ULTIMO.md")


def licoes_do_campo(valor):
    """'papel: lição' por linha -> [(papel, lição)]; 'nada novo' -> []; formato errado -> None."""
    valor = (valor or "").strip()
    if re.fullmatch(r"nada novo\.?", valor, re.I):
        return []
    pares = [re.match(r"^(?:- )?`?([a-z][a-z-]*)`?:\s+(\S.*)$", l.strip()) for l in valor.splitlines() if l.strip()]
    return [(m.group(1), m.group(2).strip()) for m in pares] if pares and all(pares) else None


def inserir_licao(txt, linha):
    """Põe a linha no fim da seção '## Lições'; None se não houver a seção ou se passar do limite."""
    m = re.search(r"^## Lições[^\n]*\n", txt, re.M)
    if not m:
        return None
    prox = re.search(r"^## ", txt[m.end():], re.M)
    fim = m.end() + prox.start() if prox else len(txt)
    novo = txt[:fim].rstrip("\n") + "\n" + linha + "\n" + ("\n" + txt[fim:] if prox else "")
    return novo if len(novo) <= LIMITE_CONTEXTO else None


def _contexto(papel):
    arq = RAIZ / "contexto" / f"{papel}.md"
    if not re.fullmatch(r"[a-z][a-z-]*", papel) or not arq.is_file():
        sys.exit(f"papel '{papel}' não tem contexto/{papel}.md")
    return arq


def licao(papel, texto, ficha="-", ponto="-", origem="maestro", gravar=True, base=None):
    """Confere (e, com gravar, grava) a lição no contexto do papel e no registro único pedidos/LICOES.md.
    Sem gravar, devolve o contexto como ficaria; `base` é esse texto da lição anterior (duas lições do mesmo papel somam)."""
    arq = _contexto(papel)
    texto = re.sub(r"\s+", " ", texto).strip()
    origem = origem.replace("ú", "u")
    if not texto or origem not in ORIGENS or not re.fullmatch(r"-|[1-5]", ponto) or not re.fullmatch(r"-|[\w.-]+", ficha):
        sys.exit(f"Não grava: lição vazia, origem fora de {', '.join(ORIGENS)}, ponto fora de 1 a 5 ou ficha com caractere estranho.")
    hoje = datetime.now()
    marca = ", ".join(x for x in (f"{hoje:%d/%m}", "" if origem == "ficha" else origem, f"ficha {ficha}" if ficha != "-" else "", f"ponto {ponto}" if ponto != "-" else "") if x)
    atual = arq.read_text(encoding="utf-8") if base is None else base
    linha = f"- **{marca}:** {texto}"
    novo = inserir_licao(atual, linha)
    if novo is None and not re.search(r"^## Lições", atual, re.M):
        sys.exit(f"Não grava: contexto/{papel}.md não tem a seção '## Lições'.")
    if novo is None:
        sys.exit(f"Não grava: contexto/{papel}.md passaria de {LIMITE_CONTEXTO} caracteres (tem {len(atual)}; a lição pede {len(linha) + 1}). "
                 "Consolide: mova as lições mais antigas ao CONTEXTO-HISTORICO.md e tente de novo.")
    if not gravar:
        return novo
    arq.write_text(novo, encoding="utf-8")
    reg = PEDIDOS / "LICOES.md"
    if not reg.exists():
        reg.write_text("# Lições da equipe (registro único, só acréscimo)\n\n> Gravado por `python3 ferramentas/pedido.py licao` e pelo `fechar`. "
                       "Não edite à mão: a lição também está no \"Lições\" do `contexto/<papel>.md`.\n\n"
                       "| Data | Papel | Origem | Ficha | Ponto | Lição |\n|---|---|---|---|---|---|\n", encoding="utf-8")
    with open(reg, "a", encoding="utf-8") as h:
        h.write(f"| {hoje:%d/%m/%Y} | {papel} | {origem} | {ficha} | {ponto} | {texto.replace('|', '/')} |\n")
    print(f"lição gravada em contexto/{papel}.md e pedidos/LICOES.md")
    if RAIZ == Path(__file__).resolve().parent.parent:  # no repositório de verdade (não no teste), o placar acompanha
        subprocess.run([sys.executable, str(RAIZ / "ferramentas" / "placar.py")], cwd=RAIZ, capture_output=True)


def fechar(nome, virou):
    arq = achar(nome)
    txt = arq.read_text(encoding="utf-8")
    if not (campo(txt, "Estado") or "").startswith("aberta"):
        sys.exit("Não fecha: a ficha já está fechada (fechar de novo repetiria a linha do histórico e as lições).")
    faltam = [c for c in CAMPOS if (campo(txt, c) or VAZIO) == VAZIO and c not in ("Resultado",)]
    if faltam:
        sys.exit("Não fecha: falta preencher " + ", ".join(faltam))
    aprendidas = []
    if arq.name[:10] >= DESDE_APRENDI:
        aprendidas = licoes_do_campo(campo(txt, APRENDI))
        if aprendidas is None:
            sys.exit(f"Não fecha: o campo \"{APRENDI}\" falta ou está fora do formato. Escreva na ficha "
                     f"\"**{APRENDI}:** papel: lição\" (uma por linha, papel = nome do contexto/<papel>.md) ou \"nada novo\".")
        previa = {}
        for papel, t in aprendidas:  # confere todas, somadas por papel, antes de gravar qualquer uma
            previa[papel] = licao(papel, t, arq.name[:15], origem="ficha", gravar=False, base=previa.get(papel))
    sem = falta_no_quadro(arq.name[:15])
    if sem:
        sys.exit(f"Não fecha: falta no contexto/QUADRO.md o aviso desta ficha (`{arq.name[:15]}`) com as 3 partes. Falta: " + "; ".join(sem)
                 + ". Escreva no topo do quadro um bloco \"## data · assunto\" que cite a ficha, com \"**O dono pediu:**\", \"**O que mudou:**\" "
                 "e o que muda para cada papel (\"**Todos:**\", \"**Arquiteto:**\"...).")
    parados = contextos_parados(arq, txt)  # antes de gravar as lições: lição no contexto não conta como contexto atualizado
    hoje = datetime.now()
    txt = trocar(trocar(txt, "Estado", f"fechada em {hoje:%d/%m/%Y}"), "Resultado", virou)
    arq.write_text(txt, encoding="utf-8")
    for papel, t in aprendidas:
        licao(papel, t, arq.name[:15], origem="ficha")
    prompt = re.sub(r"\s+", " ", campo(txt, CAMPOS[1]))
    prompt = prompt if len(prompt) <= 260 else prompt[:260].rsplit(" ", 1)[0] + "…"
    with open(RAIZ / "CONTEXTO-HISTORICO.md", "a", encoding="utf-8") as h:
        h.write(f"| {hoje:%d/%m/%Y} | \"{prompt.replace('|', '/')}\" | {virou.replace('|', '/')} Ficha: `{arq.relative_to(RAIZ)}` |\n")
    indice()
    quadro()
    print("fechada; linha escrita no CONTEXTO-HISTORICO.md. O aviso do contexto/QUADRO.md foi conferido (3 partes); marque \"Feito\" em pedidos/PLANO.md.")
    print("\n".join(parados), end="\n" if parados else "")
    if aviso_auditoria():
        print(aviso_auditoria())


def indice():
    linhas = []
    for f in reversed(fichas()):
        t = f.read_text(encoding="utf-8")
        quem = re.sub(r"\s+", " ", campo(t, "Quem executa") or "")[:90]
        linhas.append(f"| {f.name[:10]} | [{t.splitlines()[0][2:]}]({f.relative_to(PEDIDOS).as_posix()}) | {campo(t, 'Estado')} | {quem} |")
    (PEDIDOS / "FILA.md").write_text(
        "# Fila de pedidos do dono\n\n> Gerada por `python3 ferramentas/pedido.py indice`. Não edite à mão. Como funciona: [`LEIA-ME.md`](LEIA-ME.md).\n\n"
        "| Data | Pedido | Estado | Quem executa |\n|---|---|---|---|\n" + "\n".join(linhas) + "\n", encoding="utf-8")


def conferir():
    erros = []
    for f in fichas():
        t = f.read_text(encoding="utf-8")
        aberta = (campo(t, "Estado") or "").startswith("aberta")
        for c in CAMPOS:
            v = campo(t, c)
            if v is None:
                erros.append(f"{f.name}: falta o campo '{c}'")
            elif v in ("", VAZIO) and not (aberta and c in FECHADA):
                erros.append(f"{f.name}: campo '{c}' vazio")
        if (campo(t, "Estado") or "").startswith("fechada") and f.name[:10] >= DESDE_APRENDI and licoes_do_campo(campo(t, APRENDI)) is None:
            erros.append(f"{f.name}: fechada sem '{APRENDI}' no formato 'papel: lição' ou 'nada novo'")
    print("\n".join("  " + e for e in erros))
    if aviso_auditoria():  # aviso, não erro: não trava o salvamento
        print("[AVISO] " + aviso_auditoria())
    return not erros


if __name__ == "__main__":
    a = sys.argv[1:]
    if "--de" in a:  # --de 2026-11-22-205428: usa esse prompt da entrada, não o último
        i = a.index("--de"); DE = a[i + 1]; del a[i:i + 2]
    cmd = a[0] if a else ""
    if cmd == "nova" and len(a) >= 2:
        nova(a[1], int(a[a.index("--juntar") + 1]) if "--juntar" in a else 1)
    elif cmd == "recado" and len(a) == 2:
        recado(a[1])
    elif cmd == "listar":
        listar(estado="fechada" if "--fechadas" in a else "aberta")
    elif cmd == "fechar" and len(a) == 3:
        fechar(a[1], a[2])
    elif cmd == "licao" and len(a) >= 3:
        if len(a) % 2 == 0 or any(k not in ("--ficha", "--ponto", "--origem") for k in a[3::2]):
            sys.exit(__doc__)
        op = {k: a[a.index(f"--{k}") + 1] for k in ("ficha", "ponto", "origem") if f"--{k}" in a}
        licao(a[1], a[2], op.get("ficha", "-"), op.get("ponto", "-"), op.get("origem", "maestro"))
    elif cmd == "quadro":
        quadro()
    elif cmd == "indice":
        indice()
    elif cmd == "auditar":
        auditar()
    elif cmd == "conferir":
        indice()
        sys.exit(0 if conferir() else 1)
    else:
        sys.exit(__doc__)
