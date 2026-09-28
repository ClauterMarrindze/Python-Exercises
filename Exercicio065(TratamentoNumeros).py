#=======================================================================================================================
'''
Exercicio 065 - Crie um programa que leia varios numeros inteiros pelo teclado, no final da execucao
mostre a media entre todos valores e qual foi o maior e menor valores lidos, o programa deve perguntar ao
usuario se ele quer ou não contiuar a digitar os valores. mostre todos os pedidos no final.
'''
#=======================================================================================================================

print('=' * 50)
print('\033[1;35m{:^50}\033[m'.format('TRATAMENTO DE NUMEROS'))
print('=' * 50)
resposta = 'S'
soma = quantidade = media = maior = menor = 0
while resposta in 'Ss':
    numero = int(input('Introduze um número: '))
    soma = soma + numero # ou soma += numero
    quantidade = quantidade + 1 # ou quantidade += 1
    if quantidade == 1 :
        maior = menor = numero
    else :
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quantidade
print('=' * 50)
print(f'A quantidade de numeros digitados foi {quantidade}.'
      f'\nA soma dos numeros digitados foi {soma}.'
      f'\nA media dos numeros digitados foi {media}.'
      f'\nO maior numero foi {maior} e o menor foi {menor}.')
print('=' * 50)
print('\033[1;33m{:^50}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 50)