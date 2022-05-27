# Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cid = str(input('Nome da sua cidade?')).strip()
nome = cid.lower()
print(nome[0:5] == 'santo') 

# print(nome[0:5].upper() == 'SANTO')
