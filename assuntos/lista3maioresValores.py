import heapq  
lista = [2, 3, 5, 6, 8, 4, 2, 1, 10, 15]

# Os 3 maiores:
heapq.nlargest(3, lista)
print(heapq.nlargest(3, lista))