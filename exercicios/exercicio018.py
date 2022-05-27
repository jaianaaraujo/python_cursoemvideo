#Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math 

an = float(input('Qual medida vertical?'))
angulo = math.radians(an)
coseno = math.cos(angulo)
tangente = math.tan(angulo)
seno = math.sin(angulo)

print('O conseno é: {:.2f}, o tangente é: {:.2f},  e o seno é: {:.2f}'.format(coseno, tangente, seno))