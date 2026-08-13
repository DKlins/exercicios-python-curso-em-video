p = 1
nomebarato = ' '
pt = caro = 0
print('-='*5, end= ' ')
print('SUA COMPRA', end=' ')
print('-='*5)
while True:
    nome = str(input(f'Digite o \033[1;33mnome\033[m do {p}° produto: ')).strip().capitalize()
    preço = float(input(f'Digite o \033[1;33mpreço\033[m do {p}° produto: R$'))
    c = ' '
    while c not in 'SN':
        c = str(input(f'Você quer adicionar mais produtos? [S/N] ')).strip().upper()[0]
        print('-='*20)
    if p == 1 or preço <= mp:
        mp = preço
        nomebarato = nome
    pt += preço
    if preço > 1000:
        caro += 1
    if c in 'N':
        break
    p += 1
print(f'TOTAL DA COMPRA: R${pt:.2f} \nQuantidade de produtos que custa mais de R$1000: {caro} \nNome do produto mais barato: {nomebarato}; Valor: {mp:.2f}')


