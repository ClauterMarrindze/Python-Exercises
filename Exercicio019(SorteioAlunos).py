# ===========================================================================
''' Exercicio 019:
    Um professor quer sortear um dos seus 4 alunos para apagar o quadro
    Faca um programa que ajude ele, lendo o nome deles e escrevendo o
    nome do escolhido.
'''
#==========================================================================
'''
import random
nome1 = str(input('Introduze o nome do primeiro aluno: '))
nome2 = str(input('Introduze o nome do segundo aluno: '))
nome3 = str(input('Introduze o nome do terceiro aluno: '))
nome4 = str(input('Introduze o nome do quarto aluno: '))
lista = [nome1, nome2, nome3, nome4]
print('O aluno escolhido para limpar o quadro é o(a):',random.choice(lista))
'''
#===========================================================================
'''
import random
nome1 = str(input('Introduze o nome do primeiro aluno: '))
nome2 = str(input('Introduze o nome do segundo aluno: '))
nome3 = str(input('Introduze o nome do terceiro aluno: '))
nome4 = str(input('Introduze o nome do quarto aluno: '))
lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)
print('O(A) aluno(a) escolhido(a) foi o(a) {}.'.format(escolhido))
'''
#============================================================================
from random import choice
print('=' * 45)
print('{:^55}'.format('\033[1;35mSORTEIO DE ALUNOS\033[m'))
print('=' * 45)

cores = {'limpa':'\033[m','branco':'\033[1;30m','vermelho':'\033[1;31m','verde':'\033[1;32m',
         'amarelo':'\033[1;33m','azul':'\033[1;34m','roxo':'\033[1;35m','ciano':'\033[1;36m',
         'cinza':'\033[1;37m'}

nome1 = str(input('Introduze o nome do \033[1;31mprimeiro\033[m aluno : '))
nome2 = str(input('Introduze o nome do \033[1;32msegundo\033[m aluno : '))
nome3 = str(input('Introduze o nome do \033[1;33mterceiro\033[m aluno : '))
nome4 = str(input('Introduze o nome do \033[1;34mquarto\033[m aluno : '))
lista = [nome1, nome2, nome3, nome4]
print('=' * 45)
print('O(A) \033[1;36mescolhido(a)\033[m foi o(a)', cores['verde'], choice(lista), cores['limpa'])
print('=' * 45)
print('{:^55}'.format('\033[1;33mFIM DO PROGRAMA\033[m'))
print('=' * 45)
#=============================================================================











