from time import sleep
from random import randint
jogos = []
temp = []
print('-'*30)
print(f'{'JOGA NA MEGA SENA':^30}')
print('-'*30)
j = int(input('Quantos jogos você quer que eu sorteie? '))
for x in range (0, j):
    for numero in range (0, 6):
        random = randint(1, 60)
        if random not in temp:
            temp.append(random)
    jogos.append(temp[:])
    temp.clear()
print(f'Sorteando {j} jogos...')
sleep(1)
for pos,jogo in enumerate(jogos):
    print(f'Jogo {pos+1}: {sorted(jogo)}')
    sleep(1)
print(f'{'BOA SORTE!':^30}')





