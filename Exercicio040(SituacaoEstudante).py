#===========================================================================================
'''
    Exercicio 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
    mostrando uma mensagem no final, de acordo com a media atingida:
    - abaixo de 5.0: reprovado
    - entre 5.0 e 6.9: recuperado
    - media 7.0 ou superior: aprovado
'''
#====================================================================================================
print('=' * 40)
print('\033[1;32m{:^40}\033[m'.format('SITUACAO ACADEMICA'))
print('=' * 40)
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
print('-' * 40)
media = (nota1 + nota2) / 2
if media < 5 :
    print('Infelizmente, está \033[1;31mREPROVADO!\033[m')
    print('Media : \033[1;31m{:.2f}\033[m '.format(media))
elif media >= 5 and media <= 6.9 :
    print('Parabéns, está \033[1;32mRECUPERADO\033[m!')
    print('Media : \033[1;33m{:.2f}\033[m '.format(media))
    print('\033[1;33mEstude Bastante\033[m!')
elif media >= 7.0 :
    print('Parabéns, está \033[1;36mAPROVADO\033[m!')
    print('Media : \033[1;35m{:.2f}\033[m '.format(media))
print('-' * 40)
print('\033[1;34m{:^40}\033[m'.format('Tenha um bom dia!'))
print('\033[1;33m{:^40}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 40)
#===================================================================================================
#
