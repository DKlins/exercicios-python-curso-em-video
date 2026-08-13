mulheres = []
pessoas = []
p = {}
idades = []
maiores = []
while True:
    p['nome'] = str(input('Digite o nome: ')).strip().capitalize()
    p['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    p['idade'] = int(input('Idade: '))
    pessoas.append(p.copy())
    idades.append(p['idade'])
    if p['sexo'] in 'F':
        mulheres.append(p.copy())
    p.clear()
    c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if c in 'N':
        break
print('-='*20)
print(f'-Foram cadastradas {len(pessoas)} pessoas.')
media = sum(idades)/len(pessoas)
print(f'-A média de idade do grupo é {media:.2f}')
print(f'-Todas as mulheres:', end=' ')
for m in mulheres:
    print(m['nome'], end=' ')
for p in pessoas:
        if p['idade'] > media:
            maiores.append(p['nome'])
print()
print(f'-Todas as pessoas com idade acima da média:', end=' ')
for p in maiores:
    print(p, end=' ')




