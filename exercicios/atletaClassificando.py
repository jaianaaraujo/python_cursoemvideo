# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

from datetime import date
nasc = int(input('Sua data de nascimento: '))
ano = date.today().year
idade = ano - nasc
if idade <= 9:
    print('Até 9 anos: MIRIM')
elif idade <= 14:
    print(' Até 14 anos: INFANTIL')
elif idade <= 19:
    print('Até 19 anos: JÚNIOR')
elif idade <= 25:
    print('Até 25 anos: SÊNIOR')
else: 
    print(' Acima de 25 anos: MASTER')