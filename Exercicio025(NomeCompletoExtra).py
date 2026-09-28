#===========================================================================
'''
EXERCICIO 025:
Crie um programa que leia o nom de uma pessoa e diga se
ela tem 'silva' no nome.
'''
#====================================================================
'''
nome = str(input('Introduze o se nome : ')).strip()
print('O seu nome tem silva ? :','silva' in nome.lower())
#print('O seu nome tem silva ? :','SILVA' in nome.upper())
'''

print('=' * 40)
print('\033[1;34m{:^40}\033[m'.format('ANALISE DE NOMES'))
print('=' * 40)
nome = str(input('Introduze o se \033[1;35mnome\033[m : ')).strip().upper()
print('-' * 40)
print('O seu nome tem \033[1;34mMarrindze\033[m ? :','MARRINDZE' in nome)
print('\033[1;37mTRUE\033[m - \033[1;32mVERDADEIRO\033[m\n\033[1;37mFALSE\033[m - \033[1;31mFALSO\033[m')
print('=' * 40)
print('\033[1;33m{:^40}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 40)
#print('O seu nome tem silva ? :''MARRINDZE' in nome.upper())
#=====================================================================
