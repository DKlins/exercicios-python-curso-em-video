from time import sleep
valor = float(input('Valor do produto: R$'))
print('\033[1;34m1- À vista (Dinheiro/Cheque/Pix/Débito)\033[m\n\033[1;31m2- Cartão de crédito\033[m')
pagamento = int(input('Forma de pagamento: '))
print('PROCESSANDO...')
sleep(2)
if pagamento == 1:
    vf = valor - (valor * 10 / 100)
    print(f'O produto de valor: \033[33mR${valor:.2f}\033[m \ncom \033[4m10% DE DESCONTO\033[m \033[1;34mà vista\033[m \nFicará no valor de: \033[32mR${vf:.2f}')
elif pagamento == 2:
    print('\033[1;31mCARTÃO DE CRÉDITO\033[m \n[ 1 ]- À VISTA\n[ 2 ]- Em até 2x\n[ 3 ]- Em 3x ou mais')
    prazo = int(input('Em quantas vezes você vai dividir? '))
    print('PROCESSANDO...')
    sleep(2)
    if prazo == 1:
        vf = valor - (valor * 5 / 100)
        print(f'O produto de valor: \033[1;33mR${valor:.2f}\033[m \ncom \033[36m\033[4m5% de desconto\033[m\033[m no \033[1;31mcartão à vista \nFicará no valor de: \033[1;32mR${vf:2f}')
    elif prazo == 2:
        d = valor / prazo
        print(f'Manteremos o valor normal do produto \nEm 2x de: \033[32mR${d:.2f}\033[m no cartão')
    elif prazo >= 3:
        vf = valor + (valor * 20/ 100)
        d = vf / prazo
        print(f'O produto de valor: \033[1;33mR${valor:.2f}\033[m \nCom \033[4macréscimo de 20%\033[m no cartão\033[m \nFicou em {prazo}x de: R$\033[1;32m{d:.2f}')
else:
    print('Forma de pagamento não encontrada!')


