import moeda

v = float(input('Digite o valor: R$'))
print(f'O dobro de R${v} é {moeda.dobro(v)}')
print(f'A metade de R${v} é {moeda.metade(v)}')
print(f'Aumentando 10% de R${v} temos {moeda.aumentar(v, 10)}')
print(f'Diminuindo 50% de R${v} temos {moeda.diminuir(v, 50)}')