#=========================================================================================================
'''
 Exercicio 042: Refaca o desafio 35 dos triangulos, acrescentando o recurso de mostrar na tela que
    tipo de triangulo será formado :
    _Equilatero: todos lados iguais ;
    _Isósceles: dois lados iguais ;
    _Escaleno: todos lados diferentes ;
'''
#======================================================================================================

print('=' * 50)
print('\033[1;37m{:^50}\033[m'.format('TIPOS DE TRIANGULO'))
print('=' * 50)
lado1 = float(input('Digite o \033[1;37mprimeiro\033[m lado : '))
lado2 = float(input('Digite o \033[1;37msegundo\033[m lado : '))
lado3 = float(input('Digite o \033[1;37mterceiro\033[m lado : '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2 :
    print('Os Lados acima podem formar um triangulo'
          )
    if lado1 == lado2 == lado3 :
        print('Triangulo \033[1;34mEQUILATERO\033[m')

    elif lado1 != lado2 != lado3 != lado1 :
        print('Triangulo \033[1;35mESCALENO\033[m')

    else :
        print('Triangulo \033[1;36mISÓSCELLES\033[m')

else:
    print('\033[1;31mOs Lados acima não podem formar um triangulo!\033[m')
print('=' * 50)
print('\033[1;33m{:^50}\033[m'.format('FIM DO PROGRAMA'))
print('=' * 50)

#===========================================================================================================