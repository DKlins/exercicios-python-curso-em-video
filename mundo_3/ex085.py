numeros = [[],[]]
for x in range(0, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0 and n not in numeros:
        numeros[0].append(n)
    elif n % 2 == 1 and n not in numeros:
        numeros[1].append(n)
print(f'Os valores pares digitados foram: {sorted(numeros[0])}')
print(f'Os valores ímpares digitados foram: {sorted(numeros[1])}')

