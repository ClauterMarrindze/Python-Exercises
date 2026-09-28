#========================================================================================
'''
    EXERCICIO 035:
    Desenvolva um programa que leia o comprimento de 3 retas, e diga se elas podem
    ou não formar um triangulo.
'''
#=========================================================================================
'''
    REGRA:
    Pra formar um triângulo, cada um dos segmentos de reta tem que ser menor que a 
    soma do comprimento dos outros dois segmentos.
'''
print('=' * 45)
print('\033[1;35m{:^40}\033[m'.format('ANALISADOR DE TRIANGULOS'))
print('=' * 45)

reta1 = float(input('Informe o comprimento da \033[1;32mprimeira reta\033[m : '))
reta2 = float(input('Informe o comprimento da \033[1;33msegunda reta\033[m : '))
reta3 = float(input('Informe o comprimento da \033[1;34mterceira reta\033[m : '))
print('=' * 45)
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os Segmentos de \033[1;37mreta\033[m acima mencionados\n'
          '\033[1;32mPODEM FORMAR UM TRIANGULO\033[m.')
else:
    print('Os Segmentos de \033[1;37mreta\033[m acima mencionados\n'
          '\033[1;31mNAO PODEM FORMAR UM TRIANGULO\033[m.')
print('=' * 45)
print('\033[1;33m{:^45}\033[m'.format('FIM DO PROGRAMA'))
print('{}'.format('=' * 45))


