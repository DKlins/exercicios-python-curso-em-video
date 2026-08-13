r1 = float(input('EM CENTÍMETROS \nDigite o comprimento primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
if r1 > r2 and r1 > r3:
    if r2 + r3 > r1:
        print('As retas PODEM formar um triângulo!')
    else:
        print('As retas NÃO podem formar um triângulo!')
if r2 > r1 and r2 > r3:
    if r1 + r3 > r2:
        print('As retas PODEM formar um triângulo!')
    else:
        print('As retas NÃO podem formar um triângulo')
if r3 > r1 and r3 > r2:
    if r1 + r2 > r3:
        print('As retas PODEM formar um triângulo!')
    else:
        print('As retas NÃO podem formar um triângulo!')
