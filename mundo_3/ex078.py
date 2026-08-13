lista = []
for p in range(0, 5):
    lista.append(int(input(f'Digite o valor da posição {p}: ')))
    if p == 0:
        ma = me = lista[p]
    if lista[p] >= ma:
        ma = lista[p]
    if lista[p] < me:
        me = lista[p]
print(f'O maior número adicionado foi {ma} nas posições ', end= '')
for i, n in enumerate(lista):
    if n == ma:
        print(f'{i}...', end= '')
print(f'\nO menor número adicionado foi {me} nas posições ', end= '')
for i, n in enumerate(lista):
    if n == me:
        print(f'{i}...', end= '')
