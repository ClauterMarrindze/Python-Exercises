#=======================================================================================================================
'''
Exercicio 084 - Faça um programa que leia o nome e peso de várias pessoas
 guardando tudo em uma lista. No final mostre :
# a) Quantas pessoas foram cadastradas.
# b) Uma listagem com as pessoas mais pesadas.
# c) Uma listagem com as pessoas mais leves.
'''
#=======================================================================================================================

'''print('=' * 40)
print(f'{'DADOS DE PESSOAL':^40}')
print('-' * 40)
listaDados = list()
nomes = list()
pesos = list()
contador = 0
menorPeso = maiorPeso = 0

while True:
    nomes.append(str(input('Digite o nome do pessoa: ')))
    pesos.append(float(input('Digite o peso do pessoa: ')))
    contador += 1

    listaDados.append(nomes)
    listaDados.append(pesos)
    print('-' * 40)
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        print('-' * 40)
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('-' * 40)
    if continuar in 'N':
        break
print('-' * 40)
print(f'Foram cadastradas {contador} pessoas.')
print('-' * 40)
print('As pessoas mais pesadas cadastradas foram: ', end=' ')
for pos, pesos, nomes in enumerate(listaDados):
    menorPeso = maiorPeso = pesos[1]
    if maiorPeso > pesos[1]:
        maiorPeso = pesos[1]
print(f'{maiorPeso} kg')
print('-' * 40)
print(f'O me')'''

temporaria = list()
principal = list()
maior = menor = 0
while True:
    temporaria.append(str(input('Digite o nome da pessoa: ')))
    temporaria.append(float(input('Digite o peso da pessoa: ')))
    if len(principal) == 0:
        maior = menor = temporaria[1]
    else:
        if temporaria[1] > maior:
            maior = temporaria[1]
        if temporaria[1] < menor:
            menor = temporaria[1]

    principal.append(temporaria[:])
    temporaria.clear()

    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta in 'N':
        break
print('-' * 40)
print(f'Ao todo foram cadastradas {len(principal)} pessoas.')
print(f'O maior peso foi de {maior} kg que é de ', end=' ')
for pessoa in principal:
    if pessoa[1] == maior:
        print(f'[{pessoa[0]}]', end=' ')
print()
print(f'O menor peso foi de {menor} kg que é de ', end=' ')
for pessoa in principal:
    if pessoa[1] == menor:
        print(f'[{pessoa[0]}]', end=' ')
print()
print('=' * 40)