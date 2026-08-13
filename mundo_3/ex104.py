def leiaint(msg):
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            return valor
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')