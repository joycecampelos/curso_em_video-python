'''
DESAFIO 051 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
'''

primeirotermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimotermo = primeirotermo + (10 - 1) * razao

for c in range(primeirotermo, decimotermo + razao, razao):
    print(c, end = ' ➡ ')
print('FIM!')
