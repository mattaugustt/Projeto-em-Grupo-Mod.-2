from entrevista import Entrevista  #importa a classe 'Entrevista' do arquivo 'entrevista'
import csv  #apesar de importarmos no arquivo do código, é melhor prevenir
from datetime import datetime as dt  #o mesmo motivo do anterior.

class main():
    pass

print(
'''########################################################
#           Pesquisa de mercado sobre animes           #
########################################################'''
)
print('')
e1 = Entrevista()
e1.pesquisa()
print('Finalizado. Obrigado!')
