#=============================================================================================================
'''
Exercicio 053 : Crie um programa que leia uma frase qualquer e diga se ela é
um Palíndromo, desconsiderando os espaços.
Ex: apos a sopa
a sacada da casa
a torre da derrota
o lobo ama o bolo
anotaram a data da maratona
'''
#================================================================================================================

'''print('=' * 50)
print('\033[1;35m{:^50}\033[m'.format(' PALAVRAS PALINDROMO '))
print('=' * 50)
frase = str(input('Introduza uma frase : ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1) :
    inverso += junto[letra]
    # ou inverso = inverso + junto[letra]
print('-' * 50)
print('O inverso da frase : \033[1;32m{}\033[m'.format(junto))
print('É a frase : \033[1;35m{}\033[m'.format(inverso))
print('-' * 50)
if inverso == junto:
    print('A frase é um \033[1;36mPALINDROMO\033[m!')
else:
    print('A frase não é um \033[1;31mPALINDROMO\033[m!')
print('=' * 50)
print('\033[1;33m{:^50}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 50)'''

#================================================================================================================
#                                    OUTRA MANEIRA DE RESOLVER O EXERCICIO

print('=' * 50)
print('\033[1;35m{:^50}\033[m'.format(' PALAVRAS PALINDROMO '))
print('=' * 50)
frase = str(input('Introduza uma frase : ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('-' * 50)
print('O inverso da frase : \033[1;32m{}\033[m'.format(junto))
print('É a frase : \033[1;35m{}\033[m'.format(inverso))
print('-' * 50)
if inverso == junto:
    print('A frase é um \033[1;36mPALINDROMO\033[m!')
else:
    print('A frase não é um \033[1;31mPALINDROMO\033[m!')
print('=' * 50)
print('\033[1;33m{:^50}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 50)

#==================================================================================================================