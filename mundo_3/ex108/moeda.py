def dobro(n):
    d = n * 2
    return d

def metade(n):
    m = n / 2
    return m

def aumentar(n, a):
    porc = n * (a / 100)
    a = n + porc
    return a

def diminuir(n, a):
    porc = n * (a / 100)
    d = n - porc
    return d

def moeda(n):
    f = f'R${n:.2f}'.replace('.',',')
    return f

