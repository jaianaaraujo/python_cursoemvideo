n = s = 0 # n e cont começam com zero 
while True:
    n = int(input('Digite um número: '))
    if n == 999: # se o número for igual a 999
        break # ele vai dar brak, sair e calcular oq está em baixo
    s +=n # A soma só vai acontecer se o n não for 999
print(f'A soma vale {s}')


