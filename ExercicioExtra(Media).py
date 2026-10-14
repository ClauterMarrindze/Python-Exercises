print('=' * 40)
print('\033[1;36m{:^40}\033[m'.format('SIGA 10.0'))
print('=' * 40)
soma = contador = 0

for c in range(0, 3):
    notas = float(input(f'Insira a {c+1}a nota: '))
    soma += notas
    contador += 1
print('=' * 40)

media = soma/contador
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