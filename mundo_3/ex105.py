def notas(*num, sit=False):
        """
        Recebe as notas do aluno e retorna diferentes informações.
        :param num: Notas do aluno
        :param sit: Situação do aluno
        :return: Retorna a maior nota, a menor nota, a média das notas e a situação se solicitada
        """
        r = {}
        r['Quantidade'] = len(num)
        r['Maior'] = max(num)
        r['Menor'] = min(num)
        r['Media'] = sum(num) / len(num)
        if sit:
            if r['Media'] >= 6:
                r['Situação'] = 'BOA'
            else:
                r['Situação'] = 'RUIM'
        return r

resp = notas(5.5, 10, 6, sit= True)
print(resp)
help(notas)
