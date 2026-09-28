#==================================================================================================================
'''
Exercicio 054 : Crie um programa que leia o ano de sete pessoas, No final,
mostre quantas pessoas ainda não atingiram a maioridade(21 anos) e quantas já são
maiores de idade.
'''
#=================================================================================================================
from datetime import date
anoAtual = date.today().year
totalMaior = 0
totalMenor = 0
print('=' * 50)
print('\033[1;34m{:^50}\033[m'.format('PESSOAS MAIORES E MENORES!'))
print('=' * 50)
for pessoa in range(1, 8):
    nascimento = int(input('Introduze o ano de nascimento da {}a pessoa : '.format(pessoa)))
    idade = anoAtual - nascimento
    if idade >= 21:
        # totalMaior += 1
        totalMaior = totalMaior + 1
        #print('É \033[1;32mMaior de idade\033[m!\nTem \033[1;36m{}\033[m anos.')
    else:
        # totalMenor += 1
        totalMenor = totalMenor + 1
        #print('É \033[1;31mMenor de idade\033[m!\nTem \033[1;35m{}\033[m anos.')
print('-' * 50)
print('Tiveram \033[1;32m{}\033[m pessoas maiores de idade!'.format(totalMaior))
print('E também tiveram \033[1;31m{}\033[m pessoas menores de idade!'.format(totalMenor))
print('=' * 50)
print('\033[1;33m{:^50}\033[m'.format(' FIM DO PROGRAMA '))
print('=' * 50)