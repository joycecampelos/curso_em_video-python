'''
DESAFIO 038 - Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''

primeirovalor = int(input('Primeiro número: '))
segundovalor = int(input('Segundo número: '))

if primeirovalor > segundovalor:
    print('O primeiro valor é maior')
elif segundovalor > primeirovalor:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')
