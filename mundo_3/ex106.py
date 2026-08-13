from time import sleep

def ajuda(msg):
    while True:
        hel = str(input(msg).lower().strip())
        if hel in 'fim':
            print('\033[1;32;40mOBRIGADO POR USAR O SISTEMA DE AJUDA PYHELP! VOLTE SEMPRE\033[m')
            return
        else:
            print(f"\033[1;44mAcessando manual do comando '{hel}'...\033[m")
            sleep(0.5)
            print('\033[7;40m')
            help(hel)

print('\033[1;32;40m~'*40)
print('BEM VINDO AO SISTEMA DE AJUDA PYHELP')
print('~'*40)
ayuda = ajuda('\033[mFunção ou biblioteca > ')

