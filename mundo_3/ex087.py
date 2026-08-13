numeros = [[],[],[]]
somap = soma3 = 0
for v in numeros:
    for x in range (0, 3):
        v.append(int(input(f'Digite um número para {[numeros.index(v), x]}: ')))
print('-='*30)
for v in numeros:
    if numeros.index(v) > 0:
        print('\n', end='')
    for n in v:
        if v.index(n) == 2:
            soma3 += n
        if n % 2 == 0:
            somap += n
        print(f'[{n:^5}] ', end='')
print(f'\nA soma dos valores pares é {somap}.')
print(f'A soma dos valores da terceira coluna é {soma3}.')
print(f'O maior valor da segunda linha é {max(numeros[1])}.')