m = ma = me = cont = 0
c = 'S'
while c not in 'N':
    n = int(input('Digite um número inteiro: '))
    c = str(input('Você quer continuar? (S/N) ')).strip().upper()
    if cont == 0:
        ma = me = n
    m += n
    if n > ma:
        ma = n
    elif n < me:
        me = n
    cont += 1
print(f'A media entre os números foi {m/cont} \nO maior número foi {ma} \nO menor número foi {me}')