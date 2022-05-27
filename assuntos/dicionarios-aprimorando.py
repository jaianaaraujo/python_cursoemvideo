# APRENDA COM ESSE EXERCICIO COMPLETO
time = list()
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
print(f'O jogador {dados["nome"]} jogou {dados["partidas"]}')
for indice, valor in enumerate(gols):
    print(f'     => Na partida {indice+1}º, fez {valor} gols.')
