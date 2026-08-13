import moeda

v = float(input('Digite o valor: R$').replace(',','.'))
print(f'O dobro de {moeda.moeda(v)} é {moeda.moeda(moeda.dobro(v))}')
print(f'A metade de {moeda.moeda(v)} é {moeda.moeda(moeda.metade(v))}')
print(f'Aumentando 10% temos {moeda.moeda(moeda.aumentar(v, 10))}')
print(f'Diminuindo 50% temos {moeda.moeda(moeda.diminuir(v, 50))}')