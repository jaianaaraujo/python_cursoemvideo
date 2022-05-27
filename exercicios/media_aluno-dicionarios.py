# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = dict()
aluno['nome'] = input('Nome: ').strip() # criando a chave e pedindo ao usuário para inserir algum valor
aluno['media'] = float(input(f'A média do {aluno["nome"]}: '))


# ANALISANDO A SITUAÇÃO DE APROVAÇÃO DO ALUNO
if aluno['media'] >= 7:
    aluno['situacao'] = 'aprovado'
elif  5 <= aluno['media'] < 7:
    aluno['situacao'] = 'recuperacao'
else:
    aluno['situacao'] = 'reprovado'

print('+=' * 15)

# ACESSANDO TODAS CHAVES E VALORES INSERIDAS PELOS USUÁRIO UMA A UMA
for k, v in aluno.items():
    print(f' {k} é igual ao {v}')

print(aluno)