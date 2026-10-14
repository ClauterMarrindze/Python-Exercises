#=======================================================================================================================
# Exercicio 080 - Crie um programa onde o usuário possa digitar cinco valores numéricos e
# cadastre-os em uma lista, ja na posicao correta de insercao(sem usar o sort()).
# No final, mostre a lista ordenada na tela.
#=======================================================================================================================
# VERSAO ORIGINAL

print('=' * 60)
print(f'\033[1;34m{'LISTA ORDENADA':^60}\033[m')
print('=' * 60)
listaNumeros = list()
primeiro = ultimo = 0
for c in range(0, 5):
    numeros = (int(input(f'Insira o \033[1;35m{c+1}\033[mo valor: ')))
    if c == 0 or numeros > listaNumeros[-1]:
        listaNumeros.append(numeros)
        print('\033[1;35mAdicionado com sucesso\033[m!!!')
        print('-' * 60)
    else:
        posicao = 0
        while posicao < len(listaNumeros):
            if numeros <= listaNumeros[posicao]:
                listaNumeros.insert(posicao, numeros)
                print(f'\033[1;32mAdicionado com sucesso\033[m.')
                print('-' * 60)
                break
            posicao += 1
print(f'Os valores difgitados na ordem foram : {listaNumeros}')
print('=' * 60)

# VERSAO APRIMORADA
# Fazer ele colocar só uma vez um determinado numero


