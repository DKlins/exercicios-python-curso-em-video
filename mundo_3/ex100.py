from random import randint

def sorteia(lst):
    for x in range(0 , 5):
        lst.append(randint(1, 100))
    print(f'A lista com os 5 números aleatórios gerados: {lst}')

def soma(lst):
    so = 0
    for n in lst:
        if n % 2 == 0:
            so += n
    print(f'A soma dos números pares da lista é {so}')

lista = []
sorteia(lista)
soma(lista)
