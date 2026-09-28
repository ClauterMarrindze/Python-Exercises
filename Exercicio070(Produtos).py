#+======================================================================================================================
'''
Exercicio 070 - Crie um programa que leia o nome e preco de vários produtos.
O programa devera perguntar se o usuário vai continuar. No final, mostre:
a) Qual é o total gasto na compra.
b) quantos produtos custam mais de R$1000.
c) Qual é o nome do produto mais barato.
'''
#=======================================================================================================================
print('=' * 50)
print(f'\033[1;36m{'MINI MERCADO':^50}\033[m')
print('=' * 50)
quantidadeMil = barato = totalGasto = quantidade =  0
barato1 = ' '
while True:
    produto = str(input('Introduze o nome do produto : ')).strip().upper()
    preco = float(input('Introduze o preço do produto : R$'))
    quantidade += 1
    totalGasto += preco
    if preco > 1000:
        quantidadeMil += 1

    if quantidade == 1 or preco < barato:
        barato = preco
        barato1 = produto

    print('-' * 50)

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print('-' * 50)
print(f'No total, compraste {quantidade} produtos.\nE custaram R${totalGasto:.2f}.')
print(f'No total {quantidadeMil} produtos custam mais de R$1000.')
print(f'O produto mais barato foi o {barato1} e custa {barato:.2f}. ')
print('=' * 50)
print(f'\033[1;33m{'FIM DO PROGRAMA':^50}\033[m')
print('=' * 50)

'''else :
        if preco < barato:
            barato = preco
            barato1 = produto'''

