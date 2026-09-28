#=================================================================
'''
EXERCICIO 023: Faca um programa que leia um numero de 0 a 9999
               e mostre na tela cada um dos digitos separados:
        Ex: Digite um numero : 1834
        unidades : 4
        dezenas : 3
        centenas : 8
        milhares: 1
'''
#===============================================================
'''
numero = int(input('Introduze um numero: '))
n = str(numero)
print('Analisando o número {}'.format(numero))
print('Milhares: {}'.format(n[0]))
print('Centenas: {}'.format(n[1]))
print('Dezenas: {}'.format(n[2]))
print('Unidades: {}'.format(n[3]))
'''
# Melhorando o programa
print('=' * 30)
print('\033[1;31m{:^30}\033[m'.format('MILHARES'))
print('=' * 30)
numero = int(input('Introduze um numero : '))
print('-' * 30)

milhares = numero // 1000 % 10
centenas = numero // 100 % 10
dezenas = numero // 10 % 10
unidades = numero // 1 % 10

print('Analisando o número \033[1;34m{}\033[m...'.format(numero))
print('\033[1;31mMilhares\033[m: \033[1;35m{}\033[m'.format(milhares))
print('\033[1;32mCentenas\033[m: \033[1;34m{}\033[m'.format(centenas))
print('\033[1;34mDezenas\033[m: \033[1;32m{}\033[m'.format(dezenas))
print('\033[1;35mUnidades\033[m: \033[1;31m{}\033[m'.format(unidades))
print('=' * 30)
print('\033[1;33m{:^33}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 30)
#==============================================================





