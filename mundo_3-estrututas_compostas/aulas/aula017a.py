num = [2, 5, 9, 1]

num[2] = 3  # Muda o número
print(num)

num.append(7)  # Adiciona números no final da lista
print(num)

num.sort()  # Organiza os números em ordem crescente
print(num)

num.sort(reverse=True)  # Organiza os números em ordem decrescente
print(num)

num.insert(2, 0)  # Inseri o número depois da vírgula na posição antes da vírgula
print(num)

del num[3]
print(num)

num.pop()  # Remove o último número
print(num)

num.pop(2)  # Remove o número na posição 2
print(num)

num.remove(2)  # Remove o valor colocado em parentêses
# Obs.: mesmo tendo valores iguais, ele removerá o primeiro que achar
print(num)

# Verifica se o número existe na lista, se sim, remove ele
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4!')

print(f'Essa lista tem {len(num)} elementos.')
