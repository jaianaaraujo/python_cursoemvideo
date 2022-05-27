n = int(input('Digite um número: ')) # pego o número
i = 1 # o inicio já começa com 1
soma = 0 # e aqui eu vou somando
while i <= n:
    soma += i # Eu vou somando o valor de cada passada até chegar o n. Na primeira passada será a soma de 0 + 1
    i += 1

print(soma)
    