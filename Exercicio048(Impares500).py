#================================================================================================================
'''
Exercicio 048 : Faça um programa que calcule a soma entre todos os numeros
ímpares que são múltiplos de três e que se encontram no intervalo de 1 até
500.
'''
#==================================================================================================================

'''soma = 0
print('=' * 50)
print('\033[1;35m{:^50}\033[m'.format('IMPARES MULTIPLOS DE 3!'))
print('=' * 50)
for c in range(1, 500):
    if c % 2 == 1:
        if c % 3 == 0:
            print(c)
            soma += c
print('=' * 50)
print('A soma dos impares multiplos e 3 é : {}'.format(soma))
print('=' * 50)
print('\033[1;33m{:^50}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 50)'''

soma = 0
contador = 0
for c in range(1, 501, 2):
  if c % 3 == 0:
        print(c)
        # soma += c ou
        # contador += 1
        contador = contador + 1
        soma = soma + c
print('São {} valores somados e multiplos de 3.'.format(contador))
print('A soma é :',soma,'.')
#===================================================================================================================