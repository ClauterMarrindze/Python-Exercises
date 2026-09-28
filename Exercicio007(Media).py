# Exercicio 007.
# ==========================================================
# Desenvolva um programa que leia as duas notas de um aluno,
# calcule e mostre a sua média.
# =================================================================================

print('=' * 40)
print('\033[1;33m{:^40}\033[m'.format('SISTEMA \033[mDE \033[1;33mGESTAO \033[m DE \033[1;33mALUNOS'))
print('=' * 40)
nota1 = float(input('Introduze a primeira nota : '))
nota2 = float(input('Introduza a segunda nota : '))
print('=' * 40)

soma = nota1 + nota2
media = (nota1 + nota2) / 2
cores = {'limpo':'\033[m',
         'branco':'\033[1;4;30m',
         'vermelho':'\033[1;4;31m',
         'verde':'\033[1;4;32m',
         'amarelo':'\033[1;4;33m',
         'azul':'\033[1;4;34m',
         'roxo':'\033[1;4;35m',
         'ciano':'\033[1;4;36m',
         'cinzento':'\033[1;4;37m'}
# Usando o format()
print('A soma das suas notas é igual a {}{:.1f}{}.\nA sua media é de '
      '{}{:.1f}{} valores.'.format(cores['cinzento'], soma, cores['limpo'],
                               cores['verde'], media, cores['limpo']))
print('=' * 40)

# Outra maneira
# print('A soma de {} e {} e igual a {} valores.'.format(nota1, nota2, soma))
# print('A sua media é igual a {:.2f} valores.'.format(media))

# Sem o format()
# print('A soma das suas notas é igual a ', soma)
# print('A media das suas notas é igual a ', media)
#=================================================================================





