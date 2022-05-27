# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

dados = dict()
dados['nome'] = input('Nome: ')
dados['partidas'] = int(input('Partidas: '))
gols = []

# GOLS
for c in range(dados['partidas']):
    gols_partida = int(input(f'Quantos gols na {c +1}º partida: '))
    gols.append(gols_partida)
   
dados['gols'] = gols
dados['total'] = sum(gols) # o SUM ele soma todos os números da lista
print('-=' * 30)
print(dados)
print('-=' * 30)
for keys, values in dados.items():
    print(f'O campo {keys} tem o valor {values}.')
print('-=' * 30)


print(f'O jogador {dados["nome"]} jogou {dados["partidas"]}')

for indice, valor in enumerate(gols):
    print(f'     => Na partida {indice+1}º, fez {valor} gols.')


# OUTRA FORMA DE PEGAR OS GOLS
""" jogador['gols'] = list()
for c in range(0, int(input(f"Quantas partidas {jogador['nome']} jogou?: "))):
    jogador['gols'].append(int(input(f"  Quantos gols na partida {c+1}?: "))) """