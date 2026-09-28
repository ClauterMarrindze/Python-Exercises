#=============================================================================================
'''
Exercicio 057 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
#=========================================================================================================
'''
print('=' * 40)
print('\033[1;36m{:^40}\033[m'.format(' GENEROS - SEXOS '))
print('=' * 40)
sexo = str(input('Introduze seu sexo: \033[1;36m[M/F]\033[m ')).strip().upper()[0]
print('-' * 40)

while sexo not in 'MmFf':
    sexo = str(input('\033[1;31mDados Inválidos\033[m'
                     '\nIntroduze seu sexo: \033[1;35m[M/F]\033[m ')).strip().upper()[0]
    print('-' * 40)
print('Sexo {} registrado com \033[1;32msucesso\033[m!'.format(sexo))
print('=' * 40)
print('\033[1;32m{:^40}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 40)
#print(f'Sexo {sexo} registrado com \033[1;32msucesso\033[m!')
'''
#=========================================================================================================
#                                UPGRADE
print('=' * 40)
print('{:^60}'.format(' \033[1;36mGENEROS\033[m - \033[1;35mSEXOS\033[m '))
print('=' * 40)
sexo = str(input('Introduze seu sexo: \033[1;36m[M/F]\033[m ')).strip().upper()[0]
print('-' * 40)

while sexo not in 'MmFf':
    sexo = str(input('\033[1;31mDados Inválidos!\033[m'
                     '\nIntroduze seu sexo: \033[1;35m[M/F]\033[m ')).strip().upper()[0]
if sexo in 'Mm':
    print('Sexo \033[1;36mMasculino\033[m registrado com \033[1;32msucesso\033[m!')
else :
    print('Sexo \033[1;35mFeminino\033[m registrado com \033[1;32msucesso\033[m!')
print('=' * 40)
print('\033[1;33m{:^40}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 40)

#==========================================================================================================


