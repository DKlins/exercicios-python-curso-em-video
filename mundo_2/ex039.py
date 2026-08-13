from datetime import date
nascimento = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento
if idade < 18:
    print(f'\033[1;32mVocê ainda vai se alistar ao serviço militar no ano de {nascimento+18}!\033[m \n\033[33mFaltam: {18-idade} anos')
elif idade > 18:
    print(f'\033[1;31mJá passou o tempo de se alistar em: {idade-18} anos\033[m \n\033[1;32mProcure a junta militar!\nPendente desde: {nascimento+18}')
else:
    print(f'\033[1;32mÉ hora de se alistar! Procure a junta militar!')
