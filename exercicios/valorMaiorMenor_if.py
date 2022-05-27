# Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.


from re import A


a = int(input('Qua o primeiro numero? '))
b = int(input('Qual o segundo número? '))
c = int(input('Qual o terceiro numero? '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando quem é o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O menor número digitado foi {}'.format(menor))
print('O maior número digitado foi {}.'.format(maior))