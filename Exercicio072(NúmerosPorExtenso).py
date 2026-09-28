#=======================================================================================================================
'''
Exercicio 072:
Faça um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de 0 ate 20.
O programa devera ler um numero pelo teclado (entre 0 ate 20) e mostra-lo por extenso.
'''
#=======================================================================================================================
print('=' * 50)
print(f'\033[1;34m{'NUMEROS POR EXTENSO':^50}\033[m')
print('=' * 50)
numeros = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito'
              ,'nove','dez','onze','doze','treze','catorze','quinze','dezasseis','dezassete','dezoito',
           'dezanove','vinte')
while True:
    numero = int(input('Introduza um numero : '))
    print('-' * 50)
    if 0 <= numero <= 20:
        break
    else:
        print('\033[1;31mNumero invalido, tente novamente\033[m!')
        print('-' * 50)
print(f'O usuário digitou {numeros[numero]}.')
print('=' * 50)
print(f'\033[1;33m{'FIM DO PROGRAMA':^50}\033[m')
print('=' * 50)


