"""Confere se o código do projeto tem erro, de uma vez só.

Uso: python3 ferramentas/checar.py
Confere: sintaxe de todo .py, .cjs e .js (fora de node_modules), as 24 plantas no validador,
a regra das paredes, o tamanho dos contextos, o índice e os resumos, o PDF do e-book (sem página
estourada, numa pasta temporária) e se toda skill e todo agente passaram pelo roteiro de entrada
(CONSELHO.md, seção 6).
Atenção: não só confere, também REGRAVA arquivos do repositório: os dados das plantas
(ebook/plantas/dados/*.json), as fichas (ebook/plantas/PLANTAS.md), a lista de conserto
(ebook/plantas/CONSERTOS.md), os módulos do motor 3D
(video/src/plantas/<ID>.js) e a seção "Situação agora" do PAINEL.md. Rode e confira o git diff.
A calculadora do parceiro e o PDF oficial só são gravados por `python3 ebook/gerador/livro.py` puro.
Sai com código 1 se algo falhar.
"""
import html
import json
import subprocess
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
falhas = []


def rodar(nome, cmd):
    r = subprocess.run(cmd, cwd=RAIZ, capture_output=True, text=True)
    ok = r.returncode == 0
    print(f"[{'OK ' if ok else 'ERRO'}] {nome}")
    if not ok:
        falhas.append(nome)
        print((r.stdout + r.stderr).strip()[-1500:])
    return r


ignorar = ("node_modules", ".git", "saida")
for f in sorted(RAIZ.rglob("*.py")):
    if any(p in f.parts for p in ignorar):
        continue
    try:
        compile(f.read_text(encoding="utf-8"), str(f), "exec")
    except SyntaxError as e:
        falhas.append(str(f.relative_to(RAIZ)))
        print(f"[ERRO] sintaxe {f.relative_to(RAIZ)}: linha {e.lineno}: {e.msg}")
print("[OK ] sintaxe dos .py" if not falhas else "")

for f in sorted(list(RAIZ.rglob("*.cjs")) + list((RAIZ / "video" / "src").rglob("*.js"))):
    if any(p in f.parts for p in ignorar):
        continue
    cmd = ["node", "--check", str(f)] if f.suffix == ".cjs" else ["node", "--experimental-default-type=module", "--check", str(f)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        falhas.append(str(f.relative_to(RAIZ)))
        print(f"[ERRO] sintaxe {f.relative_to(RAIZ)}: {r.stderr.strip()[-400:]}")
print("[OK ] sintaxe dos .cjs/.js")

# Skill e agente novo alcançam o projeto (CONSELHO.md, seção 6)
conselho = (RAIZ / "CONSELHO.md").read_text(encoding="utf-8")
ecossistema = (RAIZ / "ECOSSISTEMA.md").read_text(encoding="utf-8") if (RAIZ / "ECOSSISTEMA.md").exists() else ""
fora = []
for sk in sorted((RAIZ / ".claude" / "skills").glob("*/SKILL.md")):
    nome = sk.parent.name
    if "## Neste projeto" not in sk.read_text(encoding="utf-8"):
        fora.append(f"skill {nome}: falta a seção '## Neste projeto (X1-Plantas)' no SKILL.md")
    if "Prompt de entrada" not in sk.read_text(encoding="utf-8"):
        fora.append(f"skill {nome}: falta o 'Prompt de entrada' específico")
    if f"`{nome}`" not in conselho and f"/{nome}`" not in conselho:
        fora.append(f"skill {nome}: não está citada no CONSELHO.md")
    if f"`{nome}`" not in ecossistema:
        fora.append(f"skill {nome}: não está no inventário ECOSSISTEMA.md")
for ag in sorted((RAIZ / ".claude" / "agents").glob("*.md")):
    if f"`{ag.stem}`" not in conselho:
        fora.append(f"agente {ag.stem}: não está citado no CONSELHO.md")
    if f"`{ag.stem}`" not in ecossistema:
        fora.append(f"agente {ag.stem}: não está no inventário ECOSSISTEMA.md")
    if "Seu prompt de entrada" not in ag.read_text(encoding="utf-8"):
        fora.append(f"agente {ag.stem}: falta o 'Seu prompt de entrada'")
    if f"contexto/{ag.stem}.md" not in ag.read_text(encoding="utf-8"):
        fora.append(f"agente {ag.stem}: não manda ler o seu contexto/{ag.stem}.md")
    if not (RAIZ / "contexto" / f"{ag.stem}.md").exists():
        fora.append(f"agente {ag.stem}: falta o arquivo contexto/{ag.stem}.md")
    # Nome e conversa da equipe (dono, 26/11/2026: nome para cada agente e eles conversando como colegas)
    if "Seu nome é" not in ag.read_text(encoding="utf-8") or "contexto/CONVERSA.md" not in ag.read_text(encoding="utf-8"):
        fora.append(f"agente {ag.stem}: falta o nome ('Seu nome é') ou a leitura de contexto/CONVERSA.md")
# Orçamento de contexto: o que todo mundo lê não pode voltar a inchar (caracteres)
# Tetos subidos em 24/11/2026 com o "sim" do dono (cartão p21 do quadro: "Sobe os limites, como recomendado. Tente sempre
# deixar os arquivos o menor possível, claro com o mesmo resultado"). A auditoria das regras mostrou 9 de 26 arquivos no teto
# e avisos dele encurtados para caber. Passar do teto agora é AVISO, não erro: nada sai de um arquivo sem ir inteiro para
# outro que o mesmo papel lê. O CLAUDE.md não muda de teto (o dono não mandou mexer nele).
LIMITES = [("CLAUDE.md", 6500), ("CONTEXTO.md", 10000), ("ebook/CLAUDE.md", 2500), ("video/CLAUDE.md", 2500), ("ferramentas/CLAUDE.md", 2500)]
LIMITES += [(f"contexto/{p.name}", 6000 if p.name == "QUADRO.md" else 5000) for p in sorted((RAIZ / "contexto").glob("*.md")) if p.name != "RESUMO.md"]
LIMITES += [(f"contexto/entregas/{p.name}", 5000) for p in sorted((RAIZ / "contexto" / "entregas").glob("*.md")) if p.name != "REGISTRO.md"]
# Mapa do sistema: todo programa aparece no MAPA-DO-SISTEMA.md (é por ele que o Graphify vê como um alimenta o outro)
_mapa = (RAIZ / "MAPA-DO-SISTEMA.md").read_text(encoding="utf-8") if (RAIZ / "MAPA-DO-SISTEMA.md").exists() else ""
_progs = subprocess.run(["git", "ls-files", "*.py", "*.cjs", "video/src/*.js", "video/src/*.html"], cwd=RAIZ, capture_output=True, text=True).stdout.split()
fora += [f"programa fora do MAPA-DO-SISTEMA.md: {p}" for p in _progs if not p.startswith("video/src/plantas/") and f"({p})" not in _mapa]
if fora:
    falhas.append("roteiro de entrada de skills e agentes")
    print("[ERRO] roteiro de entrada de skills e agentes:\n  " + "\n  ".join(fora))
else:
    print("[OK ] skills e agentes passaram pelo roteiro de entrada")
grandes, compridos = [], []
for nome, limite in LIMITES:
    if not (RAIZ / nome).exists():
        grandes.append(f"{nome}: o arquivo não existe")
        continue
    n = len((RAIZ / nome).read_text(encoding="utf-8"))
    if n > limite:
        (grandes if nome == "CLAUDE.md" else compridos).append(f"{nome}: {n} caracteres, passa de {limite}. Enxugue sem perder conteúdo: o que sair vai inteiro para outro arquivo que o mesmo papel lê")
if not (RAIZ / "contexto" / "entregas" / "ULTIMO.md").exists():
    grandes.append("contexto/entregas/ULTIMO.md: falta o último resumo de passagem")
# Cada papel aponta no máximo 3 resumos (dono, 22/11/2026: ler pouco); o conserto vira conferência, para não voltar
for p in sorted((RAIZ / "contexto").glob("*.md")):
    n = p.read_text(encoding="utf-8").count("RESUMO.md)")
    if p.name not in ("RESUMO.md", "QUADRO.md", "EQUIPE.md") and n > 3:
        grandes.append(f"contexto/{p.name}: aponta {n} resumos; o máximo é 3")
if compridos:
    print("[AVISO] arquivo de contexto comprido (não trava; dono, 24/11: o menor possível com o mesmo resultado):\n  " + "\n  ".join(compridos))
if grandes:
    falhas.append("orçamento de contexto")
    print("[ERRO] orçamento de contexto:\n  " + "\n  ".join(grandes))
else:
    print("[OK ] orçamento de contexto")

# A regra das paredes tem teste: se alguém mexer no desconto, as áreas impressas mudam sem aviso
sys.path.insert(0, str(RAIZ / "ferramentas"))
import plantas as PL  # noqa: E402
_ps = {p["id"]: p for p in PL.carregar()}
_c = lambda pid, cid: next(c for c in _ps[pid]["comodos"] if c["id"] == cid)
_casos = [("sala da C05: 3,00 de eixo, parede externa de um lado e passagem aberta do outro", PL.util(_ps["C05"], _c("C05", "sala"))[0], 2.85),
          ("quarto casal da E04: 3,00 de eixo entre a divisa e o pátio, duas paredes externas", PL.util(_ps["E04"], _c("E04", "quarto1"))[0], 2.70),
          ("banheiro da S03: giro de 1,50 m", min(PL.util(_ps["S03"], _c("S03", "banho"))[:2]) >= 1.5, True)]
# Régua das 51 plantas de referência (aviso; dono, 23/11/2026): cada regra tem uma casa que falha e uma que passa
_tem = lambda pid, regra: any(x[0] == regra for x in _ps[pid]["_r"].referencias)
_e03 = __import__("copy").deepcopy(_ps["E02"])  # a E03 deixou de ter corredor lateral em 23/11/2026; a E02 ainda tem
_e03["recuos"] = {"esq": 0.9, "dir": 0.0}  # lote de 4,5 m de frente: o corredor lateral vira exceção dita
_r03 = PL.validar(_e03)
_casos += [("referência 1, circulação: C03 (9%) fora", _tem("C03", "1"), True), ("referência 1: C01 (4%) dentro", _tem("C01", "1"), False),
           ("referência 1: E02 em lote de 4,5 m vira exceção dita", (any(x[0] == "1" for x in _r03.referencias), any("exceção" in a for a in _r03.ref_info)), (False, True)),
           ("referência 2, banheiro: C04 (1,08) fora", _tem("C04", "2"), True), ("referência 2: S03 (1,50 de giro) dentro", _tem("S03", "2"), False),
           ("referência 3, quarto: E02 (2,30) fora", _tem("E02", "3"), True), ("referência 3: C07 (3,04) dentro", _tem("C07", "3"), False),
           ("referência 4, serviço: C04 (0,99, sem saída) fora", _tem("C04", "4"), True), ("referência 4: C03 (2,09, porta para fora) dentro", _tem("C03", "4"), False),
           ("referência 5a, por dentro: E02 (pelo corredor coberto) fora", _tem("E02", "5a"), True), ("referência 5a: C01 dentro", _tem("C01", "5a"), False),
           ("referência 5b, cozinha: C04 (1,74) fora", _tem("C04", "5b"), True), ("referência 5b: C01 (2,18) dentro", _tem("C01", "5b"), False),
           ("frente estreita: E03 sim, C01 não", (_ps["E03"]["_r"].metricas["frente_estreita"], _ps["C01"]["_r"].metricas["frente_estreita"]), (True, False))]
_ruins = [f"{n}: deu {v}, esperado {e}" for n, v, e in _casos if (abs(v - e) > 1e-6 if not isinstance(e, (bool, tuple)) else v != e)]
if _ruins:
    falhas.append("regra das paredes")
    print("[ERRO] regra das paredes:\n  " + "\n  ".join(_ruins))
else:
    print(f"[OK ] regra das paredes e régua das referências ({len(_casos)} casos)")

rodar("validador das plantas", [sys.executable, "ferramentas/plantas.py", "validar"])
rodar("dados das plantas (JSON)", [sys.executable, "ferramentas/plantas.py", "exportar"])
rodar("fichas (PLANTAS.md)", [sys.executable, "ferramentas/plantas.py", "fichas"])
rodar("lista de conserto (CONSERTOS.md)", [sys.executable, "ferramentas/plantas.py", "referencias"])
rodar("índice e resumos das pastas (nenhum documento fora)", [sys.executable, "ferramentas/resumos.py", "--conferir"])
_r_ped = rodar("fichas dos pedidos do dono (campos e fila)", [sys.executable, "ferramentas/pedido.py", "conferir"])
for _l in _r_ped.stdout.splitlines():  # ficha fechada sem auditoria (F21): aviso, não erro
    if _l.startswith("[AVISO]"):
        print(_l)
# O PDF não fala de preço (decisão do dono, 24/11/2026: "47, pdf não fala de preço"): o preço fica só no WhatsApp
import re as _re_preco
_citam = [f.name for f in sorted((RAIZ / "ebook" / "saida").glob("*.html")) if _re_preco.search(r"R\$\s?\d", f.read_text(encoding="utf-8"))]
if _citam:
    falhas.append("preço dentro do PDF")
    print(f"[ERRO] o PDF cita preço ({', '.join(_citam)}): o dono decidiu que o PDF não fala de preço")
else:
    print("[OK ] o PDF não cita preço (decisão do dono)")
rodar("plano geral (seções, dependências, no máximo 2 passos abertos em Agora)", [sys.executable, "ferramentas/plano.py", "conferir"])
# Todo link entre documentos abre (juntar ou renomear arquivo não pode quebrar nada em silêncio).
# Um conferidor só: o do painel (o mesmo que avisa no atualizar-painel.py).
import importlib.util
_esp = importlib.util.spec_from_file_location("painel", RAIZ / "ferramentas" / "atualizar-painel.py")
_painel = importlib.util.module_from_spec(_esp); _esp.loader.exec_module(_painel)
quebrados = _painel.conferir_links()
if quebrados:
    falhas.append("links entre documentos")
    print("[ERRO] links quebrados:\n  " + "\n  ".join(quebrados[:20]))
else:
    print("[OK ] links entre documentos")
# O dono usa um PC com Windows (23/11, tarefa A10): a suposição do Mac não volta. Registros ficam de fora.
_MAC = re.compile(r"Mac do dono|Mac dele")
_MAC_EXCECOES = ("CONTEXTO-HISTORICO.md", "contexto/CONVIVENCIA.md", "contexto/dono/", "pedidos/entrada/",
                 "pedidos/AUDITORIAS.md", "pedidos/LICOES.md", "pedidos/2026-11/", "pedidos/anexos/")
_mac = []
for f in sorted(RAIZ.rglob("*")):
    if f.suffix not in (".md", ".py", ".html") or any(p in f.parts for p in ignorar) or f == Path(__file__).resolve():
        continue
    rel = f.relative_to(RAIZ).as_posix()
    if rel.startswith(_MAC_EXCECOES):
        continue
    for n, linha in enumerate(f.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
        if _MAC.search(linha):
            _mac.append(f"{rel}:{n}")
if _mac:
    falhas.append("suposição do Mac do dono")
    print("[ERRO] o dono usa PC com Windows, não Mac:\n  " + "\n  ".join(_mac[:20]))
else:
    print("[OK ] nenhuma suposição de Mac do dono")
# Fechar ficha não pode apagar as seções depois do Resultado (auditoria 4: o plano da 2151 sumiu assim)
import importlib.util as _iu
_e = _iu.spec_from_file_location("pedido", RAIZ / "ferramentas" / "pedido.py"); _p = _iu.module_from_spec(_e); _e.loader.exec_module(_p)
_ficha = "**Estado:** aberta\n\n**Resultado:** (a preencher)\n\n## Plano\n\nnão some\n"
_fechada = _p.trocar(_ficha, "Resultado", "virou")
if "## Plano" in _fechada and "não some" in _fechada and _p.campo(_fechada, "Resultado") == "virou":
    print("[OK ] fechar ficha guarda as seções de depois")
else:
    falhas.append("fechar ficha apaga seções"); print("[ERRO] fechar ficha apaga as seções depois do Resultado")
# Lição ao fechar ficha (fila da noite, A2): vai ao fim do "Lições", recusa no limite, formato do campo "O que aprendi"
_ctx = "# x\n\n## Lições\n\n- antiga\n\n## Depois\n\nfica\n"
_ins = _p.inserir_licao(_ctx, "- nova")
_ok_licao = (_ins is not None and _ins.index("- nova") < _ins.index("## Depois") and "fica" in _ins
             and _p.inserir_licao(_ctx + "x" * _p.LIMITE_CONTEXTO, "- nova") is None and _p.inserir_licao("# sem seção\n", "- nova") is None
             and _p.licoes_do_campo("maestro: a\n`revisor-de-risco`: b") == [("maestro", "a"), ("revisor-de-risco", "b")]
             and _p.licoes_do_campo("nada novo") == [] and _p.licoes_do_campo("só texto solto") is None and _p.licoes_do_campo(None) is None)
if _ok_licao:
    print("[OK ] lição ao fechar ficha (lugar, limite, formato)")
else:
    falhas.append("lição ao fechar ficha"); print("[ERRO] lição ao fechar ficha: lugar, limite ou formato errado")
# De ponta a ponta, com fichas falsas numa pasta temporária (veto do Fable ao A2)
import contextlib, io, tempfile
with tempfile.TemporaryDirectory() as _d:
    _d = Path(_d); _raiz, _ped = _p.RAIZ, _p.PEDIDOS
    _p.RAIZ, _p.PEDIDOS = _d, _d / "pedidos"
    try:
        (_d / "contexto").mkdir(); (_d / "pedidos" / "2026-11").mkdir(parents=True)
        # o fechar exige o aviso da ficha no quadro com as 3 partes (F27): as fichas falsas de 0001 a 0005 têm, a 0006 não, a 0007 tem uma linha só
        (_d / "contexto" / "QUADRO.md").write_text("# Quadro\n\n## 23/11 · falsas\n\n- **O dono pediu:** x (fichas `2026-11-22-0001`, " + ", ".join(f"`2026-11-23-000{n}`" for n in range(1, 6))
                                                   + ")\n- **O que mudou:** y\n- **Todos:** z\n\n## 23/11 · curta\n\n- o pedido 2026-11-23-0007 virou uma linha só\n", encoding="utf-8")
        (_d / "contexto" / "maestro.md").write_text("# m\n\n## Lições\n\n- antiga\n", encoding="utf-8")
        (_d / "contexto" / "cheio.md").write_text("# c\n\n## Lições\n\n" + "x" * (_p.LIMITE_CONTEXTO - 60) + "\n", encoding="utf-8")
        _ler = lambda rel: (_d / rel).read_text(encoding="utf-8") if (_d / rel).exists() else ""
        def _falsa(nome, aprendi=None, estado="aberta"):
            t = "# falsa\n\n" + "".join(f"**{c}:** {estado if c == 'Estado' else 'ok'}\n\n" for c in _p.CAMPOS)
            (_d / "pedidos" / "2026-11" / f"{nome}.md").write_text(t + (f"**{_p.APRENDI}:** {aprendi}\n\n" if aprendi else "") + "## Plano\n\nfica\n", encoding="utf-8")
        def _roda(f, *a):
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    return f(*a) is not False
            except SystemExit as e:
                return e.code in (0, None)
        _aberta = lambda nome: "**Estado:** aberta" in _ler(f"pedidos/2026-11/{nome}.md")
        _meio = "y" * ((_p.LIMITE_CONTEXTO - len(_ler("contexto/maestro.md"))) // 2)  # duas cabem uma a uma, não juntas
        _falsa("2026-11-22-0001-antiga"); _falsa("2026-11-23-0001-sem"); _falsa("2026-11-23-0002-boa", "maestro: aprendi isto")
        _falsa("2026-11-23-0003-cheia", "maestro: não pode gravar\ncheio: não cabe"); _falsa("2026-11-23-0004-duas", f"maestro: a {_meio}\nmaestro: b {_meio}")
        _falsa("2026-11-23-0005-mista", "Nada novo para o redator.\nmaestro: não pode sumir")
        casos = [("ficha antiga fecha sem o campo", _roda(_p.fechar, "0001-antiga", "virou") and _roda(_p.conferir)),
                 ("ficha nova sem o campo não fecha", not _roda(_p.fechar, "0001-sem", "virou") and _aberta("2026-11-23-0001-sem")),
                 ("lição grava no contexto e no registro", _roda(_p.fechar, "0002-boa", "virou") and "aprendi isto" in _ler("contexto/maestro.md")
                  and _ler("pedidos/LICOES.md").count("aprendi isto") == 1 and "fica" in _ler("pedidos/2026-11/2026-11-23-0002-boa.md")),
                 ("recusa no limite sem gravar nada", not _roda(_p.fechar, "0003-cheia", "virou") and _aberta("2026-11-23-0003-cheia")
                  and "não pode gravar" not in _ler("contexto/maestro.md") + _ler("pedidos/LICOES.md")),
                 ("duas lições do mesmo papel somam", not _roda(_p.fechar, "0004-duas", "virou") and _aberta("2026-11-23-0004-duas")
                  and _meio not in _ler("contexto/maestro.md") + _ler("pedidos/LICOES.md")),
                 ("'nada' com lição junto não fecha", not _roda(_p.fechar, "0005-mista", "virou") and _aberta("2026-11-23-0005-mista")),
                 ("lição avulsa: origem e ponto conferidos", not _roda(_p.licao, "maestro", "x", "-", "9", "prova") and not _roda(_p.licao, "maestro", "x", "-", "-", "qualquer")
                  and not _roda(_p.licao, "maestro", "  ") and _roda(_p.licao, "maestro", "avulsa", "-", "3", "prova")),
                 ("fechar de novo não repete a lição", not _roda(_p.fechar, "0002-boa", "de novo") and _ler("pedidos/LICOES.md").count("aprendi isto") == 1)]
        _falsa("2026-11-23-0006-calada", "nada novo"); _falsa("2026-11-23-0007-curta", "nada novo")
        casos.append(("sem aviso de 3 partes no quadro não fecha", not _roda(_p.fechar, "0006-calada", "virou") and _aberta("2026-11-23-0006-calada")
                      and not _roda(_p.fechar, "0007-curta", "virou") and _aberta("2026-11-23-0007-curta")))
        _falsa("2026-11-23-0009-fechada-sem", estado="fechada em 23/11/2026")
        casos.append(("conferir acusa fechada nova sem o campo", not _roda(_p.conferir)))
    finally:
        _p.RAIZ, _p.PEDIDOS = _raiz, _ped
_ruins = [n for n, ok in casos if not ok]
if _ruins:
    falhas.append("lição ao fechar ficha, de ponta a ponta"); print("[ERRO] lição ao fechar ficha, de ponta a ponta: " + "; ".join(_ruins))
else:
    print(f"[OK ] lição ao fechar ficha, de ponta a ponta ({len(casos)} casos com fichas falsas)")
rodar("máscara da busca nas conversas (dados pessoais e chaves)", [sys.executable, "ferramentas/conversas.py", "testar"])
rodar("caderno de pesquisa (formato e fonte)", [sys.executable, "ferramentas/pesquisa.py", "conferir"])
rodar("placar do veto em dia", [sys.executable, "ferramentas/placar.py", "--conferir"])
rodar("módulos do motor 3D", [sys.executable, "ferramentas/planta3d.py"])
# 3D e e-book: mesma área por cômodo (F7, 24/11/2026: o desenho azul mostrava a área de eixo a eixo, 14,1 m² na sala da C01,
# e o e-book a área livre, 12,5). O módulo de cada casa tem de trazer a área livre do validador, no formato do e-book (0,0).
_m1 = lambda v: f"{v:.1f}".replace(".", ",")
_area3d = []
for pl in PL.carregar():
    _js = (RAIZ / "video" / "src" / "plantas" / f"{pl['id']}.js").read_text(encoding="utf-8")
    _amb = {a["id"]: a.get("area_livre") for a in json.loads(re.search(r"export const ambientes = (\[.*?\]);\n", _js).group(1))}
    for _cid, (_, _, _a) in pl["_r"].metricas["util"].items():
        if _cid in _amb and (_amb[_cid] is None or _m1(_amb[_cid]) != _m1(_a)):
            _area3d.append(f"{pl['id']} {_cid}: 3D {_amb[_cid]}, e-book {_m1(_a)}")
if _area3d:
    falhas.append("3D e e-book com área diferente"); print("[ERRO] 3D e e-book: área diferente por cômodo: " + "; ".join(_area3d[:12]))
else:
    print("[OK ] 3D e e-book: mesma área por cômodo (área livre do validador no desenho azul)")
# Móvel sobre móvel (máquina sobre o tanque, vaso dentro do box), achado do Designer em 23/11/2026
import planta3d as _p3  # noqa: E402
_sob = [f"{pl['id']} {amb}: {a} sobre {b}" for pl in _p3.PL.carregar() for (amb, a, b) in _p3.sobrepostos(_p3.construir(pl)[3])]
if _sob:
    falhas.append("móvel sobre móvel"); print("[ERRO] móvel sobre móvel: " + "; ".join(_sob[:12]))
else:
    print("[OK ] nenhum móvel sobre outro nas plantas mobiliadas")
# Móvel na parede, cadeira em cima da cama e quarto sem parede (achados do dono no 3D, 23/11/2026): erro, não aviso
_par = [f"{pl['id']} {amb}: {tipo} entra {cm} cm na parede {qual}" for pl in _p3.PL.carregar() for (amb, tipo, qual, cm) in _p3.moveis_na_parede(pl)]
_ext = [x for x in _par if "externa" in x]
if _par:
    falhas.append("móvel atravessando parede" + (" externa" if _ext else "")); print("[ERRO] móvel atravessando parede: " + "; ".join(_par[:12]))
else:
    print("[OK ] nenhum móvel atravessa parede (externa ou interna) no 3D")
_cad = [f"{pl['id']} {amb}: cadeira em cima de {tipo}" for pl in _p3.PL.carregar() for (amb, tipo) in _p3.cadeiras_sem_lugar(pl)]
if _cad:
    falhas.append("cadeira sobre cama ou outro móvel"); print("[ERRO] cadeira sobre cama ou outro móvel: " + "; ".join(_cad[:12]))
else:
    print("[OK ] nenhuma cadeira de escrivaninha em cima de cama ou de outro móvel")
# Cadeira da escrivaninha posta à mão encostando no armário (F01, quarto 3, 23/11/2026): a zona de puxar fica livre
_zona = [f"{pl['id']} {m['amb']}: {o['tipo']} na zona da cadeira" for pl in _p3.PL.carregar() for mv in [_p3.construir(pl)[3]]
         for m in mv if m["tipo"] == "escrivaninha" for o in mv
         if o["amb"] == m["amb"] and o["tipo"] not in _p3.NAO_COLIDE + ("escrivaninha", "cadeira") and _p3.sobrepoe(_p3.pegada(o), _p3.zona_da_cadeira(m), -0.005)]
if _zona:
    falhas.append("cadeira sem os 0,75 m de puxar"); print("[ERRO] cadeira sem os 0,75 m de puxar: " + "; ".join(_zona))
else:
    print("[OK ] toda escrivaninha com 0,60 x 0,75 m livres para a cadeira")
# Geladeira na frente da janela (C01) e cadeira de 38 cm na divisa (E03), achados ao mobiliar as 3 casas, 24/11/2026
def moveis_ruins(plantas):
    """Móvel alto na frente de janela e cadeira de jantar a menos de 45 cm da parede, nas plantas dadas."""
    return ([f"{pl['id']} {amb}: {tipo} na frente da janela ({cm} cm)" for pl in plantas for (amb, tipo, cm) in _p3.altos_na_janela(pl)]
            + [f"{pl['id']} {amb}: cadeira de jantar com {cm} cm até a parede (mínimo {round(100 * _p3.CADEIRA_PAREDE)})"
               for pl in plantas for (amb, cm) in _p3.cadeiras_apertadas(pl)])


_mr = moveis_ruins(_p3.PL.carregar())
# prova de que a conferência pega o erro: E03 com a mesa de volta na divisa e C01 com a geladeira na frente da janela
_prova = {p["id"]: p for p in _p3.PL.carregar() if p["id"] in ("C01", "E03")}
for _c in _prova["E03"]["comodos"]:
    if _c["id"] == "cozinha":
        _c["moveis"] = [dict(m, x=0.925) if m["tipo"] == "mesaJantar" else m for m in _c["moveis"]]
for _c in _prova["C01"]["comodos"]:
    if _c["id"] == "cozinha":
        _c["moveis"] = [dict(m, x=1.075, y=2.675, rot=3.14159) if m["tipo"] == "geladeira" else m for m in _c["moveis"]]
_pegou = moveis_ruins(_prova.values())
if _mr or len(_pegou) != 2:
    falhas.append("móvel alto na janela ou cadeira apertada")
    print("[ERRO] móvel alto na frente de janela ou cadeira de jantar apertada: " + ("; ".join(_mr) if _mr else f"a prova não pegou os 2 erros postos de propósito ({_pegou})"))
else:
    print("[OK ] nenhum móvel alto na frente de janela e toda cadeira de jantar com 45 cm até a parede (prova: pegou os 2 erros postos de propósito)")
# Guarda-roupa sem 60 cm na frente e porta que bate em tanque, pia, vaso, bancada, box ou máquina (C01: a cama a 10 cm das
# portas do guarda-roupa e a folha da cozinha no tanque), achados do levantamento das 3 casas, 24/11/2026
def frente_e_folha(plantas):
    """Guarda-roupa com menos de 60 cm livres na frente e porta que bate em móvel fixo ao abrir, nas plantas dadas."""
    return ([f"{pl['id']} {amb}: guarda-roupa com {cm} cm livres na frente (mínimo {round(100 * _p3.FRENTE_ARMARIO)})"
             for pl in plantas for (amb, cm) in _p3.armarios_sem_frente(pl)]
            + [f"{pl['id']} {amb}: a porta {porta} bate no {tipo} ({cm} cm)" for pl in plantas for (amb, porta, tipo, cm) in _p3.portas_em_fixos(pl)])


_ff = frente_e_folha(_p3.PL.carregar())
# prova: na C01, a cama de volta a 10 cm da frente do guarda-roupa e o tanque de volta no canto da porta da cozinha
_prova = {p["id"]: p for p in _p3.PL.carregar() if p["id"] == "C01"}
for _c in _prova["C01"]["comodos"]:
    if _c["id"] == "quarto2":
        _c["moveis"] = [dict(m, y=2.4) if m["tipo"] == "armario" else m for m in _c["moveis"]]
    if _c["id"] == "servico":
        _c["moveis"] = [dict(m, y=0.42) if m["tipo"] == "tanque" else m for m in _c["moveis"]]
_pegou = frente_e_folha(_prova.values())
if _ff or len(_pegou) != 2 or not all(any(k in x for x in _pegou) for k in ("guarda-roupa", "tanque")):
    falhas.append("guarda-roupa sem frente ou porta batendo em móvel fixo")
    print("[ERRO] guarda-roupa sem 60 cm na frente ou porta que bate em móvel fixo: "
          + ("; ".join(_ff) if _ff else f"a prova não pegou os 2 erros postos de propósito ({_pegou})"))
else:
    print("[OK ] todo guarda-roupa com 60 cm livres na frente e nenhuma porta bate em tanque, pia, vaso, bancada, box ou máquina"
          " (prova: pegou os 2 erros postos de propósito)")
# Prévia mais velha que os dados da casa (motor mudou porta, móveis e 3D em 23/11 e as prévias ficaram de 20 a 22/11)
import imagens2d as _i2  # noqa: E402
_carimbos = json.loads(_i2.CARIMBOS.read_text(encoding="utf-8")) if _i2.CARIMBOS.exists() else {}
_velhas = [i for i in (p["id"] for p in PL.carregar())
           if not (_i2.PREVIAS / f"{i}.png").exists() or _carimbos.get(i) != _i2.carimbo(i)]
if _velhas:
    falhas.append("prévia velha"); print(f"[ERRO] prévia mais velha que os dados da casa ({', '.join(_velhas)}): python3 ferramentas/imagens2d.py --previas {' '.join(_velhas)}")
else:
    print("[OK ] as prévias batem com os dados das casas (carimbo em ebook/plantas/previas/carimbos.json)")
_quartos = []
for pl in _p3.PL.carregar():
    _tipo = {c["id"]: c["tipo"] for c in pl["comodos"]}
    _nome = {c["id"]: c["nome"] for c in pl["comodos"]}
    for pt in pl.get("portas", []):
        if len(pt) > 2 and pt[2] == "aberto" and "ext" not in pt[:2]:
            a, b = pt[0], pt[1]
            for q, o in ((a, b), (b, a)):
                if _tipo[q] in ("dorm", "casal") and (_tipo[o] in _p3.PL.EXTERNOS | _p3.PL.SEMIEXTERNOS or "gourmet" in _nome[o].lower()):
                    _quartos.append(f"{pl['id']} {_nome[q]} aberto para {_nome[o]}")
if _quartos:
    falhas.append("quarto aberto para área externa ou gourmet"); print("[ERRO] quarto sem parede para área externa ou gourmet: " + "; ".join(_quartos))
else:
    print("[OK ] nenhum quarto aberto para área externa ou gourmet")
# Janela em cima da porta (achado do Arquiteto, 23/11/2026): aviso até as casas de fora do lançamento serem refeitas
_jp = [f"{pl['id']} {jan} sobre a porta {porta}" for pl in _p3.PL.carregar() for (porta, jan) in _p3.janelas_sobre_portas(pl)]
if _jp:
    print(f"[AVISO] janela em cima de porta ({len(_jp)}): " + "; ".join(_jp))
rodar("e-book, plantas grátis e calculadora (sem página estourada)", [sys.executable, "ebook/gerador/livro.py", "--conferir"])
# Edição de lançamento (dono, 23/11/2026: 3 casas): a calculadora e as plantas grátis só com casas da edição
# ("casas_lancamento" no config.json; vazia = todas). As 24 plantas continuam no validador, acima.
_cfg_ed = json.loads((RAIZ / "ebook" / "config.json").read_text(encoding="utf-8"))
_todas = [p["id"] for p in PL.carregar()]
_ed = _cfg_ed.get("casas_lancamento") or _todas
_grat = _cfg_ed.get("plantas_gratis") or [_cfg_ed.get("planta_gratis", "C01")]
_calc = re.search(r"const CASAS = (\[.*?\]);", (RAIZ / "ebook" / "vendas" / "calculadora-lote.html").read_text(encoding="utf-8"), re.S)
_calc = json.loads(_calc.group(1)) if _calc else []
_pags = [c.get("pag") for c in _calc]
_ed_erros = ([f"casa da edição que não existe: {i}" for i in _ed if i not in _todas]
             + ([f"calculadora com {sorted(c['id'] for c in _calc)}, edição {sorted(_ed)}"] if sorted(c["id"] for c in _calc) != sorted(_ed) else [])
             + (["página da calculadora fora de ordem ou sem número"] if not all(isinstance(n, int) and n > 0 for n in _pags) or _pags != sorted(set(_pags)) else [])
             + [f"planta grátis fora da edição: {i}" for i in _grat if i not in _ed]
             + [f"PDF grátis velho em ebook/saida: {a.name}" for a in sorted((RAIZ / "ebook" / "saida").glob("planta-gratis-*.pdf")) if a.stem.removeprefix("planta-gratis-") not in _grat])
if _ed_erros:
    falhas.append("edição de lançamento"); print("[ERRO] edição de lançamento: " + "; ".join(_ed_erros))
else:
    print(f"[OK ] edição de lançamento: {len(_ed)} casas na calculadora e no PDF, plantas grátis {', '.join(_grat)}")
# Recuos da página "Qual casa cabe no seu lote?" (conserto de 24/11/2026): o texto mostra UM conjunto de recuos
# (frente e fundos da primeira casa, a primeira lateral de cada tipo). Se as casas da edição tiverem recuos de
# referência diferentes entre si, o texto esconde o de alguma casa: falha até o texto do livro.py mostrar todos.
def recuos_escondidos(plantas_ed, mostrado):
    """Recuos de referência de casa da edição que o texto da página do lote não mostra.
    mostrado = o que livro.recuos_da_edicao devolve: (frente, fundos, lateral ou None, frases extras)."""
    v = lambda x: f"{x:g}".replace(".", ",")
    rf, rfu, rlat, rext = mostrado
    laterais = (f"{rlat} m " if rlat else "") + (rext or "")
    falta = []
    for p in plantas_ed:
        rec = p["_r"].metricas["recuos"]
        if v(rec["frente"]) != rf:
            falta.append(f"{p['id']} frente {v(rec['frente'])} m (o texto diz {rf} m)")
        if v(rec["fundos"]) != rfu:
            falta.append(f"{p['id']} fundos {v(rec['fundos'])} m (o texto diz {rfu} m)")
        falta += [f"{p['id']} lateral {v(x)} m (não aparece no texto)" for x in sorted({rec["esq"], rec["dir"]}) if x and f"{v(x)} m " not in laterais]
    return falta


sys.path.insert(0, str(RAIZ / "ebook" / "gerador"))
import livro as _livro  # noqa: E402
_pl_ed = [p for p in PL.carregar() if p["id"] in _ed]
_rec_esc = recuos_escondidos(_pl_ed, _livro.recuos_da_edicao(_pl_ed)) if _pl_ed else []
if _rec_esc:
    falhas.append("recuos da página do lote"); print('[ERRO] "Qual casa cabe no seu lote?" mostra um conjunto só de recuos, mas as casas da edição têm recuos diferentes: ' + "; ".join(_rec_esc))
else:
    print(f"[OK ] recuos da página do lote: as {len(_pl_ed)} casas da edição têm os recuos que o texto mostra")
# Porta de entrada amarela (Designer, 24/11/2026): "Como ler uma planta" diz "a porta de entrada é amarela". Em cada
# casa e em cada desenho (revista, maquete e a planta simples com móveis) há UMA porta marcada data-porta="entrada";
# nas humanizadas, também uma seta ENTRADA. As outras portas para fora têm a soleira cinza (data-porta="fora").
def portas_de_entrada_erradas(desenhos):
    """desenhos: [(nome, svg, quer_seta)]. Devolve o que não tem exatamente uma porta de entrada (e uma seta)."""
    ruins = []
    for nome, svg, quer_seta in desenhos:
        n, s = svg.count('data-porta="entrada"'), svg.count('data-seta="entrada"')
        if n != 1 or (quer_seta and s != 1):
            ruins.append(f"{nome}: {n} porta(s) de entrada marcada(s)" + (f", {s} seta(s) ENTRADA" if quer_seta else ""))
    return ruins


_desenhos = [(f"{p['id']} {est}", _livro.svg_humanizada(p, est), True) for p in PL.carregar() for est in ("revista", "maquete")]
_desenhos += [(f"{p['id']} simples", _livro.svg_planta(p, moveis=True), False) for p in PL.carregar()]
_ent = portas_de_entrada_erradas(_desenhos)
_prova = portas_de_entrada_erradas([("prova", _desenhos[0][1].replace('data-porta="entrada"', 'data-porta="fora"'), True),
                                    ("prova2", _desenhos[0][1] * 2, True)])
if _ent or len(_prova) != 2:
    falhas.append("porta de entrada amarela")
    print("[ERRO] casa sem exatamente uma porta de entrada marcada: " + ("; ".join(_ent[:12]) if _ent else f"a prova não pegou os 2 erros ({_prova})"))
else:
    print(f"[OK ] uma porta de entrada amarela por casa ({len(_desenhos)} desenhos; prova: pegou os 2 erros postos de propósito)")
# Bônus sem conteúdo (achado do Revisor, 24/11/2026; CDC, arts. 30 e 37): o "O que vem junto" do PDF só pode listar
# bônus que tenha página no PDF (data-bonus="<nome>"; o livro.py registra em PAGINAS_BONUS).
def bonus_sem_conteudo(paginas):
    """paginas: o HTML de cada página do e-book. Devolve os bônus listados em "O que vem junto" sem página própria."""
    doc = "".join(paginas)
    bloco = re.search(r"<h3>O que vem junto</h3>(.*?)(?:<h3>|</div>)", doc, re.S)
    itens = [html.unescape(i) for i in re.findall(r"<li>(.*?)</li>", bloco.group(1), re.S)] if bloco else []
    return [i for i in itens if f'data-bonus="{html.escape(i)}"' not in doc]


_pl_livro = _livro.edicao(sorted(PL.carregar(), key=lambda p: ("CEFS".index(p["id"][0]), p["id"])), _cfg_ed)
_paginas = _livro.montar(_pl_livro, _cfg_ed, {"lote": 3, **{p["id"]: 0 for p in _pl_livro}}).paginas
_bsc = bonus_sem_conteudo(_paginas)
_prova_b = bonus_sem_conteudo(['<h3>O que vem junto</h3><ul class="lista"><li>Prova</li><li>Tem</li></ul></div>',
                               '<section class="pagina" data-bonus="Tem"></section>'])
if _bsc or _prova_b != ["Prova"]:
    falhas.append("bônus sem conteúdo no PDF")
    print("[ERRO] o PDF anuncia bônus sem página: " + ("; ".join(_bsc) if _bsc else f"a prova não pegou o erro ({_prova_b})"))
else:
    _anun = _livro.bonus_com_conteudo(_cfg_ed)
    print(f"[OK ] bônus do PDF: {len(_anun)} anunciado(s), todos com página (prova: pegou o bônus sem página posto de propósito)")
rodar("painel",[sys.executable, "ferramentas/atualizar-painel.py"])

# Campo do dono ainda vazio: não é erro de código, mas o PDF não pode ir ao cliente assim (auditoria de 22/11)
_cfg = json.loads((RAIZ / "ebook" / "config.json").read_text(encoding="utf-8"))
_pend = [k for k, v in _cfg.items() if (isinstance(v, str) and v.startswith("[")) or (isinstance(v, list) and any(str(x).startswith("[") for x in v))]
if _pend:
    print(f"[AVISO] o PDF sai com campo pendente ({', '.join(_pend)}): rascunho, não mande ao cliente até o dono decidir")


# O resumo geral não pode envelhecer sem ninguém ver (F8, auditoria de 24/11, R4): compara o último commit de cada arquivo
def aviso_contexto_velho(t_contexto, t_decisoes, limite_h=6):
    """A frase do aviso se o CONTEXTO.md for mais de `limite_h` horas mais velho que as decisões do dono; senão, vazio."""
    horas = (t_decisoes - t_contexto) / 3600
    return f"[AVISO] o CONTEXTO.md está mais velho que as decisões do dono ({horas:.0f} horas): atualize o 'Em aberto'" if horas > limite_h else ""


def _ultimo_commit(arq):
    try:
        return int(subprocess.run(["git", "log", "-1", "--format=%ct", "--", str(arq)], cwd=RAIZ, capture_output=True, text=True, timeout=30).stdout.strip())
    except (OSError, ValueError, subprocess.SubprocessError):
        return None  # git não respondeu ou arquivo sem commit: não avisa nem quebra


_dec = sorted((RAIZ / "pedidos" / "anexos").glob("decisoes-do-dono-*.md"))
_tc, _td = _ultimo_commit(RAIZ / "CONTEXTO.md"), _ultimo_commit(_dec[-1]) if _dec else None
if _tc and _td and aviso_contexto_velho(_tc, _td):
    print(aviso_contexto_velho(_tc, _td))
if _p.aviso_ultimo_velho():  # o resumo de passagem também envelhece (F30, auditoria R5): aviso, não erro
    print(_p.aviso_ultimo_velho())
print(f"\n{'Tudo certo.' if not falhas else str(len(falhas)) + ' problema(s): ' + ', '.join(falhas)}")
sys.exit(1 if falhas else 0)
