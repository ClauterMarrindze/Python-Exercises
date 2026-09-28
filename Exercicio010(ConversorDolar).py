# Exercicio 010.
#
#      Crie um programa que leia quanto dinheiro uma pessoa tenha na carteira e mostre quantos dólares
#      ela pode comprar.(Considere USD 1,00 = RS 3,27 e USD 1,00 = MT 63,9088).

#======================================================================================================
# Com o dolar valendo 3,27
print('=' * 55)
print('\033[1;32m{:^65}'.format('CONVERSOR \033[mDE \033[1;32mMOEDAS\033[m'))
print('=' * 55)
valorRS = float(input('Quanto dinheiro possuis na carteira? \033[1;36mR$\033[m : '))
cores = {'limpo':'\033[m','vermelho':'\033[1;31m',
         'verde':'\033[1;32m','amarelo':'\033[1;33m',
         'azul':'\033[1;34m','roxo':'\033[1;35m',
         'ciano':'\033[1;36m','cinzento':'\033[1;37m'}
compraDolarRS =  valorRS / 3.27
print('=' * 55)
print('Com {}R$ {}{:.2f}{} (Reais) \nPodes ter {}US$ {}{:.2f}{} (Dólares).'
      .format(cores['ciano'], cores['cinzento'], valorRS, cores['limpo'],
              cores['ciano'], cores['verde'], compraDolarRS, cores['limpo']))
print('=' * 55)
#print('Com esse dinheiro podes ter ', compraDolar1, ' USD (Dólares).')

#valorMt = float(input('Quanto dinheiro possuis na carteira? Mt: '))
#compraDolarMt = valorMt / 63.9088

#print('Com {:.2f} Mt (Meticais) podes ter {:.2f} USD (Dólares).'.format(valorMt, compraDolarMt))
#print('Com esse valor podes ter ', compraDolarMt, ' USD (Dólares). ')

#======================================================================================================
# Exercicio Bonus (Dolar - Real, Metical)

#valorUSD1 = float(input('Quanto dinheiro possuis na carteira? USD: '))
#compraReal = valorUSD1 * 3.27
#print('Com {:.2f} USD (Dólares) podes comprar {:.2f} R$ (Reais).'.format(valorUSD1, compraReal))
#print('Com esse valor podes comprar ', compraReal, ' USD (Dolares).')


#valorUSD2  = float(input('Quando dinheiro possuis na carteira? USD: '))
#compraMetical = valorUSD2 * 63.9088
#print('Com {:.2f} USD (Dólares) podes comprar {:.2f} Mt (Meticais).'.format(valorUSD2, compraMetical))
#print('Com esse valor podes comprar', compraMetical,' Mt (Meticais).')
#========================================================================================================





