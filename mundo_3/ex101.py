from datetime import date

def voto(year):
    """"A função serve para mostrar a condição de voto do usuário.
    São possível três condições:
    :OPCIONAL- Você tem 70 anos ou mais e pode optar por não votar.
    :OBRIGATÓRIO- Você tem 18 anos ou mais e tem o voto obrigatório.
    :NEGADO- Você tem menos de 18 anos e não precisa votar."""
    idade = date.today().year - year
    resposta = ''
    if idade > 18 and idade >= 70:
        resposta = 'OPCIONAL'
    elif idade >= 18:
        resposta = 'OBRIGATÓRIO'
    elif idade < 18:
        resposta = 'NEGADO'
    return resposta

ano = int(input('Digite o seu ano de nascimento: '))
print(f'Você tem {date.today().year - ano} anos e tem o voto: {voto(ano)}')