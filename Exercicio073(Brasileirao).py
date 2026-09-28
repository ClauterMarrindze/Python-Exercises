#=======================================================================================================================
'''
Exercicio 073:
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brazileiro de futebol,
na ordem de colocacao. Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os ultimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posiocao na tabela está o time do chapecoence.
'''
#=======================================================================================================================
print('=' * 90)
print(f'\033[1;32m{'BRAZILEIRAO 2026/27':^90}\033[m')
print('=' * 90)
Brazileirao = ('Palmeiras','Flamengo','Athletico-PR','Fluminense','Cruzeiro','Bahia',
               'Red Bull Bragantino','Atlético-MG','Corinthians','Coritiba','Botafogo',
               'Vitória','São Paulo','Santos','Grêmio','Internacional','Mirassol',
               'Remo','Vasco da Gama','Chapecoense')
# Alínea A
print('Os 5 primeiros colocados da tabela : ')
print(Brazileirao[:5])
print('-' * 90)
# Alinea B
print('Os ultimos 4 colocados da tabela : ')
print(Brazileirao[-4:])
print('-' * 90)
# Alinea C
print('Lista em ordem Alfabetica :')
print(f'{sorted(Brazileirao)}')
print('-' * 90)
# Alinea D
print(f'Chapecoense está na {Brazileirao.index('Chapecoense') + 1} posicao.')
print('=' * 90)
print(f'\033[1;33m{'FIM DA COMPETIÇÃO':^90}\033[m')
print('=' * 90)
'''for clubes in Brazileirao:
    print(clubes)'''