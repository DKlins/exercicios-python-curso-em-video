n = int(input('Digite um número para mostrar o seu fatorial: '))
count = n
f = 1
while count > 0:
    print(count, end= '')
    print(' X ' if count > 1 else ' = ', end= '')
    f *= count
    count -= 1
print(f'O fatorial do número {n} é {f}')