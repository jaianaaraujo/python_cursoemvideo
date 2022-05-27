estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy()) # estou adicionando dentro da lista os dicionários 
print(brasil)
for elemento in brasil:
    for keys, values in elemento.items():
        print(keys, values)
