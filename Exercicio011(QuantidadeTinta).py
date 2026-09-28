#Exercicio011.
#
#     Faca um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a
#     quantidade de tinta necessária para pintar a parede, sabendo que cada litro de tinta pinta uma
#     área de 2m Quadrados.

#====================================================================================================

print('=' * 45)
print('\033[1;35m{:^45}\033[m'.format('PINTAR PAREDE'))
print('=' * 45)
largura = float(input('Introduza a largura da parede(m) : '))
altura = float(input('Introduze a altura da parede(m) : '))
print('=' * 45)

area = largura * altura
quantidadeTinta = area / 2
cores = {'limpo':'\0333[m','branco':'\033[1;30m',
         'vermelho':'\033[1;31m','verde':'\033[1;32m',
         'amarelo':'\033[1;33m','azul':'\033[1;34m',
         'roxo':'\033[1;35m','ciano':'\033[1;36m',
         'cinzento':'\033[1;37m'}

print('Sua parede tem dimensão de \033[1;37m{:.2f}\033[m x \033[1;37m{:.2f}\033[m'
      '\nA sua area é de \033[1;31m{}m2\033[m.'
      .format(largura, altura, area))
#print('A sua area (da parede) é de {} metros quadrados.'.format(area))
#print('A sua area (da parede) é de ',area,' metros quadrados. ')

print('A quantidade de tinta para \033[1;36m{:.2f}\033[m metros\nSão de \033[1;35m{:.2f}\033[m litros.'
      .format(area,  quantidadeTinta))
print('=' * 45)
print('\033[1;33m{:^45}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 45)
#print('A quantidade de tinta para a sua parede é de ', quantidadeTinta,' litros de tinta.')
#=====================================================================================================











