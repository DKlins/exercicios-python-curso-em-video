from datetime import date
atual = date.today().year
maior = 0
menor = 0
for x in range (0, 7):
    nasc = int(input(f'Em que ano a {x}° nasceu? '))
    if atual - nasc >= 21:
        maior += 1
    else:
        menor += 1
print(f'Pessoa de maior: {maior} \nPessoas de menor: {menor}')