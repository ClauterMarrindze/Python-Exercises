#==================================================================================
''' Exercicio 016:
    Crie um programa que leia um numero real qualquer pelo teclado
    e mostre na tela a sua porcao inteira.
    ex: Digite um numero : 6.127
    O numero 6.127 tem a parte inteira 6
'''
#=================================================================================
'''
num = float(input('Introduze um numero qualquer: '))
porcaoInteira = int(num)
#print('A parte Inteira do numero é {}.'.format(porcaoInteira))
print('O numero {} tem a parte inteira {}.'.format(num, porcaoInteira))
'''
#=================================================================================
'''
CODIGO ECONOMICO

num = float(input('Introduze um numero qualquer: '))
#print('A parte Inteira do numero é {}.'.format(porcaoInteira))
print('O numero {} tem a parte inteira {}.'.format(num, int(num)))
'''
#=================================================================================
# Usando import
'''
import math
num = float(input('Introduze um numero: '))
print('O numero {} tem a parte inteira {}.'.format(num, math.trunc(num)))
'''
#=================================================================================
# CODIGO ECONOMICO E ESPECIFICO
from math import trunc
print('=' * 40)
print('{:^50}'.format('\033[1;36mPARTE INTEIRA DE UM NUMERO\033[m'))
print('=' * 40)
num = float(input('Introduze um numero : '))

cores = {'limpo': '\033[m','vermelho': '\033[1;31m','ciano':'\033[1;36m',
         'roxo':'\033[1;35m'}
print('-' * 40)
print('A parte inteira do numero {}{}{} é {}{}{}.'
      .format(cores['vermelho'], num, cores['limpo'],
              cores['ciano'], trunc(num), cores['limpo']))
print('=' * 40)
print('{:^50}'.format('\033[1;33mFIM DO PROGRAMA\033[m'))
print('=' * 40)
#==================================================================================
