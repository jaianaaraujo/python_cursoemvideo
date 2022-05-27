''' Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares. 
'''

num = (int(input('Digite o primeiro número: ')),
      int(input('Digite o segundo número: ')),
      int(input('Digite o terceiro número: ')),
      int(input('Digite o quarto número: ')))
print(f'Você digitou os valores {num}')

# Quantas vezes o valor 9 apareceu
print(f'O valor 9 apareceu {num.count(9)} vezes')

if 3 in num:
    # Em que posição foi digitado o primeiro valor 3
    print(f'O número 3 apareceu pela primeira vez na {num.index(3)+1}º posição')
else:
    print('O valor 3 nãpo foi digitado em nenhuma posição.')
# Quais foram os números pares

for p in num:
    if num % 2 == 0:
        print(num, end=' ')