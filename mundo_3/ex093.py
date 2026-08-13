jogador = {}
gols = []
jogador['nome'] = str(input('Nome do jogador: ')).capitalize().strip()
partidas = int(input('Partidas jogadas: '))
for x in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {x+1}? ')))
jogador['gols'] = gols.copy()
jogador['total'] = sum(gols)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador['nome']} jogou {partidas} partidas')
for p, g in enumerate(gols):
    print(f'=> Na partida {p+1}, fez {g} gols.')
print(f'Foi um total de {sum(gols)} gols.')
