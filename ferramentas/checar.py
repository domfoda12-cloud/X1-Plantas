"""Confere se o código do projeto tem erro, de uma vez só.

Uso: python3 ferramentas/checar.py
Confere: sintaxe de todo .py, .cjs e .js (fora de node_modules), as 24 plantas no validador,
os módulos do motor 3D, o painel e se toda skill e todo agente passaram pelo roteiro de entrada
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
    if nome not in conselho:
        fora.append(f"skill {nome}: não está citada no CONSELHO.md")
    if f"`{nome}`" not in ecossistema:
        fora.append(f"skill {nome}: não está no inventário ECOSSISTEMA.md")
for ag in sorted((RAIZ / ".claude" / "agents").glob("*.md")):
    if ag.stem not in conselho:
        fora.append(f"agente {ag.stem}: não está citado no CONSELHO.md")
    if f"`{ag.stem}`" not in ecossistema:
        fora.append(f"agente {ag.stem}: não está no inventário ECOSSISTEMA.md")
    if "Seu prompt de entrada" not in ag.read_text(encoding="utf-8"):
        fora.append(f"agente {ag.stem}: falta o 'Seu prompt de entrada'")
    if "CONTEXTO.md" not in ag.read_text(encoding="utf-8"):
        fora.append(f"agente {ag.stem}: não manda ler o CONTEXTO.md")
if fora:
    falhas.append("roteiro de entrada de skills e agentes")
    print("[ERRO] roteiro de entrada de skills e agentes:\n  " + "\n  ".join(fora))
else:
    print("[OK ] skills e agentes passaram pelo roteiro de entrada")

rodar("validador das plantas", [sys.executable, "ferramentas/plantas.py", "validar"])
rodar("módulos do motor 3D", [sys.executable, "ferramentas/planta3d.py"])
rodar("painel", [sys.executable, "ferramentas/atualizar-painel.py"])

print(f"\n{'Tudo certo.' if not falhas else str(len(falhas)) + ' problema(s): ' + ', '.join(falhas)}")
sys.exit(1 if falhas else 0)
