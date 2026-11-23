"""Abre cada conversa com o essencial: fichas abertas, o "## Agora" do quadro, os avisos seguintes e o último resumo.

É chamado sozinho pelo Claude Code quando uma conversa começa, volta, é limpa ou compactada (gancho SessionStart
em .claude/settings.json): recebe pela entrada padrão um JSON com o campo "source" e devolve, pela saída padrão,
um texto curto (até 2000 caracteres) que entra no contexto da conversa. Vale para a conversa principal; os
agentes continuam lendo o quadro pelo próprio arquivo.
Só lê dentro do projeto, não grava nada, não roda outro programa e nunca trava a conversa (sai sempre com 0).
Ideia adaptada de everything-claude-code, MIT, Copyright (c) 2026 Affaan Mustafa (.claude/LICENCA-everything-claude-code.txt).
"""
import json
import os
import sys
from pathlib import Path

TETO = 2000          # o que passar disso pesa em toda conversa
TETO_AGORA = 900    # o bloco "## Agora" do quadro (hoje tem uns 450)
TETO_AVISOS = 1100   # títulos e "O dono pediu" dos avisos depois do "## Agora"
TETO_ULTIMO = 700    # começo do contexto/entregas/ULTIMO.md
FINAL = "O resto está em contexto/QUADRO.md e em contexto/entregas/ULTIMO.md."
COMPACTOU = "O contexto foi resumido: releia a ficha aberta em pedidos/ antes de seguir."


def raiz():
    env = os.environ.get("CLAUDE_PROJECT_DIR")
    return Path(env).resolve() if env else Path(__file__).resolve().parent.parent


def ler(base, rel):
    """Texto de um arquivo do projeto; vazio se faltar ou se o caminho sair do projeto (link para fora)."""
    try:
        arq = (base / rel).resolve()
        arq.relative_to(base)
        return arq.read_text(encoding="utf-8")
    except (OSError, ValueError, UnicodeDecodeError):
        return ""


def cortar(texto, teto):
    """Até `teto` caracteres, cortado em linha inteira."""
    if len(texto) <= teto:
        return texto
    linhas, total = [], 0
    for linha in texto.splitlines():
        if total + len(linha) + 1 > teto:
            break
        linhas.append(linha)
        total += len(linha) + 1
    return "\n".join(linhas)


def fichas_abertas(base):
    n = 0
    for f in base.glob("pedidos/20*/*.md"):
        if "**Estado:** aberta" in ler(base, f.relative_to(base)):
            n += 1
    return f"Fichas abertas em pedidos/: {n}."


def blocos_do_quadro(quadro):
    """Divide o quadro nos blocos '## ...'; devolve o '## Agora' e a lista dos avisos seguintes."""
    blocos, atual = [], None
    for linha in quadro.splitlines():
        if linha.startswith("## "):
            atual = [linha]
            blocos.append(atual)
        elif atual is not None:
            atual.append(linha)
    agora = next((b for b in blocos if b[0].strip() == "## Agora"), None)
    resto = [b for b in blocos if b is not agora]
    return ("\n".join(agora).strip() if agora else ""), resto


def avisos(resto):
    linhas, total = ["Avisos seguintes do quadro:"], 0
    for b in resto:
        pediu = next((l.strip() for l in b[1:] if "O dono pediu" in l), "")
        trecho = b[0] + ("\n" + pediu if pediu else "")
        if total + len(trecho) + 1 > TETO_AVISOS:
            break
        linhas.append(trecho)
        total += len(trecho) + 1
    return "\n".join(linhas) if len(linhas) > 1 else ""


def montar(fonte, base):
    quadro = ler(base, "contexto/QUADRO.md")
    agora, resto = blocos_do_quadro(quadro)
    ultimo = ler(base, "contexto/entregas/ULTIMO.md").strip()
    partes = [fichas_abertas(base)]
    if fonte == "compact":
        partes.append(COMPACTOU)
    fim = FINAL
    # o fixo primeiro; o "## Agora" ganha o que sobrar, depois os avisos e o ULTIMO.md, cada um no seu teto
    sobra = TETO - len("\n\n".join(partes + [fim])) - 2
    if agora:
        partes.append(cortar(agora, min(TETO_AGORA, sobra)))
        sobra -= len(partes[-1]) + 2
    for texto, teto in ((avisos(resto), TETO_AVISOS), (("Último resumo de passagem:\n" + ultimo) if ultimo else "", TETO_ULTIMO)):
        pedaco = cortar(texto, min(teto, sobra))
        if pedaco and "\n" in pedaco:  # só o cabeçalho, sem conteúdo, não vale a linha
            partes.append(pedaco)
            sobra -= len(pedaco) + 2
    partes.append(fim)
    return cortar("\n\n".join(partes), TETO)


def main():
    try:
        dados = json.loads(sys.stdin.read() or "{}")
        fonte = dados.get("source", "") if isinstance(dados, dict) else ""
    except (ValueError, OSError):
        fonte = ""
    base = raiz()
    if not (base / "contexto" / "QUADRO.md").is_file():
        return
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart",
                                             "additionalContext": montar(fonte, base)}}, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
