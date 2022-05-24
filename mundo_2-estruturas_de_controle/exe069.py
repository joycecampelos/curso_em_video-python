'''
DESAFIO 069 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
'''

contidade = contsexo = contmulheres = 0

while True:
    print('-' * 21)
    print(' CADASTRE UMA PESSOA')
    print('-' * 21)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if idade >= 18:
        contidade += 1
    if sexo == 'M':
        contsexo += 1
    if idade < 20 and sexo == 'F':
        contmulheres += 1

    continuar = ' '
    while continuar not in 'SN':
        print('-' * 21)
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {contidade} pessoas.')
print(f'Ao todo tem(os) {contsexo} homem(s) cadastrados.')
print(f'E tem(os) {contmulheres} mulher(es) com menos de 20 anos.')
