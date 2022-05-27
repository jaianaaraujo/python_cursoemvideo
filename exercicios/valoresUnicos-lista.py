# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 

numeros = list() # criei uma lista vazia
while True: # enquanto for verdadeiro
    n = int(input('Digite um valor: ')) # Vou pegando os valores
    if n not in numeros: # se o n que digitei não estiver na lista numeros, então o acrescento na lista
        numeros.append(n) # aqui vou acrescendo o n na lista depois de fazer a validação acima
        print('Valor adicionado com sucesso!')
    else: # se caso tiver o n digitado já na lista
        print('Valor duplicado! Não adicionarei.') # informo que é um valor duplicado
    r = input('Quer continuar? [S/N]') # pergunto se quer continuar ou não
    if r in 'Nn': # se no R ele digitar N ou n o programa termina
        break
print('*' * 30)
# COLOCANDO EM ORDEM CRESCENTE
numeros.sort() # ordenando em ordem crescente
print(f'Você digitou os valores {numeros}')