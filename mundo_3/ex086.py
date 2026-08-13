numeros = [[],[],[]]
for v in numeros:
    for x in range (0, 3):
        v.append(int(input(f'Digite um número para {[numeros.index(v), x]}: ')))
print('-='*30)
for v in numeros:
    for n in v:
        print(f'[{n:^5}]', end='')
    print()