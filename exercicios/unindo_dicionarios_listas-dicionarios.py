""" Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média """
galera = list()
pessoa = dict() # é um dicionário
soma = media = 0
while True: 
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa.clear() # porque no próximo ciclo já virá uma pessoa nova
        pessoa['sexo'] = input('sexo: [M/F] ').upper()[0] # colocando em letra maiuscula e pegando só a primeira letra
        if pessoa['sexo'] in 'MF':
            break
        print(f'ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy()) # adiconando os dicionários dentro da lista
   
    while True: # Para saber se quer continuar ou não
        resposta = input('Quer continuar? [S/N] ').upper()[0]
        if resposta in 'SN':
            break
        print(f'ERRO! Responda apenas S ou N.')
    if resposta == 'N':
        break
print('=-' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A média das idades são {media} anos')
print(f'As mulheres cadastradas foram:', end='')
for p in galera:
    if p['sexo'] in 'fF':
        print(f'{p["nome"]}')
# lista pessoas acima da média
print()
print('D) Lista das pessoas que estão acima da média: ', end='')
for p in galera:
    if p['idade'] > media:
        print(f'{p["idade"]}')