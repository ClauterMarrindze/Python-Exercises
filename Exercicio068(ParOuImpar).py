#========================================================================================================
'''
Exercicio 068 - Faca um programa que jogue par ou impar com o computador.O jogo só será
interrompido quando o jogador PERDER, mostrando o total de vitórias que ele conquistou no final do jogo.
'''
#==========================================================================================================
from random import randint
print('=' * 50)
print(f'{'\033[1;36mPAR\033[m OU \033[1;35mIMPAR\033[m':^70}')
print('=' * 50)
vitoria = 0
while True:
    jogador = int(input('Introduze um valor : '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo =  ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}.')
    print(f'Total de {total}', end=' ')
    print('Deu par' if total % 2 == 0 else 'Deu impar')
    print('=' * 50)
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce \033[1;36mGanhou\033[m!')
            vitoria += 1
            print('=' * 50)
        else :
            print('Voce \033[1;31mPerdeu\033[m!')
            print('=' * 50)
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce \033[1;36mGanhou\033[m!')
            vitoria += 1
            print('=' * 50)
        else:
            print('Voce \033[1;31mPerdeu\033[m!')
            print('=' * 50)
            break
    print('Vamos jogar novamente...')
    print('=' * 50)
print(f'Game Over!\nVoce Venceu \033[1;36m{vitoria}\033[m vezes')
print('=' * 50)
print(f'\033[1;33m{'FIM DO JOGO!':^50}\033[m')
print('=' * 50)

