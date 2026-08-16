
def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criacao do arquivo!')

def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<20}{dado[1]:>3} anos')
    finally:
        a.close()

def escreverarquivo(txt, nome='desconhecido', idade=0):
    try:
        a = open(txt, 'at')
    except:
        print('Ocorreu um erro ao abrir o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Nao foi possivel escrever no arquivo')
    finally:
        a.close()



