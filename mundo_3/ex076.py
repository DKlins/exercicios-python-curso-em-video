lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-'*50)
print(f'{'LISTAGEM DE PREÇOS':^50}')
print('-'*50)
for item in lista:
    if type(item) == str:
        print(f'{item:.<40}', end= '')
    elif type(item) == float:
        print(f'R${item:>8.2f}')
print('-'*50)