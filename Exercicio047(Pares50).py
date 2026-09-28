#===============================================================================================================
'''
Exercicio 047 : Faça um programa que mostre na tela todos  os numeros pares
que estão no intervalo de 1 e 50.
'''
#=================================================================================================================

print('=' * 50)
print('\033[1;36m{:^50}\033[m'.format('NUMEROS PARES'))
print('=' * 50)
print('Números pares no intervalo de \033[1;36m1\033[m e \033[1;35m50\033[m : ')
'''
for c in range(1, 51):
    if c % 2 == 0 :
         print(c, end='\n')
print('-' * 50)
print('\033[1;35m{:^50}\033[m'.format('Todos os pares mostrados na tela!'))
print('-' * 50)
print('\033[1;33m{:^50}\033[m'.format('FIM DO PROGRAMA!'))
print('=' * 50)'''

# Outra Maneira
for c in range(2, 51, 2):
    print(c, end=' ')
#==================================================================================================================