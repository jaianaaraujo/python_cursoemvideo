# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()
print('********* Analisando o seu nome **********')
print('Seu nome em maiusculo é: {} '.format(nome.upper()))
print('Seu nome em letra minuscula é: {} '.format(nome.lower()))
print('Quantas letras tem seu nome sem considerar os epaços em branco: {} '.format(
    len(nome) - nome.count(' ')))

print('Seu primeiro nome tem {} letras '.format(nome.find(' ')))

separa = nome.split()  # O slipit jogara os nomes dentro de uma lista

print('Seu primeiro nome tem {} letras'.format(len(separa[0])))
