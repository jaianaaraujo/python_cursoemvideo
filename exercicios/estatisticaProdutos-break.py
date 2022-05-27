''' Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''

totG = totM = menorP = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    totG += preco
    if preco > 1000:
        totM += 1
    elif cont ==1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi {totG:10.2f}') # 10 casas ao todo e duas casas decimais flutuantes
print(f'Tem {totM} custando mais de R$ 1000,00')
print(f'O produto mais barato {barato} custa R$ {menor:.2f}')