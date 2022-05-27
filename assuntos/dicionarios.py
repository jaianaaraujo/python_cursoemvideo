""" Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python. Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves literais. """

# Com dicionários eu posso ter indices literais, ou seja, escrever o que tem ali em vez de números

dados = dict()
dados = {'nome': 'Pedro', 'idade': 25}

# ======= ADICIONANDO ELEMENTOS NO DICIONÁRIO =========

#No dicionários o append não funciona, eu teria que colocar um append em uma lista, e colocar o dicionários assim: dicionario.copy() dentro do append
dados['sexo'] = 'M' # perceba que não existia esse indice sexo, então acabei de criar um indice sexo com o valor M

# ======= REMOVENDO ELEMENTOS NO DICIONÁRIO =========
del dados['idade'] # ele vai eliminar o indice idade

# ======= RETORNANDO TODOS OS VALORES DO DICIONÁRIO =========
print(dados.values()) # ele retorna todos os valores do dicionário

# ======= RETORNANDO TODOS AS CHAVES/KEYS DO DICIONÁRIO =========
print(dados.keys()) # aqui eu pegarei as chaves(que são como se fossem os indices)

# ======= PEGANDO TODOS OS VALORES E KEYS DICIONÁRIO =========
print(dados.items()) # ele pega tanto as chaves como o valores

# EXEMPLO DE USO:
filme = dict()
filme = {
    'filme': 'Panda',
    'ano': 2021,
    'diretor': 'George Williass'
}

for k, v in filme.items():
    print(f'O {k} é {v}')


# EU POSSO CRIAR UMA LISTA E DENTRO DESSA LISTA TER DICIONÁRIOS
# listas são identificadas por números(indices), enquanto dicionários são identificados por keys(nomes/indices literários)

lista3 = [
    # indice 0 - lista
 { 'filme': 'Panda',
    'ano': 2021,
    'diretor': 'George Williass'},
   
    # indice 11 - lista
 {'filme': 'Panda',
    'ano': 2021,
    'diretor': 'George Williass'}
]

print(lista3[0]['ano']) # estou pegando o indice 0, e dentro do indice zero estou pegando a chave ano
