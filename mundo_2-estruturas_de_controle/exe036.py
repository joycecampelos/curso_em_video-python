'''
DESAFIO 036 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.
'''

valordacasa = float(input('Valor da casa: R$'))
salariodocomprador = float(input('Salário do comprador: R$'))
anosdofinanciamento = int(input('Quantos anos de financiamento? '))

valordasparcelas = valordacasa / (anosdofinanciamento * 12)
print(f'Para pagar uma casa de R${valordacasa:.2f} em {anosdofinanciamento} anos, a prestação será de R${valordasparcelas:.2f}.')

minimoparaaprovacao = salariodocomprador * (30 / 100)

if valordasparcelas <= minimoparaaprovacao:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
