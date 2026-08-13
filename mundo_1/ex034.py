s = float(input('Digite o seu salário: R$'))
if s > 1250:
    a = (10 * s / 100) + s
    print(f'O seu novo salário, com aumento de 10%, ficou: R${a:.2f}')
else:
    a = (15 * s / 100) + s
    print(f'O seu novo salário, com aumento de 15%, ficou: R${a:.2f}')

