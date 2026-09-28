# Exercicio 013.
# ===================================================================
# Faca um programa que leia o salário de um trabalhador/funcionário
# e mostre o seu novo salário com aumento de 15%.
#=====================================================================
print('=' * 40)
print('\033[1;36m{:^40}\033[m'.format('AUMENTO SALARIAL'))
print('=' * 40)
salario = float(input('Introduze os seu salário \033[1;36mR$\033[m : '))
aumento = salario * (15/100)
novoSalario = salario + aumento
#novoSalario = salario + (salario * (15/100))

cores = {'limpo':'\033[m', 'branco':'\033[1;30m', 'vermelho':'\033[1;31m',
         'verde':'\033[1;32m', 'amarelo':'\033[1;33m', 'azul':'\033[1;34m',
         'roxo':'\033[1;35m', 'ciano':'\033[1;36m', 'cinzento':'\033[1;37m'}

print('=' * 40)
print('Teras um aumento de \033[1;33m15%\033[m no salario\nQue são  \033[1;36mR$\033[m {}{:.2f}{}.\n'
      'O seu novo salario é de \033[1;36mR$\033[m {}{:.2f}{}.'
      .format(cores['verde'], aumento, cores['limpo'],
              cores['roxo'], novoSalario, cores['limpo']))
print('=' * 40)
print('\033[1;33m{:^40}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 40)
#=====================================================================

'''
salario = float(input('Introduze o salario do funcioário Mt: '))
aumento = salario * 0.15
novoSalario = salario + aumento
#novoSalario = salario + (salario * 0.15)

print('Teras um aumento de 15% no salario, que são {:.2f}Mt.\n'
      'O seu novo salario é de {:.2f}Mt.'
      .format(aumento, novoSalario)) 
'''
#=====================================================================





