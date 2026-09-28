#=======================================================================================================================
'''
Exercicio 063 - Escreva um programa que leia um número n inteiro qualquer e mostre na tela
os n primeiros elementos de uma sequencia de fibonacci.

Exemplo :
0 - 1 - 1 - 2 - 3 - 5 - 8
'''
#=======================================================================================================================

print('=' * 60)
print('\033[1;36m{:^60}\033[m'.format('SEQUÊNCIA DE FIBONACCI'))
print('=' * 60)
quantidade = int(input('Quantos termos deseja mostrar ? '))
termo1 = 0
termo2 = 1
print('-' * 60)
print('{} -> {}'.format(termo1, termo2), end=' ')
contador = 3
while contador <= quantidade:
    termo3 = termo1 + termo2
    print('-> {}'.format(termo3), end=' ')
    termo1 = termo2
    termo2 = termo3
    contador = contador + 1
    print(end='\n' if contador > quantidade else '')
    # contador += 1
print('=' * 60)
print('\033[1;33m{:^60}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 60)

#=======================================================================================================================














