print('10 NÚMEROS OU MAIS DE UMA PROGRESSÃO ARITMÉTICA')
p = int(input('Digite o primeiro número: '))
r = int(input('Digite a razão dos números: '))
c = 10
soma = p
cont = 0
while c != 0:
    print(soma)
    soma += r
    if c == 1:
        mais = int(input('Você quer mostrar mais quantos números? Para finalizar digite 0 '))
        if mais > 0:
            c += mais
    c -= 1
    cont += 1
print(f'FIM! \n{cont} termos mostrados.')