# Exercicio 012.
#===========================================================================
# Faca um programa que leia o preco de um produto e mostre seu novo preco,
# com 5% de desconto.
#===========================================================================

#preco = float(input('Introduza o preço do produto: '))
#desconto = preco * 0.05
#novoPreco = preco - desconto

# Usado o .format()
#print('Teras 5% de desconto, que são {} Reais.\n'
     # 'O novo preco do produto é {} Reais'
     # .format(desconto, novoPreco))

# Sem o .format()
#print('Teras 5% de desconto, que são', desconto,
#      ' Reais.\nO novo preco do produto é ',novoPreco,' Reais')
# ===========================================================================


print('=' * 40)
print('\033[1;36m{:^40}\033[m'.format('DESCONTO DE PREÇOS'))
print('=' * 40)
preco = float(input('Introduza o preço do produto \033[mR$\033[m : '))
#desconto = preco * (5/100)
#novoPreco = preco - desconto
novoPreco = preco - (preco * (5 / 100))

# Usado o .format()
#print('Teras 5% de desconto, que são R${:.2f} Reais.\n'
#      'O novo preco do produto é R${:.2f} Reais'
#      .format('''desconto''', novoPreco))
cores = {'limpo':'\033[m', 'branco':'\033[1;30m', 'vermelho':'\033[1;31m',
         'verde':'\033[1;32m','amarelo':'\033[1;33m', 'azul':'\033[1;34m',
         'roxo':'\033[1;35m','ciano':'\033[1;36m','cinzento':'\033[1;37m'}

print('=' * 40)
print('O produto que custava \033[1;32mR$\033[m{}{:.2f}{}.\nNa Promoção com '
      'desconto de {}5%{}\nVai custar \033[1;32mR$\033[m{}{:.2f}{}'
      .format(cores['vermelho'], preco, cores['limpo'],
              cores['ciano'], cores['limpo'],
              cores['roxo'], novoPreco, cores['limpo']))
print('=' * 40)
print('\033[1;32m{:^40}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 40)

# Sem o .format()
#print('Teras 5% de desconto, que são', desconto,
#      ' Reais.\nO novo preco do produto é ',novoPreco,' Reais')
#============================================================================









