#==========================================================
'''
    EXERCICIO 024: Crie um programa que leia o nome da sua
    cidade e diga se ela comeca com o nome 'Santo'.
'''
'''
cidade = str(input('Introduze o nome da cidade : ')).strip()
print('Tem o nome da cidade em primeiro?')
print('=' * 20)
print(cidade[0:5].lower() == 'SANTO')
print(cidade[:5].lower() == 'Santo')
print('=' * 20)
'''
#==========================================================
#                     Pra Maputo
print('=' * 60)
print('\033[1;36m{:^60}\033[m'.format('CIDADE ESPECIAL'))
print('=' * 60)
cidade = str(input('Introduze o nome da \033[1;35mcidade\033[m: ')).strip()
print('Tem o nome da cidade em \033[1;36m(MAPUTO)\033[m em \033[1;31mprimeiro\033[m?')
print('-' * 60)
print('\033[1;37mTrue\033[m - \033[1;32mVerdadero\033[m')
print('\033[1;37mFalse\033[m - \033[1;31mFalso\033[m')
print('-' * 60)
print(cidade[0:6].upper() == 'MAPUTO')
print(cidade[:6].lower() == 'maputo')
print('=' * 60)
print('\033[1;33m{:^60}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 60)
#===========================================================












