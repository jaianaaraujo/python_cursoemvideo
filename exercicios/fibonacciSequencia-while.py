# Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
# A sequencia de fibonacci sempre começa com 0 e 1, e o terceiro termo é sempre 0 + 1
print('-' * 30)
print('Sequencia de Fibonacci')
print('-' * 30)
n = int(input('Quantos termos você quer mostarar? '))
t1 = 0
t2 = 1
print('~' * 30)
print(f'{t1} -> {t2}', end='')
cont = 3  # Já começa do 3 pq já mostrei o primeiro, segundo e terceiro termo
while cont <= n:
    t3 = t1 + t2  # t3 é a soma de t1 mais t2
    print(f' -> {t3}')
    t1 = t2
    t2 = t3
    cont += 1
