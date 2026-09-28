#=================================================================================
'''
    EXERCICIO 028: Escreva um programa que faca o computador 'pensar' em um
    numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o
    numero escolhido pelo computador.
    O programa devera escrever o na tela se o usuario venceu ou perdeu.
'''
#=================================================================================

from random import randint
from time import sleep

# Numero de escolha secreta do computador
numeroComputador = randint(0,5)
print('=' * 50)
print('\033[1;35m{:^50}\033[m'.format('JOGO DE ADVINHA'))
print('=' * 50)
print('Vou \033[1;34mpensar\033[m em um numero entre 0 e 5...\n\033[mTente Adivinhar\033[m...')
print('=' * 50)

# Jogador tenta advinhar
numeroJogador = int(input('\033[1;36mEm que número eu pensei\033[m? '))
print('\033[1;33mPROCESSANDO\033[m...')
sleep(3)
print('=' * 50)
if numeroComputador == numeroJogador:
    print('\033[1;36mO jogador venceu!\033[m\n\033[1;31mO computador perdeu!\033[m')
    print('-' * 50)
    print('\033[1;36mParabens, Pensamos no mesmo número\033[m.')
else:
    print('\033[1;36mO computador venceu\033[m!\n\033[1;31mO jogador perdeu!\033[m')
    print('-' * 50)
    print('Eu pensei no \033[1;34mnumero {}\033[m e não no \033[1;31m{}\033[m'.format(numeroComputador, numeroJogador))
print('=' * 50)
print('\033[1;33m{:^50}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 50)

#================================================================================