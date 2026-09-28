#=======================================================================================================================
'''
Exercicio 061 - Refaça o desafio 051, lendo o primeiro termo e a razão de uma
Progressão Aritmetica (PA), mostrando o os 10 primeiros termos da Progressão usando a estrutura
while.
'''
#=======================================================================================================================
''''
print('=' * 60)
print('\033[1;35m{:^60}\033[m'.format(' Progressão Aritmetica '))
print('=' * 60)
print('\033[1;37m{:^60}\033[m'.format('Gerador de uma Progressão Arítmética'))
print('-' * 60)
primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Introduze a razão : '))
termo = primeiroTermo
contador = 1
print('-' * 60)
print('Os 10 primeiros termos da Progressão Aritmética são :')
while contador <= 10:
    print('{} '.format(termo), end='')
    print('\033[1;36m->\033[m' if contador < 10 else '.', end = ' ')
    print(end = '\n' if contador >= 10 else '')
    termo = termo + razao
    contador = contador + 1
    # contador += 1
    # termo += razao
print('=' * 60)
print('\033[1;33m{:^60}\033[m'.format("FIM DO PROGRAMA"))
print('=' * 60)
'''
 #                       DOING WITH CICLE FOR

print('=' * 60)
print('\033[1;35m{:^60}\033[m'.format(' Progressão Aritmetica '))
print('=' * 60)
print('\033[1;35m{:^60}\033[m'.format('Gerador de uma Progressão Arítmética'))
print('-' * 60)
primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Introduze a razão : '))
print('-' * 60)
termo = primeiroTermo
print('Os 10 primeiros termos da progressão são : ')
for c in range(1, 11):
    print('{} '.format(termo), end='')
    print('\033[1;35m->\033[m' if c < 10 else '.', end=' ')
    print(end='\n' if c >= 10 else '')
    termo = termo + razao
print('=' * 60)
print('\033[1;33m{:^60}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 60)
#'''
