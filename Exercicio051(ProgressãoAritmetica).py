#===================================================================================================================
'''
Exercicio 051 : Desenvolva um programa que leia o primeiro termo e a razao
de uma Progressao Aritmetica. No final, mostre os 10 primeiros termos dessa
progressão.
'''
#==================================================================================================================

print('=' * 60)
print('\033[1;36m{:^60}\033[m'.format('PROGRESSÃO ARITMETICA'))
print('=' * 60)
print('\033[1;35m{:^60}\033[m'.format('10 TERMOS DE UMA PROGRESSÃO ARITMETICA'))
print('=' * 60)
primeiro = int(input('Primeiro termo da Progressao : '))
razao = int(input('Razão da Progressao : '))
print('-' * 60)
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{} '.format(c), end='')
    print('\033[1;35m->\033[m ' if c < decimo else '.', end='')
    print(end='\n' if c >= decimo else '' )
print('=' * 60)
print('\033[1;33m{:^60}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 60)

#==================================================================================================================


