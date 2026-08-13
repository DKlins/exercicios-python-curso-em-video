n = int(input('Digite um número inteiro: '))
total = 0
for x in range(1, n + 1):
    if n % x == 0:
        total += 1
print(f'O número {n}', end=' ')
if total == 2:
    print('é um número primo!')
else:
    print('NÃO é um número primo!')