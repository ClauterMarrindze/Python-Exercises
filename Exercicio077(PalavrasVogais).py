#=======================================================================================================================
'''
Exercicio 077:
Crie um programa que tenha uma tupla com várias palavras (Não usar acentos).
Depois disso, voce deve mostrar, para cada palavra, quais são as suas vogais.
'''
#=======================================================================================================================
print('=' * 50)
print(f'\033[1;31m{'PALAVRAS':^50}\033[m')
print('=' * 50)
palavras = ('aprender','programar','python','ficar','milionario','rico',
            'mercado','tecnologia','estudar','futuro','sempre','Carreira',
            'Seriedade','Familia','Provedor')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos : ', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
print('\n')
print('=' * 50)
print(f'{'FIM DO PROGRAMA':^50}')
print('=' * 50)