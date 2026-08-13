numeros = []
quant = 0
while True:
    numeros.append(int(input('Digite um valor para adicionar a lista: ')))
    c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if c in 'N':
        break
numeros.sort(reverse=True)
print(f'Foram digitados {len(numeros)} números \nOs valores em ordem decrescente: {numeros}')
if 5 in numeros:
    print(f'O número 5 se encontra na lista!')
else:
    print('O número 5 não se encontra na lista')