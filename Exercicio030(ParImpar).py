#======================================================================================
'''
EXERCICIO 030: Crie um programa que leia um numero inteiro e mostre se ele é par
ou impar.
'''
#======================================================================================
'''
numero = int(input('Introduze um numero inteiro:'))
if numero % 2 == 0:
    #print('O numero é Par.')
    print('O número {} é Par.'.format(numero))
else:
    #print('O número é impar.')
    print('O número {} é Impar.'.format(numero))
'''
#======================================================================================
print('=' * 50)
print('{:^50}'.format('\033[1;36mPAR\033[m / \033[1;35mIMPAR\033[m'))
print('=' * 50)
numero = int(input('Introduze um \033[1;37mnumero\033[m \033[1;36minteiro\033[m : '))
print('-' * 50)
cores = {'limpo':'\033[m','branco':'\033[1;30m' ,'vermelho':'\033[1;31m', 'verde':'\033[1;32m',
         'amarelo':'\033[1;33m', 'azul':'\033[1;34m', 'roxo':'\033[1;35m', 'ciano':'\033[1;36m',
         'cinzento':'\033[1;37m'}

if numero % 2 == 1:
    #print('O número é Impar.')
    print('O \033[1;37mnumero\033[m {}{}{} é {}Impar{}.'.format(cores['ciano'], numero, cores['limpo'],
                                                cores['vermelho'], cores['limpo']))
    print('=' * 50)
else:
    #print('O número é Par.')
    print('O \033[1;37mnúmero\033[m {}{}{} é {}Par{}.'.format(cores['ciano'], numero, cores['limpo'],
                                              cores['verde'], cores['limpo']))
    print('=' * 50)
print('\033[1;33m{:^50}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 50)
#=====================================================================================
#                                    MODO GUANABARA

