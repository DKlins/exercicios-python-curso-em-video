from math import hypot
o = float(input('Valor do cateto oposto: '))
a = float(input('Valor do cateto adjacente: '))
h = hypot(o,a)
print(f'Comprimento da hipotenusa: {h:.2f}')