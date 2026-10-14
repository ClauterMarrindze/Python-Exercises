#=======================================================================================================================
'''
Exercicio 086 - Crie um programa que cria uma matriz 3x3 e preencha com valores
lidos pelo teclado.
3 linhas x 3 colunas
No final mostre a matriz na tela, com a formatacao correta.
'''
#=======================================================================================================================
print('=' * 50)
print(f'\033[1;35m{"MATRIZ":^50}\033[m')
print('=' * 50)
matriz = [[0, 0, 0], [0 ,0 ,0], [0 ,0 ,0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Insira um valor para [{linha+1}, {coluna+1}]: '))
print('=' * 50)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('=' * 50)
#=======================================================================================================================









