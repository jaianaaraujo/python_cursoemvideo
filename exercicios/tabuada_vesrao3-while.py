# Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. 


while True:
    n = int(input('Quer ver qual tabuada? '))
    if n < 0: # todo número menor que zero é negativo
        break
    for c in range(1, 11):
        print(f'{c} x {n} = {n*c}')
print('Tabuada encerrada!!!')