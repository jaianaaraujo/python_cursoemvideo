# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
# Prestar atenção que ele pede os 10 primeiros termos.

print('*' * 20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimoTermo = primeiro + (10 -1) * razao # essa é a fórmula para descobrir o décimo tempo
print('*' * 20)
for n in range(primeiro, decimoTermo, razao):
    print('{} '.format(n), end= ' -> ')
print('Acabou!!!! ')