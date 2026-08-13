n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print(f'\033[33mSua média foi: {media}\033[m \n\033[31mREPROVADO!')
elif 5 <= media < 7:
    print(f'\033[33mSua média foi: {media}\033[m \n\033[31mRECUPERAÇÃO!')
else:
    print('\033[1;32mAPROVADO! PARABÉNS!')