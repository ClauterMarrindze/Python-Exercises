#======================================================================================================================
'''
Exercicio 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o
    seu preço e condicao de pagamento:
    - A vista Dinheiro/Cheque: 10% de desconto
    - A vista no Cartao: 5% de desconto
    - Em até 2x no cartao: preco normal
    - 3x ou mais no cartao: 20% de juros
'''
#======================================================================================================================
print('=' * 50)
print('\033[1;36m{:^50}\033[m'.format('SHOPPING CENTER KLY'))
print('=' * 50)
preco = float(input('Informe o preco total dos produtos : '))
print('''Escolha o modo de pagamento...
[ 1 ] - A Vista Dinheiro/Cheque
[ 2 ] - A Vista no Cartao
[ 3 ] - 2 vezes no Cartao
[ 4 ] - 3 vezes ou mais no Cartao ''')
print('-' * 50)
opcao = int(input('Escolha a sua opcao : '))
print('-' * 50)

if opcao == 1 :
    desconto1 = preco * 0.10
    precoTotal = preco - desconto1
    print('Parabéns, terá desconto de 10%\nQue são {:.2f} a menos do total.'.format(desconto1))
    print('No total, irá pagar {:.2f}Mt sem juros'.format(precoTotal))

elif opcao == 2 :
    desconto2 = preco * 0.05
    precoTotal = preco - desconto2
    print('Parabéns, terá desconto de 5%\nQue são {:.2f} a menos do total.'.format(desconto2))
    print('No total, irá pagar {:.2f}Mt sem juros'.format(precoTotal))

elif opcao == 3 :
    parcela = preco / 2
    print('No total, irá pagar {:.2f}Mt sem juros'
          '\nEm duas Parcelas (Irá pagar 2 vezes o valor acima).'.format(parcela))

elif opcao == 4 :
    precoTotal = preco + (preco * 0.20)
    totalParcela = int(input('Quantas parcelas? : '))
    parcela = precoTotal / totalParcela
    print('No total irá pagar {:.2f}Mt com juros'.format(precoTotal))
    print('Em {} parcelas de {:.2f}Mt'.format(totalParcela, parcela))
else:
    print('\033[1;31m{:^50}\033[m'.format('OPÇÃO INVÁLIDA!'))
    print('\033[m{:^50}\033[m'.format('TENTE NOVAMENTE!'))
    print('\033[1;32mIrás pagar {:.2f}Mt\033[m'.format(preco))
print('=' * 50)
print('\033[1;33m{:^50}\033[m'.format('TENHA UM BOM DIA!'))
print('\033[1;34m{:^50}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 50)