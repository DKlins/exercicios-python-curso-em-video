frase = str(input('Digite uma frase: ')).strip().upper()
se = frase.replace(' ','')
esarf = se[::-1]
print(f'A frase {se} ao contrário é {esarf}')
if esarf in se:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo!')
