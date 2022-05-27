# Faça uma função que some todos os inteiros de uma lista de N dimensões.
# dentro dessa lista poderá ter outras listas
def soma_inteiros(lista):
    soma = contador = 0
    while contador < len(lista):
        if type(lista[contador]) == int:
            soma += lista[contador]
        else:  # se ele não for um inteiro
            # ele chama novamente a função para calcular aquilo que não é o inteiro
            soma_parcial = soma_inteiros(lista[contador])
            soma += soma_parcial
        contador += 1
    return soma


lista = [1, 4, [4, 5, 6, [7]], 4, 6, 7, 8, 9, 0, 1, 2, 3, [4, 5, 6, 7]]
print(soma_inteiros(lista))
