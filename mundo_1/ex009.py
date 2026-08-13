n = int(input('TABUADA \nDigite um número: '))
print('='*12)
for numero in range(1,11):
    print(f'{n} X {numero:2} = {n*numero}')
print('='*12)