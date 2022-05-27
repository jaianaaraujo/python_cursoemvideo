# Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

# COPIANDO OS DADOS
pessoas = list()
dados= ['Ivan', 25]
pessoas.append(dados[:])
print(pessoas)

# LISTA DENTRO DE LISTA (ACESSANDO)
pessoas1 = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas[0][0]) # eu quero o indice zero da lista pessoas1, e desse indice que peguei, eu quero o indice zero dentro dele
print(pessoas1[1][1]) # aqui será ['Maria', 19] e 19
print(pessoas[2][0])

# ------------- PARTE PRÁTICA ----------------
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste)
teste[0] = 'Maria'  # como eu fiz um append direto, ele alterará em ambas as listas
print(galera)

# EXEMPLO DE CÓPIA
a = [2, 4, 5, 6, 7, 8, 9, 10]
b = a[:] # dessa forma o python não vai criar ligação entre elas, apenas copiará
b[2] = 8888
print(a)
print(b)