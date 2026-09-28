#======================================================================================================================
'''
Exercicio 069 - Crie um programa que leia a idade de varias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
a) Quantas pesssoas tem mais de 18 anos .
b) Quantos homens foram cadastrados.
c) Quantas mulheres tem menos de 20 anos.
'''
#=======================================================================================================================
print('=' * 50)
print(f'\033[1;36m{'CADASTRO DE PESSOAL':^50}\033[m')
print('=' * 50)
quantIdade = 0
quantidadeMulher = 0
quantidadeHomem = 0
while True:
    idade = int(input('Introduze a idade : '))
    sexo = ''
    while sexo not in 'MF':
        sexo = str(input('Introduza o sexo  [M/F] : ')).strip().upper()[0]
    if idade >= 18:
        quantIdade += 1
    if sexo == 'M':
        quantidadeHomem += 1
    if sexo == 'F' and idade < 20:
        quantidadeMulher += 1
    print('=' * 50)
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] : ')).strip().upper()[0]
    if opcao == 'N':
        break
    print('=' * 50)
print(f'Total de pessoas maiores de 18 cadastradas: {quantIdade}')
print(f'Total de homens cadastrados: {quantidadeHomem}')
print(f'Total de mulher cadastrados menores de 20 : {quantidadeMulher}')
print('=' * 50)
print(f'\033[1;33m{'FIM DO PROGRAMA':^50}\033[m')
print('=' * 50)

