'''
DESAFIO 061 - Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''

primeirotermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeirotermo
cont = 1

while cont <= 10:
    print(termo, end=' ➡ ')
    termo += razao
    cont += 1

print('FIM!')
