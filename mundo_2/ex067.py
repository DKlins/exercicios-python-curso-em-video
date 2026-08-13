num = 1
n = int(input('Digite um número para ver sua TABUADA: (digite um número negativo para sair) '))
print('-='*20)
while True:
    if n < 0:
        break
    print(f'{n} X {num} = {n * num}')
    if num == 10:
        num = 0
        print('-='*20)
        n = int(input('Digite um número para ver sua TABUADA: (digite um número negativo para sair) '))
        print('-=' * 20)
    num += 1
print('PROGRAMA FINALIZADO')
