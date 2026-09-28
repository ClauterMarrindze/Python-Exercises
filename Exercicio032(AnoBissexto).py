#=========================================================================================
'''
    EXERCICIO 032:
    Faca um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
'''
#==========================================================================================
#import datetime
from datetime import date


print('=' * 50)
print('\033[1;31m{:^50}\033[m'.format('ANO BISSEXTO'))
print('=' * 50)
print('''\033[1;37mChama-se ano BISSEXTO o ano ao qual é acrescentado
um dia extra ficando ele com 366 dias, um dia a mais
do que os anos normais de 365 dias, ocorrendo a
cada quatro anos\033[m.\033[1;36m 
(excepto anos multiplos de 100 que não são múltiplos de 400)\033[m''')
print('=' * 60)

print('\033[1;35mNB: Se fores digitar 0, ira analisar o ano atual\033[m.')
print('-' * 60)
ano = int(input('Introduze o \033[1;32mano de analise\033[m : '))

cores = {'limpo':'\033[m','branco':'\033[1;30m','vermelho':'\033[1;31m',
         'azul':'\033[1;34m','amarelo':'\033[1;33m','verde':'\033[1;32m','roxo':'\033[1;35m',
         'ciano':'\033[1;36m','cinzento':'\033[1;37m'}

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {}{}{} é \033[1;36mBISSEXTO\033[m'.format(cores['cinzento'], ano, cores['limpo']))
else:
    print('O ano {}{}{} \033[1;31mnão\033[m é \033[1;35mBISSEXTO\033[m'
          .format(cores['cinzento'], ano, cores['limpo']))
print('=' * 40)
print('\033[1;33m{:^40}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 40)

#============================================================================================