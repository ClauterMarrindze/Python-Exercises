#=============================================================================================================
'''
Exercicio 052 : Faca um programa que leia um numero inteiro e diga se ele é
ou não um número primo.
'''
#=================================================================================================================

print('=' * 50)
print('\033[1;34m{:^50}\033[m'.format('NUMERO PRIMO'))
print('=' * 50)
numero = int(input('Introduze um numero inteiro : '))
total = 0
print('-' * 50)
print('NB: \033[1;35mOs numeros pintados em \033[2;34mazul \033[1;35msão os '
      '\nquais o numero que introduziste é divisível\033[m. ')
print('-' * 50)
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[1;34m', end=' ')
        total = total + 1
        # ou total += 1
    else:
        print('\033[1;31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(numero, total))
if total == 2:
    print('O numero {} é PRIMO!'.format(numero))
else:
    print('O numero {} não é PRIMO!'.format(numero))
print('=' * 50)
print('\033[1;33m{:^50}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 50)

#=================================================================================================================
