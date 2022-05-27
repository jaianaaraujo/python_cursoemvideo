# Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

from time import sleep

velocidade = float(input('Qual é a velocidade atual do carro?'))
sleep(2)
print('*' * 30)
print('Analisando a sua velocidade...')
print('*' * 30)
sleep(2)
if velocidade<=80:
    print('Tenha um bom dia e dirija com segurança!')
else:
    multa = (velocidade - 80) * 7
    print('Você foi multado. A multa vai custar R$7,00 por cada km acima do limite. Totalizando: {:.2f}'.format(multa))


