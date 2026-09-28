#==================================================================================================================
'''
Exercicio 046 : Faca um programa que mostre na tela uma contagem regressiva
para o estouro e fogos de artificio, indo de 10 até 0,com pausa de 1 segundo
entre eles.
'''
#==============================================================================================================
from time import sleep
from rich import emoji

print('=' * 50)
print('\033[1;36m{:^50}\033[m'.format('FOGOS DE ARTIFICIO'))
print('=' * 50)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('=' * 50)
print('\033[1;35m{:^50}\033[m'.format('BANG! BANG! BOOOOMMMMM!!!'))
print('=' * 50)
#===============================================================================================================