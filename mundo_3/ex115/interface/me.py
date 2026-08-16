def linha():
    print('-'*30)

def cabecalho(str):
    linha()
    print(f'{str:^30}')
    linha()

def menu(lista):
    linha()
    print(f'{'MENU PRINCIPAL':^30}')
    linha()
    for p, v in enumerate(lista):
        print(f'{p+1} - {v}')
    linha()

def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
            return num
        except:
            print('\033[1;31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO\033[m')



