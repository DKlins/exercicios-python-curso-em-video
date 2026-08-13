from random import randint
from time import sleep
print('-='*10)
print('    PAR OU ÍMPAR')
print('-='*10)
v = 0
while True:
    n = 11
    while n > 10:
        n = int(input('Digite um número de 1 a 10: '))
    escolha = 'oi'
    while escolha not in 'PI':
        escolha = str(input('Você quer par ou ímpar? [P/I] ')).upper().strip()
    cpu = randint(1, 10)
    soma = n + cpu
    print('-='*5, end= '')
    print('PROCESSANDO', end= '')
    print('-='*5)
    if soma % 2 == 0:
        sleep(1)
        print(f'Seu número foi \033[1;34m{n}\033[m, a CPU escolheu \033[1;35m{cpu}\033[m \nA soma deu PAR!', end=' -> ')
        if escolha in 'P':
            print('\033[1;32mVOCÊ GANHOU!\033[m \nVAMOS JOGAR NOVAMENTE!')
            print('-='*20)
            v += 1
        elif escolha in 'I':
            print('\033[1;31mVOCÊ PERDEU!\033[m')
            break
    elif soma % 2 != 0:
        sleep(1)
        print(f'Seu número foi \033[1;34m{n}\033[m, a CPU escolheu \033[1;35m{cpu}\033[m \nA soma deu IMPAR!', end=' -> ')
        if escolha in 'I':
            print('\033[1;32mVOCÊ GANHOU!\033[m \nVAMOS JOGAR NOVAMENTE!')
            print('-=' * 20)
            v += 1
        elif escolha in 'P':
            print('\033[1;31mVOCÊ PERDEU!\033[m')
            break
print(f'Você ganhou \033[1;33m{v} vezes consecutivas!\033[m OBRIGADO POR JOGAR! ')