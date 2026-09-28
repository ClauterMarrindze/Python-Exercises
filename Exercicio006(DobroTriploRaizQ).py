# Exercicio 006.
#=================================================================================
# Crie um algoritmo que lê um numero e mostre o seu dobro,
# triplo e raiz quadrada.

'''
==================================================================================
numero = float(input('Introduza um numero: '))

dobro = numero * 2
triplo = numero * 3
raizQuadrada = numero**(1/2)

# Mostrar o resultado usando o format.()
print('O dobro de {} é igual a {}.\nO triplo de {} é igual a {}.\n
A raiz quadrada de {} é igual a {:.2f}.'.format(numero, dobro, numero,
triplo, numero, raizQuadrada))

# Outra maneira usando o format.()
print('O dobro de {} é igual a {}.'.format(numero, dobro))
print('O triplo de {} é igual a {}.'.format(numero, triplo))
print('A raiz quadrada de {} é igual a {:.2f}.'.format(numero, raizQuadrada))

# Sem usar o format()
print('O dobro do número introduzido é igual a ', dobro)
print('O triplo do numero introduzido é igual a ', triplo)
print('A raiz quadrada do número introduzido é igual a ', raizQuadrada)
=============================================================================================
'''
print('=' * 40)
print('\033[1;34m{:^57}\033[m'.format('DOBRO \033[1;31mTRIPLO\033[1;36m RAIZ-QUADRADA\033[m'))
print('=' * 40)
numero = int(input('Introduza um numero : '))
cores = {'limpo':'\033[m',
         'branco':'\033[1;4;30m',
         'vermelho':'\033[1;4;31m',
         'verde':'\033[1;4;32m',
         'amarelo':'\033[1;4;33m',
         'azul':'\033[1;4;34m',
         'roxo':'\033[1;4;35m',
         'ciano':'\033[1;4;36m',
         'cinzento':'\033[1;4;37m'}

# Mostrar o resultado usando o format.()
print('=' * 40)
print('O dobro de {}{}{} é igual a {}{}{}.\nO triplo de {}{}{} é igual a {}{}{}.\n'
      'A raiz quadrada de {}{}{} é igual a {}{:.2f}{}.'
      .format(cores['ciano'], numero, cores['limpo'],
              cores['verde'], (numero * 2), cores['limpo'],
              cores['ciano'], numero, cores['limpo'],
              cores['amarelo'], (numero * 3), cores['limpo'],
              cores['ciano'], numero,cores['limpo'],
              cores['azul'], (numero ** (1/2)), cores['limpo']))
# raiz quadrada = pow(numero, (1/2))
print('=' * 40)
#============================================================================================