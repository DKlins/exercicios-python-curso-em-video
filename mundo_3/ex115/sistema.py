from arquivo import arq
from interface import me

txt= 'davi.txt'

if not arq.arquivo_existe(txt):
    arq.criararquivo(txt)

options = ['Ver pessoas cadastradass', 'Cadastrar nova pessoa', 'Sair do sistema']
while True:
    me.menu(options)
    op = me.leiaint('Sua opcao: ')
    if op == 3:
        me.linha()
        print('Saindo do sistema...Volte sempre!')
        me.linha()
        break
    elif op == 1:
        arq.lerarquivo(txt)
    elif op == 2:
        me.cabecalho('NOVO CADASTRO')
        nome = str(input('NOME: '))
        idade = me.leiaint('IDADE:')
        arq.escreverarquivo(txt, nome, idade)

    else:
        print('\033[31mERRO! DIGITE UMA OPCAO VALIDA\033[m')