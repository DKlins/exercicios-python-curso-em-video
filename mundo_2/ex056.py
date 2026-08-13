sidade = 0
velho = 0
nomevelho = ' '
mulheres = 0
for x in range(1, 5):
    print(f'===== {x}° PESSOA =====')
    nome = str(input('Digite seu nome: ')).strip().capitalize()
    idade = int(input('Digite sua idade: '))
    sexo = int(input('1- Masculino \n2- Feminino \nDigite seu sexo: '))
    sidade += idade
    if sexo == 1:
        if idade > velho:
            velho = idade
            nomevelho = nome
    elif sexo == 2:
        if idade < 20:
            mulheres += 1
print('='*10)
print(f'A média de idade do grupo é {sidade/4:.1f} \nNome do homem mais velho: {nomevelho} \nMulheres com menos de 20 anos: {mulheres}')


