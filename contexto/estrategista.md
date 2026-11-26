# Contexto do Estrategista

> Só o que importa para este papel; as regras fixas estão no seu arquivo de agente. **Antes de trabalhar, leia o [quadro](QUADRO.md).** Resumo geral: [`CONTEXTO.md`](../CONTEXTO.md); histórico, só para detalhe antigo: [`CONTEXTO-HISTORICO.md`](../CONTEXTO-HISTORICO.md). Resumo da última tarefa: [`entregas/ULTIMO.md`](entregas/ULTIMO.md), só se a sua continua a anterior.

## O que está decidido (fonte: `CONTEXTO.md`, "Lançamento")

- **O e-book à venda tem 3 casas** (C01, E03, F01; `ebook/config.json`, `casas_lancamento`); as 24 são o catálogo. Título "Antes do primeiro tijolo" (dono, 26/11 07:01). R$ 47 na primeira semana, teste com R$ 67 em semanas alternadas; o PDF não fala de preço. Garantia de 7 dias da entrega do link. Pix no WhatsApp, com o CPF dele. Anúncio: R$ 20 por dia, depois do teste sem gastar (dono, 23/11).
- **O funil, o WhatsApp e a conferência do Pix são do dono**, que atende sozinho e trabalha de dia (ficha `2026-11-26-0926`). Plano de funil diz em que passo e em que horário depende dele; a folha do funil é para ele.
- Pesquisa a fundo de mercado, preço e concorrente vai ao `pesquisador`; você usa a conclusão dele (dono, 26/11).
- **Próximas casas:** você e o Nilo indicam as mais vendáveis, o dono aprova (dono, 23/11). O dado que decide é o lote mais pedido (`PAINEL.md`, seção 7).
- Orçamento: divisão proposta do limite semanal (animações 45%, vídeo 30%, e-book 25%) e saldo do OpenArt em `ORCAMENTO.md`; cada uso do OpenArt pede o "sim" do dono.

## Custo do trabalho da equipe: o número gravado

O gasto de cada rodada de fluxo está em [`pedidos/fluxos/RODADAS.md`](../pedidos/fluxos/RODADAS.md); por fluxo e por conferidor, `python3 ferramentas/fluxo.py relatorio`. Em 26/11 (uma rodada de cada; a do júri teve 2 voltas): o júri (`decisao`) gastou 1.806.457 tokens da ferramenta, o `planta` 510.641; a prova de entrada, 68.978 de saída. Conferidor de juízo com 5 rodadas sem achado próprio é candidato a corte (`pedidos/fluxos/LEIA-ME.md`).

## Em aberto com você

- **Primeiro número do funil:** nenhuma conversão medida. Teste mais barato: as 4 contagens por semana na planilha do dono (conversas, mandaram a medida, só cabe a Casa Compacta, pagaram e não devolveram), proposta do [funil simulado](../pedidos/anexos/funil-simulado-2026-11-26.md); quem anota e quando começa a semana são perguntas 1 e 2 do `teste-de-preco-como-medir.md`.
- **Funil simulado (seção 3d), escrito para o sócio:** a pergunta 1 está respondida (o dono confere o Pix); a 2 vira o horário de atendimento dele; 3 a 5 (lote em que só cabe a Casa Compacta, quem desconfia, "gera" dos PDFs com o sol) seguem com ele.
- Bônus (selo de rascunho até um profissional ler), o que vai de graça (cartão `j3-gratis-literal`) e prometer as próximas casas ("ainda não sei"; `promessa_atualizacao` vazio): do dono.
- Quanto resta do limite semanal (Configurações → Uso), para fechar o orçamento em números.
- A calculadora de lote num link que abra no celular do dono (cartão C7).
- Testar PLANTA contra LOTE como palavra do comentário.

## Onde olhar

`ESTRATEGIA.md`, `PAINEL.md` (seções 3, 4, 7 e 8), `ebook/referencias/MERCADO.md` ("Quem compra" e "Concorrentes"), `pedidos/anexos/teste-de-preco-como-medir.md`, `pedidos/fluxos/RODADAS.md`.

## Leia barato

Os fios do que o dono quer: [`dono/IDEIAS-GERAIS.md`](dono/IDEIAS-GERAIS.md). Primeiro o resumo da pasta: [venda e WhatsApp](../ebook/vendas/RESUMO.md), [Instagram](../instagram/RESUMO.md), [jurídico](../reports/RESUMO.md); tudo: [`INDICE.md`](../INDICE.md).

## Lições

O que deu errado e não pode voltar (uma linha cada, com data; vem das auditorias e das correções do dono).
- **Lições antigas:** [`pedidos/historico/licoes-estrategista.md`](../pedidos/historico/licoes-estrategista.md), inteiras; leia antes de trabalho grande.
- **23/11, dono:** o plano supôs uma página de vendas que não existe. O caminho é anúncio, comentário, WhatsApp e Pix; desde 26/11 o funil é do dono, que atende sozinho (ficha 0926). Confira todo plano contra isso antes de entregar (leitura nossa da fala de 16/11).
- **26/11, prova:** nível 1: deixei passar o gancho "Lote com 10 m de frente?" na legenda da Família Compacta, sem o fundo (pede no mínimo 12,8 m) e sem aviso do recuo. Vale a "Regra do lote" de `contexto/revisor-de-risco.md`.
