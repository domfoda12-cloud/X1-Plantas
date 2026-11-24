"""O PDF dos 2 bônus do e-book (passo D35 do pedidos/PLANO.md, 24/11/2026): sai junto do e-book, no mesmo comando.

Decisões do dono no quadro (24/11): os bônus saem num ARQUIVO SEPARADO, e as perguntas ao engenheiro em 3 PÁGINAS.
Um PDF só (bonus.pdf): capa curta, o checklist por fase e as perguntas (29, com 2 linhas de resposta cada, nome do
profissional e data). Feito para imprimir em A4, preto e branco, e escrever à mão: linhas de 7 mm, caixas de marcar
grandes, sem fundo escuro, letra de 10 pt para cima.
Sem preço (o PDF não fala de preço) e sem o título do e-book por extenso (está em troca): usa ROTULO_EBOOK.
O texto NÃO é digitado aqui: sai dos dois .md conferidos pelo Revisor de risco
  pedidos/anexos/bonus-checklist-da-obra.md       (Arquiteto)
  pedidos/anexos/bonus-perguntas-ao-engenheiro.md (Redator)
e o que é da equipe fica de fora: cabeçalho de status, "Nota sobre a ordem das fases", "Fontes",
"O que não conferi", "As 5 frases mais arriscadas", "Para a equipe", as marcas [H], [F1...] e (F1...).
Os rótulos escritos aqui (capa, "Contatos da obra", "Profissional", "Data") têm o SIM do Revisor
(pedidos/anexos/veto-bonus-pdf-separado-2026-11-24.md): não mude sem passar por ele.

Não roda sozinho: quem chama é o livro.py (gerar), que passa o próprio módulo (o aviso legal, o gerador de PDF).
Os estilos estão no fim do livro.css, presos em .bn. O rascunho de origem: ebook/plantas/rascunhos/bonus.py.
Para de vez (o livro.py sai com erro) se: página estourada, pergunta fora da sequência 1..29, preço no texto,
título do e-book por extenso, falta de um aviso, ou selo de rascunho faltando (sem a leitura registrada) ou sobrando.
"""
import html
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

E = html.escape
RAIZ = Path(__file__).resolve().parents[2]
MD_CHECK = RAIZ / "pedidos/anexos/bonus-checklist-da-obra.md"
MD_PERG = RAIZ / "pedidos/anexos/bonus-perguntas-ao-engenheiro.md"
ARQUIVO = "bonus.pdf"  # o nome do arquivo, ao lado do ebook.pdf; o e-book cita este nome (paginas.py, ONDE_BONUS)
# O selo de rascunho (Revisor, D34): só sai depois da leitura do profissional registrada. Enquanto o config.json não
# tiver "bonus_lido_por_profissional": true, o selo aparece (etiqueta nas páginas 2 em diante e caixa na capa).
# Quem põe true é o dono, com o registro da leitura e a data; o selo nunca vira "revisado por profissional".
CARIMBO = "Rascunho: espera a leitura de um profissional registrado"
ROTULO_EBOOK = "E-book de plantas de casas térreas"  # o título está em troca: não vai por extenso


def em_arquivo(config):
    """Os bônus do config.json que saem no arquivo separado: os 2 nomes, se forem de verdade e os textos existirem.
    Lista vazia = não há PDF dos bônus e o e-book não fala dele."""
    nomes = [b for b in config.get("bonus", []) if not b.startswith("[")]
    return nomes[:2] if len(nomes) >= 2 and MD_CHECK.exists() and MD_PERG.exists() else []


# ---------------------------------------------------------------- leitura dos .md

def limpa(t):
    """Tira as marcas da equipe ([H], [F1 ...], (F1 ...)) e o que é código."""
    t = re.sub(r"\s*\[[^\]]*\]", "", t)
    t = re.sub(r"\s*\((?:F\d|H\b)[^)]*\)", "", t)
    t = t.replace("`", "")
    t = re.sub(r"\.{2,}", ".", re.sub(r":\.", ".", t))
    return re.sub(r"\s+([.,;:])", r"\1", t).strip()


def inline(t):
    """Markdown de linha (negrito, itálico) para HTML, depois de escapar."""
    t = html.escape(limpa(t))
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)\*(?![\w*])", r"<i>\1</i>", t)
    return t


def secoes(md, nivel="## "):
    """{título: [linhas]} das seções de um nível."""
    out, atual = {}, None
    for ln in md.splitlines():
        if ln.startswith(nivel):
            atual = ln[len(nivel):].strip()
            out[atual] = []
        elif atual is not None:
            out[atual].append(ln)
    return out


INTERNAS = ("Nota sobre", "Fontes", "O que não conferi", "As 5 frases", "Para a equipe")


def ler_checklist():
    sec = secoes(MD_CHECK.read_text(encoding="utf-8"))
    aviso = next(" ".join(l.strip() for l in v if l.strip()) for k, v in sec.items() if k.startswith("Aviso que abre"))
    aviso = aviso.strip().strip('"“”')
    mom = next(" ".join(l.strip() for l in v if l.strip()) for k, v in sec.items() if k.startswith("Os momentos"))
    mom = limpa(mom)
    mom = " ".join(f for f in re.split(r"(?<=\.)\s+", mom) if "é minha" not in f)  # frase da equipe
    tit_mom, resto = mom.split(":", 1)
    partes = [p.strip() for p in resto.split(" · ")]
    ultimo, _, extra = partes[-1].partition(". ")
    partes[-1] = ultimo.rstrip(".")
    fases = []
    for k, v in sec.items():
        mt = re.match(r"Fase (\w+)\. (.+)", k)
        if not mt or k.startswith(INTERNAS):
            continue
        f = {"n": mt.group(1), "titulo": mt.group(2).strip(), "pular": "", "itens": [], "notas": []}
        for ln in v:
            s = ln.strip()
            if s.startswith("**Se pular:**"):
                f["pular"] = inline(s[len("**Se pular:**"):])
            elif s.startswith("- "):
                f["itens"].append(s[2:])
            elif s.startswith(">"):
                f["notas"].append(inline(s.lstrip("> ")))
            elif s == "---":
                break
        fases.append(f)
    return {"aviso": aviso, "mom_titulo": tit_mom.strip(), "momentos": partes, "mom_extra": extra.strip(), "fases": fases}


def ler_perguntas():
    md = MD_PERG.read_text(encoding="utf-8")
    pub = md.split("## A folha (texto para o público)", 1)[1].split("\n---", 1)[0]
    d = {"blocos": [], "como": [], "leve": [], "minhas": ""}
    paras, bloco, modo = [], None, None
    for ln in pub.splitlines():
        s = ln.strip()
        if not s or set(s) <= {"_"}:
            continue
        if s.startswith("### "):
            d["titulo"] = s[4:]
        elif s.startswith("#### "):
            mt = re.match(r"#### (\d+)\. (.+)", s)
            bloco = {"n": mt.group(1), "titulo": mt.group(2), "perg": []}
            d["blocos"].append(bloco)
            modo = "bloco"
        elif s == "**Como usar**":
            modo = "como"
        elif s.startswith("**Minhas perguntas**"):
            d["minhas"] = inline(s)
        elif s.startswith("- [ ] "):
            d["leve"].append(inline(s[6:]))
        elif s.startswith("- ") and modo == "como":
            d["como"].append(inline(s[2:]))
        elif re.match(r"\*\*\d+\.\*\*", s):
            n, q = re.match(r"\*\*(\d+)\.\*\* (.+)", s).groups()
            bloco["perg"].append((n, inline(q)))
        elif s.startswith("O que ele respondeu"):
            d["rotulo"] = s.split(":")[0] + ":"
        else:
            paras.append(s)
    # o que sobra, na ordem do arquivo: subtítulo, aviso do topo, frase-chave, humor ... e o aviso do fim
    d["sub"] = inline(paras[0].strip("*"))
    d["aviso"] = inline(paras[1])
    d["chave"] = inline(paras[2])
    d["humor"] = inline(paras[3])
    d["fim"] = inline(paras[-1].strip("*"))
    d["n_blocos"] = len(d["blocos"])  # o bloco 6 é a lista "O que eu levo comigo"
    return d


# ---------------------------------------------------------------- desenhos (traço simples, sem medida)

AZ, TI, CL, AM = "#0B4FA8", "#17202B", "#E7EFFA", "#FFF4DA"


def svg(corpo, vb="0 0 64 44"):
    return (f'<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg" fill="none" stroke="{AZ}" stroke-width="1.1" '
            f'stroke-linecap="round" stroke-linejoin="round">{corpo}</svg>')


def tijolos(x, y, w, h, fiada=4, tam=8):
    s = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}"/>']
    for i in range(1, int(h // fiada) + 1):
        yy = y + i * fiada
        if yy < y + h:
            s.append(f'<path d="M{x} {yy}H{x + w}"/>')
    for i in range(int(h // fiada) + 1):
        y0, y1 = y + i * fiada, min(y + (i + 1) * fiada, y + h)
        off = (tam / 2) if i % 2 else 0
        xx = x + off + tam
        while xx < x + w:
            s.append(f'<path d="M{xx} {y0}V{y1}" stroke-width=".7"/>')
            xx += tam
    return "".join(s)


CHAO = f'<path d="M2 38H62" stroke="{TI}" stroke-width="1.3"/>'
DESENHOS = {
    # 0a: o papel do lote e o projeto
    "0a": svg(f'<path d="M14 4H40L48 12V40H14Z" fill="#fff"/><path d="M40 4V12H48"/>'
              f'<rect x="20" y="16" width="22" height="18" stroke-dasharray="2 1.5"/><rect x="24" y="21" width="12" height="9" fill="{CL}"/>'
              f'<path d="M19 10H33"/>'),
    # 0b: a placa da obra e as ligações de água e luz
    "0b": svg(f'{CHAO}<path d="M16 38V24M40 38V24"/><rect x="10" y="8" width="36" height="16" fill="#fff"/>'
              f'<path d="M15 13H35M15 17H41M15 20H29" stroke-width=".8"/>'
              f'<path d="M54 10L49 19H54L50 27" stroke="{TI}"/><path d="M55 31C55 28 52.5 26 52.5 26S50 28 50 31A2.5 2.5 0 0 0 55 31Z" fill="{CL}"/>'),
    # 1: a casa marcada no chão do lote, com a trena
    "1": svg(f'<rect x="6" y="4" width="52" height="30"/><rect x="16" y="10" width="28" height="18" stroke-dasharray="2 1.5"/>'
             + "".join(f'<circle cx="{x}" cy="{y}" r="1.3" fill="{TI}" stroke="none"/>' for x, y in ((16, 10), (44, 10), (16, 28), (44, 28)))
             + f'<rect x="6" y="37" width="52" height="4" fill="{AM}" stroke="{TI}" stroke-width=".7"/>'
             + "".join(f'<path d="M{6 + i * 4} 37V{39 if i % 2 else 40}" stroke="{TI}" stroke-width=".5"/>' for i in range(1, 13))),
    # 2: a vala aberta no chão
    "2": svg(f'<path d="M2 20H22V36H42V20H62" stroke="{TI}" stroke-width="1.3"/>'
             + "".join(f'<circle cx="{x}" cy="{y}" r=".6" fill="{AZ}" stroke="none"/>' for x, y in
                       ((8, 25), (14, 30), (6, 33), (50, 26), (56, 31), (48, 35), (28, 40), (36, 41), (17, 39), (54, 40)))
             + f'<path d="M30 8V17M27 14L30 17L33 14"/>'),
    # 3: a umidade do chão parada embaixo da parede
    "3": svg(f'{tijolos(20, 6, 24, 18)}<rect x="18" y="24" width="28" height="9" fill="#fff"/>'
             f'<path d="M17 24H47" stroke="{TI}" stroke-width="2"/><path d="M2 33H62" stroke="{TI}" stroke-width="1.3"/>'
             + "".join(f'<path d="M{x} 42V37M{x - 2} 39L{x} 37L{x + 2} 39" stroke-width=".9"/>' for x in (24, 32, 40))),
    # 4: a parede subindo, com o vão da janela
    "4": svg(f'{CHAO}{tijolos(6, 6, 52, 32)}<rect x="22" y="14" width="18" height="13" fill="#fff"/>'),
    # 5: pilares, viga e laje
    "5": svg(f'{CHAO}<rect x="10" y="12" width="6" height="26" fill="#fff"/><rect x="48" y="12" width="6" height="26" fill="#fff"/>'
             f'<rect x="6" y="6" width="52" height="6" fill="{CL}"/><path d="M28 12V38M36 12V38" stroke-width=".8" stroke-dasharray="1.5 1.5"/>'),
    # 6: o telhado
    "6": svg(f'{CHAO}<rect x="12" y="22" width="40" height="16" fill="#fff"/><path d="M6 23L32 6L58 23Z" fill="#fff"/>'
             + "".join(f'<path d="M{32 - i * 4.3} {6 + i * 2.8}L{32 + i * 4.3} {6 + i * 2.8}" stroke-width=".7"/>' for i in range(1, 6))
             + '<rect x="28" y="28" width="8" height="10"/>'),
    # 7: o cano e o fio dentro da parede, antes de fechar
    "7": svg(f'{CHAO}<rect x="6" y="6" width="52" height="32" fill="#fff"/>'
             f'<path d="M16 38V18H30" stroke-width="2.2"/><path d="M44 6V20" stroke="{TI}" stroke-dasharray="2 1.4"/>'
             f'<rect x="40" y="20" width="8" height="6" stroke="{TI}"/><path d="M28 15V21" stroke-width="1.6"/>'),
    # 8: a parede meio tijolo, meio rebocada, e o piso com o ralo
    "8": svg(f'{tijolos(6, 4, 26, 26)}<rect x="32" y="4" width="26" height="26" fill="{CL}"/>'
             f'<path d="M2 34H62" stroke="{TI}" stroke-width="1.3"/><ellipse cx="46" cy="38" rx="4" ry="1.6"/>'
             f'<path d="M34 37.6C38 36.8 40 37.6 42 38" stroke-width=".8"/>'),
    # 9: a porta e a janela
    "9": svg(f'{CHAO}<rect x="8" y="8" width="16" height="30" fill="#fff"/><circle cx="20.5" cy="24" r="1" fill="{AZ}" stroke="none"/>'
             f'<rect x="32" y="12" width="24" height="16" fill="{CL}"/><path d="M44 12V28"/><path d="M30 28.5H58" stroke="{TI}"/>'),
    # 10: o azulejo e o rolo de tinta
    "10": svg("".join(f'<rect x="{6 + c * 8}" y="{6 + r * 8}" width="8" height="8" fill="#fff"/>' for r in range(4) for c in range(4))
              + f'<rect x="44" y="8" width="16" height="7" rx="2" fill="{AM}" stroke="{TI}"/><path d="M52 15V20H48V36" stroke="{TI}"/>'
              f'<rect x="46.5" y="30" width="3" height="9" rx="1" fill="{TI}" stroke="none"/>'),
    # 11: a casa pronta, o documento e a chave
    "11": svg(f'{CHAO}<path d="M6 22L22 10L38 22V38H6Z" fill="#fff"/><rect x="18" y="28" width="8" height="10"/>'
              f'<path d="M44 12H56L60 16V36H44Z" fill="#fff"/><path d="M47 19H56M47 23H56M47 27H52" stroke-width=".7"/>'
              f'<circle cx="54" cy="31.5" r="2.4" stroke="{TI}"/>'),
}

# os sinais de cada tipo de item: forma diferente, para ler em preto e branco
SINAIS = {
    "olho": svg(f'<path d="M3 12C7 5 17 5 21 12C17 19 7 19 3 12Z" stroke="{TI}" stroke-width="1.6"/><circle cx="12" cy="12" r="3" fill="{TI}" stroke="none"/>', "0 0 24 24"),
    "balao": svg(f'<path d="M4 5H20V16H11L6 20V16H4Z" stroke="{TI}" stroke-width="1.6"/>'
                 f'<path d="M10 9C10 7.6 14 7.6 14 9.2C14 10.6 12 10.6 12 12.2" stroke="{TI}" stroke-width="1.5"/><circle cx="12" cy="14" r=".9" fill="{TI}" stroke="none"/>', "0 0 24 24"),
    "camera": svg(f'<path d="M3 8H7L9 5H15L17 8H21V19H3Z" stroke="{TI}" stroke-width="1.6"/><circle cx="12" cy="13" r="3.4" stroke="{TI}" stroke-width="1.6"/>', "0 0 24 24"),
    "pasta": svg(f'<path d="M3 6H10L12 8H21V19H3Z" stroke="{TI}" stroke-width="1.6"/><path d="M3 11H21" stroke="{TI}" stroke-width="1.2"/>', "0 0 24 24"),
}
LEGENDA = [("olho", "Confira"), ("balao", "Pergunte ao engenheiro"), ("camera", "Fotografe antes de cobrir"), ("pasta", "Guarde")]
ALERTA = svg(f'<path d="M12 3L22 20H2Z" stroke="{TI}" stroke-width="1.8"/><path d="M12 9V14" stroke="{TI}" stroke-width="2"/><circle cx="12" cy="17" r="1.1" fill="{TI}" stroke="none"/>', "0 0 24 24")
PARE = svg(f'<path d="M8 2H16L22 8V16L16 22H8L2 16V8Z" fill="#fff" stroke="{TI}" stroke-width="1.8"/><path d="M8 12H16" stroke="{TI}" stroke-width="2.4"/>', "0 0 24 24")


def sinal(item):
    v = re.sub(r"^\*\*", "", item).split()[0].strip(":*").lower()
    if v in ("confira", "teste"):
        return "olho"
    if v.startswith("fotograf"):
        return "camera"
    if v in ("guarde", "leve"):
        return "pasta"
    return "balao"  # pergunte, peça, se for financiar


# ---------------------------------------------------------------- páginas

# Campos da folha "Contatos da obra" (texto do Designer, só rótulo de formulário: passou pelo Revisor)
CONTATOS = ["Engenheiro ou arquiteto", "Número da ART ou do RRT", "Pedreiro ou empreiteiro",
            "Prefeitura (setor de obras)", "Companhia de água", "Companhia de luz"]


def linhas(n, extra=""):
    """Linhas de escrever: n traços de LINHA de altura; o que não cabe some inteiro (nunca meia linha)."""
    return f'<div class="linhas {extra}">' + "<i></i>" * n + "</div>"


def pagina(conteudo, n, total, rotulo, classe=""):
    rod = f'<div class="rodape"><span>{E(_AVISO)}</span><span class="num">{E(rotulo)} · {n} de {total}</span></div>'
    carimbo = "" if _LIDO or classe == "cp" else f'<div class="carimbo">{E(CARIMBO)}</div>'  # na capa, o selo grande já diz
    return (f'<section class="pagina bn {classe}">{carimbo}'
            f'<div class="miolo">{conteudo}</div>{rod}</section>')


def html_fase(f):
    itens = "".join(f'<li><span class="caixinha"></span><span class="sinal">{SINAIS[sinal(it)]}</span><p>{inline(it)}</p></li>'
                    for it in f["itens"])
    notas = "".join(f'<p class="nota">{n}</p>' for n in f["notas"])
    return (f'<div class="fase"><div class="f-cab"><div><span class="eti-b">Fase {E(f["n"])}</span><h2>{E(f["titulo"])}</h2></div>'
            f'<div class="f-des">{DESENHOS.get(f["n"], "")}</div></div>'
            f'<div class="pular"><span class="sinal">{ALERTA}</span><p><b class="r">Se pular:</b> {f["pular"]}</p></div>'
            f'<ul class="itens">{itens}</ul>{notas}'
            f'<div class="anot-f">{linhas(40)}<span>Anotações</span></div></div>')


_LIDO = False  # config.json, "bonus_lido_por_profissional": só com true o selo de rascunho some
_AVISO = ""  # o aviso legal do rodapé de toda página: o mesmo do e-book (livro.AVISO), posto por montar()


def montar(config, aviso):
    """Capa, checklist e perguntas, numa sequência só de páginas. Devolve (html das páginas, conferências)."""
    global _AVISO, _LIDO
    _AVISO = aviso
    _LIDO = config.get("bonus_lido_por_profissional") is True
    selo = "" if _LIDO else f'\n      <div class="selo"><span class="sinal">{ALERTA}</span>{E(CARIMBO)}</div>'
    ck, pg = ler_checklist(), ler_perguntas()
    nome_ck, nome_pg = em_arquivo(config)
    fases = ck["fases"]
    grupos = [fases[i:i + 2] for i in range(0, len(fases), 2)]  # 2 fases por folha
    perg = [b for b in pg["blocos"] if b["perg"]]
    leve = [b for b in pg["blocos"] if not b["perg"]][0]
    folhas_pg = [perg[:1], perg[1:3], perg[3:]]  # 3 páginas (decisão do dono): lote | planta e prefeitura | etapas e dinheiro
    ini_ck = 2
    ini_pg = ini_ck + 1 + len(grupos)
    total = ini_pg + len(folhas_pg) - 1
    n_perg = sum(len(b["perg"]) for b in perg)
    n_itens = sum(len(f["itens"]) for f in fases)
    EB = ROTULO_EBOOK[0].lower() + ROTULO_EBOOK[1:]  # no meio da frase: "do e-book de plantas..."

    capa = f"""
      <div class="cp-topo"><span class="eti-b">Bônus do {E(EB)}</span>
        <h1 class="cp-tit">{E(nome_ck)} e {E(nome_pg[0].lower() + nome_pg[1:])}</h1></div>{selo}
      <div class="dentro">
        <div><span class="pg-n">páginas<br>{ini_ck} a {ini_pg - 1}</span><div><h2>{E(nome_ck)}</h2>
          <p>{len(fases)} fases, do lote ao habite-se, com {n_itens} caixas de marcar e linhas para anotar.</p></div></div>
        <div><span class="pg-n">páginas<br>{ini_pg} a {total}</span><div><h2>{E(nome_pg)}</h2>
          <p>{n_perg} perguntas, com 2 linhas para a resposta de cada uma, o nome do profissional e a data. {pg["sub"]}</p></div></div>
      </div>
      <div class="fita-cp"><span>imprima em A4 · preto e branco</span></div>
      <p class="imprimir">Feito para imprimir e escrever à mão. Para levar só as perguntas, imprima as páginas {ini_pg} a {total}: uma cópia para cada profissional.</p>
      """
    pags = [pagina(capa, 1, total, "Bônus", "cp")]

    abertura = f"""
      <div class="bc-topo"><span class="eti-b">Bônus 1 do {E(EB)}</span><h1 class="bc-tit">{E(nome_ck)}</h1></div>
      <div class="aviso-b"><b>Antes de usar</b>{E(ck["aviso"])}</div>
      <div class="leg">{''.join(f'<div><span class="sinal">{SINAIS[k]}</span>{E(t)}</div>' for k, t in LEGENDA)}</div>
      <p class="leg-cx"><span class="caixinha"></span>Marque com a caneta o que já foi feito.</p>
      <div class="mom"><h3>{E(ck["mom_titulo"])}</h3>
        <div class="linha-obra"><div class="trena"></div>
        <div class="paradas">{''.join(f'<div><span class="sinal">{PARE}</span>{E(m)}</div>' for m in ck["momentos"])}</div></div>
        <p class="mom-extra">{E(ck["mom_extra"])}</p></div>
      <div class="indice-b"><h3>As fases</h3>{''.join(f'<p><b>{E(f["n"])}</b><span>{E(f["titulo"])}</span><i>{ini_ck + 1 + i // 2}</i></p>' for i, f in enumerate(fases))}</div>"""
    pags.append(pagina(abertura, ini_ck, total, nome_ck))
    for i, g in enumerate(grupos):
        corpo = "".join(html_fase(f) for f in g)
        if len(g) == 1:  # a última folha tem uma fase só: o resto vira a lista de contatos da obra
            corpo += ('<div class="contatos"><h3>Contatos da obra</h3>'
                      + "".join(f'<p><span>{E(c)}</span><i></i></p>' for c in CONTATOS) + '</div>')
        pags.append(pagina(corpo, ini_ck + 1 + i, total, nome_ck))

    prof = '<div class="prof"><span>Profissional:</span><i></i><span>Data:</span><i></i></div>'
    for k, blocos in enumerate(folhas_pg):
        corpo = "".join(html_bloco(b, pg["rotulo"]) for b in blocos)
        if k == 0:
            topo = f"""
      <div class="pg-cab"><span class="eti-b">Bônus 2 do {E(EB)}</span><h2>{E(pg["titulo"])}</h2><p class="sub">{pg["sub"]}</p></div>
      <div class="aviso-b">{pg["aviso"]}</div>
      <div class="chave"><p>{pg["chave"]}</p><p>{pg["humor"]}</p></div>
      <div><p class="como-t">Como usar</p><ul class="como">{''.join(f'<li>{c}</li>' for c in pg["como"])}</ul></div>{prof}"""
        else:
            topo = f'<div class="pg-mini">{prof}</div>'
        fim = ""
        if k == len(folhas_pg) - 1:
            fim = f"""
      <div class="pg3-baixo">
        <div class="minhas"><p>{pg["minhas"]}</p>{linhas(20)}</div>
        <div class="leve"><h3><span>{leve["n"]}</span>{E(leve["titulo"])}</h3><ul>{''.join(f'<li><span class="caixinha"></span><p>{x}</p></li>' for x in pg["leve"])}</ul></div>
      </div>
      <p class="fim-b">{pg["fim"]}</p>"""
        pags.append(pagina(f'{topo}<div class="blocos">{corpo}</div>{fim}', ini_pg + k, total,
                           f"Perguntas, folha {k + 1} de {len(folhas_pg)}", "pg"))

    numeros = [int(n) for b in perg for n, _ in b["perg"]]
    return pags, {"fases": len(fases), "itens": n_itens, "numeros": numeros, "aviso_ck": ck["aviso"],
                  "aviso_pg": pg["aviso"], "fim_pg": pg["fim"], "ini_pg": ini_pg, "total": total}


def html_bloco(b, rotulo):
    qs = "".join(f'<div class="q"><span class="n">{n}.</span><p>{q}</p>{linhas(2, "resp")}</div>' for n, q in b["perg"])
    return (f'<div class="bloco" style="flex-grow:{len(b["perg"])}"><div class="b-cab"><span>{b["n"]}</span>'
            f'<div><h3>{E(b["titulo"])}</h3><em>{E(rotulo.rstrip(":"))}</em></div></div><div class="grade">{qs}</div></div>')


def conferir(paginas, c):
    """O que não pode sair errado, antes de gerar o PDF."""
    erros = []
    if c["numeros"] != list(range(1, 30)):
        erros.append(f"perguntas fora da sequência 1..29: {c['numeros']}")
    texto = re.sub(r"<[^>]+>", " ", "".join(paginas))
    texto = re.sub(r"\s+", " ", texto.replace("&quot;", '"').replace("&#x27;", "'"))
    if re.search(r"R\$|\breais\b", texto):
        erros.append("preço no texto (o PDF não fala de preço)")
    if "Antes do primeiro tijolo" in texto:
        erros.append("título do e-book por extenso (está em troca)")
    for nome, frase in (("aviso legal", _AVISO), ("aviso do checklist", c["aviso_ck"])):
        if frase not in texto:
            erros.append(f"falta o {nome} inteiro")
    if texto.count(_AVISO) < len(paginas):
        erros.append("alguma página sem o aviso legal no rodapé")
    if not _LIDO:
        if texto.count(CARIMBO) < len(paginas):
            erros.append("falta o selo de rascunho em alguma página (a leitura do profissional não está registrada)")
    elif re.search(r"rascunho", texto, re.I):
        erros.append("selo de rascunho no texto com a leitura do profissional registrada")
    if re.search(r"revisado por", texto, re.I):  # o selo nunca vira "revisado por profissional"
        erros.append('"revisado por" no texto')
    return erros


# ---------------------------------------------------------------- PDF e PNG

def gerar(LV, config, saida, env, previa=None):
    """Grava saida/bonus.pdf com o mesmo CSS e o mesmo gerador de PDF do e-book (LV é o módulo livro).
    Com previa (pasta), salva também um PNG de cada página em previa/bonus/. Devolve True se saiu sem erro."""
    pags, c = montar(config, LV.AVISO)
    erros = conferir(pags, c)
    if erros:
        print("AVISO: PDF dos bônus: " + "; ".join(erros))
        return False
    doc = (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Bônus · {E(ROTULO_EBOOK)}</title>'
           f'<style>{LV.CSS}</style></head><body>{"".join(pags)}</body></html>')
    destino = Path(saida) / ARQUIVO
    with tempfile.TemporaryDirectory() as tmp:
        arq = Path(tmp) / "bonus.html"
        arq.write_text(LV.sem_quebra(doc), encoding="utf-8")
        cmd = ["node", str(LV.AQUI / "pdf.cjs"), str(arq), str(destino)]
        if previa:
            shutil.rmtree(Path(previa) / "bonus", ignore_errors=True)  # prévia velha com mais páginas não fica para trás
            cmd.append(str(Path(previa) / "bonus"))
        r = subprocess.run(cmd, env=env, capture_output=True, text=True)
    print(r.stdout.strip(), r.stderr.strip())
    print(f"bônus: {len(pags)} páginas: capa 1, checklist 2 a {c['ini_pg'] - 1} ({c['fases']} fases, {c['itens']} caixas), "
          f"perguntas {c['ini_pg']} a {c['total']} ({len(c['numeros'])}, de {c['numeros'][0]} a {c['numeros'][-1]})")
    return r.returncode == 0
