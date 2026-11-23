"""Confere se o código do projeto tem erro, de uma vez só.

Uso: python3 ferramentas/checar.py
Confere: sintaxe de todo .py, .cjs e .js (fora de node_modules), as 24 plantas no validador,
a regra das paredes, o tamanho dos contextos, o índice e os resumos, o PDF do e-book (sem página
estourada, numa pasta temporária) e se toda skill e todo agente passaram pelo roteiro de entrada
(CONSELHO.md, seção 6).
Atenção: não só confere, também REGRAVA arquivos do repositório: os dados das plantas
(ebook/plantas/dados/*.json), as fichas (ebook/plantas/PLANTAS.md), os módulos do motor 3D
(video/src/plantas/<ID>.js), a lista de casas da calculadora do parceiro
(ebook/vendas/calculadora-lote.html) e a seção "Situação agora" do PAINEL.md. Rode e confira o git diff.
Sai com código 1 se algo falhar.
"""
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
# Orçamento de contexto: o que todo mundo lê não pode voltar a inchar (caracteres)
LIMITES = [("CLAUDE.md", 6500), ("CONTEXTO.md", 8000), ("ebook/CLAUDE.md", 2500), ("video/CLAUDE.md", 2500), ("ferramentas/CLAUDE.md", 2500)]
LIMITES += [(f"contexto/{p.name}", 3500) for p in sorted((RAIZ / "contexto").glob("*.md")) if p.name != "RESUMO.md"]
LIMITES += [(f"contexto/entregas/{p.name}", 3500) for p in sorted((RAIZ / "contexto" / "entregas").glob("*.md")) if p.name != "REGISTRO.md"]
# Mapa do sistema: todo programa aparece no MAPA-DO-SISTEMA.md (é por ele que o Graphify vê como um alimenta o outro)
_mapa = (RAIZ / "MAPA-DO-SISTEMA.md").read_text(encoding="utf-8") if (RAIZ / "MAPA-DO-SISTEMA.md").exists() else ""
_progs = subprocess.run(["git", "ls-files", "*.py", "*.cjs", "video/src/*.js", "video/src/*.html"], cwd=RAIZ, capture_output=True, text=True).stdout.split()
fora += [f"programa fora do MAPA-DO-SISTEMA.md: {p}" for p in _progs if not p.startswith("video/src/plantas/") and f"({p})" not in _mapa]
if fora:
    falhas.append("roteiro de entrada de skills e agentes")
    print("[ERRO] roteiro de entrada de skills e agentes:\n  " + "\n  ".join(fora))
else:
    print("[OK ] skills e agentes passaram pelo roteiro de entrada")
grandes = []
for nome, limite in LIMITES:
    if not (RAIZ / nome).exists():
        grandes.append(f"{nome}: o arquivo não existe")
        continue
    n = len((RAIZ / nome).read_text(encoding="utf-8"))
    if n > limite:
        grandes.append(f"{nome}: {n} caracteres, passa do limite de {limite}. Mova o excesso para CONTEXTO-HISTORICO.md ou divida")
if not (RAIZ / "contexto" / "entregas" / "ULTIMO.md").exists():
    grandes.append("contexto/entregas/ULTIMO.md: falta o último resumo de passagem")
# Cada papel aponta no máximo 3 resumos (dono, 22/11/2026: ler pouco); o conserto vira conferência, para não voltar
for p in sorted((RAIZ / "contexto").glob("*.md")):
    n = p.read_text(encoding="utf-8").count("RESUMO.md)")
    if p.name not in ("RESUMO.md", "QUADRO.md", "EQUIPE.md") and n > 3:
        grandes.append(f"contexto/{p.name}: aponta {n} resumos; o máximo é 3")
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
_ruins = [f"{n}: deu {v}, esperado {e}" for n, v, e in _casos if (abs(v - e) > 1e-6 if not isinstance(e, bool) else v != e)]
if _ruins:
    falhas.append("regra das paredes")
    print("[ERRO] regra das paredes:\n  " + "\n  ".join(_ruins))
else:
    print("[OK ] regra das paredes (3 casos)")

rodar("validador das plantas", [sys.executable, "ferramentas/plantas.py", "validar"])
rodar("dados das plantas (JSON)", [sys.executable, "ferramentas/plantas.py", "exportar"])
rodar("fichas (PLANTAS.md)", [sys.executable, "ferramentas/plantas.py", "fichas"])
rodar("índice e resumos das pastas (nenhum documento fora)", [sys.executable, "ferramentas/resumos.py", "--conferir"])
rodar("fichas dos pedidos do dono (campos e fila)", [sys.executable, "ferramentas/pedido.py", "conferir"])
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
        (_d / "contexto" / "QUADRO.md").write_text("# Quadro\n", encoding="utf-8")
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
rodar("módulos do motor 3D", [sys.executable, "ferramentas/planta3d.py"])
rodar("e-book, plantas grátis e calculadora (sem página estourada)", [sys.executable, "ebook/gerador/livro.py", "--conferir"])
rodar("painel", [sys.executable, "ferramentas/atualizar-painel.py"])

# Campo do dono ainda vazio: não é erro de código, mas o PDF não pode ir ao cliente assim (auditoria de 22/11)
_cfg = json.loads((RAIZ / "ebook" / "config.json").read_text(encoding="utf-8"))
_pend = [k for k, v in _cfg.items() if (isinstance(v, str) and v.startswith("[")) or (isinstance(v, list) and any(str(x).startswith("[") for x in v))]
if _pend:
    print(f"[AVISO] o PDF sai com campo pendente ({', '.join(_pend)}): rascunho, não mande ao cliente até o dono decidir")
print(f"\n{'Tudo certo.' if not falhas else str(len(falhas)) + ' problema(s): ' + ', '.join(falhas)}")
sys.exit(1 if falhas else 0)
