# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

# um dicionário que tenha 4 jogadores, e cada jogador jogue um número aleatório (randint)
# guardar os resultados em dicionário
from random import randint # randomizar
from time import sleep # o sleep tem um dalay para carregar tal coisa em segundos
from operator import itemgetter # itemgetter ele vai ajudar a organizar 
jogador = { # criei o dicionário, coloquei as chaves com o nome de cada jogador, e em seguida como valor atribuir um randint
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}

# colocar os dicionários em ordem sabendo que o vencedor tirou o maior número no dado
for keys, values in jogador.items():
    print(f'A {keys} tirou o {values} no dado')
    sleep(1)

# Criando o ranking
ranking = list()
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True ) # itemgetter parte 1 ele colocará em ordem de valor, se eu tivesse colocado itemgetter 0 ele seria em ordem de chave

# SORTED = ORGANIZAR
# ITEMGETTER
# REVERSE = para deixar do maior para o menor

 # VALIDANDO A LISTA RANKING
print(' == RANKING: == ')
for index, valor in enumerate(ranking):
    print(f'{index+1}º lugar: {valor[0]} com {valor[1]}.') # valor 0 é a chave e valor 1 é o valor dessa chave
    sleep(1)
