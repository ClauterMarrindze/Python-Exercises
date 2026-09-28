#=======================================================================================================
'''
    Exercicio 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa
    O programa vai perguntar o valor da casa, o salario do comprador, e em quantos anos ele vai pagar.

    calcule o valor da prestacao mensal, sabendo que ela não pode exceder 30% do salario ou entao o
    emprestimo sera negado.
'''
print('=' * 50)
print('\033[1;36m{:^50}\033[m'.format('EMPRESTIMO BANCARIO'))
print('=' * 50)
casa = float(input('Informe o \033[1;35mvalor\033[m da casa R$ : '))
salario = float(input('Introduze o \033[1;36mseu salario\033[m R$: '))
anos = int(input('Em quantos anos deseja \033[1;34mpagar a casa\033[m : '))
print('=' * 50)
prestacaoMensal = casa / (anos * 12)
salarioMinimo = salario * 0.30
if prestacaoMensal > salarioMinimo :
    print('\033[1;31mEMPRESTIMO NEGADO!\033[m')
    print('\033[1;32mA SUA PRESTACAO EXCEDE O REQUISITADO!\033[m')
    print('PRESTACAO:R${:.2f}'.format(prestacaoMensal))
else:
    print('\033[1;32mEMPRESTIMO APROVADO!\033[m')
    print('Durante \033[1;35m{}\033[m anos\nIrá pagar R$\033[1;36m{:.2f}\033[m mensalmente!' # end=''
          .format(anos, prestacaoMensal))
print('=' * 50)
print('\033[1;33m{:^50}\033[m'.format('TENHA UM BOM DIA!'))
print('\033[1;33m{:^50}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 50)
#================================================================================================
#                                MODO GUANABARA


