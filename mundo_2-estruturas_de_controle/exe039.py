'''
DESAFIO 039 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import date
anodenascimento = int(input('Ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - anodenascimento

print(f'Quem nasceu em {anodenascimento} tem {idade} anos em {anoatual}.')

if idade < 18:
    print(f'Ainda falta {18 - idade} ano(s) para o alistamento.')
    print(f'Seu alistamento será em {anoatual + (18 - idade)}.')
elif idade > 18:
    print(f'Você já deveria ter se alistado há {idade - 18} ano(s).')
    print(f'Seu alistamento foi em {anoatual - (idade - 18)}.')
else:
    print('Você tem que se alistar IMEDIATAMENTE!')
