print('10 NÚMEROS DE UMA PROGRESSÃO ARITMÉTICA')
p = int(input('Digite o primeiro número: '))
r = int(input('Digite a razão dos números: '))
c = 10
soma = p
while c != 0:
    print(soma, end= ' -> ')
    soma += r
    c -= 1
print('FIM!')