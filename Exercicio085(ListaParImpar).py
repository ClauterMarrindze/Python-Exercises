#=======================================================================================================================
'''
Exercicio 085 - Crie um programa onde o usuário possa digitar 7 valores
numericos e cadastre-os em uma lista unica que mantenha separados os valores
pares e ímpares. No final, mostre os valores pares e impares em ordem crescente.
'''
#=======================================================================================================================
print('=' * 40)
print(f'{'LISTA DE PARES E IMPARES':^40}')
print('=' * 40)
numeros = [[], []]
valor = 0
for c in range(0, 7):
    valor = int(input(f'Insira o {c+1}o valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print('-' * 40)
print(f'Todos os valores : {numeros}')
print('-' * 40)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores impares digitados foram: {numeros[1]}')
print('=' * 40)