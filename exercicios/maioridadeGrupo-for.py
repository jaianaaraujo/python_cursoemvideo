# Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
maiorIdade = 0
menorIdade = 0
anoH = date.today().year
for i in range(1, 7):
    anoN = int(input(f'Em que ano a {i}º pessoa nasceu? '))
    idade = anoH - anoN
    if idade <= 18:
        menorIdade +=1
    elif idade >= 18:
        maiorIdade += 1

print(f'Ao todo tivemos {maiorIdade} pessoas maiores de idade.')
print(f'E também tivemos {menorIdade} pessoas menores de idade.')