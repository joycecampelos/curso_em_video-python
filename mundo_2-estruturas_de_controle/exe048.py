'''
DESAFIO 048 - Faça um programa que calcula a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''

soma = qtd = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        soma += c
        qtd += 1
print(f'A soma de todos os {qtd} valores solicitados é {soma}.')
