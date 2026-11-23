"""Escrito do zero; não usa nem contém código do cass (vetado pela licença, ficha 2151).

Busca no que o dono já disse nas conversas do Claude Code deste projeto (só leitura).

Pedido do dono (22/11/2026): achar o que ele já disse em qualquer conversa, para nenhum agente perguntar de novo.
Lê os registros que o próprio Claude Code grava
em ~/.claude/projects/<pasta deste projeto>/*.jsonl, na máquina onde roda (no computador do dono, todas as conversas de lá; na nuvem,
só a conversa atual).

  python3 ferramentas/conversas.py buscar E07 quartos       # falas do dono com todas as palavras
  python3 ferramentas/conversas.py buscar E07 --tudo        # inclui as respostas do Claude
  python3 ferramentas/conversas.py testar                   # confere a máscara (roda no checar.py)

Regras (Revisor de risco): só leitura, nada é gravado; só a pasta deste projeto; trecho de até 200 caracteres;
e-mail, telefone, CPF e chaves aparecem como [oculto]; sem caminho de arquivo. Ao repositório só vai a decisão,
reescrita em uma linha, com a data e "conversa anterior" (pedidos/LEIA-ME.md).
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PASTA = Path.home() / ".claude" / "projects" / re.sub(r"[^A-Za-z0-9]", "-", str(RAIZ))
LIMITE = 20  # no máximo 20 falas por busca
MASCARA = re.compile(
    r"-----BEGIN [A-Z ]*KEY-----.*?(?:-----END [A-Z ]*KEY-----|$)"                       # chave privada
    r"|[\w.+-]+@[\w-]+\.[\w.]+"                                                        # e-mail
    r"|\b\d{2}[ .]?\d{3}[ .]?\d{3}[ ./]?\d{4}[ -]?\d{2}\b"                              # CNPJ
    r"|\b\d{3}[ .]?\d{3}[ .]?\d{3}[ -]?\d{2}\b"                                        # CPF
    r"|\b\d{1,2}[ .]?\d{3}[ .]?\d{3}[ -]?[\dXx]\b"                                      # RG
    r"|\b(?:\d[ -]?){13,19}\b"                                                          # cartão
    r"|\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b"                  # chave Pix aleatória
    r"|\(?\b\d{2}\)?[ .]?9?[ .]?\d{4}[ .-]?\d{4}\b"                                       # telefone
    r"|\b(?:sk-ant-|sk_live_|sk_test_|sk-|ghp_|gho_|ghs_|github_pat_|glpat-|hf_|ya29\.|AKIA|AIza|xox[abp]-|APP_USR-)[\w.-]{6,}"  # chaves de API
    r"|\beyJ[\w-]{10,}\.[\w-]+\.[\w-]+"                                                 # JWT
    r"|\b(?:Bearer|Basic)\s+[\w.=+/-]{8,}"                                              # cabeçalho de autorização
    r"|[\"']?(?:api[_-]?key|client[_-]?secret|secret|password|passwd|senha|token|key|chave)[\"']?\s*[=:]\s*[\"']?[^\s\"',}]+"  # campo=valor
    r"|[?&](?:key|token|secret)=[^\s&]+"                                                  # na URL
    r"|\b(?:a )?senha (?:é|e)\s+\S+"                                                      # "a senha é X"
    r"|\bag[eê]ncia\s*:?\s*\d{3,5}[ -]?\d?|\bconta\s*:?\s*\d{4,12}[ -]?\d?", re.I | re.S)
NAO_E_FALA = ("<", "Another Claude session", "[SYSTEM", "Stop hook feedback", "This session is being continued")


def sem_acento(s):
    return unicodedata.normalize("NFKD", s.lower()).encode("ascii", "ignore").decode()


def mascarar(s):
    return MASCARA.sub("[oculto]", s)


def pasta_do_projeto():
    """Só a pasta deste repositório, pelo caminho real; nada de outra pasta nem de link simbólico."""
    if not PASTA.is_dir() or PASTA.is_symlink() or PASTA.resolve().parent != (Path.home() / ".claude" / "projects").resolve():
        sys.exit("sem registros do Claude Code deste projeto nesta máquina")
    return PASTA


def falas(tudo=False):
    """(data, quem, texto) de cada fala, sem repetir (o mesmo texto aparece na fila e no prompt)."""
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
                texto, quem = d.get("content"), "dono"
            elif d.get("type") == "user" and isinstance((d.get("message") or {}).get("content"), str):
                texto, quem = d["message"]["content"], "dono"
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
        sys.exit("diga ao menos uma palavra")
    achou = 0
    # a fala mais nova primeiro (a regra mais nova vence), e só depois o corte em 20
    for data, quem, texto in sorted(falas(tudo), key=lambda f: f[0], reverse=True):
        plano = re.sub(r"\s+", " ", texto)
        if all(t in sem_acento(plano) for t in termos):
            limpo = mascarar(plano)  # máscara antes do corte: o corte não deixa meia chave à mostra
            i = max(0, sem_acento(limpo).find(termos[0]))
            print(f"{data} · {quem}: …{limpo[max(0, i - 60):i + 140]}…")
            achou += 1
            if achou >= LIMITE:
                print(f"(parou em {LIMITE}; use mais palavras)")
                break
    print(f"{achou} fala(s).")


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
    print("máscara ok" if not vazou else f"máscara FALHOU: {vazou}")
    sys.exit(1 if vazou else 0)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["testar"]:
        testar()
    elif a[:1] == ["buscar"] and len(a) > 1:
        buscar([t for t in a[1:] if t != "--tudo"], "--tudo" in a)
    else:
        sys.exit(__doc__)
