# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
totmulher20 = 0
for p in range(1, 5):
    print(f'------- {p}ª PESSOA ------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]')).strip()
    somaIdade += idade
    if p == 1 and sexo in 'Mm': #Assim ele reconhecerá tanto M maiusculo como minúsculo
        maiorIdadeHomem = idade
        nomeVelho = nome
    elif sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    elif sexo in 'Ff' and idade < 20:
        totmulher20 += 1
        
mediaIdade = somaIdade/4
print(f'A média de idade do grupo é {mediaIdade}.')
print(f'O homem mais velho tem {maiorIdadeHomem} anos e se chama {nomeVelho}.')
print(f'Ao todo são {totmulher20} mulheres menores de 20 anos.')