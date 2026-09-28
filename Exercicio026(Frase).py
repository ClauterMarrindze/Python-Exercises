#================================================================
'''
 EXERCICIO 026:
Faca um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra 'A'
- Em que posicao ela aparece a primeira vez.
- Em que posicao ela aparece a ultima vez.
'''
print('=' * 50)
print('\033[1;32m{:^50}\033[m'.format('ANALISE DE FRASES'))
print('=' * 50)
frase = str(input('Introduze uma frase : ')).strip().upper()
print('=' * 50)
print('A letra (A) aparece','\033[1;33m',frase.count('A'),'\033[m',
      'vez(es) na frase \n','\033[1;34m',frase,'\033[m')
print('A \033[1;31mprimeira letra (A)\033[m aparece na posicao','\033[1;35m',frase.find('A')+1,'\033[m')
print('A \033[1;32multima letra (A)\033[m aparece na posicao','\033[1;36m',frase.rfind('A')+1,'\033[m')
print('=' * 50)
print('\033[1;33m{:^50}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 50)




