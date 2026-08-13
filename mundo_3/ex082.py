numeros = pares = impares = []
while True:
    numeros.append(int(input('Digite um valor para adicionar a lista: ')))
    c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if c in 'N':
        break
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(f'A lista criada: {numeros}')
print(f'Os números pares: {pares}')
print(f'Os números ímpares: {impares}')