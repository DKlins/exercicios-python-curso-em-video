n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
if n1 > n2:
    print('\033[1;32mO primeiro valor é maior')
elif n2 > n1:
    print('\033[1;32mO segundo valor é maior')
else:
    print('\033[1;31mNão existe valor maior, os dois são iguais!')