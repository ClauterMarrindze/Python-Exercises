#=========================================================================
'''
    Exercicio 018:
    Faca um programa que que leia um angulo qualquer e mostre na
    tela o valor do seno, cosseno e tangente desse angulo.
'''
import math

#==========================================================================
'''
import math
angulo = float(input('Digite o valor do angulo: '))

#seno = math.sin(math.radians(angulo)
#cosseno = math.cos(math.radians(angulo))
#tangente = math.tan(math.radians(angulo))

print('O angulo introduzido tem seno igual a {:.4f}'
      '\nO angulo introduzido tem cosseno igual a {:.4f}'
      '\nO angulo introduzido tem tangente igual a {:.4f}'
      .format(math.sin(angulo), math.cos(angulo), math.tan(angulo)))
'''
#==========================================================================
'''
from math import sin, cos, tan
angulo = float(input('Digite o valor do angulo: '))
print('='*20)
print('Seno = {:.3f}\nCosseno = {:.3f}\nTangente = {:.3f}'
      .format(sin(angulo), cos(angulo), tan(angulo)))
print('='*20)
'''
#=========================================================================
# CONVERTENDO PRA RADIANOS

from math import sin, cos, tan, radians

print('=' * 40)
print('{:^50}'.format('\033[1;34mCIRCULO TRIGONOMÉTRICO\033[m'))
print('=' * 40)
angulo = float(input('Digite o valor do angulo : '))
print('-' * 40)
cores = {'limpo':'\033[m','vermelho':'\033[1;31m','verde':'\033[1;32m',
         'amarelo':'\033[1;33m','azul':'\033[1;34m','roxo':'\033[1;35m',
         'ciano':'\033[1;36m','cinza':'\033[1;37m'}

print('O angulo de {}{}{}, tem \033[1;33mSENO\033[m de {}{:.2f}{}'
      '\nO angulo de {}{}{}, tem \033[1;34mCOSSENO\033[m de {}{:.2f}{}'
      '\nO angulo de {}{}{}, tem \033[1;35mTANGENTE\033[m de {}{:.2f}{}'
       .format(cores['roxo'], angulo, cores['limpo'],
               cores['verde'], sin(radians(angulo)), cores['limpo'],
               cores['roxo'], angulo, cores['limpo'],
               cores['amarelo'], cos(radians(angulo)), cores['limpo'],
               cores['roxo'], angulo, cores['limpo'],
               cores['vermelho'],tan(radians(angulo)), cores['limpo'],))
print('=' * 40)
print('{:^50}'.format('\033[1;33mFIM DO PROGRAMA\033[m'))
print('=' * 40)
#=========================================================================










