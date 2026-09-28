#=================================================================================
'''
EXERCICIO 022: Crie um programa que leia o nome completo de uma pessoa e mostre :
- O nome com todas as letras maiúsculas
- O nome com todas as letras minusculas
- Quantas letras possui ao todo, sem considerar espacos.
- Quantas letras tem o primeiro nome.
'''
#=================================================================================
'''
nome = str(input('Introduze o seu nome completo: '))
print('='*35)
print('Em Maiúsculas :',nome.upper())
print('Em minúsculas :',nome.lower())
print('O nome possui ao todo ',len(nome.strip()) - nome.count(' '),' letras.')
primeiro = nome.split()
print('O primeiro nome tem ',len(primeiro[0]),' letras.')
print('='*35)
'''
#=================================================================================
#                                  MODO GUANABARA

print('=' * 50)
print('\033[1;35m{:^50}\033[m'.format('NOME COMPLETO ESPECIALIZADO'))
print('=' * 50)
nome = str(input('Introduza o seu \033[1;34mnome completo\033[m : ')).strip()
print('=' * 50)

cores = {'limpo':'\033[m','branco':'\033[1;30m','vermelho':'\033[1;31m',
         'verde':'\033[1;32m','amarelo':'\033[1;33m','azul':'\033[1;34m',
         'roxo':'\033[1;35m','ciano':'\033[1;36m','cinza':'\033[1;37m'}

print('Em \033[1;31mmaiúsculas\033[m :','\033[1;35m',nome.upper(),'\033[m')
print('Em \033[1;34mminusculas\033[m :','\033[1;36m',nome.lower(),'\033[m')
print('O seu nome tem ao todo','\033[1;34m',len(nome) - nome.count(' '),'letras\033[m.')
primeiro = nome.split()
print('O primeiro nome é','\033[1;31m',(primeiro[0]),'\033[m',', e tem','\033[1;36m',len(primeiro[0]),'letras\033[m.')
#print('O seu primeiro nome é tem ',nome.find(' '),' letras.')
print('=' * 50)
print('\033[1;33m{:^50}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 50)

#==================================================================================