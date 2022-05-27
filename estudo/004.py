def maxLista(lista:list) -> int:
    max = lista[0]
    i = len(lista)
    while i != 0:
        if max < lista[i-1]:
            max = lista[i-1]
        i -= 1
    return max

print(maxLista([13,2,3,5,6,10,1,11]))