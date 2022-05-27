# Listas

lanche = ['c', 'h', 'su', 'piz', 'pic', 'cook']

# INSERINDO
lanche.append('jj')  # Adiciona algo no final da lista
lanche.insert(0, 'cf')  # Aqui eu escolho em qual índice queremos adicionar

# EXCLUINDO
del lanche[3]
lanche.pop(3)  # normalmente o pop é utilizado para eliminar o último parametro, mas podemos também, indicar o indice que queremos eliminar
lanche.remove('pic')  # você coloca o que você quer eliminar pelo conteúdo

# EXEMPLO DE USO
if 'piz' in lanche:
    lanche.remove('piz')

# DECLARANDO LISTA

valores = list(range(4, 11))
print(valores)  # Vai imprimir uma lista de 4 até 10

# ORDENANDO
valores.sort()  # ordenar na ordem alfabética ou númerica
valores.sort(reverse=True)  # Ordenará de forma inversa
print(valores)

# TAMANHO DA LISTA
