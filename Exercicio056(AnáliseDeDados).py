#===============================================================================================================

'''
Exercicio 056 : Desenvolva um programa que leia o nome, idade e sexo
de 4 pessoas, no final do programa, mostre:
- A media de idade do grupo
- Qual é o nome do homem mais velho
- Quantas mulheres tem menos de 20(21) anos.
'''

#=================================================================================================================
print('=' * 50)
print('\033[1;36m{:^50}\033[m'.format('ANÁLISE DE DADOS PESSOAIS'))
print('=' * 50)
somaIdade = 0
mediaIdade = 0
maiorIdadeH = 0
totalMulher = 0
nomeVelho = ''

for pessoas in range(1, 5):
    print('\033[1;35m[{}a Pessoa]\033[m =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'.format(pessoas))
    nome = str(input('Introduze o nome : ')).strip()
    idade = int(input('Introduza a idade : '))
    sexo = str(input('Introduza o sexo(M/F) : ')).strip()
    somaIdade += idade # ou somaIdade = somaIdade + 1
    if pessoas == 1 and sexo in 'Mm':
        maiorIdadeH = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeH:
        maiorIdadeH = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totalMulher += 1
        # totalMulher = totalMulher + 1

mediaIdade = somaIdade / 4
print('=' * 50)
print('A média da idade do grupo é de {} anos'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorIdadeH, nomeVelho))
print('Ao todo, são {} mulheres com menos de 20 anos.'.format(totalMulher))
print('=' * 50)
print('\033[1;33m{:^50}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 50)








