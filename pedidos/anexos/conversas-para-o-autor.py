"""Search what *you* said in your own Claude Code sessions for one project (read-only).

Written from scratch by an AI coding agent (Claude); it does not use or contain any code from cass.
Run it from your project folder. It reads only the session logs Claude Code keeps for that folder
(~/.claude/projects/<that folder>/*.jsonl), never writes anything, shows the newest first, caps results at 20,
and masks common patterns of e-mails, phone numbers, ID/card/bank numbers and API keys before showing a snippet.

  python3 conversas.py buscar <words>         # your own messages containing all the words
  python3 conversas.py buscar <words> --tudo  # also the assistant's replies
  python3 conversas.py testar                 # self-test of the masking
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path.cwd().resolve()  # run it from the project folder
PASTA = Path.home() / ".claude" / "projects" / re.sub(r"[^A-Za-z0-9]", "-", str(RAIZ))
LIMITE = 20  # at most 20 results per search
MASCARA = re.compile(
    r"-----BEGIN [A-Z ]*KEY-----.*?(?:-----END [A-Z ]*KEY-----|$)"
    r"|[\w.+-]+@[\w-]+\.[\w.]+"
    r"|\b\d{2}[ .]?\d{3}[ .]?\d{3}[ ./]?\d{4}[ -]?\d{2}\b"
    r"|\b\d{3}[ .]?\d{3}[ .]?\d{3}[ -]?\d{2}\b"
    r"|\b\d{1,2}[ .]?\d{3}[ .]?\d{3}[ -]?[\dXx]\b"
    r"|\b(?:\d[ -]?){13,19}\b"
    r"|\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b"
    r"|\(?\b\d{2}\)?[ .]?9?[ .]?\d{4}[ .-]?\d{4}\b"
    r"|\b(?:sk-ant-|sk_live_|sk_test_|sk-|ghp_|gho_|ghs_|github_pat_|glpat-|hf_|ya29\.|AKIA|AIza|xox[abp]-|APP_USR-)[\w.-]{6,}"
    r"|\beyJ[\w-]{10,}\.[\w-]+\.[\w-]+"
    r"|\b(?:Bearer|Basic)\s+[\w.=+/-]{8,}"
    r"|[\"']?(?:api[_-]?key|client[_-]?secret|secret|password|passwd|senha|token|key|chave)[\"']?\s*[=:]\s*[\"']?[^\s\"',}]+"
    r"|[?&](?:key|token|secret)=[^\s&]+"
    r"|\b(?:a )?senha (?:é|e)\s+\S+"
    r"|\bag[eê]ncia\s*:?\s*\d{3,5}[ -]?\d?|\bconta\s*:?\s*\d{4,12}[ -]?\d?", re.I | re.S)
NAO_E_FALA = ("<", "Another Claude session", "[SYSTEM", "Stop hook feedback", "This session is being continued")


def sem_acento(s):
    return unicodedata.normalize("NFKD", s.lower()).encode("ascii", "ignore").decode()


def mascarar(s):
    return MASCARA.sub("[oculto]", s)


def pasta_do_projeto():
    """Only this project's own log folder, by real path; no other folder, no symlinks."""
    if not PASTA.is_dir() or PASTA.is_symlink() or PASTA.resolve().parent != (Path.home() / ".claude" / "projects").resolve():
        sys.exit("no Claude Code logs for this project on this machine")
    return PASTA


def falas(tudo=False):
    """(date, who, text) for each message, without duplicates."""
    vistas = set()
    for arq in sorted(pasta_do_projeto().glob("*.jsonl")):
        if arq.is_symlink():
            continue
        for linha in arq.open(encoding="utf-8", errors="ignore"):
            try:
                d = json.loads(linha)
            except ValueError:
                continue
            texto, quem = None, None
            if d.get("type") == "queue-operation" and d.get("operation") == "enqueue":
                texto, quem = d.get("content"), "you"
            elif d.get("type") == "user" and isinstance((d.get("message") or {}).get("content"), str):
                texto, quem = d["message"]["content"], "you"
            elif tudo and d.get("type") == "assistant":
                partes = (d.get("message") or {}).get("content") or []
                texto = " ".join(p.get("text", "") for p in partes if isinstance(p, dict) and p.get("type") == "text")
                quem = "claude"
            if d.get("isMeta") or not texto or not isinstance(texto, str) or texto.lstrip().startswith(NAO_E_FALA):
                continue
            chave = (quem, texto.strip())
            if chave in vistas:
                continue
            vistas.add(chave)
            yield (d.get("timestamp") or "")[:16].replace("T", " "), quem, texto


def buscar(termos, tudo=False):
    termos = [sem_acento(t) for t in termos]
    if not termos:
        sys.exit("give at least one word")
    achou = 0
    # newest first, then the cut at 20
    for data, quem, texto in sorted(falas(tudo), key=lambda f: f[0], reverse=True):
        plano = re.sub(r"\s+", " ", texto)
        if all(t in sem_acento(plano) for t in termos):
            limpo = mascarar(plano)  # mask before cutting, so no half-key shows
            i = max(0, sem_acento(limpo).find(termos[0]))
            print(f"{data} · {quem}: …{limpo[max(0, i - 60):i + 140]}…")
            achou += 1
            if achou >= LIMITE:
                print(f"(stopped at {LIMITE}; add more words)")
                break
    print(f"{achou} result(s).")


def testar():
    falso = ("tel 11 98765 4321 e (11) 9 8765-4321 e 11.98765.4321, cpf 123 456 789 00, rg 12.345.678-9, "
             '{"token": "abc123xyz", "password": "p4ss"}, API_KEY=zzz111, client_secret=yyy222, url?key=kkk333, '
             "a senha é bolo123, sk_live_abcdef123, APP_USR-12345678, ghs_abcdefgh, glpat-abcdefgh, hf_abcdefgh, "
             "ya29.abcdefgh, Authorization: Basic dXNlcjpwYXNz, agência 1234-5 conta 123456-7, "
             "email joao@exemplo.com, cel (11) 98765-4321, cpf 123.456.789-00, cnpj 12.345.678/0001-90, "
             "cartao 4111 1111 1111 1111, pix 123e4567-e89b-12d3-a456-426614174000, sk-ant-abc123def456ghi, "
             "ghp_abcdefgh1234, AIzaSyABCDEFGH123, eyJhbGciOiJIUzI1.eyJzdWIiOiIx.abc, Bearer abcdefgh123, "
             "senha=segredo, -----BEGIN PRIVATE KEY-----MIIE-----END PRIVATE KEY-----")
    saida = mascarar(falso)
    vazou = [x for x in ("98765 4321", "9 8765", "98765.4321", "456 789", "345.678", "abc123xyz", "p4ss", "zzz111",
                         "yyy222", "kkk333", "bolo123", "sk_live_abc", "APP_USR-123", "ghs_abc", "glpat-abc", "hf_abc",
                         "ya29.abc", "dXNlcjpw", "1234-5", "123456-7", "joao@", "98765", "456.789", "345.678", "4111 1111", "e89b", "sk-ant-abc", "ghp_abc",
                         "AIzaSy", "eyJhbG", "Bearer abc", "segredo", "MIIE") if x in saida]
    print("masking ok" if not vazou else f"masking FAILED: {vazou}")
    sys.exit(1 if vazou else 0)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["testar"]:
        testar()
    elif a[:1] == ["buscar"] and len(a) > 1:
        buscar([t for t in a[1:] if t != "--tudo"], "--tudo" in a)
    else:
        sys.exit(__doc__)
