#=======================================================================================================================
# Exercicio 082 - Crie um programa que vai ler vários números e coloca-los numa lista.
# Depois disso crie duas listas que vao armazenar apenas valores pares e impares.
# No final mostre o conteudo das tres listas geradas

#=======================================================================================================================

print('=' * 60)
listaNumeros = []
listaPares = []
listaImpares = []
print(f'\033[1;35m{'LISTA DE PARES E IMPARES':^60}\033[m')
print('=' * 60)
while True:
    listaNumeros.append(int(input('Insira um numero: ')))
    print('-' * 60)

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    print('-' * 60)
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('-' * 60)
    if continuar in 'N':
        break
print(f'Lista de numeros inseridos: \033[1;33m{listaNumeros}\033[m')
print('-' * 60)
print(f'Lista de numeros pares:', end = ' ')
for numero in listaNumeros:
    if numero % 2 == 0:
        listaPares.append(numero)
        print(f'\033[1;36m{numero}\033[m ', end='')
print(end = '\n')
print(f'Lista de numeros impares:', end = ' ')
for numero in listaNumeros:
    if numero % 2 == 1:
        listaImpares.append(numero)
        print(f'\033[1;35m{numero}\033[m ', end='')
print(end = '\n')
print('=' * 60)