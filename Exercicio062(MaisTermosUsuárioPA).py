#=======================================================================================================================
'''
Exercicio 062 - Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais
alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
'''
#=======================================================================================================================

print('=' * 60)
print('\033[1;36m{:^60}\033[m'.format('PROGRESSÃO ARITMÉTICA'))
print('=' * 60)
print('Gerador de termos de uma Progressão Aritmética'
      '\nIntroduzidos pelo Usuário.')
print('-' * 60)
primeiro = int(input('Introoduza o Primeiro termo : '))
razao = int(input('Introduza a razao : '))
termo = primeiro
contador = 1
total = 0
mais = 10
print('-' * 60)
print('Os primeiros 10 termos duma PA:')
while mais != 0:
    total = total + mais
    # ou total += mais
    while contador <= total:
        print('{} '.format(termo), end='')
        print('\033[1;36m->\033[m' if contador < total else '.', end = ' ')
        print(end = '\n' if contador >= total else '')
        termo += razao
        contador += 1
    print('-' * 60)
    print('Acréscimos...')
    mais = int(input('Quantos mais termos deseja mostrar : '))
print('-' * 60)
print('Progressão finalizada com \033[1;36m{}\033[m termos'.format(total))
print('=' * 60)
print('\033[1;33m{:^60}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 60)

#=======================================================================================================================












