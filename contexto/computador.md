# No computador do dono: o que o Paydon pode e não pode

> Rede de segurança pedida pelo dono (26/11) antes de dar acesso total ao computador dele. Vale para toda conversa que rode no computador dele (app do Claude ou Remote Control). Afrouxar qualquer linha só com o "sim" dele.

## Pode, sem perguntar
- Ler e escrever **só dentro da pasta que ele compartilhou** (o cofre "Paydon Codes", que é este projeto).
- Rodar as ferramentas do projeto (`checar.py`, `salvar.py`, gerador em prévia) dentro dessa pasta.

## Pergunta antes, sempre
- Instalar ou atualizar programa, mudar configuração do Windows ou de outro app, mexer fora da pasta compartilhada.
- Qualquer coisa com conta, senha, banco, e-mail, WhatsApp ou navegador logado.

## Nunca
- Apagar arquivo: o que sair vai para a pasta `_lixeira/` do cofre, com data, e só ele esvazia.
- Ler pastas pessoais (Documentos, Fotos, Downloads, Desktop) fora da compartilhada; copiar dado pessoal para o projeto.
- Desligar antivírus, firewall, atualização ou backup; rodar script baixado sem ler; comandos de formatar, registro do Windows ou de administrador.
- Gastar, publicar, mandar mensagem ou e-mail (as regras de sempre valem aqui também).

## Registro
- Cada ação no computador dele que não seja só ler vira uma linha em `contexto/computador-registro.md` (data com `date`, o que fez, como desfazer).
- Antes da primeira sessão no computador: ele cria um ponto de restauração do Windows (ver o resumo da conversa de 26/11).
