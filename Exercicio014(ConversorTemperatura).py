# Exercicio 014
# =====================================================================
# Escreva um programa que converta uma temperatura digitada em graus
# Celcius e converta para graus Fareinheit.
#=====================================================================================

print('=' * 60)
print('{:^80}'.format('\033[1;31mCONVERSOR\033[m DE \033[1;36mTEMPERATURA\033[m'))
print('=' * 60)
tempCelcius = float(input('Introduza a temperatura corrente \033[1;34m(Graus celcius)\033[m : '))
faranH = ((9 * tempCelcius) / 5) + 32

cores = {'limpo':'\033[m', 'branco':'\033[1;30m', 'vermelho':'\033[1;31m',
         'verde':'\033[1;32m', 'amarelo':'\033[1;33m', 'azul':'\033[1;34m',
         'roxo':'\033[1;35m', 'ciano':'\033[1;36m', 'cinzento':'\033[1;37m'}
print('=' * 60)
print('A temperatura de {}{:.1f}{} graus \033[1;36mcelcius\033[m.'
      '\nCorresponde a {}{:.1f}{} graus \033[1;35mfaranHeit\033[m.'
      .format(cores['azul'], tempCelcius, cores['limpo'],
              cores['amarelo'], faranH, cores['limpo']))
print('=' * 60)
print('\033[1;33m{:^60}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 60)
#====================================================================================
# Mais tarde acrescente para todas as restantes temperaturas.
#====================================================================================
# Exercicio Bonus
# Faça o contrario do 1o pedido.
'''
tempFaranheit = float(input('Introduza a temperatura corrente (Graus faranheit) : '))
#celcius = ((tempFaranheit * 5) / 9) - 32
#celcius = tempFaranheit - 32

print('A temperatura de {:.2f} graus faranheit.'
      '\nCorresponde a {:.2f} graus celcius.'.format(tempFaranheit, celcius))
'''
#=====================================================================================




