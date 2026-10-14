#=======================================================================================================================
# Exercicio 083 -
# Crie um programa onde o usuário digite uma expressão matemática
# qualquer que use parenteses.
# Seu aplicativo deve analisar se a expressao passada está com os
# parenteses devidamente colocados.

#=======================================================================================================================

print('=' * 50)
print(f'\033[1;34m{'EXPRESSAO MATEMATICA':^50}\033[m')
print('=' * 50)
listaExpressao = []
expressao = str(input('Insira uma expressao: '))
for simbolo in expressao:
    if simbolo == '(':
        listaExpressao.append('(')
    elif simbolo == ')':
        if len(listaExpressao) > 0:
            listaExpressao.pop()
        else:
            listaExpressao.append(')')
            break
print('=' * 50)
if len(listaExpressao) == 0:
    print('\033[1;32mA sua expressão é válida\033[m!')
    print('=' * 50)
else:
    print('\033[1;31mA sua expressão não é válida\033[m!')
    print('=' * 50)