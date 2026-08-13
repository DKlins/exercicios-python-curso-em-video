d = float(input('Digite a distância da viagem em Km: '))
if d <= 200:
    preço = 0.50 * d
else:
    preço = 0.45 * d
print(f'A distância da viagem é: {d:.2f} Km \nO valor da viagem ficou: R${preço:.2f}')