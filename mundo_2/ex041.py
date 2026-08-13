from datetime import date
ano = int(input('Ano de nascimento: '))
idade= date.today().year - ano
print(f'Você tem {idade} anos')
if 1 < idade <= 9:
    print('Categoria: MIRIM')
elif 10 < idade <= 14:
    print('Categoria: INFANTIL')
elif 15 < idade <= 19:
    print('Categoria: JUNIOR')
elif 19 < idade <= 20:
    print('Categoria: SÊNIOR')
elif idade > 20:
    print('Categoria: MASTER')


