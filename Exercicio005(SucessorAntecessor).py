# Exercicio 005.
# ===========================================================================
# Faça um programa que leia um número inteiro e
# mostre na tela o seu antecessor e seu sucessor.
# ===========================================================================

print('=' * 40)
print('\033[1;31m{:^50}\033[m'.format('ANTECESSOR\033[m E \033[1;32mSUCESSOR\033[m'))
print('=' * 40)
numero = int(input('Introduza um valor(Inteiro) : '))
cores = {'limpo':'\033[m',
         'branco':'\033[1;30m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'roxo':'\033[1;35m',
         'ciano':'\033[1;36m',
         'cinzento':'\033[1;37m',}
#antecessor = numero1 - 1
#sucessor = numero1 + 1

# Usando o Format.()
# print('O antecessor de {} é o numero {}.'.format(numero1, antecessor))
# print('O sucessor de {} é o numero {}.'.format(numero1, sucessor))

# Outra maneira de mostrar
#print('O Antecessor de {} é o numero {}. \nO Sucessor de {} é o numero {}.'
#      .format(numero1, antecessor, numero1, sucessor))

#print('O seu antecessor é',numero - 1,'.\nE o seu sucessor é ',numero + 1,'!')
print('=' * 40)
print('O antecessor de {}{}{} é {}{}{}.\nE o sucessor de {}{}{} é {}{}{}.'
      .format(cores['roxo'], numero, cores['limpo'] ,
              cores['vermelho'], numero - 1, cores['limpo'],
              cores['roxo'], numero, cores['limpo'],
              cores['verde'], numero + 1, cores['limpo']))
print('=' * 40)

# Sem usar o format.()
#print('O antecessor do numero introduzido é', antecessor)
#print('O sucessor do numero introduzido é', sucessor)
#=============================================================================