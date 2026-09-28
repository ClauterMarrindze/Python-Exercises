print('=' * 40)
print('\033[1;36m{:^40}\033[m'.format('SIGA 10.0'))
print('=' * 40)
nota1 = float(input('Introduze a \033[1;33mprimeira nota\033[m : '))
nota2 = float(input('Introduza a \033[1;35msegunda nota\033[m : '))
nota3 = float(input('Introduza a \033[1;36mterceira nota\033[m : '))
print('=' * 40)

media = (nota1 + nota2 + nota3)/3
cores = {'limpo':'\033[m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'cinzento':'\033[1;37m',
         'roxo':'\033[1;35m'}

if media < 10:
    print('A sua media é de {}{:.2f}{} valores.'
          '\nInfelizmente está \033[1;31mEXCLUIDO\033[m!!!'
          .format(cores['cinzento'], media, cores['limpo']))
elif media >= 10 and media < 14:
    print('A sua media é de {}{:.2f}{} valores.'
          '\nParabéns, está \033[1;32mADMITIDO\033[m!!!'
          .format(cores['cinzento'], media , cores['limpo']))
else:
    print('A sua media é de {}{:.2f}{} valores.'
          '\nParabéns, está \033[1;32mDISPENSADO\033[m!!!'
          .format(cores['roxo'], media, cores['limpo']))
print('=' * 40)
print('\033[1;33m{:^40}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 40)