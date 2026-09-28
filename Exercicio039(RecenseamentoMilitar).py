#===========================================================================================================
'''
 Exercicio 039:  Faca um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
    - Se ele ainda vai se alistar ao serviço militar
    - Se é hora de se alistar
    - Se já passou o tempo de alistamento

    Seu programa tambem deve mostrar o tempo que falta ou que passou o tempo de alistamento.
'''
#===========================================================================================================
from datetime import date

print('=' * 40)
print('\033[1;32m{:^40}\033[m'.format('RECENSEAMENTO MILITAR'))
print('=' * 40)

anoAtual = date.today().year
nascimento = int(input('Introduze o ano de nascimento : '))
idade = anoAtual - nascimento

print('Quem nasceu em {}\nTem(Terá) {} anos em {}'.format(nascimento, idade, anoAtual))
print('=' * 40)

if idade == 18:
    print('Você tem que fazer o Recenseamento Militar.\n\033[1;31mIMEDIATAMENTE\033[m!')
    print('=' * 40)
elif idade < 18:
    print('\033[1;31mVocê ainda não tem 18 anos\033[m.\nAinda faltam {} anos.'.format(18 - idade))
    print('Farás em {}.'.format(anoAtual + (18 - idade)))
    print('=' * 40)
elif idade > 18:
    print('Você já deveria ter feito o \nRecenseamento Militar ',end = '')
    print('Já há {} anos.'.format(idade - 18))
    print('Isso em {}'.format(anoAtual - (idade - 18)))
    print('=' * 40)
print('\033[1;33m{:^40}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 40)

# Meter um upgrade pra sexo, se for mulher não precisa fazer, se for homem, é isso tudo ai.

#===========================================================================================================

