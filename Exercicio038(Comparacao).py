#==========================================================================================================
'''
Exercicio 038: Escreva um programa que leia dois numeros inteiros e compare-os mostrando na tela:
    O primeiro valor é maior;
    O segundo valor é maior;
    Não existe valor maior, os dois são iguais;
'''
#============================================================================================================
print('=' * 50)
print('\033[1;33m{:^50}\033[m'.format('COMPARACAO DE NUMEROS'))
print('=' * 50)
numero1 = int(input('Informe o \033[1;35mprimeiro\033[m numero : '))
numero2 = int(input('Informe o \033[1;36msegundo\033[m numero : '))
print('-' * 50)
if numero1 > numero2 :
    print('O \033[1;35mprimeiro\033[m número é \033[1;34mmaior\033[m!')
elif numero2 > numero1 :
    print('O \033[1;36mSegundo\033[m numero é \033[1;33mMaior\033[m!')
elif numero1 == numero2 :
    print('\033[1;37mNenhum\033[m dos dois é maior!\n\033[1;31mNão existe\033[m, são iguais!')
'''
else numero1 == numero2 :
    print('\033[1;37mNenhum\033[m dos dois é maior!\n\033[1;31mNão existe\033[m, são iguais!')
'''
print('=' * 50)
print('\033[1;33m{:^50}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 50)
#============================================================================================================