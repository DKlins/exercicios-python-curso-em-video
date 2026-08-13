tabela = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco', 'Vitória', 'Atlético MG', 'Fluminense', 'Grêmio', 'Juventude', 'Bragantino', 'Athletico PR', 'Criciúma', 'Atlético GO', 'Cuiabá')
print('BRASILEIRÃO 2024 \nOs 5 primeiros colocados:')
for pos, time in enumerate(tabela):
    if pos < 5:
        print(f'{pos+1}°- {time}')
    elif pos > 15:
        if pos == 16:
            print('-='*20)
            print('Os 4 últimos colocados:')
        print(f'{pos+1}°- {time}')
print('-='*20)
print('Times em ordem alfabética: ')
for time in sorted(tabela):
    print(time)
print('-='*20)
print(f'O Corinthians está na {tabela.index('Corinthians')+1}° posição ')
