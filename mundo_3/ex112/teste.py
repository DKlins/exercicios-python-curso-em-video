from utilidadesCeV import moeda
from utilidadesCeV.dado import leiadinheiro, leiaint

p = leiadinheiro('Digite o valor: R$')
moeda.resumo(p, 50, 10)