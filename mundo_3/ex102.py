def fatorial(num, show=False):
    """
    Digite um número e saiba o resultado do seu fatorial.
    :param num: Número a ser analisado
    :param show: Opcional, mostra o cálculo feito a chegar no resultado no fatorial. Por padrão, show=False.
    :return: O valor do fatorial, se declarado show=True, também é mostrado o cálculo feito.
    """
    pos = num - 1
    while pos >= 1:
        if show:
            if pos == num - 1:
                print(num, end='x')
            if pos > 1:
                print(f'{pos}', end='x')
            else:
                print(f'{pos}', end='= ')
        num *= pos
        pos -= 1
    print(num)

fatorial(10, show=True)
fatorial(5, show=False)