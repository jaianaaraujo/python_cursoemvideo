""" Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves. """

temporario = []
principal = []
maior = menor = 0
while True:
    temporario.append(input('Nome: '))
    temporario.append(float('Peso: '))
    principal.append(temporario[:]) # Gera uma cópia sem ligação entre elas 
    if len(principal) == 0:
         maior = menor = temporario[1]
    else:
        if temporario[1] > maior:
            maior = temporario[1]  
        elif temporario[1] < menor:
            menor = temporario[1]
    temporario.clear() 
    resposta = input('Quer continuar? [S/N]').strip().lower()[0]
    if resposta in'nN':
        break
print('*+=' * 30)
print(f'Os dados foram {principal}')
print(f'Ao todo, você cadastrou {len(principal)}')
print(f'O maior peso foi de {maior}Kg')
for p in principal:
    if p[1] == maior:
        print(f'Está pessoa {p[0]} tem o {maior}kg peso maior')
print(f'O menor peso foi {menor}kg')