lista1 = [1, 4, 5] 
lista2 = [2, 2, 3]
lista3= [ (lista1 + lista2) for lista1, lista2 in zip(lista1, lista2) ]

print(lista3)