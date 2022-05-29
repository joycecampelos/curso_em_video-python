pessoas = {'Nome': 'Gustavo', 'Sexo': 'M', 'Idade': 22}

#print(pessoas['Nome'])
#print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos.')
#print(pessoas.keys()) #Mostra as chaves (nome, sexo e idade)
#print(pessoas.values()) #Valores atribuidos nas chaves
#print(pessoas.items()) #Mostra os itens da tabela
pessoas['Nome'] = 'Leandro'
pessoas['Peso'] = 98.5
del pessoas['Sexo']
for k, v in pessoas. items():
    print(f'{k} = {v}')
