from urllib import request, error

try:
    site = request.urlopen('http://www.google.com.br')
except error.URLError:
    print('O site está indisponivel no momento!')
else:
    print('O site está disponível no momento')
