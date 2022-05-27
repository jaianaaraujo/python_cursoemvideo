# Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

n = str(input('Digite se nome')).strip()
nome = n.split()
tamanho = len(nome)

print('Seu primeiro nome é: {}, e seu segundo nome é {}'.format(nome[0], nome[len(nome)-1]))

print(nome[tamanho - 1]) #para mostrar o último, eu pego o total do tamanho, lembrando que começa a contar do zero, e para que der certo diminuo por 1

#o [-1] pode ser utilizado para se referir ao último objeto de uma lista, assim como [-2] seria a penúltima e assim por diante.