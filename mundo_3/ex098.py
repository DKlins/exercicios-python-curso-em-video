from time import sleep

def contador(a, b, c):
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    cont = a
    while True:
        print(cont, end=' ')
        sleep(0.5)
        if a < b:
            cont += c
            if cont > b:
                break
        elif a > b:
            cont -= c
            if cont < b:
                break
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
