'''
DESAFIO 056 - Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
'''

nomevelho = ''
soma = maisvelho = mulheresnovas = 0

for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma += idade
    if sexo in 'Mm' and idade > maisvelho:
        maisvelho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulheresnovas += 1

print(f'A média de idade do grupo é de {soma / 4 :.1f} anos.')
print(f'O homem mais velho tem {maisvelho} anos e se chama {nomevelho}.')
print(f'A todo são {mulheresnovas} mulher(es) com menos de 20 anos.')
