soma = 0
for x in range (0, 6):
    n = int(input(f'Digite o {x}° número: '))
    if n % 2 == 0:
        soma += n
print(f'A soma dos números pares digitados é {soma}')
