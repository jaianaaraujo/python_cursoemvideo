n = 1
lista = []

totalLista = len(lista)
while n <= 10:
    num = int(input('Digite o número: '))
    lista.append(num)
    n+=1
invertida = lista[::-1]
print(invertida)

