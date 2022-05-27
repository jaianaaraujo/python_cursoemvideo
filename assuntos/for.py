# Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o "for", que é uma estrutura versátil e simples de entender. Por exemplo:
# Lça com variável de controle: ela dar um limitador
from tkinter import N


for c in range(0, 4): # O range informa o ponto inicial e o ponto final onde acaba
     print(c)
print('Acabou')

# Calculadora:
n = int(input('Qual número você quer calcular? '))
for c in range(1, 11):
    print('{} * {} =  {} '.format(c, n, c * n))
    

# SOMATÓRIO

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n 
print('O somatório de todos os valor é: {}'.format(s))
