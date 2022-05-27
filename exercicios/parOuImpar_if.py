# Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Me diga qual é o número?'))

if (n % 2) == 0: # % o resto da divisão desse numero por 2 for igual a zero
    print('par')
else:
    print('Impar')
