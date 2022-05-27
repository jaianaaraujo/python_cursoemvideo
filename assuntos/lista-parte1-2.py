num = [2, 5, 6, 7, 9, 10, 4, 6, 7, 5, 7, 8, 9, 2, 5, 9]
print(num)
num[3] = 2
num.append(9)
num.insert(4, 5)
num.sort() #Ele colocará em ordem. Ele altera a lista original
sorted(num) # Ele cria uma nova list colocando em ordem
num.sort(reverse=True) # Ele colocará a lista de traz para frente
print(f'Essa lista tem {len(num)} elementos')
num.pop(2) # remove o que está na posição 2
num.remove(2) # ele remove onde tem o número 2, no entanto, remove o primeiro. Caso queira excluir todos onde está escrito 2 podemos fazer isso c

# EXEMPLO:
while 5 in num:
    num.remove(5)
else:
    ('Não encontrei o num')
print(num)

# EXEMPLO PARA ENCONTRAR O INDICE

valores =[]
valores.append(4)
valores.append(6)
valores.append(8)
for c, v in enumerate(valores):
    print(f' na posição {c}, encontrei o valor: {v}...', end='') # para ficar todos na mesma linha, eu posso colocar END=''


# EXEMPLO DE COMO COPIAR CORRETAMENTE UMA LISTA PARA OUTRA

a = [2, 4, 5, 6, 7, 8, 9, 10]
b = a[:] # dessa forma o python não vai criar ligação entre elas, apenas copiará
b[2] = 8888
print(a)
print(b)