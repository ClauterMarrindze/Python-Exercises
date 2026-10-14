#=======================================================================================================================
# Exercicio 079 - Crie um programa onde o usuário possa digitar varios valores numéricos e cadastre-os
# numa lista. Caso o numero já exista lá dentro ele não será adicionado, no final serão
# exibidos todos vallores únicos digitados, em ordem crescente.
#=======================================================================================================================
print('=' * 50)
print(f'\033[1;36m{'LISTA DE NÚMEROS ÚNICOS':^50}\033[m')
print('=' * 50)
listaNumeros = []
while True:
    numero = int(input('Insira um valor:'))
    if numero not in listaNumeros:
        listaNumeros.append(numero)
        print('-' * 50)
        print('\033[1;36mValor adicionado com sucesso\033[m!!!')
        print('-' * 50)
    else:
        print('-' * 50)
        print('\033[1;31mValor inserido já existente\033[m!!!')
        print('-' * 50)

    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    print('-' * 50)
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
        print('=' * 50)
    if continuar == 'N':
        break
listaNumeros.sort()
print(f'Lista Inserida: {listaNumeros}')
print('=' * 50)




















