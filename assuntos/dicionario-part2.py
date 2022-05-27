pessoas = {
    'nome': 'Gustavo',
    'sexo': 'M',
    'idade': 22
}

print(f'O {pessoas["nome"]} tem {pessoas["idade"]}')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys(): # pegado as chaves
    print(f'Segue as chaves: \n{k}')

for v in pessoas.values(): # pegando os valores
    print(v)

for k, v in pessoas.items(): # pegand os valores e chaves
    print(f'{k} = {v}')