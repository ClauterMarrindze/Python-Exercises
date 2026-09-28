#=======================================================================================================================
'''
Exercicio 075:
Desenvolva um programa que leia 4 valores pelo teclado e guarda-os em numa tupla, no final mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posicao foi digitado o primeiro valor 3.
C) Quais foram os numeros pares.  NB: Use tuplas
'''
#=======================================================================================================================
print('=' * 50)
print(f'\033[1;34m{'ARMAZENAMENTO DE NUMEROS':^50}\033[m')
print('=' * 50)
numeros = (int(input('Digite um numero: ')),
            int(input('Digite outro numero: ')),
            int(input('Digite mais um numero: ')),
            int(input('Digite o ultmo numero: ')))
print('-' * 50)
print(f'Os numeros digitados foram : {numeros}')
print('-' * 50)
# Alinea A
print(f'O numero 9 apareceu {numeros.count(9)} veze(s)')
print('-' * 50)
# Alinea B
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3) + 1}a posicao. ')
else:
    print('\033[1;31mO valor 3 não foi digitado em nenhuma posicao\033[m.')
print('-' * 50)
print('Os Valores pares sao : ', end=' ')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
print('\n')
print('=' * 50)
print(f'\033[1;33m{'FIM DO PROGRAMA':^50}\033[m')
print('=' * 50)

