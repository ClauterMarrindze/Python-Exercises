#================================================================================================
'''
    EXERCICIO 031: Desenvolva um programa que pergunte a distancia de uma viagem em
    kilometros. Calcule o preco da passagem, cobrando R$0.50 por kilometro para viagens até
    200km e R$0.45 para viagens mais longas.
'''
#=================================================================================================
'''
distancia = float(input('Introduze a distancia da viagem em km:'))
if distancia <= 200:
    preco1 = distancia * 0.50
    #print('Por bilhete de passagem irá pagar R$',preco1)
    print('Por bilhete de passagem ira pagar R${:.2f}'.format(preco1))
else:
    preco2 = distancia * 0.45
    #print('Por bilhete de passagem ira pagar R$',preco2)
    print('Por bilhete de passagem ira pagar R${:.2f}'.format(preco2))
print('BOA VIAGEM')
'''
#===================================================================================================
#                                                MODO GUANABARA
print('=' * 50)
print('\033[1;35m{:^50}\033[m'.format('BILHETERIA'))
print('=' * 50)
distancia = float(input('Qual é a \033[1;35mdistancia\033[m da \033[1;34mviagem\033[m em \033[1;31mkm\033[m : '))
print('=' * 50)
cores = {'limpo': '\033[m','branco':'\033[1;30m','vermelho':'\033[1;31m','azul':'\033[1;34m',
         'amarelo':'\033[1;33m','verde':'\033[1;32m','roxo':'\033[1;35m','ciano':'\033[1;36m',
         'cinzento':'\033[1;37m'}

print('Você está prestes a \033[1;32mcomeçar\033[m uma \033[1;35mviagem\033[m de {}{}km{}'
      .format(cores['cinzento'], distancia, cores['limpo']))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('E o preco da sua \033[1;36mpassagea\033[m será de R${}{:.2f}{}'
      .format(cores['ciano'], preco, cores['limpo']))
print('=' * 50)
print('\033[1;33m{:^50}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 50)


#===================================================================================================
#                                       FAZENDO COM IF SIMPLIFICADO
'''
distancia = float(input('Qual é a distancia da viagem em km :'))
print('=' * 50)
print('Você está prestes a comecar uma viagem de {}km'.format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preco da sua passagem irá custar R${:.2f} '.format(preco))
print('=' * 50)
'''
