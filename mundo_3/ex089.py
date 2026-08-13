alunos = []
temp = []
medias = []
a = 0
quant = 0
while True:
    temp.append(str(input('Digite o nome: ')).strip().capitalize())
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))
    medias.append(sum(temp[1:])/2)
    alunos.append(temp[:])
    temp.clear()
    c = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if c in 'N':
        break
print('-='*20)
print(f'{'Nº':<2}', end=' '*5)
print(f'{'Aluno':<10}', end=' '*5)
print(f'{'Media':<10}')
print('-'*30)
for pos, aluno in enumerate(alunos):
    print(f'{pos:<2}', end=' '*5)
    print(f'{aluno[0]:<10}', end=' '*5)
    print(f'{medias[pos]:<10}')
print('-'*30)
while a != 999:
    a = int(input('Quer ver as notas de qual aluno? (999 interrompe) '))
    if a != 999:
        print(f'As notas de {alunos[a][0]} foram: {alunos[a][1:]}')
        print('-'*30)
print('OBRIGADO! VOLTE SEMPRE!')