#==========================================================================================================
'''
  Exercicio 041: A confederacao nacional de natacao precisa de um programa que leia o ano de nascimento
    de um atleta e mostre sua categoria de acordo com sua idade:
    - até 9 anos : mirim
    - ate 14 anos: Infantil
    - ate 19 anos: Junior
    - ate 20 anos: Senior
    - Acima: Master
'''
#===================================================================================================================
from datetime import date

anoAtual = date.today().year

print('=' * 50)
print('\033[1;34m{:^50}\033[m'.format('CATEGORIA DE NATAÇÃO'))
print('=' * 50)
nascimento = int(input('Ano de nascimento do atleta : '))
idade = anoAtual - nascimento
print(f'O atleta tem \033[1;37m{idade}\033[m anos.')
print('=' * 50)
if idade <= 9:
    print('CLASSIFICAÇÃO : \033[1;31mMIRIM\033[m')
    print('=' * 50)
elif idade <= 14:
    print('CLASSIFICAÇÃO : \033[1;32mINFANTIL\033[m')
    print('=' * 50)
elif idade <= 19:
    print('CLASSIFICAÇÃO : \033[1;33mJUNIOR\033[m')
    print('=' * 50)
elif idade <= 25:
    print('CLASSIFICAÇÃO : \033[1;34mSENIOR\033[m')
    print('=' * 50)
elif idade > 25: # ou else :
    print('CLASSIFICAÇÃO : \033[1;35mMASTER\033[m')
    print('=' * 50)
print('\033[1;33m{:^50}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 50)
#==========================================================================================================

