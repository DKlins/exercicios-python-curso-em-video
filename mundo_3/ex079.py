numeros = []
c = 'S'
while c not in 'N':
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não é possível adicionar...')
    c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print(f'O valores adicionados foram: {sorted(numeros)}')
