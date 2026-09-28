# Exercicio 009.
#========================================================
#   Faça um programa que leia um numero inteiro qualquer
#   e mostre na tela a sua tabuada.

#=========================================================
#numero = int(input('Introduza um número desejado : '))
#  Usando o format().
'''
print('='*15)
print('{:^15}'.format(nome))
print('='*15)
print('{} x 1 = {}'.format(numero, numero*1))
print('{} x 2 = {}'.format(numero, numero*2))
print('{} x 3 = {}'.format(numero, numero*3))
print('{} x 4 = {}'.format(numero, numero*4))
print('{} x 5 = {}'.format(numero, numero*5))
print('{} x 6 = {}'.format(numero, numero*6))
print('{} x 7 = {}'.format(numero, numero*7))
print('{} x 8 = {}'.format(numero, numero*8))
print('{} x 9 = {}'.format(numero, numero*9))
print('{} x 10 = {}'.format(numero, numero*10))
print('{} x 11 = {}'.format(numero, numero*11))
print('{} x 12 = {}'.format(numero, numero*12))
print('{} x 13 = {}'.format(numero, numero*13))
print('{} x 14 = {}'.format(numero, numero*14))
print('{} x 15 = {}'.format(numero, numero*15))
print('='*15)
'''
#==========================================================


# Outra Maneira de fazer (Guanabara)
nome = 'TABUADA (V1.0)'
print('=' * 35)
print('\033[1;36m{:^35}\033[m'.format(nome))
print('=' * 35)
numero = (int(input('Introduza um numero a desejar : ')))
cores = {'limpo':'\033[m', 'vermelho':'\033[1;31m',
         'verde':'\033[1;32m', 'amarelo':'\033[1;33m',
         'azul':'\033[1;34m', 'roxo':'\033[1;35m',
         'ciano':'\033[1;36m', 'cinzento':'\033[1;37m'}

print('=' * 35)
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cores['cinzento'], numero, cores['limpo'], cores['vermelho'], 1, cores['limpo'], cores['verde'], numero*1, cores['limpo']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cores['cinzento'], numero, cores['limpo'], cores['amarelo'], 2, cores['limpo'], cores['verde'], numero*2, cores['limpo']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cores['cinzento'], numero, cores['limpo'], cores['azul'], 3, cores['limpo'], cores['verde'], numero*3, cores['limpo']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cores['cinzento'], numero, cores['limpo'], cores['roxo'], 4, cores['limpo'], cores['verde'], numero*4, cores['limpo']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cores['cinzento'], numero, cores['limpo'], cores['ciano'], 5, cores['limpo'], cores['verde'], numero*5, cores['limpo']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cores['cinzento'], numero, cores['limpo'], cores['vermelho'], 6, cores['limpo'], cores['verde'], numero*6, cores['limpo']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cores['cinzento'], numero, cores['limpo'], cores['amarelo'], 7, cores['limpo'], cores['verde'], numero*7, cores['limpo']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cores['cinzento'], numero, cores['limpo'], cores['azul'], 8, cores['limpo'], cores['verde'], numero*8, cores['limpo']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cores['cinzento'], numero, cores['limpo'], cores['roxo'], 9, cores['limpo'], cores['verde'], numero*9, cores['limpo']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cores['cinzento'], numero, cores['limpo'], cores['ciano'], 10, cores['limpo'], cores['verde'], numero*10, cores['limpo']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cores['cinzento'], numero, cores['limpo'], cores['vermelho'], 11, cores['limpo'], cores['verde'], numero*11, cores['limpo']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cores['cinzento'], numero, cores['limpo'], cores['amarelo'], 12, cores['limpo'], cores['verde'], numero*12, cores['limpo']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cores['cinzento'], numero, cores['limpo'], cores['azul'], 13, cores['limpo'], cores['verde'], numero*13, cores['limpo']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cores['cinzento'], numero, cores['limpo'], cores['roxo'], 14, cores['limpo'], cores['verde'], numero*14, cores['limpo']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cores['cinzento'], numero, cores['limpo'], cores['ciano'], 15, cores['limpo'], cores['verde'], numero*15, cores['limpo']))
# O {:2} é para colocar em formatacao de 2 digitos, assim
# estarao alinhados.
print('=' * 35)
#=============================================================








