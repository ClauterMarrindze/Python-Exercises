#=======================================================================================================================
'''
Exercicio 088 - Faça um programa que ajude um jogador da MEGA SENA a criar
palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre
1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''
#=======================================================================================================================

print('=' * 60)
print(f'{'MEGA SENA':^60}')
print('=' * 60)
from random import randint
from time import sleep
lista = list()
jogos = list()
total = 0

quantidade = int(input('Quantos jogos você quer gerar? '))
while total < quantidade:
    contador = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            contador += 1
        if contador >= 6:
            break

    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-' * 60)
print('=' * 20, f'SORTEANDO {quantidade} JOGOS', '=' * 20)
print('-' * 60)
sleep(2)
for indice, jogo in enumerate(jogos):
    print(f'Jogo {indice+1}: {jogo}')
    sleep(2)
print('=' * 60)
print(f'\033[1;33m{"BON CHANCCEE!":^60}\033[m')
print('=' * 60)