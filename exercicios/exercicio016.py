#Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc
num = float(input('Digite um número'))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))
#O trun ele elimina tudo que estiver depois da virgula ou ponto
# Como estou importando só o trunc, na hora de chamá-lo não coloco Math, colo apenas o trunc 

''' print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
  '''