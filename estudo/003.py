def calc_fibonnaci(n:int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calc_fibonnaci(n-1) + calc_fibonnaci(n-2)

def list_fibonnaci(n:int) -> list:
    lista = []
    i = 1
    while i <= n:
        lista.append(calc_fibonnaci(i))
        i += 1
    return lista

print(list_fibonnaci(10))