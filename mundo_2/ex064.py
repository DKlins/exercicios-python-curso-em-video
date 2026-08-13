n = s = c = 0
while n != 999:
    n = int(input('Digite um número inteiro (digite 999 para sair): '))
    if n != 999:
        s += n
        c += 1
print(f'Você digitou {c} números \nA soma entre eles foi {s}')

