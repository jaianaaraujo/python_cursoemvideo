# Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

n1 = input('Qual o  primeiro nome?')
n2 = input('Qual o segundo nome?')
n3 = input('Qual o terceiro nome?')
n4 = input('Qual o quarto nome?')

lista = [n1, n2, n3, n4]
shuffle(lista)
print('A lista oficial é essa:')
print(lista)
