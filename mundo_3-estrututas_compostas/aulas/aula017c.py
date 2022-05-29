a = [2, 3, 4, 7]
b = a[:]
#Obs.: [:] significa que está copiando todos os elementos de A para B
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')