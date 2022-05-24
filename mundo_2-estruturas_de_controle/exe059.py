'''
DESAFIO 059 - Crie um programa que leia dois valores e mostre um menu na tela. Seu programa deverá realizar a operação solicitada em cada caso:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
'''

from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

opção = 0

while opção != 5:

    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('>>>>> Qual é a sua opção? '))

    if opção == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma}.')
    elif opção == 2:
        multiplicação = n1 * n2
        print(f'O resultado de {n1} x {n2} é {multiplicação}.')
    elif opção == 3:
        maior = 0
        if n1 > n2:
            maior = n1
            print(f'Entre {n1} e {n2} o maior valor é {maior}.')
        elif n2 > n1:
            maior = n2
            print(f'Entre {n1} e {n2} o maior valor é {maior}.')
        else:
            print('Os valores são iguais.')
    elif opção == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente!')

    print('=-=' * 10)
    sleep(2)

print('Fim do programa! Volte sempre!')
