"""Conta os arquivos que a conversa abriu e lembra do documento novo, sem nunca bloquear nada.

É chamado sozinho pelo Claude Code depois de cada Read, Edit ou Write (gancho PostToolUse em .claude/settings.json):
recebe pela entrada padrão um JSON com session_id, tool_name e tool_input.file_path. Faz duas coisas:
1. Contador: guarda os caminhos distintos desta conversa e, ao passar de 30 e de 45, uma vez cada, avisa que a tarefa
   está grande demais (o CLAUDE.md pede dividir). Leituras feitas pelo Bash não entram, por isso "cerca de".
2. Documento novo: quando um Write grava um .md que ainda não está no git, lembra de rodar o resumos.py, uma vez por
   caminho; se o .md ficou solto na raiz, lembra também das pastas certas.
Só grava caminhos (nunca conteúdo) num JSON da pasta temporária do sistema. Nunca sai com código 2, nunca devolve
decision nem permissionDecision: só acrescenta um aviso ao contexto. Sai sempre com 0.
Ideia adaptada de everything-claude-code, MIT, Copyright (c) 2026 Affaan Mustafa (.claude/LICENCA-everything-claude-code.txt).
"""
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

LIMITES = (30, 45)  # o CLAUDE.md fala em "uns 30 arquivos"; o segundo aviso é para quem não dividiu no primeiro
PASTAS = "pedidos/, contexto/, pesquisas/, ebook/, video/, instagram/, animacoes-3d/, reports/"


def id_seguro(sid):
    """Só letras, números e hífen; qualquer outra coisa (barra, ponto, vazio) vira 'sem-id'."""
    return sid if isinstance(sid, str) and re.fullmatch(r"[A-Za-z0-9-]{1,100}", sid) else "sem-id"


def carregar(arq):
    try:
        d = json.loads(arq.read_text(encoding="utf-8"))
        if isinstance(d, dict):
            return {"caminhos": list(d.get("caminhos", [])), "avisos": list(d.get("avisos", [])),
                    "md_avisados": list(d.get("md_avisados", []))}
    except (OSError, ValueError, TypeError):
        pass  # sem arquivo ou corrompido: começa do zero
    return {"caminhos": [], "avisos": [], "md_avisados": []}


def gravar(arq, estado):
    """Gravação atômica: escreve ao lado e troca de nome."""
    tmp = arq.with_name(arq.name + f".{os.getpid()}.tmp")
    tmp.write_text(json.dumps(estado, ensure_ascii=False), encoding="utf-8")
    os.replace(tmp, arq)


def fora_do_git(raiz, caminho):
    try:
        r = subprocess.run(["git", "-C", str(raiz), "ls-files", "--error-unmatch", "--", str(caminho)],
                           capture_output=True, timeout=3)
        return r.returncode != 0
    except (OSError, subprocess.SubprocessError):
        return False  # sem git, não dá para saber: melhor não lembrar à toa


def main():
    dados = json.loads(sys.stdin.read() or "{}")
    if not isinstance(dados, dict):
        return
    entrada = dados.get("tool_input") or {}
    caminho = entrada.get("file_path") if isinstance(entrada, dict) else None
    if not isinstance(caminho, str) or not caminho:
        return
    ferramenta = dados.get("tool_name", "")
    raiz = Path(os.environ.get("CLAUDE_PROJECT_DIR") or dados.get("cwd") or Path(__file__).resolve().parent.parent).resolve()
    arq = Path(tempfile.gettempdir()) / f"x1-arquivos-{id_seguro(dados.get('session_id'))}.json"
    estado = carregar(arq)
    caminho = os.path.normpath(caminho)
    avisos = []

    if caminho not in estado["caminhos"]:
        estado["caminhos"].append(caminho)
    n = len(estado["caminhos"])
    for limite in LIMITES:
        if n > limite and limite not in estado["avisos"]:
            estado["avisos"].append(limite)
            avisos.append(f"Cerca de {n} arquivos nesta tarefa: o CLAUDE.md pede dividir. Feche o que está aberto "
                          "e escreva a passagem em contexto/entregas/ULTIMO.md.")

    if ferramenta == "Write" and caminho.endswith(".md") and caminho not in estado["md_avisados"]:
        p = Path(caminho) if os.path.isabs(caminho) else raiz / caminho
        try:
            dentro = p.resolve().relative_to(raiz)
        except (OSError, ValueError):
            dentro = None
        if dentro is not None and fora_do_git(raiz, dentro):
            estado["md_avisados"].append(caminho)
            texto = "Documento novo: rode python3 ferramentas/resumos.py."
            if len(dentro.parts) == 1:
                texto += (" Arquivo fica junto do que tem a mesma função: confira se ele não pertence a "
                          f"{PASTAS}")
            avisos.append(texto)

    gravar(arq, estado)
    if avisos:
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PostToolUse",
                                                 "additionalContext": " ".join(avisos)}}, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
