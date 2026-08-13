from random import randint
from time import sleep
print('.'*33)
print('PENSANDO EM UM NÚMERO de 0 a 5...')
sleep(2)
print('.'*33)
print('PROCESSANDO...')
sleep(2)
numero = randint(0,5)
n = int(input('Tente descobrir o número em que eu pensei: '))
if n == numero:
    print(f'Você ACERTOU! Número {numero}')
else:
    print(f'Você ERROU! Número {numero}')
