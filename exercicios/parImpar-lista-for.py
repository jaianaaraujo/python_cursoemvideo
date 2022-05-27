lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 11]
for i in range(0, len(lista) ):
    valorLista = lista[i]
    if valorLista % 2 == 0:
        print(f'Esse {valorLista} é par')
    else:
        valorImpar = lista[i]
        print(f'Esse {valorImpar} é impar')
