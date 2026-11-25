"""Salvar e enviar só com a conferência verde (conserto de vez: o Maestro enviou duas vezes com o checar.py vermelho em 23/11).

  python3 ferramentas/salvar.py "mensagem do commit"

Roda resumos.py e checar.py; se o checar.py não sair com 0, para e mostra o erro (nada é salvo).
Se passar: git add -A, commit com as linhas de atribuição e push para a main e para a branch atual.
"""
import os
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
# o modelo da sessão muda (dono, 25/11: não assinar sempre como Fable); troque aqui ou use X1_MODELO
MODELO = os.environ.get("X1_MODELO", "Claude Opus 5.5")
ATRIBUICAO = (f"\n\nCo-Authored-By: {MODELO} <noreply@anthropic.com>\n"
              "Claude-Session: https://claude.ai/code/session_01DYdRuF8rs2sLvVqr7VsfNR")


def rodar(*cmd):
    return subprocess.run(cmd, cwd=RAIZ, capture_output=True, text=True)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].strip():
        sys.exit(__doc__)
    rodar(sys.executable, "ferramentas/resumos.py")
    c = rodar(sys.executable, "ferramentas/checar.py")
    if c.returncode != 0:
        print(c.stdout[-3000:], c.stderr[-1000:])
        sys.exit("NADA FOI SALVO: o checar.py não passou. Conserte e rode de novo.")
    rodar("git", "add", "-A")
    if rodar("git", "diff", "--cached", "--quiet").returncode == 0:
        sys.exit("nada para salvar")
    r = rodar("git", "commit", "-q", "-m", sys.argv[1].strip() + ATRIBUICAO)
    if r.returncode:
        sys.exit(r.stdout + r.stderr)
    rodar("git", "fetch", "-q", "origin", "main")
    m = rodar("git", "merge", "-q", "--no-edit", "origin/main")
    if m.returncode:
        sys.exit("a junção com a main deu conflito: resolva à mão\n" + m.stdout + m.stderr)
    ramo = rodar("git", "branch", "--show-current").stdout.strip()
    for alvo in ("HEAD:main", f"HEAD:{ramo}"):
        p = rodar("git", "push", "-q", "origin", alvo)
        if p.returncode:
            sys.exit(f"push para {alvo} falhou:\n{p.stderr}")
    print("salvo e enviado:", rodar("git", "log", "--oneline", "-1").stdout.strip())
