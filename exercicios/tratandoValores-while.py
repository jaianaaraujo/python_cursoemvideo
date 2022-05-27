# Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n = 0
total = 0
cont = 0
while n != 999: #condição de parada
    total+=n
    n = int(input('Digite um número [999 para parar]: '))
    cont+=1
    if n == 999:
        print('Parando de calcular! ')
print(f'Você digitou {cont} e a soma entre eles foi {total}')