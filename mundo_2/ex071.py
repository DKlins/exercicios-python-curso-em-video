nome = 'DK BANK'
print('='*90)
print(f'{nome:^90}')
print('='*90)
n = int(input('Qual valor a ser sacado? R$'))
cedula = 50
quantidade = 0
while True:
    if n >= cedula:
        n -= cedula
        quantidade += 1
    else:
        if quantidade > 0:
            print(f'Total de {quantidade} cédulas de R${cedula}')
            quantidade = 0
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        if n == 0:
            print('Obrigado! Volte sempre!')
            print('=' * 90)
            break