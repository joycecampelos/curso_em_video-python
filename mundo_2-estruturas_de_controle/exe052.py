'''
DESAFIO 052 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''

numero = int(input('Digite um número: '))
qtd = 0

for c in range(1, numero + 1):
    if numero % c == 0:
        qtd += 1
print(f'O número {numero} foi divisível {qtd} vezes.')
if qtd == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
