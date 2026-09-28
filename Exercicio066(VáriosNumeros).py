#=======================================================================================================================
'''
Exercicio 066 - Crie um programa que leia vários números inteiros pelo teclado.
O programa só para quando o usuário digitar o valor 999, que é a condicao de parada.
No final mostre quantos numeros foram digitados e qual foi a soma deles(desconsiderando o flag(999))
'''
#=======================================================================================================================

print('=' * 50)
print('{:^70}'.format('\033[1;35mNUMEROS\033[m/\033[1;31mFLAG\033[m'))
print('=' * 50)
contador = soma = 0
while True:
    numero = int(input('Introduze um valor : '))
    if numero == 999:
        break
    contador += 1
    soma += numero
    # ou soma = soma + 1
    # ou contador = contador + 1
print('=' * 50)
print(f'No total foram {contador} numero(s) digitado(s)')
print(f'A soma da {soma}.')
print('=' * 50)
print(f'\033[1;33m{'FIM DO PROGRAMA!':^50}\033[m')
print('=' * 50)