print('10 NÚMEROS DE UMA PROGRESSÃO ARITMÉTICA')
p = int(input('Digite o primeiro número: '))
r = int(input('Digite a razão dos números: '))
for x in range (p, p + r*10, r):
    print(x, end= ' ')
print('FIM!')
