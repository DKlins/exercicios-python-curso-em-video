def leiadinheiro(msg):
    while True:
        num = str(input(msg)).replace(',','.').strip()
        if num.isalpha() or num == '':
            print('\033[1;31mERRO! TENTE NOVAMENTE. DESSA VEZ, DIGITE UM VALOR NUMÉRICO\033[m')
        else:
            return float(num)

def leiaint(msg):
    while True:
        num = str(input(msg))
        if num.isnumeric():
            return int(num)
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
