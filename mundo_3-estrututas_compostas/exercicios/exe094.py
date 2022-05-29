'''
DESAFIO 094 - Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
a) Quantas pessoas foram cadastradas
b) A média de idade
c) Uma lista com as mulheres
d) Uma lista de pessoas com idade acima da média
'''

pessoa = dict()
lista = list()
soma = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    lista.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print(f'\nA) Ao todo temos {len(lista)} pessoas cadastradas.')
média = soma / len(lista)
print(f'B) A média de idade é de {média:.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in lista:
    if p['Sexo'] == 'F':
        print(f'[{p["Nome"]}] ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in lista:
    if p['Idade'] >= média:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<< ENCERRADO >>>')
