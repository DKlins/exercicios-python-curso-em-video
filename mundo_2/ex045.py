from random import randint
from time import sleep
itens = ('Oi', 'Pedra', 'Papel', 'Tesoura')
escolha = randint(1,3)
computador = itens[escolha]
print('-'*10)
print('\033[31mJOKENPO.PY\033[m')
print('-'*10)
print('LOADING...')
sleep(1)
print('[ 1 ] Pedra \n[ 2 ] Papel \n[ 3 ] Tesoura')
escolha2 = int(input('Escolha uma opção: '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!')
sleep(1)
player = itens[escolha2]
print('-='*10)
print(f'Você escolheu: {player} \nCPU escolheu: {computador}')
if escolha2 == 1:
    if escolha == 1:
        print('\033[1;36mEMPATE!\033[m')
    elif escolha == 2:
        print('\033[1;31mVOCÊ PERDEU!\033[m')
    elif escolha == 3:
        print('\033[1;32mVOCÊ GANHOU!\033[m')
elif escolha2 == 2:
    if escolha == 1:
        print('\033[1;32mVOCÊ GANHOU!\033[m')
    elif escolha == 2:
        print('\033[1;36mEMPATE!\033[m')
    elif escolha == 3:
        print('\033[1;31mVOCÊ PERDEU!\033[m')
elif escolha2 == 3:
    if escolha == 1:
        print('\033[1;31mVOCÊ PERDEU!\033[m')
    elif escolha == 2:
        print('\033[1;32mVOCÊ GANHOU!\033[m')
    elif escolha == 3:
        print('\033[1;36mEMPATE!\033[m')
else:
    print('\033[1;31mOPÇÃO INVÁLIDA! TENTE NOVAMENTE!\033[m')
print('-='*10)

