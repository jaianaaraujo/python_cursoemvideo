def limpa_divisiveis(lista:list):
    contador = 0
    while contador < len(lista):
        if lista[contador] % 2 == 0 or lista[contador] % 5 ==0:
            lista.pop(contador)
            continue
        contador+=1
    return lista
print(limpa_divisiveis([5,4,8,6,9,7,5,3,1,1]))