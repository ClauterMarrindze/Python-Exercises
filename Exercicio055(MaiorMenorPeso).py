#===============================================================================================================
'''
Exercicio 055 : Faça um programa que leia o peso de 5 pessoas, No final,
mostre qual foi o maior e o menor peso lidos.
'''
#==================================================================================================================

print('=' * 50)
print('\033[1;36m{:^50}\033[m'.format('MAIOR E MENOR PESO'))
print('=' * 50)
maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input('Introduze o peso(Kg) da \033[m{}a\033[m pessoa : '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('-' * 50)
print(f'O \033[1;36mmaior\033[m peso lido foi \033[1;35m{maior}\033[mKg!')
print(f'O \033[1;31mmenor\033[m peso lido foi \033[1;31m{menor}\033[mKg!')
print('=' * 50)
print('\033[1;33m{:^50}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 50)

#====================================================================================================================
