#=======================================================================================================================
'''
Exercicio 067 - Faca um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor
digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''
#=======================================================================================================================

print('=' * 50)
print(f'\033[1;36m{'TABUADA V3.0':^50}\033[m')
print('=' * 50)
while True:
    numero = int(input('Introduze um numero para a tabuada desejada : '))
    if numero < 0:
        break
    print('=' * 50)
    for c in range(1, 16):
        print(f'{numero} x {c:2} = {numero * c}')
    print('=' * 50)
print('=' * 50)
print(f'\033[1;33m{'TABUADA ENCERRADA':^50}\033[m')
print('=' * 50)

