d = int(input('Digite quantos dias o veículo foi alugado: '))
k = float(input('Digite quantos Km o veículo rodou: '))
p = (60 * d) + (0.15 * k)
print(f'Você precisará pagar: R${p:.2f}')