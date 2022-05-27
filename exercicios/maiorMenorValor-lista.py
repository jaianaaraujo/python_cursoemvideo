#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 

listanum = []
maior = 0
menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: '))) 
    if c == 0: # Se o contador for igual a zero (indice zero) tanto o maior e o menor serão o número que está no indice zero
        maior = menor = listanum[c]
    else: # Se não estive no indice 0 então ele começa a fazer essas validações
        if listanum[c] > maior:
            maior = listanum[c]
        elif listanum[c] < menor:
            menor = listanum[c]
print('+=' * 30)
print(f'Você digitou os seguintes valores: {listanum}')
print(f'O maior número é {maior} e o menor número é o {menor}')
print('+=' * 30)

# MOSTRANDO O INDICE
for i, v in enumerate(listanum):
    if v == maior:
        print(f'O {maior} valor está na posição {i}º da lista')
    elif v == menor:
        print(f'O menor valor {menor} está na posição {i}º da lista')
