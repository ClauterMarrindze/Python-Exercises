#=======================================================================================================================
'''
Exercicio 071 - Faça um programa que simule o funcionamento de um caixa electronico.
No inicio, pergunte ao usuário qual será o valor a ser sacado(numero inteiro).
E o programa vai informar quantas cédulas(recibos) de cada valor serão entregues.

OBS: Considere que o caixa possui cedulas(recibos) de R$50, R$20, R$10, e R$1.
'''
#=======================================================================================================================
print('=' * 50)
print(f'\033[1;36m{'CAIXA ELECTRÓNICO':^50}\033[m')
print('=' * 50)
valor = int(input('Introduze o valor do extrato : R$'))
total = valor
extratoAtual = 50
totalExtrato = 0
print('=' * 50)
while True:
    if total >= extratoAtual:
        total -= extratoAtual
        # total = total - extratoAtual
        totalExtrato += 1
        # totalExtrato = totalExtrato + 1
    else:
        if totalExtrato > 0:
            print(f'Total de {totalExtrato} estrato(s) de R${extratoAtual}')
        if extratoAtual == 50:
            extratoAtual = 20
        elif extratoAtual == 20:
            extratoAtual = 10
        elif extratoAtual == 10:
            extratoAtual = 1
        totalExtrato = 0
        if total == 0:
            break
print('=' * 50)
print(f'\033[1;33m{'FIM DA EXECUÇÃO':^50}\033[m')
print(f'\033[1;33m{'GET BACK EARLY AND ALWAYS!':^50}\033[m')
print('=' * 50)