#=======================================================================
'''
    EXERCICIO 033: Faca um programa que leia tres numeros e
    mostre qual é o maior e qual é o menor.
'''
#=========================================================
'''
numero1 = float(input('Introduze o primeiro numero : '))
numero2 = float(input('Introduze o segundo numero : '))
numero3 = float(input('Introduze o terceiro numero : '))
#=========================================================
# Teste do maior 
maior = numero1
if numero2 > numero1 and numero2 > numero3:
    maior = numero2
if numero3 > numero2 and numero3 > numero1:
    maior = numero3

print('=' * 25)    
print('O Maior Numero é ',maior)
#=========================================================
# Teste do menor 
menor = numero1
if numero2 < numero1 and numero2 < numero3:
    menor = numero2
if numero3 < numero2 and numero3 < numero1:
    menor = numero3
    
print('O Menor Numero é ',menor)
print('=' * 25)
'''
#=========================================================

#============================================================
#                   MODO GUANABARA
#============================================================
print('=' * 35)
print('{:^65}'.format('\033[1;36mMAIOR\033[m E \033[1;35mMENOR\033[m \033[1;37mNUMERO\033[m'))
print('=' * 35)
a = int(input('Introduza o \033[1;31mprimeiro numero\033[m : '))
b = int(input('Introduza o \033[1;32msegundo numero\033[m : '))
c = int(input('Introduza o \033[1;33mterceiro numero\033[m : '))

# Pra testar o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# Pra testar o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

cores = {'limpo': '\033[m','branco': '\033[1;30m','vermelho':'\033[1;31m','verde':'\033[1;32m',
         'azul': '\033[1;34m','amarelo':'\033[1;33m','roxo':'\033[1;35m','ciano':'\033[1;36m',
         'cinzento':'\033[1;37m'}

print('=' * 35)
print('O \033[1;37mmenor\033[m valor é {}{}{}'.format(cores['ciano'], menor, cores['limpo']))
print('O \033[1;31mmaior\033[m valor é {}{}{}'.format(cores['roxo'], maior, cores['limpo']))
print('=' * 35)
print('\033[1;33m{:^35}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 35)
#===============================================================