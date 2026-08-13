velocidade = float(input('Digite qual foi a velocidade do carro em Km/h: '))
if velocidade > 80:
    valor = 7 * (velocidade-80)
    print(f'Você foi MULTADO! \nSua velocidade excedeu o limite de 80Km/h \nValor a pagar: R${valor:.2f}')
else:
    print('A sua velocidade está dentro do limite! Dirija sempre com segurança!')
