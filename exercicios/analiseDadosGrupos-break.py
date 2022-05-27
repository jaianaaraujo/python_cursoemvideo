''' Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.  '''

tot18 = totH = totM = 0
while True: # O loop infinito 
    idade = int(input('Idade: '))
    sexo= ' '
    while sexo not in 'MF': # enquanto não for encontrado M ou F no sexo ele continuará perguntando
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0] 
    if idade >= 18:
        tot18+=1
    if sexo == 'M':
        totH +=1
    if sexo == 'F' and idade < 20:
        totM+=1
    resp = ' ' # a resposta ficando vazia
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao total temos {totH} homens cadastrados')
print(f'E temps {totM} mulheres com menos de 20 anos')
