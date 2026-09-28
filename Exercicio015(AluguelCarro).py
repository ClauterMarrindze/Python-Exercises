# Exercicio 015
#=====================================================================
# Escreva um programa que pergunte a quantidade de kilometros rodados
# por um carro alugado e a quantidade de dias pelos quais foi alugado.
# calcule o preço a pagar, sabeno que o carro custa R$60 por dia, e
# R$0.15 por kilometro.
#======================================================================
print('=' * 50)
print('\033[1;36m{:^50}\033[m'.format('ALUGUEL DE CARROS!'))
print('=' * 50)
dias = int(input('Por quantos dias o carro rodou : '))
kilometragem = float(input('Quantos kilometros o carro rodou : '))
preco = ((kilometragem * 0.15) + (dias * 60))

cores = {'limpo':'\033[m','vermelho':'\033[1;31m','azul':'\033[1;34m',
         'amarelo':'\033[1;33m', 'roxo':'\033[1;35m','ciano':'\033[1;36m'}
print('=' * 50)
# kilo = kilometragem * 0.15
# quantDias = dias * 60
# preco = kilometragem + quantDias
#print('O aluguel do carro ira te custar R$',preco)
print('O aluguel do carro ira te custar \033[1;36mR$\033[m{}{:.2f}{}'
      .format(cores['roxo'], preco, cores['limpo']))
print('=' * 50)
print('{:^60}'.format('\033[1;33mFIM DO PROGRAMA\033[m'))
print('=' * 50)
#======================================================================








