# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resposta = 'S'
cont = 0
soma = 0
while resposta in 'sS':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    resposta = input('Quer continuar? [S/N]').upper().strip()
print('')
media = soma / cont
print(f' Você digitou {cont} números e a média foi {media}')