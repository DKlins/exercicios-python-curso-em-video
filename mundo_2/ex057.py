parar = 0
while parar == 0:
    sexo = str(input('Qual o seu sexo? Digite M ou F: ')).strip().upper()
    if sexo in 'M':
        print(f'\033[1;34mOK. Seu sexo é Masculino!\033[m')
        parar += 1
    elif sexo in 'F':
        print(f'\033[1;35mOK. Seu sexo é Feminino!\033[m')
        parar += 1
    else:
        print('\033[1;31mOpção inválida! Digite novamente!\033[m')