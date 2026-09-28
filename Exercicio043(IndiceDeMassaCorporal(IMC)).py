#=====================================================================================================================
'''
Exercicio 043: Desenvolva uma logica que lei o peso e altura de uma pessoa, calcule seu IMC
    e mostre seu status, de acordo com a tabela abaixo:

    -Abaixo de 18.5: Abaixo do peso
    -Entre 18.5 e 25: Peso ideal
    -Entre 25 e 30: Sobrepeso
    -Entre 30 e 40: Obesidade
    -acima de 40: Obesidade Mórbida
'''
#=====================================================================================================================

print('=' * 40)
print('\033[1;34m{:^40}\033[m'.format('ÍNDICE DE MASSA CORPORAL'))
print('=' * 40)
peso = float(input('Informe o seu peso (Kg): '))
altura = float(input('Informe a sua altura (m) : '))
IMC = peso / (altura ** 2) # peso dividido por altura ao quadrado
print('O IMC dessa Pessoa é de \033[1;34m{:.2f}\033[m.'.format(IMC))
if IMC < 18.5:
    print('-' * 40)
    print('Situação : \033[1;36mAbaixo do Peso\033[m')
elif 18.5 <= IMC < 25 :
    print('-' * 40)
    print('Situação : \033[1;32mPeso Ideal\033[m')
elif 25 <= IMC < 30 :
    print('-' * 40)
    print('Situação : \033[1;37mSobrepeso\033[m')
elif 30 <= IMC < 40 :
    print('-' * 40)
    print('Situação : \033[1;33mObesidade\033[m')
elif IMC >= 40 : # ou else :
    print('Situação : \033[1;31mObesidade Mórbida\033[m')
print('=' * 40)
print('\033[1;33m{:^40}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 40)
#================================================================================================================