def maior(*num):
    ma = ()
    for pos, n in enumerate(num):
        if pos == 0:
            ma = n
        elif n >= ma:
            ma = n
    if len(num) == 0:
        print('Você não tem nenhum número para analisar')
    else:
        print(f'O maior número apresentado em {num} foi {ma}')

maior(87,391, 624, 28, 99)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()