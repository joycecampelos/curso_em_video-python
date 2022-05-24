'''
DESAFIO 070 - Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
'''

print('-' * 36)
print('         LOJA SUPER BARATÃO         ')
print('-' * 36)
total = acimademil = cont = valorbarato = 0
nomebarato = ''
while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    total += preço
    if preço > 1000:
        acimademil += 1
    cont += 1
    if cont == 1 or preço < valorbarato:
        nomebarato = nome
        valorbarato = preço
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print('----------- FIM PROGRAMA -----------')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {acimademil} produto(s) custando mais de R$1000.00.')
print(f'O produto mais barato foi a(o) {nomebarato} que custa R${valorbarato:.2f}')
