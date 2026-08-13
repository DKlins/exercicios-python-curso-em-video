from random import randint
from time import sleep
jogador = {}
jogadores = [[],[],[],[]]
print('Valores sorteados:')
for j in range (0, 4):
    jogador[f'{j+1}'] = randint(1, 6)
    print(f'O jogador {j+1} tirou {jogador[f'{j+1}']}')
    jogadores[j].append(jogador[f'{j+1}'])
print('Ranking dos jogadores:')
jogadores.sort(reverse=True)
for pos,joga in enumerate(jogadores):
    print(f'{pos+1}° Lugar:', end=' ')
    print(joga)