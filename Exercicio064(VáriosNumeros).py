#=======================================================================================================================
'''
Exercicio 064 - Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final mostre quantos foram digitados e qual foi a soma entre eles (Desconsiderando o flag, que é
esse 999)
'''
#=======================================================================================================================

print('=' * 60)
print('\033[1;35m{:^60}\033[m'.format('NÚMEROS INTEIROS'))
print('=' * 60)
print('Podes digitar qualquer número\n\033[1;31m999 é a condição de parada\033[m.')
numero = contador = soma = 0
print('-' * 60)
numero = int(input('Introduze um número : '))
while numero != 999:
    contador += 1
    soma += numero
    numero = int(input('Introduze um número : '))
    # soma = soma + numero
    # contador = contador + 1
print('-' * 60)
print('Você introduziu {} números.'.format(contador))
print('A soma dos numeros introduzidos é : {}'.format(soma))

'''print('Você introduziu {} números.'.format(contador - 1))
print('A soma dos numeros introduzidos é : {}'.format(soma - 999))'''

print('=' * 60)
print('\033[1;31m{:^60}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 60)

#=======================================================================================================================





