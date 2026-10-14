#=======================================================================================================================
'''
Exercicio 087 - Aprimore o desafio anterior, mostrando no final.
a) A soma de todos os valores pares digitados.
b) A soma dos valores da 3a coluna.
c) O maior valor da segunda linha
'''
#=======================================================================================================================
'''print('=' * 40)
print(f'{'MATRIZ APRIMORADA':^40}')
print('=' * 40)
soma = somaColuna3 = 0

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Introduze um numero para a posicao {linha+1}x{coluna+1}'))
print('=' * 40)
for linha in range(0, 3):
    for coluna in range(0, 3):
        if matriz[linha][coluna] % 2 == 0:
            soma += matriz[linha][coluna]
        if matriz[][3]:
            somaColuna3 += matriz[][3]
        if matriz[][coluna]:

print('=' * 40)'''
#=======================================================================================================================
print('=' * 50)
print(f'\033[1;35m{"MATRIZ":^50}\033[m')
print('=' * 50)
matriz = [[0, 0, 0], [0 ,0 ,0], [0 ,0 ,0]]
somaColuna3 = somaPares = maiorlinha2 = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Insira um valor para [{linha+1}, {coluna+1}]: '))
print('=' * 50)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somaPares += matriz[linha][coluna]
    print()
for linha in range(0, 3):
    somaColuna3 += matriz[linha][2]
for coluna in range(0, 3):
    if coluna == 0:
        maiorlinha2 = matriz[1][coluna]
    elif matriz[1][coluna] > maiorlinha2:
        maiorlinha2 = matriz[1][coluna]

print('=' * 50)
print(f'A soma dos pares é {somaPares}.')
print(f'A soma dos valores da 3a coluna é {somaColuna3}.')
print(f'O maior valor da 2a linha é {maiorlinha2}.' )
print('=' * 50)
