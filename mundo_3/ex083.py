exp = str(input('Digite uma expressão com parênteses: ')).strip()
if exp.count('(') == exp.count(')'):
    if exp.index('(') < exp.index(')'):
        print('Sua expressão é válida')
    else:
        print('Sua expressão não é válida')

