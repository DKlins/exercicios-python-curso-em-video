def dobro(n, op = False):
    d = n * 2
    return d if op is False else moeda(d)

def metade(n, op = False):
    m = n / 2
    return m if op is False else moeda(m)

def aumentar(n, a, op = False):
    porc = n * (a / 100)
    a = n + porc
    return a if op is False else moeda(a)

def diminuir(n, a, op = False):
    porc = n * (a / 100)
    d = n - porc
    return d if op is False else moeda(d)

def moeda(n):
    f = f'R${n:.2f}'.replace('.', ',')
    return f

def resumo(n, a, r):
    print('-'*30)
    print(f'{'RESUMO DO VALOR':^30}')
    print('-' * 30)
    print(f'Preço analisado: \tR${n}',)
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{a}% de aumento: \t{aumentar(n, a, True)}')
    print(f'{r}% de redução: \t{diminuir(n, r, True)}')
    print('-' * 30)

