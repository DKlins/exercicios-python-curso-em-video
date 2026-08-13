casa = float(input('Valor do imóvel: R$'))
salario = float(input('Seu salário atual: R$'))
anos = int(input('Anos a pagar: '))
meses = anos * 12
prestacao = casa / meses
porc = (prestacao / salario) * 100
if porc <= 30:
    print(f'\033[1;32mEmpréstimo aprovado! \033[m \nSeu salário de \033[32mR${salario:.2f}\033[m \nÉ compatível com a prestação de: \033[31mR${prestacao:.2f}\033[m \nA ser pago durante: \033[33m{meses} meses\033[m')
elif porc > 30:
    print(f'\033[31mEmpréstimo negado! \nSeu salário de R${salario:.2f} \nNÃO é compatível com a prestação de: R${prestacao:.2f} \nA ser pago durante: {meses} meses')