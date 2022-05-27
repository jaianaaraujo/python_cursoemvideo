# Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.


distancia = float(input('Qualquer distância? '))
print('Você está preste a começar uma viagem de {} km'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
    print('E o preço da sua passagem será de R${:.2f}'.format(preco))
else:
    preco = distancia * 0.45
    print('E o preço da sua passagem será de R${:.2f}'.format(preco))

# Outra forma de responder

''' 
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(preco)

'''