'''
DESAFIO 057 - Faça um programa que leia o sexo de uma pessoa, mas só aceita os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]

'''condição = 1
while condição != 0:
    if sexo in 'M' or sexo in 'F':
        print(f'Sexo {sexo} registrado com sucesso.')
        condição = 0
    else:
        sexo = str(input('Dados inválidos. Por favor, informe seu sexo: '))
        condição = 1'''

while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')
