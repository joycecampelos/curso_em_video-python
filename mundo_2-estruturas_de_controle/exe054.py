'''
DESAFIO 054 - Crie um programa que leia o ano de nascimento da sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''

from datetime import date
anoatual = date.today().year
maiores = menores = 0

for c in range(1, 8):
    anodenascimento = int(input(f'Em que ano a {c} pessoa nasceu? '))
    idade = anoatual - anodenascimento
    if idade >= 21:
        maiores += 1
    else:
        menores += 1
print(f'Ao todo tivemos {maiores} pessoas maiores de idade.')
print(f'E também tivemos {menores} pessoas menores de idade.')
