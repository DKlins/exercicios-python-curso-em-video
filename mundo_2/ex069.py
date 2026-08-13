m = h = ma = 0
p = 1
print('-='*10)
print('\033[1;31mCADASTRO DE PESSOAS\033[m')
while True:
    print('-='*10)
    sexo = c = ' '
    idade = int(input(f'Digite a \033[1;33midade\033[m da {p}° pessoa: '))
    while sexo not in 'MF':
        sexo = str(input(f'Digite o \033[1;33msexo\033[m da {p}° pessoa: [M/F] ')).strip().upper()[0]
    while c not in 'SN':
        c = str(input(f'Você quer \033[1;32mcontinuar\033[m para a {p+1}° pessoa? [S/N] ')).strip().upper()[0]
    if idade >= 18:
        ma += 1
    if sexo in 'M':
        h += 1
    elif sexo in 'F':
        if idade < 20:
            m += 1
    p += 1
    if c in 'N':
        print('-='*10)
        break

print(f'\033[1;33mVOCÊ CADASTROU {ma} PESSOAS MAIORES DE IDADE; \nVOCÊ CADASTROU {h} HOMENS; \n E {m} MULHERES MENORES QUE 20 ANOS.\033[m')
print('-='*20)


