#=======================================================================================================================
'''
Exercicio 074:
crie um programa que vai gerar 5 numeros aleatorios e colocar numa tupla, depois disso mostre a listagem dos numeros
gerados e tambem indique o menor e o maior valor que estao na tupla.
'''
#=======================================================================================================================
print('=' * 50)
print(f'\033[1;35m{'NUMEROS ALEATORIOS':^50}\033[m')
print('=' * 50)
from random import randint
numeros = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
#print(f'Sorteei os numeros {numeros}.')
print('Os Valores sorteados foram: ', end=' ')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\nO Maior Valor Sorteado foi {max(numeros)}')
print(f'O Menor Valor Sorteado foi {min(numeros)}')
print('=' * 50)
print(f'\033[1;33m{'FIM DO PROGRAMA':^50}\033[m')
print('=' * 50)

''' if n[0] < n[1]:
    print(f'{n[0]} ', end=' ')
    else:'''