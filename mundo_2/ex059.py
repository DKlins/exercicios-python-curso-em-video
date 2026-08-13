n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
stop = 0
while stop == 0:
    print('-='*15)
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    o = int(input('Escolha uma opção: '))
    if o == 1:
        print(f'A soma dos números {n1} e {n2} é: {n1 + n2:.2f}')
    elif o == 2:
        print(f'A multiplicação dos números {n1} e {n2} é: {n1 * n2:.2f}')
    elif o == 3:
        if n1 > n2:
            print(f'{n1} é maior do que {n2}')
        elif n2 > n1:
            print(f'{n2} é maior do que {n1}')
        else:
            print(f'{n1} é igual a {n2}')
    elif o == 4:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
    elif o == 5:
        stop += 1
    else:
        print('OPÇÃO INVALIDA! TENTE NOVAMENTE')
        stop += 1
print('PROCESSO FINALIZADO!')




