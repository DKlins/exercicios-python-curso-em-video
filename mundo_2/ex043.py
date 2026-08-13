peso = float(input('Digite seu peso (Kg) : '))
altura = float(input('Digite sua altura (m): '))
imc = peso / (altura ** 2)
print(f'Seu IMC é de {imc:.1f}')
if imc < 18.5:
    print('\033[36mVocê está ABAIXO DO PESO IDEAL')
elif 18.5 < imc < 25:
    print('\033[32mVocê está no PESO IDEAL')
elif 25 < imc < 30:
    print('\033[33mVocê se encontra em SOBREPESO!')
elif 30 < imc < 40:
    print('\033[31mVocê se encontra em OBESIDADE!')
elif 40 < imc:
    print('\033[31mVocê se encontra em OBESIDADE MÓRBIDA! BUSQUE AJUDA!')