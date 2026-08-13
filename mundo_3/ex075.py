n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
n4 = int(input('Digite o quarto valor: '))
tupla = (n1, n2, n3, n4)
print(f'Você digitou os números:', end= ' ')
for n in tupla:
    print(n, end= ' ')
print(f'\nO valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O número três apareceu pela primeira vez na {tupla.index(3)+1}° posição')
else:
    print('O número 3 não apareceu nenhuma vez')
print('Os números pares foram:', end=' ')
for n in tupla:
    if n % 2 == 0 and n > 0:
        print(n, end=' ')



