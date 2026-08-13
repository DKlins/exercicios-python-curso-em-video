def ficha(nome=False, gols= 0):
    """
    A função recebe e mostra o nome do jogador e o número de gols feito pelo mesmo.
    :param nome: Nome do jogador, se não for digitado nenhum, será declarado como <desconhecido>.
    :param gols: Número de gols feito pelo jogador, se não for digitado, será declarado com o valor 0 (ZERO).
    :return: 'O jogador {nome} fez {gols} gol(s) no campeonato'
    """
    if nome:
        print(f'O jogador {nome} fez {gols} gol(s) no campeonato')
    else:
        print(f'O jogador <desconhecido> fez {gols} gol(s) no campeonato')

n = str(input('Nome do jogador: ').strip().capitalize())
g = int(input('Número de gols: '))
ficha(n, g)
help(ficha)