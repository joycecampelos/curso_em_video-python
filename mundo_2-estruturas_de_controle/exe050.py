'''
DESAFIO 050 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.'''

soma = qtd = 0
for c in range(1, 7):
    numero = int(input(f'Digite o {c}º número: '))
    if numero % 2 == 0:
        soma += numero
        qtd += 1
print(f'Você informou {qtd} número(s) PAR(ES) e a soma dele(s) é {soma}.')
