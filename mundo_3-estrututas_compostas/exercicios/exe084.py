"""Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""
pessoas = []
nomesepesos = []
maiorpeso = menorpeso = 0
while True:
    nomesepesos.append(str(input('Nome: ')))
    nomesepesos.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maiorpeso = menorpeso = nomesepesos[1]
    else:
        if nomesepesos[1] > maiorpeso:
            maiorpeso = nomesepesos[1]
        if nomesepesos[1] < menorpeso:
            menorpeso = nomesepesos[1]
    pessoas.append(nomesepesos[:])
    nomesepesos.clear()
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'Nn':
        break
    print()
print(f'\nAo todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maiorpeso}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maiorpeso:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {menorpeso}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menorpeso:
        print(f'[{p[0]}]', end=' ')
print()
