"""Confere se o código do projeto tem erro, de uma vez só.

Uso: python3 ferramentas/checar.py
Confere: sintaxe de todo .py, .cjs e .js (fora de node_modules), as 24 plantas no validador,
a regra das paredes, o tamanho dos contextos, o índice e os resumos, o PDF do e-book (sem página
estourada, numa pasta temporária), se toda skill, todo comando (.claude/commands) e todo agente
passaram pelo roteiro de entrada (CONSELHO.md, seção 6), se o .claude/settings.json está são e,
como aviso, se há chave ou token gravado em arquivo do repositório (só arquivo:linha e tipo).
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
# Skill (.claude/skills/<nome>/SKILL.md) e comando (.claude/commands/<nome>.md): mesmas 4 conferências;
# o nome pode vir citado como `nome` ou `/nome`. Sem a pasta de comandos, o laço só não roda.
_pecas = [("skill", sk.parent.name, sk) for sk in sorted((RAIZ / ".claude" / "skills").glob("*/SKILL.md"))]
_pecas += [("comando", c.stem, c) for c in sorted((RAIZ / ".claude" / "commands").glob("*.md"))]
for tipo, nome, arq in _pecas:
    texto = arq.read_text(encoding="utf-8")
    if "## Neste projeto" not in texto:
        fora.append(f"{tipo} {nome}: falta a seção '## Neste projeto (X1-Plantas)' em {arq.relative_to(RAIZ)}")
    if "Prompt de entrada" not in texto:
        fora.append(f"{tipo} {nome}: falta o 'Prompt de entrada' específico")
    if f"`{nome}`" not in conselho and f"`/{nome}`" not in conselho:
        fora.append(f"{tipo} {nome}: não está citad{'a' if tipo == 'skill' else 'o'} no CONSELHO.md")
    if f"`{nome}`" not in ecossistema and f"`/{nome}`" not in ecossistema:
        fora.append(f"{tipo} {nome}: não está no inventário ECOSSISTEMA.md")
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
    falhas.append("roteiro de entrada de skills, comandos e agentes")
    print("[ERRO] roteiro de entrada de skills, comandos e agentes:\n  " + "\n  ".join(fora))
else:
    print("[OK ] skills, comandos e agentes passaram pelo roteiro de entrada")

# .claude/settings.json: JSON válido; todo gancho termina em "|| true" (gancho que falha não pode travar a
# conversa) e todo ferramentas/*.py que ele chama existe (com "2>/dev/null || true", um script apagado
# ou renomeado deixaria o gancho morto em silêncio); o UserPromptSubmit continua guardando o pedido.
_cfg_sessao = RAIZ / ".claude" / "settings.json"
_ruim_cfg = []
try:
    _ganchos = json.loads(_cfg_sessao.read_text(encoding="utf-8")).get("hooks", {})
except (OSError, ValueError, AttributeError) as e:
    _ganchos, _ruim_cfg = {}, [f"não abre como JSON de configuração: {e}"]
try:  # gancho de outro tipo (prompt, sem "command") não é conferido; estrutura torta vira erro, não traceback
    _cmds = [(ev, h["command"]) for ev, grupos in _ganchos.items() for g in grupos for h in g.get("hooks", [])
             if h.get("type", "command") == "command"]
    if not all(isinstance(c, str) for _, c in _cmds):
        raise TypeError
except (AttributeError, TypeError, KeyError):
    _cmds = []
    _ruim_cfg.append("estrutura inesperada em hooks (esperado: evento, lista de grupos, ganchos com command)")
for ev, cmd in _cmds:
    if not cmd.rstrip().endswith("|| true"):
        _ruim_cfg.append(f"gancho {ev} não termina em '|| true': {cmd}")
    _ruim_cfg += [f"gancho {ev} chama ferramentas/{py}, que não existe" for py in re.findall(r"ferramentas/([\w.-]+\.py)", cmd)
                  if not (RAIZ / "ferramentas" / py).exists()]
if not _ruim_cfg and not any(ev == "UserPromptSubmit" and "ferramentas/guardar-pedido.py" in cmd for ev, cmd in _cmds):
    _ruim_cfg.append("o UserPromptSubmit não chama mais ferramentas/guardar-pedido.py (os pedidos do dono deixam de ser guardados)")
if _ruim_cfg:
    falhas.append(".claude/settings.json")
    print("[ERRO] .claude/settings.json:\n  " + "\n  ".join(_ruim_cfg))
else:
    print(f"[OK ] .claude/settings.json ({len(_cmds)} gancho(s), todos com '|| true' e com o script no lugar)")

# Segredos no repositório (adaptado de everything-claude-code, MIT; .claude/LICENCA-everything-claude-code.txt).
# Só chaves: os mesmos padrões da MASCARA do ferramentas/conversas.py (chave privada, prefixos de API, JWT,
# Bearer/Basic, ?key= na URL). Lê todo arquivo rastreado ou novo (fora do .gitignore) que abre como UTF-8.
# A exceção é o valor falso inteiro dos testes da máscara, em qualquer arquivo; nunca um prefixo.
# Mostra arquivo:linha e tipo, nunca o valor. Por enquanto é AVISO (rodada de alcance).
_CHAVE = re.compile(
    r"(?P<chave_privada>-----BEGIN [A-Z ]*KEY-----.*?(?:-----END [A-Z ]*KEY-----|$))"
    r"|(?P<chave_de_API>\b(?:sk-ant-|sk_live_|sk_test_|sk-|ghp_|gho_|ghs_|github_pat_|glpat-|hf_|ya29\.|AKIA|AIza|xox[abp]-|APP_USR-)[\w.-]{6,})"
    r"|(?P<JWT>\beyJ[\w-]{10,}\.[\w-]+\.[\w-]+)"
    r"|(?P<cabeçalho_de_autorização>\b(?:Bearer|Basic)\s+[\w.=+/-]{8,})"
    r"|(?P<chave_na_URL>[?&](?:key|token|secret)=[^\s&]+)", re.I)
_LIMPA = ".,-`'\""  # o que o padrão engole no fim: o "..." de um texto, a crase de um trecho, a aspa de uma string
_FALSOS = {v.rstrip(_LIMPA) for v in (
    "?key=kkk333,", "sk_live_abcdef123", "APP_USR-12345678", "ghs_abcdefgh", "glpat-abcdefgh", "hf_abcdefgh",
    "ya29.abcdefgh", "Basic dXNlcjpwYXNz", "sk-ant-abc123def456ghi", "ghp_abcdefgh1234", "AIzaSyABCDEFGH123",
    "eyJhbGciOiJIUzI1.eyJzdWIiOiIx.abc", "Bearer abcdefgh123", "sk-ant-abc",
    "-----BEGIN PRIVATE KEY-----MIIE-----END PRIVATE KEY-----")}


def _git_z(*args):
    """git ls-files cortado em \\0: nome com acento ou espaço chega inteiro, sem aspas nem \\303."""
    r = subprocess.run(["git", "ls-files", "-z", *args], cwd=RAIZ, capture_output=True, text=True)
    return [x for x in r.stdout.split("\0") if x]


_achados, _binarios = [], 0
for _arq in sorted(set(_git_z() + _git_z("--others", "--exclude-standard"))):
    try:
        _linhas = (RAIZ / _arq).read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        _binarios += 1
        continue
    except OSError:
        continue  # apagado no disco e ainda no índice, pasta, link quebrado: nada a ler
    for _n, _l in enumerate(_linhas, 1):
        for _m in _CHAVE.finditer(_l):
            if _m.group(0).rstrip(_LIMPA) not in _FALSOS:
                _achados.append(f"{_arq}:{_n}: {_m.lastgroup.replace('_', ' ')}")
_achados += [f"{a}: arquivo .env rastreado pelo git (tire com git rm --cached e confira o .gitignore)"
             for a in _git_z("--", ".env*", "*/.env*")]
if _achados:
    print("[AVISO] segredos no repositório: possível chave gravada (o valor não é mostrado). Se for real, "
          "avise o dono para revogar no serviço; o histórico do git guarda a antiga:\n  " + "\n  ".join(_achados[:30])
          + (f"\n  (e mais {len(_achados) - 30})" if len(_achados) > 30 else ""))
else:
    print(f"[OK ] segredos no repositório (nenhuma chave nem .env; {_binarios} binários pulados)")
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
# Cada caso: (o que se confere, conta adiada com lambda, valor esperado tirado da planta, nunca da saída atual).
# A conta roda dentro de try: um caso com casa ou cômodo que não existe falha sozinho, sem derrubar o checar.
_casos = [("sala da C05: 3,00 de eixo, parede externa de um lado e passagem aberta do outro", lambda: PL.util(_ps["C05"], _c("C05", "sala"))[0], 2.85),
          ("quarto casal da E04: 3,00 de eixo entre a divisa e o pátio, duas paredes externas", lambda: PL.util(_ps["E04"], _c("E04", "quarto1"))[0], 2.70),
          ("banheiro da S03: giro de 1,50 m", lambda: min(PL.util(_ps["S03"], _c("S03", "banho"))[:2]) >= 1.5, True)]
_ruins = []
for _nome, _conta, _esperado in _casos:
    try:
        _v = _conta()
        _errado = _v != _esperado if isinstance(_esperado, bool) else abs(_v - _esperado) > 1e-6
    except Exception as e:  # noqa: BLE001 (qualquer erro do caso é falha do caso)
        _v, _errado = f"erro {type(e).__name__}: {e}", True
    if _errado:
        _ruins.append(f"{_nome}: deu {_v}, esperado {_esperado}")
if _ruins:
    falhas.append("regra das paredes")
    print(f"[ERRO] regra das paredes ({len(_ruins)} de {len(_casos)} casos):\n  " + "\n  ".join(_ruins))
else:
    print(f"[OK ] regra das paredes ({len(_casos)} casos)")

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
rodar("placar do veto em dia", [sys.executable, "ferramentas/placar.py", "--conferir"])
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
