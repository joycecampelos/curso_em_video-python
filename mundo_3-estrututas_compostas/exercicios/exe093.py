'''
DESAFIO 093 - Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''

jogador = dict()
gols = []
jogador['Nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(1, partidas + 1):
    gols.append(int(input(f'   Quantos gols na partida {c}? ')))
jogador['Gols'] = gols[:]
jogador['Total de gols'] = sum(gols)
print('-=' * 35)
print(jogador)
print('-=' * 35)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 35)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for i, v in enumerate(gols):
    print(f'    => Na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {jogador["Total de gols"]} gols.')
