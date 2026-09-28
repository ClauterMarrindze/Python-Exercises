#=======================================================================================================================
'''
Exercicio 060 - Faça um programa que leia um numero qualquer e mostre o seu factorial.

Exemplo :
5! = 5 x 4 x 3 x 2 x 1 = 120
'''
#=======================================================================================================================
#   USANDO MÓDULOS

'''from math import factorial
numero = int(input('Introduze um número :'))
factorial = factorial(numero)
print(f'O factorial de {numero} é {factorial}.')'''

print('=' * 50)
print('\033[1;37m{:^50}\033[m'.format(' FACTORIAL '))
print('=' * 50)
numero = int(input('Introduza um numero : '))
print('=' * 50)
print('Calculando {}! : '.format(numero), end=' ')
contador = numero
factorial = 1
while contador > 0:
    print('{}'.format(contador), end=' ')
    print('x' if contador > 1 else ' = ', end=' ')
    factorial *= contador
    #factorial = factorial * contador
    contador -= 1
    # ou contador = contador - 1
print('{}'.format(factorial))
print('=' * 50)
print('\033[1;33m{:^50}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 50)

#=======================================================================================================================
