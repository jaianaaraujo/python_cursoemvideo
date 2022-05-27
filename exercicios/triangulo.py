# Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1  = float(input('Qual a primeira medida? '))
r2 = float(input('Qual a segunda medida? '))
r3 = float(input('Qual a terceira medida? '))
if r1 < r2+r3 and r2 < r1+r3 and r3<r2+r1: 
    print('Podem formar triangulo')
else:
    print('Não podem formar triangulo')    