# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

from datetime import date

def voto(ano): # uma função voto que recebrá como parâmetro o ano
   atual = date.today().year # da biblioteca date eu quero a data de hoje, mas só o ano
   idade = atual - ano
   if idade < 16:
       return f'Com a idade {idade} voto negado!'
   elif idade == 16:
        return f'Com a idade {idade} voto opcional!'
   elif idade > 18:
        return f'Com a idade {idade} voto obrigatório!'
print(voto(2020))
