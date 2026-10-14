#=======================================================================================================================
# Exercicio 078 -
# Faca um programa que leia 5 valores numericos e guarde-os numa lista.
# No final, mostre na tela qual foi o maior e o menor valor inserios e as suas respectivas
# posicoes na lista.
#=======================================================================================================================
print('=' * 65)
print(f'\033[1;34m{'LISTA DE MAIORES E MENORES':^65}\033[m')
print('=' * 65)
listaValores = []
maior = menor = 0

for c in range(0, 5):
    listaValores.append(int(input(f'Introduza o {c+1}o valor: ')))
    if c == 0:
        maior = menor = listaValores[c]
    else:
        if listaValores[c] > maior:
            maior = listaValores[c]
        if listaValores[c] < menor:
            menor = listaValores[c]
print('-' * 65)
print(f'O(s) maior(es) valor(es) é \033[1;35m{maior}\033[m, e está(ão) na(s) posição(es) : ')
for i, v in enumerate(listaValores):
    if v == maior:
        print(f'\033[1;37m{i+1}\033[m ', end='')
print(end='\n')
print('-' * 65)
print(f'O(s)  menor(es) valor(es) é \033[1;35m{menor}\033[m, e está(ão) na(s) posição(es) : ')
for i, v in enumerate(listaValores):
    if v == menor:
        print(f'\033[1;35m{i+1}\033[m ', end='')
print(end='\n')
print('=' * 65)
print(f'\033[1;33m{'DONE':^65}\033[m')
print('=' * 65)