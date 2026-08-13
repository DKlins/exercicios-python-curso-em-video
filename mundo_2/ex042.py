r1 = float(input('EM CENTÍMETROS \nDigite o comprimento primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[1;32mAs retas PODEM formar um triângulo!\033[m')
    if r1 == r2 == r3:
        print('O triângulo é EQUILÁTERO!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('O triângulo é ISÓSCELES!')
    elif r1 != r2 != r3 != r1:
        print('O triângulo é ESCALENO!')
else:
    print('\033[1;31mAs retas NÃO podem formar um triângulo!\033[m')
