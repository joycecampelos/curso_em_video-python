''' Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três
listas geradas.'''

lista = []
pares = []
ímpares = []
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
    print()
for c, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        ímpares.append(v)
print(f'\nA lista completa é {lista}.')
print(f'A lista de pares é {pares}.')
print(f'A lista de ímpares é {ímpares}.')
