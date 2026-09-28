#===============================================================================================
'''
    EXERCICIO 029:  Esreva um programa que leia a velocidade de um carro.
    Se ele ultrapassar 80km/h, mostre na tela uma mensagem dizendo que ele foi multado.
    A multa vai custar R$7.00 por cada quilometro acima do limite.
'''
#=======================================================================================
'''
velocidade = int(input('Introduze a velocidade atual do carro: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    # print('Serás Multado por excesso de Velocidade!\nValor R$',multa)
    print('=' * 40)
    print('Serás Multado por excesso de Velocidade!'
          '\nPois o limite é de 80Km/h!\nValor R${:.2f}'.format(multa))
    print('Conduza com cuidado!\nTenha um bom dia!')
    print('=' * 40)
else:
    print('=' * 25)
    print('Bom Condutor!\nBoa Viagem!')
    print('Tenha um bom dia!')
    print('=' * 25)
 '''
#========================================================================================
#                                     MODO GUANABARA

print('=' * 50)
print('\033[1;35m{:^50}\033[m'.format('MULTA POR ULTRAPASSAGEM'))
print('=' * 50)
velocidade = float(input('Informe a \033[1;33mvelocidade atual do carro\033[m : '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('=' * 50)
    print('Multado por \033[1;31mexcesso de Velocidade\033[m!'
          '\n\033[1;31mLimite de Velocidade\033[m : \033[1;34m80km/h\033[m'
          '\nO \033[1;36mValor da multa\033[m é R$\033[1;35m{:.2f}\033[m'.format(multa))
    print('=' * 50)
else:
    print('=' * 50)
    print('\033[1;32mLimite de Velocidade Aceite\033[m!')
    print('\033[1;33mTenha um bom dia!\n\033[1;36mConduza com cuidado\033[m!')
    print('=' * 50)
print('\033[1;33m{:^50}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 50)

#==========================================================================================