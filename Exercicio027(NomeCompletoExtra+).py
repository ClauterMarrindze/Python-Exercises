#=====================================================================
'''
    EXERCICIO 027:
    Faca um programa que leia o nome completo de uma pessoa e
    mostre em seguida o primeiro e o ultimo nome separadamente.
    Ex: Ana Maria De Souza
    primeiro = Ana
    Ultimo = Souza (De Souza)
'''
print('=' * 50)
print('\033[1;34m{:^50}\033[m'.format('ANALISE DE NOMES'))
print('=' * 50)
nome = str(input('Introduze seu \033[1;32mnome completo\033[m : ')).strip().lower()
n = nome.split()
print('='*50)
print('O seu \033[1;32mprimeiro nome\033[m é : ','\033[1;36m',n[0],'\033[m')
print('ó seu \033[1;31multimo nome\033[m é : ','\033[1;35m',n[len(n)-1],'\033[m')
print('='*50)
print('\033[1;33m{:^50}\033[m'.format('FIM DO PROGRAMA'))
print('='*50)
#====================================================================


