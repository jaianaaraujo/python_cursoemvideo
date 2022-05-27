# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

# FUNÇÃO
def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato')

# PROGRAMA PRINCIPAL
# variável global 
n = input('Nome do Jogador: ')
g = input('Número de gols: ')

# Validando o número
if g.isnumeric():
    g = int(g)
else:
    g = 0
# Validando o nome
if n.strip() == '': #Eu tiros os espaços laterais para não dar erro e reconhecer o que está dentro dos espaços
    ficha(gol=g)
else:
    ficha(n, g) # estou colocando o valor do meu n como parâmetro, e se caso não colocar o valor do n, eu chamo a função e aparecerá apenas o gol

