# Exercicio 008.
# =========================================================================
# Escreva um programa que leia um valor em metros e o exiba convertido
# em centimetros e milimetros.

#==========================================================================
# Kilómetro Hectómetro Decametro metro Decimetro Centímetro Milímetro

print('=' * 40)
print('\033[1;35m{:^50}\033[m'.format('CONVERSOR \033[mDE\033[1;35m DISTANCIA'))
print('=' * 40)
valor = float(input('Introduza o valor(metros) : '))
kilometro = valor / 1000
hectometro = valor / 100
decametro = valor / 10

decimetro = valor * 10
centimetro = valor * 100
milimetro = valor * 1000

cores = {'limpo':'\033[m',
         'branco':'\033[1;30m', 'vermelho':'\033[1;31m',
         'verde':'\033[1;32m', 'amarelo':'\033[1;33m',
         'azul':'\033[1;34m', 'roxo':'\033[1;35m',
         'ciano':'\033[1;36m', 'cinzento':'\033[1;37m'}

# Usando o format
print('=' * 40)
print('{}{:.1f}{} metros são {}{:.4f}{} kilómetros.\n{}{:.1f}{} metros são {}{:.4f}{} hectómetros.'
       '\n{}{:.1f}{} metros são {}{:.4f}{} decámetros.\n{}{:.1f}{} metros são {}{:.1f}{} decimetros.'
       '\n{}{:.1f}{} metros são {}{:.1f}{} centimetros.\n{}{:.1f}{} metros são {}{:.1f}{} milimetros.'
       .format(cores['cinzento'], valor, cores['limpo'],
               cores['vermelho'],kilometro, cores['limpo'],
               cores['cinzento'], valor, cores['limpo'],
               cores['verde'], hectometro, cores['limpo'],
               cores['cinzento'], valor, cores['limpo'],
               cores['amarelo'], decametro, cores['limpo'],
               cores['cinzento'], valor, cores['limpo'],
               cores['azul'], decimetro, cores['limpo'],
               cores['cinzento'], valor, cores['limpo'],
               cores['roxo'], centimetro, cores['limpo'],
               cores['cinzento'], valor, cores['limpo'],
               cores['ciano'], milimetro, cores['limpo'],))
print('=' * 40)

# Sem o format()
#print('Em centimetros são :', centimetro,'cm.')
#print('Em milimetros são :', milimetro,'mm.')
#==========================================================================


