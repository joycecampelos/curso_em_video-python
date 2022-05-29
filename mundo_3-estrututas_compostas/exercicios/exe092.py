'''
DESAFIO 092 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''

from datetime import date
dados = dict()
dados['Nome'] = str(input('Nome: '))
anodenascimento = int(input('Ano de nascimento: '))
dados['Idade'] = date.today().year - anodenascimento
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['CTPS'] > 0:
    dados['Ano de Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = (dados['Ano de Contratação'] - anodenascimento) + 35
print()
for k, v in dados.items():
    print(f'- {k} tem o valor {v}.')
