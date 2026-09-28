#================================================================================================================
'''
Exercicio 049 : Refaça o desafio 009, mostrando a tabuada de um número
que o usuário escolher, só que usando o laço for.
'''
#==================================================================================================================

print('=' * 40)
print('\033[1;36m{:^40}\033[m'.format(' TABUADA PLUS (V2.0)'))
print('=' * 40)
numero = int(input('Introduze um número : '))
print('=' * 40)
for c in range(1, 16):
    #print(f'{numero} x {c} = {numero * c}')
    print('{} x {:2} = {}'.format(numero, c, numero * c))
print('=' * 40)
print("\033[1;33m{:^40}\033[m".format('FIM DO PROGRAMA'))
print('=' * 40)

#=================================================================================================================