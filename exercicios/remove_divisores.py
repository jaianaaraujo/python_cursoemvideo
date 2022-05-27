""" 
Remove Divisíveis

Faça uma função que recebe uma lista com inteiros e devolva a lista sem os números divisíveis por 2 e/ou por 5.
"""

def remove_inteiros(lista):
    index = 0
    while index < len(lista):
        if lista[index] % 2 == 0 or lista[index] % 5 == 0:
            lista.pop(index)
            continue # se eu não colocar o continue aqui, ele vai incrementar, aumentando o número do index, sendo que eu o removi
        index+=1
    return lista # eu tenho que retornar no final pq é uma função
        
resultado = remove_inteiros([5, 6, 4, 3, 2, 1, 1, 5, 3, 1, 6, 7, 9, 0, 5])
print(f'Os números que não são divisiveis por 2 e 5 são: {resultado}')