#=======================================================================================================================
# Exercicio 081 - Crie um programa que vai ler vários numeros e coloca-los numa lista.
# a) Quantos numeros foram digitados
# b) A lista de valores ordenada de forma decrescente
# c) Se o valor 5 foi digitado e está ou não na lista .

#+======================================================================================================================
print('=' * 50)
listaNumeros = []
contador = 0
print(f'\033[1;34m{'LISTA ORGANIZADA DE NUMEROS':^50}\033[m')
print('=' * 50)
while True:
    listaNumeros.append(int(input('Digite um valor: ')))
    contador += 1
    print('-' * 50)

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    print('-' * 50)
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('-' * 50)
    if continuar == 'N':
        break
print(f'Na lista há {contador} Numeros inseridos.')
print(f'Que são : ', end='')
for c in listaNumeros:
    print(f'\033[1;34m{c}\033[m ', end=' ')
print(end='\n')
print('-' * 50)
listaNumeros.sort()
listaNumeros.sort(reverse=True)
print(f'A lista na ordem decrescente: \033[1;35m{listaNumeros}\033[m')
print('-' * 50)
if 5 in listaNumeros:
    print('\033[1;32mO valor 5 foi inserido na lista\033[m')
    print(f'O valor 5 apareceu \033[1;36m{listaNumeros.count(5)}\033[m vezes')
else:
    print('\033[1;31mO valor 5 não foi inserido na lista\033[m!')
print('=' * 50)