''' Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense. '''

# EXERCICIO

times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR',
         'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás','Bahia', 'Vasco da Gama', 'Atlético-MG', 'Fluminense', 'Botafogo','Ceará SC', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

# Mostrando listas de times de forma enumerada
for posi, t in enumerate(times):
    print(f'{posi}) {t}')
print('+=*' * 15)

# Mostrando os 5 primeiros times
print(f'Os 5 primeiros colocados são: {times[:6]}')
print('+=*' * 15)
print('\n')
# Os 4 últimos colocados
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('+=*' * 15)
print('\n')

# Times em ordem alfabetica
print(f'Times em ordem alfabética: {sorted(times)}') # O sorted ele não altera a tupla, simplesmente só organiza em ordem alfabetica
print('+=*' * 15)
print('\n')

# Em que posição está o time da Chapecoense.
print(f' A posição do Chapecoense é: {times.index("Chapecoense")+1}') #coloco o mais 1 pq o indice ele começa com zero
print('\n')
