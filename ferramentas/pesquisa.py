"""Caderno de pesquisa compartilhado: toda busca na web de qualquer agente fica em pesquisas/<tema>.md.

Pedido do dono (22/11/2026): todos os agentes podem pesquisar na web, num lugar só, organizado.
Regra de economia: antes de buscar na web, `buscar`; se já tem achado com fonte, use e não busque de novo.

  python3 ferramentas/pesquisa.py buscar banheiro largura      # o que a equipe já achou
  python3 ferramentas/pesquisa.py nova --tema normas --quem arquiteto --pergunta "..." \
      --achado "..." --fonte https://... --certeza confirmado        # registra um achado
  python3 ferramentas/pesquisa.py conferir                     # formato (roda no checar.py)

Exemplo de norma (o tipo é obrigatório):
  python3 ferramentas/pesquisa.py nova --tema normas --tipo norma-orientativa --quem arquiteto \
      --pergunta "Zona bioclimática de Campinas" --achado "Zona 3 pelo Anexo A da NBR 15220-3" \
      --fonte https://... --certeza confirmado
"""
import argparse
import re
import sys
from datetime import date
from pathlib import Path

PASTA = Path(__file__).resolve().parent.parent / "pesquisas"
TEMAS = {
    "normas": "Normas, leis e código de obras",
    "plantas": "Projeto de casa: referências, medidas, arranjo",
    "mercado": "Público, preço, demanda e números de mercado",
    "concorrentes": "Concorrentes e o que eles vendem",
    "video": "Vídeo, gancho, edição e redes sociais",
    "ferramentas": "Ferramentas, skills, modelos e custos",
    "outros": "O que não cabe nos outros",
}
CERTEZAS = ("confirmado", "secundaria", "hipotese")
TIPOS = ("lei", "norma-obrigatoria", "norma-orientativa", "informativa")
# o caderno vai para o git: nada de dado pessoal (Revisor de risco, 22/11/2026)
PESSOAL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+|\(?\d{2}\)?\s?9?\d{4}-?\d{4}")
CABECA = "| Data | Quem | Pergunta | Achado | Fonte | Certeza |\n|---|---|---|---|---|---|\n"
LINHA = re.compile(r"^\| (\d{4}-\d{2}-\d{2}) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|$")


def arquivo(tema):
    arq = PASTA / f"{tema}.md"
    if not arq.exists():
        PASTA.mkdir(exist_ok=True)
        arq.write_text(f"# Pesquisa: {TEMAS[tema]}\n\n> Caderno compartilhado da equipe. Escreva só com `python3 ferramentas/pesquisa.py nova`; "
                       f"leia com `buscar`. Certeza: confirmado (texto oficial), secundaria (fonte secundária), hipotese.\n\n" + CABECA,
                       encoding="utf-8")
    return arq


def limpo(s):
    return re.sub(r"\s+", " ", s.replace("|", "/")).strip()


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("buscar"); b.add_argument("termos", nargs="+")
    n = sub.add_parser("nova")
    n.add_argument("--tema", choices=TEMAS, required=True)
    n.add_argument("--quem", required=True, help="nome do agente (arquiteto, redator...) ou maestro")
    n.add_argument("--pergunta", required=True, help="o que se queria saber, em uma frase")
    n.add_argument("--achado", required=True, help="o que a fonte diz, em uma frase, sem opinião")
    n.add_argument("--fonte", required=True, help="link https:// da página lida, ou arquivo:<caminho> do projeto")
    n.add_argument("--certeza", choices=CERTEZAS, required=True,
                   help="confirmado = texto oficial lido (só com link); secundaria = outra fonte; hipotese = não confirmado")
    n.add_argument("--tipo", choices=TIPOS, help="obrigatório no tema normas: lei obriga; norma-orientativa e informativa não")
    sub.add_parser("conferir")
    a = ap.parse_args()

    if a.cmd == "nova":
        if not a.fonte.startswith(("http://", "https://", "arquivo:")):
            sys.exit("fonte precisa ser um link (https://...) ou arquivo:<caminho>; sem fonte não entra")
        if a.fonte.startswith("arquivo:") and not (PASTA.parent / a.fonte[8:]).exists():
            sys.exit(f"o arquivo da fonte não existe: {a.fonte[8:]}")
        if a.certeza == "confirmado" and not a.fonte.startswith("http"):
            sys.exit("confirmado só com link do texto oficial lido; arquivo do projeto é 'secundaria'")
        if a.tema == "normas" and not a.tipo:
            sys.exit("no tema normas, diga --tipo (lei, norma-obrigatoria, norma-orientativa, informativa): norma orientativa nunca vira lei")
        if any(PESSOAL.search(x) for x in (a.achado, a.pergunta, a.fonte)):
            sys.exit("parece ter e-mail ou telefone: o caderno vai para o git, tire o dado pessoal")
        if "?" in a.fonte.split("#")[0] and "utm_" in a.fonte:
            a.fonte = a.fonte.split("?")[0]
        if a.tipo:
            a.achado = f"[{a.tipo}] {a.achado}"
        arq = arquivo(a.tema)
        with arq.open("a", encoding="utf-8") as f:
            f.write(f"| {date.today()} | {limpo(a.quem)} | {limpo(a.pergunta)} | {limpo(a.achado)} | {limpo(a.fonte)} | {a.certeza} |\n")
        print(f"registrado em {arq.relative_to(PASTA.parent)}")
    elif a.cmd == "buscar":
        termos = [t.lower() for t in a.termos]
        achou = 0
        for arq in sorted(PASTA.glob("*.md")):
            for l in arq.read_text(encoding="utf-8").splitlines():
                if LINHA.match(l) and all(t in l.lower() for t in termos):
                    print(f"{arq.stem}: {l}"); achou += 1
        print(f"{achou} achado(s)." + ("" if achou else " Nada registrado: pode buscar na web e depois registre com `nova`."))
    else:
        erros = []
        for arq in sorted(PASTA.glob("*.md")):
            if arq.stem not in TEMAS:
                if arq.name != "RESUMO.md":
                    erros.append(f"{arq.name}: tema fora da lista ({', '.join(TEMAS)})")
                continue
            for i, l in enumerate(arq.read_text(encoding="utf-8").splitlines(), 1):
                if l.startswith("| 2"):
                    m = LINHA.match(l)
                    fonte = m.group(5).strip() if m else ""
                    if not m or m.group(6).strip() not in CERTEZAS or not fonte.startswith(("http", "arquivo:")):
                        erros.append(f"{arq.name}:{i}: linha fora do formato (use pesquisa.py nova)")
                    elif fonte.startswith("arquivo:") and not (PASTA.parent / fonte[8:]).exists():
                        erros.append(f"{arq.name}:{i}: a fonte {fonte} não existe mais")
        print("\n".join(erros) or "caderno de pesquisa em ordem")
        sys.exit(1 if erros else 0)


if __name__ == "__main__":
    main()
