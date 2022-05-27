# Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('*' * 20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro 
cont = 1 # a cada volta ele vai incrementando no computador
while cont <= 10:
    print(f'{termo} ->', end='')
    termo += razao
    cont+=1
print('FIIIM!!!')