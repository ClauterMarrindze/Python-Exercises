#===========================================================================
'''
    EXERCICIO 034:
    Escreva um programa que pergunte o salario de um funcionarioe
    calcule o valor do seu aumento.
    para salarios superiores a R$1.250, calcule um aumento de 10%.
    para os inferiores ou iguais, o aumento é de 15%.
'''
#========================================================================================

print('=' * 60)
print('\033[1;32m{:^60}\033[m'.format('AUMENTO SALARIAL'))
print('=' * 60)
salario = float(input('Introduze o \033[1;32msalario\033[m do \033[1;34mfuncionario\033[m : '))

cores = {'limpo': '\033[m','branco': '\033[1;30m','vermelho': '\033[1;31m',
         'verde': '\033[1;32m','amarelo': '\033[1;33m','azul': '\033[1;34m',
         'roxo': '\033[1;35m','ciano': '\033[1;36m','cinza': '\033[1;37m'}

if salario > 1250:
    aumento = salario + (salario * (10/100)) #ou (salario * 0.1)
    print('=' * 60)
    print('Tiveste um aumento de \033[1;35m10%\033[m.\nQue são R${}{:.2f}{}'
          .format(cores['azul'],salario * (10/100), cores['limpo']))
    print('No \033[1;37mtotal\033[m terás R${}{:.2f}{}'.format(cores['roxo'], aumento, cores['limpo']))
    print('=' * 60)
else:
    aumento = salario + (salario * (15/100)) #ou (salario * 0.15)
    print('=' * 60)
    print('Tiveste um aumento de \033[1;36m15%\033[m.\nQue são R${}{:.2f}{}'
          .format(cores['verde'], salario * (15/100), cores['limpo']))
    print('No \033[1;37mtotal\033[m terás R${}{:.2f}{}'
          .format(cores['ciano'], aumento,  cores['limpo']))
    print('=' * 60)
print('\033[1;37m{:^60}\033[m'.format('BOM DIA'))
print('=' * 60)
print('\033[1;33m{:^60}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 60)
#========================================================================================






