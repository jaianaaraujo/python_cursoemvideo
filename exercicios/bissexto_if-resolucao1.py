# Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
# todos os anos múltiplos de 4 que também não são múltiplos de 100
from calendar import isleap

'''
ano = int(input('Que ano quer analisar? '))
if ano % 4 == 0:
    print('O ano {} é BISEXTO'.format(ano))
else:
    print('O ano {} não é BISEXTO'.format(ano)) 
    
    '''

ano = int(input('Qual ano você quer descobrir se é Bisexto? '))
print(isleap(ano))
