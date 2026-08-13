from random import randint
from time import sleep
print('\033[1;36;40mJOGO DESCUBRA O NÚMERO\033[m')
sleep(0.5)
print('\033[1;40m.\033[m'*33)
print('\033[1;40m.PENSANDO EM UM NÚMERO de 1 a 10.\033[m')
print('\033[1;40m.\033[m'*33)
sleep(2)
print('\033[1;40mPROCESSANDO...\033[m')
sleep(1)
numero = randint(1,10)
contador = 1
stop = 0
while stop == 0:
    n = int(input('\033[1;33;40mEM QUE NÚMERO EU PENSEI?\033[m '))
    if n == numero:
        print('\033[1;36;40m-=\033[m'*20)
        print(f'\033[1;32;40m    VOCÊ ACERTOU! PENSEI NO NÚMERO: {numero}\033[m \n        \033[1;32;40mNÚMERO DE TENTATIVAS: {contador}\033[m')
        stop += 1
        contador += 1
    elif n > 10:
        print('\033[1;31;40mOPÇÃO INVÁLIDA! APENAS NÚMERO DE 1 A 10\033[m')
    elif n != numero:
        print(f'\033[1;31;40mVOCÊ ERROU! TENTE NOVAMENTE\033[m')
        contador += 1
        if n > numero:
            print('\033[40mUm pouco menos...\033[m')
        else:
            print('\033[40mUm pouco mais...\033[m')
print('\033[1;36;40m-=\033[m'*20)


