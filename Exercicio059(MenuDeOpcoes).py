#======================================================================================================================
'''

Exercicio 059 - Crie um programa que leia 2 valores e mostre na tela o menu :
[ 1 ] - SOMAR
[ 2 ] - MULTIPLICAR
[ 3 ] - MAIOR
[ 4 ] - NOVOS NÚMEROS
[ 5 ] - SAIR DO PROGRAMA

Seu programa deverá realizar a operacao em cada caso.

'''

#=======================================================================================================================

from time import sleep
print('=' * 50)
print('\033[1;34m{:^50}\033[m'.format('MENU DE OPÇÕES'))
print('=' * 50)
numero1 = int(input('Introduze o primeiro valor : '))
numero2 = int(input('Introduze o segundo valor : '))
opcao = 0
print('=' * 50)
while opcao != 5:
    print('''
    [ 1 ] - \033[1;32mSOMAR\033[m
    [ 2 ] - \033[1;34mMULTIPLICAR\033[m
    [ 3 ] - \033[1;35mMAIOR\033[m 
    [ 4 ] - \033[1;36mNOVOS NUMEROS\033[m 
    [ 5 ] - \033[1;31mSAIR DO PROGRAMA\033[m
    ''')
    print('=' * 50)
    opcao = int(input('>>>>>>>>>>>>>>>>> Qual é a sua opcao ? '))
    if opcao == 1:
        soma = numero1 + numero2
        #print(f'A soma entre os valores {numero1} e {numero2} é {soma}.')
        print(f'{numero1} + {numero2} = {soma}.')
        print('=' * 50)
    elif opcao == 2:
        multiplicar = numero1 * numero2
        #print(f'A multiplicação entre os valores {numero1} e {numero2} é {multiplicar}.')
        print(f'{numero1} x {numero2} = {multiplicar}.')
        print('=' * 50)
    elif opcao == 3:
        if numero1 > numero2:
            maior = numero1
        else:
            maior = numero2
        print(f'Entre {numero1} e {numero2} o maior é {maior}.')
        print('=' * 50)
    elif opcao == 4:
        print('=' * 50)
        print('Introduze os valores novamente...')
        numero1 = int(input('Introduze o primeiro valor : '))
        numero2 = int(input('Introduze o segundo valor : '))
        print('=' * 50)
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('\033[1;31mOpcao invalida!\nTente Novamente!\033[m')
sleep(3)
print('=' * 50)
print('\033[1;33m{:^50}\033[m'.format('FIM DO PROGRAMA'))
print('\033[1;36m{:^50}\033[m'.format('VOLTE SEMPRE!'))
print('=' * 50)

#======================================================================================================================