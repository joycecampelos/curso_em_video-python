'''
DESAFIO 006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
'''

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)

print(f'\nO dobro de {n} vale {d}.\nO triplo de {n} vale {t}.\nA raiz quadrada de {n} é {r:.2f}.')
