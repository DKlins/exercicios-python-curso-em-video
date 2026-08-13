aluno = {}
aluno['nome'] = str(input('Nome do aluno: ')).capitalize().strip()
aluno['media'] = float(input(f'Media de {aluno['nome']}: '))
if aluno['media'] < 6:
    aluno['situação'] = '\033[1;31mReprovado\033[m'
else:
    aluno['situação'] = '\033[1;32mAprovado\033[m'
print(f'O nome do aluno é {aluno['nome']}')
print(f'A sua média foi {aluno['media']}')
print(f'A sua situação é: {aluno['situação']}')
