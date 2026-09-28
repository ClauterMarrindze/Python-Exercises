#==============================================================================
'''
  Exercicio 020:
  O mesmo professor que do desafio anterior quer sortear a ordem
    de apresentacao de trabalhos dos alunos.
    Faca um programa que leia o nome dos 4 alunos e mostre na tela a ordem de
    apresentacao Sorteada.
'''
#==============================================================================
'''
import random
nome1 = str(input('Introduza o nome do primeiro aluno:'))
nome2 = str(input('Introduza o nome do segundo aluno:'))
nome3 = str(input('Introduza o nome do terceiro aluno:'))
nome4 = str(input('Introduza o nome do quarto aluno:'))
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)

print('A ordem de apresentacao sera :\n {}'.format(lista))
'''
#===============================================================================
from random import shuffle

print('=' * 45)
print('\033[1;32m{:^45}\033[m'.format('SORTEIO DE APRESENTAÇÃO'))
print('=' * 45)
nome1 = str(input('Introduza o nome do \033[1;32mprimeiro\033[m aluno :'))
nome2 = str(input('Introduza o nome do \033[1;33msegundo\033[m aluno :'))
nome3 = str(input('Introduza o nome do \033[1;34mterceiro\033[m aluno :'))
nome4 = str(input('Introduza o nome do \033[1;35mquarto\033[m aluno :'))
print('-' * 45)
lista = [nome1, nome2, nome3, nome4]
shuffle(lista)

cores = {'limpa':'\033[m','roxo':'\033[1;35m','ciano':'\033[1;36m'}

print('A ordem de \033[1;32mapresentacao\033[m sera :\n {}'.format(lista))
print('=' * 45)
print('\033[1;33m{:^45}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 45)
#================================================================================






