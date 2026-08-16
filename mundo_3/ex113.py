def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
            return num
        except (TypeError, ValueError):
            print('\033[1;31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mERRO! O usuário optou por não digitar nada\033[m')
            return 0

def leiafloat(msg):
    while True:
        try:
            num = float(input(msg))
            return num
        except (TypeError, ValueError):
            print('\033[1;31mERRO! DIGITE UM NUMERO VALIDO\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mERRO! O usuário optou por não digitar nada\033[m')
            return 0

n = leiaint('Digite um número inteiro: ')
n2 = leiafloat('Digite um numero flutuante: ')
print(f'Você digitou o número inteiro {n}')
print(f'Voce digitou o numero flutuante {n2}')


