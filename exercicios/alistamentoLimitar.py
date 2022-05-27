# Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

anoAtual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade =  anoAtual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, anoAtual))
if idade < 18:
    print('você tem {} anos. Ainda irá se alistar.'.format(idade))
elif idade == 18:
    print('Hora de se alistar')
elif idade > 18:
    anos = idade - 18
    print('Você deveria ter se alistado há {} anos.'.format(anos))
    