#=======================================================================================================================
'''
Exercicio 045: Crie um programa que faça o computador jogar pedra papel e tesoura consigo.
    (Jokenpô)
'''
#=======================================================================================================================
print('=' * 50)
print('{:^80}'.format('\033[1;31mPEDRA\033[m-\033[1;32mPAPEL\033[m-\033[1;33mTESOURA\033[m'))
print('=' * 50)

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
#print('O computador escolheu {}'.format(itens[computador]))
print('''Escolha...
[ 0 ] - \033[1;33mPEDRA\033[m
[ 1 ] - \033[1;35mPAPEL\033[m
[ 2 ] - \033[1;34mTESOURA\033[m''')
print('-' * 50)
jogador = int(input('Qual é a sua jogada : '))
print('\033[1;35mPEDRA\033[m')
sleep(1)
print('\033[1;33mPAPEL\033[m')
sleep(1)
print('\033[1;34mTESOURA\033[m')
sleep(1)
print('-' * 50)
print('O computador jogou : \033[1;33m{:^10}\033[m'.format(itens[computador]))

if jogador == 0 :
    print('O jogador jogou : \033[1;36m{:^10}\033[m'.format('PEDRA'))
    if computador == 0 :
        print('\033[1;37mEMPATE\033[m')
    elif computador == 1 :
        print('\033[1;36mCOMPUTADOR VENCEU\033[m')
        print('\033[1;31mJOGADOR PERDEU\033[m')
    elif computador == 2 :
        print('\033[1;31mCOMPUTADOR PERDEU\033[m')
        print('\033[1;36mJOGADOR VENCEU\033[m')
elif jogador == 1 :
    print('O jogador jogou : \033[1;36m{:^10}\033[m'.format('PAPEL'))
    if computador == 0 :
        print('\033[1;31mCOMPUTADOR PERDEU\033[m')
        print('\033[1;36mJOGADOR VENCEU\033[m')
    elif computador == 1 :
        print('\033[1;37mEMPATE\033[m')
    elif computador == 2 :
        print('\033[1;36mCOMPUTADOR VENCEU\033[m')
        print('\033[1;31mJOGADOR PERDEU\033[m')

elif jogador == 2 :
    print('O jogador jogou : \033[1;36m{:^10}\033[m'.format('TESOURA'))
    if computador == 0 :
        print('\033[1;36mCOMPUTADOR VENCEU\033[m')
        print('\033[1;36mJOGADOR PERDEU\033[m')
    elif computador == 1 :
        print('\033[1;31mCOMPUTADOR PERDEU\033[m')
        print('\033[1;36mJOGADOR VENCEU\033[m')
    elif computador == 2 :
        print('\033[1;37mEMPATE\033[m')
else:
    print('\033[1;31m{:^50}\033[m'.format('OPCÃO INVÁLIDA!'))
print('=' * 50)
print('\033[1;33m{:^50}\033[m'.format('FIN DEL JUEGO'))
print('=' * 50)
#======================================================================================================================
