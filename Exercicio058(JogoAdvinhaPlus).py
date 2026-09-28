#============================================================================================================
'''
Exercicio 058 - Melhore o jogo do desafio - 028 onde o computador vai 'pensar' em um valor entre
0 e 10. Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites
foram necessários pra vencer.
'''
#============================================================================================================

print('=' * 50)
print('\033[1;33m{:^50}\033[m'.format('JOGO DE ADVINHA'))
print('=' * 50)
from random import randint
computador = randint(0, 10)
print('Sou seu computador...'
      '\nAcabei de pensar em um numero entre 0 e 10 ')
print('Será que você consegue advinhar?')
print('-' * 50)
acertar = False
palpites = 0
while not acertar:
    jogador = int(input('Qual é o seu \033[1;33mpalpite\033[m?'))
    palpites += 1
    # ou palpite = palpite + 1
    if jogador == computador:
        acertar = True
    else:
        if jogador < computador:
            print('-' * 50)
            print('Mais...,\033[1;32mTENTE NOVAMENTE\033[m!')
        else:
            print('-' * 50)
            print('Menos...,\033[1;31mTENTE NOVAMENTE\033[m!')
print('-' * 50)
print('Acertaste com \033[1;34m{}\033[m Tentativas, \033[1;36mParabens\033[m!'.format(palpites))
print('=' * 50)
print('\033[1;33m{:^50}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 50)

#=======================================================================================================================

