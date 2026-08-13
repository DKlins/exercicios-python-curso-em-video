pessoas = []
pesos = []
pesados = []
leves = []
dados = []
while True:
    dados.append(str(input('Digite seu nome: ')).strip().capitalize())
    dados.append(float(input('Digite o seu peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    c = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if c in 'N':
        break
for p in pessoas:
    pesos.append(p[1])
for p in pessoas:
    if max(pesos) == p[1]:
        pesados.append(p[0])
    elif min(pesos) == p[1]:
        leves.append(p[0])
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi {max(pesos)}Kg das pessoas: ', end='')
for p in pesados:
    print(p, end='...')
print(f'\nO menor peso foi {min(pesos)}Kg das pessoas: ', end='')
for p in leves:
    print(p, end='...')
