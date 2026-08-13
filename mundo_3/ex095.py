jogador = {}
jogadores = []
gols = []
while True:
    jogador['nome'] = str(input('Nome do jogador: ')).capitalize().strip()
    partidas = int(input('Partidas jogadas: '))
    for x in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {x+1}? ')))
    jogador['gols'] = gols.copy()
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    jogador.clear()
    gols.clear()
    c = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if c in 'N':
        break
print('-='*30)
print(f'{'cod':<5}', end=' ')
print(f'{'nome':<10}', end='')
print(f'{'gols':<10}', end='')
print(f'{'total'}')
print('-'*30)
for pos, j in enumerate(jogadores):
    print(f'{pos:<5}', end=' ')
    print(f'{j['nome']:<10}', end='')
    print(f'{j['gols']}', end='')
    print(f'{'.':<7}', end='')
    print(f'{j['total']}')
while True:
    print('-'*30)
    joga = int(input('Quer ver as informações de qual jogador? (Digite 999 para sair) '))
    print(f'LEVANTAMENTO DO JOGADOR {jogadores[joga]['nome']}:')
    for pos, p in enumerate(gols):
        print(f'No jogo {pos} fez {p} gols.')
    print('-'*30)
    if joga == 999:
        break
