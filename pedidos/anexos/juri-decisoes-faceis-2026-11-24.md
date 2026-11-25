# Júri das decisões fáceis de desfazer (24/11/2026)

> Regra do dono (24/11, cartão v6): "se é algo que pode ser facilmente alterado depois, continue o trabalho com a decisão do júri e me mostre a decisão tomada depois". Continuam só dele: gasto, publicar, e-mail, contratação, dados pessoais, preço e o que não se desfaz.

**Estado: nenhum passo J está fechado.** Cada decisão tem cartão no Canteiro desde 24/11 17:45, mas o dono ainda não viu. A linha "Mostrado ao dono" de cada seção só vira "sim" quando ele responder ao cartão; até lá o `plano.py feito J<n>` recusa, e é para recusar.

**Método** (`CONSELHO.md` 5b): 3 jurados, cada um por um ângulo e sem ver os outros: comprador (Haiku), dinheiro (Sonnet), risco e regra (Opus). Régua de `juri-proximas-melhorias.md`, seção 1. Presidente: o Maestro (Fable), que não opinou. Duas rodadas (o máximo).

**Não feito:** a revisão anônima cruzada (passo 2 do método) não rodou. O J6 (pasta no Drive) ficou fora: criar a pasta pede um "sim" novo do dono. O J4 (bio) espera o D29.

**Fatos conferidos pelo presidente no repositório (5, todos confirmados):** a capa não tem "de referência" (`ebook/gerador/livro.py:1151`); a opção B do grátis "leva tudo da opção A", com 3D e miniaturas (`amostra-gratis-opcoes.md:14-17,26`); o Revisor pôs "O que não fazer depois" e "Carro ou quintal" entre as 5 mais úteis (`veto-comodo-a-comodo-2026-11-24.md:21-27`); o dono deu liberdade de título em 23/11 (`decisoes-do-dono-2026-11-23.md:84`); a primeira venda espera a leitura do profissional (D6 depende do D23), então tirar páginas não adianta a venda.

**Notas** (comprador / dinheiro / risco → média):

| | Rodada 1 | Rodada 2 (proposta reescrita) |
|---|---|---|
| J1 | 6 / 6,5 / 7,5 → 6,7 | 7 / 7,5 / 8 → 7,5 |
| J2 | 5 / 7 / 5 → 5,7 | 7 / 5,5 / 8 → 6,8 |
| J3 | 3 / 7 / 5,5 → 5,2 | 7 / 7 / 7,5 → 7,2 |
| J5 | 4 / 7,5 / 4 → 5,2 | 6 / 6,5 / 8,5 → 7,0 |
| J7 | 3 / 7,5 / 4 → 4,8 | 8 / 6 / 7,5 → 7,2 |
| J8 | 5 / 6,5 / 6 → 5,8 | 7 / 6,5 / 7,5 → 7,0 |
| J9 | 7 / 6 / 5,5 → 6,2 | 7 / 6,5 / 7,5 → 7,0 |

**Nenhuma chegou a 8,5.** Pela regra das 2 rodadas, todas vão ao dono com as duas notas. Os três jurados votaram SIM ou SIM SE em todas as reescritas. Em rascunho e prévia o trabalho segue pela versão reescrita (nada disso é público nem custa dinheiro); o que é dele (título, validade do preço, formato da prévia) ficou com ele.

## J1
**Proposta do júri:** o cômodo a cômodo entra no e-book pago, nas 3 casas, na parte de cada casa. Só entra texto que o Revisor já passou; as páginas montadas passam pelo Designer e pelo Revisor antes do D20.
**Membros:** comprador: SIM SE a bancada "uns 40 cm" sair ou ganhar fonte, e cuidado com a densidade (E03 tem cerca de 2.000 palavras). Dinheiro: SIM, corre junto com a leitura do profissional e não alonga o caminho. Risco: SIM SE a linha do veto 3 (serviço da Casa Compacta) deixar de dizer "mantido".
**Como desfazer:** tirar as páginas no gerador e gerar o PDF de novo.
**Mostrado ao dono: sim** (25/11, na conversa: "2 ok"). Como desfazer: tirar as páginas no gerador e gerar o PDF de novo.

## J2
**Proposta do júri:** a equipe não escolhe o título. Fica com o dono, no cartão `p14` (as 3 opções que ele pediu), agora com a nota do Diretor: "Errar na planta sai caro" é o gancho mais forte, "A casa do seu lote" é médio. Enquanto ele não escolhe, prévias seguem com o título atual; a pasta e o anúncio esperam. Quando escolher: "de referência" na capa, e trocam-se juntos `atributos-que-vendem.md`, `VISUAL.md`, a capa do grátis e a saudação.
**Membros:** comprador: SIM. Dinheiro: SIM SE houver prazo, senão o PDF final espera. Risco: SIM SE o plano disser que só a pasta espera.
**Como desfazer:** nada mudou; o título se troca no `config.json`.
**Mostrado ao dono:** cartão `p14` atualizado em 24/11; ainda não respondido.

## J3
**Proposta do júri:** o grátis é literal ao que ele disse ("só a planta e um guia inicial"): a planta decorada da Casa Compacta, a ficha "Cabe no seu lote?" e o guia "Seu lote cabe?", depois de o Revisor ler o guia. Sem 3D, sem vista da rua, sem miniaturas das outras casas. O veto do `/oferta` para quem só cabe a Casa Compacta continua até existir a mensagem que diga o que a paga tem a mais. O PDF grátis congela antes da primeira semana do teste de preço.
**Membros:** comprador: SIM SE o guia passar no Revisor. Dinheiro: SIM SE a mensagem para quem só cabe a Casa Compacta entrar no D8. Risco: SIM SE o item 5 do guia valer para esse comprador.
**Como desfazer:** gerar o grátis de novo, antes do teste de preço começar.
**Mostrado ao dono:** cartão `j3-gratis-literal` criado em 24/11; ainda não visto. O que vai de graça é decisão dele: nada é gerado como final antes da resposta.

## J5
**Proposta do júri:** a equipe não decide (validade é parte do preço). A pergunta está com ele no cartão `p10`. Recomendação: vale o preço que a pessoa recebeu, e a mensagem diz "esse preço vale até domingo, dd/mm", sem "7 dias" (para não misturar com a garantia) e sem tom de urgência. Até ele responder vale a regra já aprovada pelo Revisor (o preço ofertado fica, `ESTRATEGIA.md:84`).
**Membros:** comprador: SIM SE a data não criar colchete novo contra o D9. Dinheiro: SIM SE for uma pergunta por cartão. Risco: SIM (8,5).
**Como desfazer:** trocar a frase nas respostas rápidas.
**Mostrado ao dono:** cartão `p10` com a recomendação, 24/11; ainda não respondido.

## J7
**Proposta do júri (invertida):** "Carro ou quintal" e "O que não fazer depois" entram no primeiro PDF, na parte geral, se passarem pelo Revisor enquanto a leitura do profissional corre; não seguram o PDF. "Antes do reboco" espera a planta de pontos. Nunca se anuncia "versão seguinte" ao comprador. A proposta original (deixar as três de fora) levou 4,8: ia contra o "seja bem detalhista" dele e não adiantava a venda.
**Membros:** comprador: SIM SE passarem pelo Revisor (8). Dinheiro: SIM SE o PDF sair sem elas quando não ficarem prontas. Risco: SIM SE o plano apontar o passo da planta de pontos.
**Como desfazer:** tirar as páginas no gerador e gerar de novo.
**Mostrado ao dono:** cartão `j7-paginas-do-arquiteto` criado em 24/11; ainda não visto.

## J8
**Proposta do júri:** a prévia são 3 a 5 telas de páginas reais do PDF final (depois do D3), da Casa Fita e da Família Compacta, com o aviso "Planta de referência", sem o 3D antigo e sem o cômodo a cômodo inteiro; no WhatsApp, imagens soltas. O formato ele escolhe no cartão `i5`. O anúncio continua com o "sim" dele.
**Membros:** comprador: SIM SE sem 3D antigo. Dinheiro: SIM SE nenhuma tela entregar o que se paga. Risco: SIM SE houver o selo "Imagem ilustrativa" onde tiver 3D.
**Como desfazer:** trocar as telas; nada é publicado sem ele.
**Mostrado ao dono:** cartão `i5` com a recomendação, 24/11; ainda não respondido.

## J9
**Proposta do júri:** "Como mobiliar" entra na parte de cada casa do pago, fora do grátis, só depois de o Diretor opinar e de o Arquiteto e o Revisor lerem a página (inclusive a palavra do título), com um arranjo só, o mesmo do cômodo a cômodo e do 3D refeito. Se não passar a tempo, o PDF sai sem ela.
**Membros:** comprador: SIM SE; a suposição "móvel pronto de loja" vira pergunta ao dono. Dinheiro: SIM SE o plano ganhar o passo. Risco: SIM SE o Diretor opinar primeiro.
**Como desfazer:** tirar as páginas no gerador e gerar de novo.
**Mostrado ao dono:** cartão `j9-como-mobiliar` criado em 24/11; ainda não visto.
