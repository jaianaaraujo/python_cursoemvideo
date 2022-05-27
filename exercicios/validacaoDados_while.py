# Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Informe seu sexo: [M/F/O] ')).upper().strip()[0] #desse upper pegarei apenas a primeira letra
# quando eu não sei quantas vezes isso irá acontecer utilizamos o enquanto

while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos! Por favor, informe seu sexo corretamente: [M/F]'))
print(f'Sexo {sexo} registrado com sucesso!')


