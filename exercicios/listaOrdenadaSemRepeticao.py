# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

numeros = list()
for i in range(0, 5):
    n = int(input('Digite um número: '))
    if i == 0 or n > numeros[-1]: # dou um append se ele for o primeiro ou se ele for maior que o último
        numeros.append(n) # acrescento no final
    else: # se ele não for igual a zero ou o numero digitado não for maior que o último
        pos = 0 # posição já começa com 0
        while pos < len(numeros): # enquanto a posição for menor que o numero de elementos da lista numeros, irei validar o que está abaixo
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                break
            pos+=1 # vou incrementando
print('-=' * 30)
print(f'Os valores digitados em ordem foram {numeros}')
