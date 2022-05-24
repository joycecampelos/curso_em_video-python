'''
DESAFIO 044 - Elabora um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''

print('=' * 10, end = '')
print('LOJAS GUANABARA', end = '')
print('=' * 10)

preço = float(input('Preço das compras: R$'))

print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opção = int(input('Qual é a opção? '))

if opção == 1:
    desconto = preço - (preço * 10 / 100)
    print(f'Sua compra de R${preço:.2f}, vai custar R${desconto:.2f} no final.')
elif opção == 2:
    desconto = preço - (preço * 5 / 100)
    print(f'Sua compra de R${preço:.2f}, vai custar R${desconto:.2f} no final.')
elif opção == 3:
    parcela = preço / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS')
    print(f'Sua compra de R${preço:.2f}, vai custar o mesmo valor no final.')
elif opção == 4:
    parcelas = int(input('Quantas parcelas? '))
    preçonovo = preço + (preço * 20 / 100)
    valorparcelas = preçonovo / parcelas
    print(f'Sua compra será parcelada em {parcelas}x de R${valorparcelas:.2f} COM JUROS')
    print(f'Sua compra de R${preço:.2f}, vai custar R${preçonovo:.2f} no final.')
else:
    print('Opção inválida. Tente novamente!')
