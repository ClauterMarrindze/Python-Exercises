#===============================================================================================================
'''
Exercicio 050 : Desenvolva um programa que leia seis numeros inteiros
e mostre na tela a soma apenas daqueles que forem pares.Se o valor digitado
for impar desconsidere-o.
'''
#====================================================================================================================

print('=' * 50)
print('\033[1;37m{:^50}\033[m'.format('SOMA DE PARES'))
print('=' * 50)
soma = 0
contador = 0
for c in range(1, 7):
    num = int(input('Introduza o {}o número : '.format(c)))
    if num % 2 == 0:
        contador = contador + 1
        #contador += 1
        soma = soma + num
        # ou soma += num
print('=' * 50)
print('No total foram introduzidos \033[1;32m{}\033[m número(s) par(es).'.format(contador))
print('A soma dos pares introduzidos é :\033[1;35m',soma,'\033[m')
print('=' * 50)
print('\033[1;33m{:^50}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 50)

#====================================================================================================================