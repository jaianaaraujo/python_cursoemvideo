# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime # importando a biblioteca datetime para pegar o ano
cadastro = dict() # crio um dicionário
cadastro['nome'] = input('Nome: ') # crio uma chave nome e coloco para perguntar o nome do usuário
ano_nasc= int(input('Ano nascimento: ')) # crio uma chave ano_nasc e coloco para perguntar ao usuário
cadastro['idade'] =  datetime.now().year - ano_nasc # calculo a idade e já atribuo na chave idade
cadastro['ctps'] = int(input('Carteira de trabalho (0 não tem): ')) # crio a chave cadastro

# VALIDANDO CARTEIRA DE TRABALHO
if cadastro['ctps'] != 0: # se o cadastro for diferente que zero
    cadastro['contratacao'] = int(input('Ano de contratação: '))  # pergunto sobre a contratação
    cadastro['salario'] = float(input('Salário: R$ ')) # pergunto sobre o salário
    cadastro['aposentadoria'] = cadastro['idade'] + ((cadastro['contratacao'] + 35) - datetime.now().year) # calculo a aposentadoria
print('+*' * 30)
print(cadastro)
print('+*' * 30)

for k, v in cadastro.items():
    print(f' - {k} tem o valor {v}')