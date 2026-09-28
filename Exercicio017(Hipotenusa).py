#====================================================================================
''' Exercicio 017:
    Faca um programa que leia o comprimento do cateto oposto
    e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento
    da hipotenusa.
    hip = ((cop**2) + (cAdj**2)) ** (1/2)
    '''
import math

#====================================================================================
'''
catetoOposto = float(input('Introduza o cateto oposto: '))
catetoAdjacente = float(input('Introduza o cateto adjacente: '))

hipotenusa = ((catetoOposto**2) + (catetoAdjacente**2))**(1/2)
print('O resultado da hipotenusa é : {:.2f}.'.format(hipotenusa))
'''
#====================================================================================
# USANDO IMPORT MATH
'''
import math
catetoOposto = float(input('Introduza o cateto oposto: '))
catetoAdjacente = float(input('Introduza o cateto adjacente: '))
hipotenusa = math.hypot(catetoOposto, catetoAdjacente)
'''
#====================================================================================
# USANDO SÓ A FUNCAO HIPOTENUSA, ECONOMICO

from math import hypot
print('=' * 40)
print('{:^50}'.format('\033[1;34mHIPOTENUSA\033[m'))
print('=' * 40)
catetoOpposto = float(input('Introduza o \033[1;33mcateto oposto\033[m : '))
catetoAdjacente = float(input('Introduza o \033[1;36mcateto adjacente\033[m : '))
cores = {'limpo':'\033[m','vermelho':'\033[1;31m','amarelo':'\033[1;33m',
         'ciano':'\033[1;36m','roxo':'\033[1;35m'}
print('-' * 40)
print('A hipotenusa irá medir {}{:.2f}{}'
      .format(cores['roxo'], hypot(catetoOpposto, catetoAdjacente), cores['limpo']))
print('=' * 40)
print('{:^50}'.format('\033[1;33mFIM DO PROGRAMA\033[m'))
print('=' * 40)
#===================================================================================







