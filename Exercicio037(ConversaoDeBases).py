#=====================================================================================
'''
 Exercicio 037: Escreva um programa que leia um numero inteiro qualquer pelo teclado
 e peça para o usuario escolher qual é a base de conversao:
    1 - Pra Binário
    2 - Pra Octal
    3 - Pra Hexadecimal
'''
#===========================================================================================================================================
print('=' * 50)
print('\033[1;34m{:^50}\033[m'.format('CONVERSOR DE BASES'))
print('=' * 50)
numero = int(input('Introduza um numero inteiro : '))
print('-' * 50)
print('Escolha uma opcao desejada... ')
print('''[1] - Converter para \033[1;34mBinario\033[m
[2] - Converter para \033[1;33mOctal\033[m
[3] - Converter para \033[1;35mHexadecimal\033[m''')
print('-' * 50)
opcao = int(input('\033[1;36mSua opcao\033[m: '))
if opcao == 1:
    print('\033[1;34m{}\033[m em \033[1;34mbinario\033[m é igual a \033[1;33m{}\033[m'.format(numero, bin(numero)[2:]))
    print('=' * 50)
elif opcao == 2:
    print('\033[1;34m{}\033[m em \033[1;33moctal\033[m é igual a \033[1;35m{}\033[m'.format(numero, oct(numero)[2:]))
    print('=' * 50)
elif opcao == 3:
    print('\033[1;34m{}\033[m em \033[1;35mHexadecimal\033[m é igual a \033[1;34m{}\033[m'.format(numero, hex(numero)[2:]))
    print('=' * 50)
else:
    print('\033[1;31m{:^50}\033[m'.format('Opcao invalida, tente novamente!'))
    print('=' * 50)
print('\033[1;33m{:^50}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 50)
#==========================================================================================================================================