peso = float(input('Digite o seu peso(kg): '))
maior = 0
menor = peso
for x in range (0, 4):
    peso = float(input('Digite o seu peso(kg): '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f'Menor peso: {menor}kg \nMaior peso: {maior}kg')
