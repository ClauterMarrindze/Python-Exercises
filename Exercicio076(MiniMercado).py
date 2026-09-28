#=======================================================================================================================
'''
Exercicio 076:
Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços, na sequencia.
No final, mostre uma listagem de precos, organizando os dados em forma tabular.NB: Use tuplas.
'''
#=======================================================================================================================
print('=' * 50)
print(f'\033[1;36m{'MATERIAL ESCOLAR':^50}\033[m')
print('=' * 50)
listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.00,
            'Estojo', 25.00,
            'Transferidor', 2.00,
            'Compasso', 1.75,
            'Mochila', 120.00,
            'Caneta', 15.00,
            'Livros', 1.75,)
for posicao in range(0, len(listagem)):
    if posicao % 2 == 0:
        print(f'{listagem[posicao]:.<40}', end='')
    else:
        print(f'R${listagem[posicao]:>8.2f}')
print('=' * 50)
print(f'\033[1;33m{'GET BACK EARLY, ALWAYS':^50}\033[m')
print('=' * 50)
