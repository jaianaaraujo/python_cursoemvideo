""" Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
 """

lista = []
while True:
    lista.append(int(input('Qual número? ')))
    r = input('Quer continuar? [S/N] ').strip().upper()[0]
    if r in 'Nn':
        break
print('*' * 30)
print(f'A quantidade de números digitados foi: {len(lista)}')
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')
lista.sort(reverse=True)
print(lista)
