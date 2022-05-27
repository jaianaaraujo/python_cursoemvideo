# resolvendo fatorial sem recursividade
def fatorial(n):
    f_inicio = 1
    for c in range(n, 0, -1):
        f_inicio*= c
    return f_inicio # em uma função eu tenho que retornar
print(fatorial(5))