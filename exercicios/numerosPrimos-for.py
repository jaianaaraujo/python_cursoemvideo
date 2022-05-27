# Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
# um número natural é primo se ele é maior que 1 e é divisível apenas por si próprio e por 1
n = int(input('Digite um número: '))
total = 0
for c in range(1, n +1):
    if n % c == 0:
        print(f'\n -> {c}', end=' ')
        total += 1
    else:
        print(f'\n  {c}', end=' ')
print(f'\n O {n} foi divisível {total} vezes ')
if total == 2: # Para que seja primo tem que ser dividido por ele mesmo e por um, ou seja, apenas 2 vezes
    print(f'O {n} é PRIMO!')
else:
    print(f'O {n} não é Primo!')