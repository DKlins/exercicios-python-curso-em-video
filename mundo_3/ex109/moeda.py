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
