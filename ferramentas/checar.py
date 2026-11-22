"""Confere se o código do projeto tem erro, de uma vez só.

Uso: python3 ferramentas/checar.py
Confere: sintaxe de todo .py, .cjs e .js (fora de node_modules), as 24 plantas no validador,
os dados, as fichas, os módulos do motor 3D, o PDF do e-book (sem página estourada), a calculadora do parceiro, o painel e se toda skill e todo agente passaram pelo roteiro de entrada
(CONSELHO.md, seção 6). Sai com código 1 se algo falhar.
"""
import subprocess
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


ignorar = ("node_modules", ".git", "saida", "research_notes")
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
LIMITES += [(f"contexto/entregas/{p.name}", 3500) for p in sorted((RAIZ / "contexto" / "entregas").glob("*.md"))]
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
rodar("módulos do motor 3D", [sys.executable, "ferramentas/planta3d.py"])
rodar("e-book, plantas grátis e calculadora (sem página estourada)", [sys.executable, "ebook/gerador/livro.py", "--conferir"])
rodar("painel", [sys.executable, "ferramentas/atualizar-painel.py"])

print(f"\n{'Tudo certo.' if not falhas else str(len(falhas)) + ' problema(s): ' + ', '.join(falhas)}")
sys.exit(1 if falhas else 0)
