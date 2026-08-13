from datetime import date
inf = {}
while True:
    inf['nome'] = str(input('Digite seu nome: ')).capitalize().strip()
    ano = int(input('Digite o ano de nascimento: '))
    inf['ano'] = date.today().year - ano
    inf['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
    if inf['ctps'] == 0:
        break
    inf['contratacao'] = int(input('Qual foi o ano de contração? '))
    inf['salario'] = float(input('Qual o valor do salário? '))
    inf['aposentadoria'] = 35 - (date.today().year - inf['contratacao'])
    break
print(f'Nome: {inf['nome']}')
print(f'Idade: {inf['ano']}')
print(f'Numero CTPS: {inf['ctps']}')
if inf['ctps'] != 0:
    print(f'Ano de contratação: {inf['contratacao']}')
    print(f'Salário: R${inf['salario']}')
    print(f'Vai se aposentar com {inf['aposentadoria'] + inf['ano']} anos.')
