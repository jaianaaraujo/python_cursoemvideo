# FUNÇÕES

def mostrarLinha():
    print('-+' * 23)
    print('-+' * 23)


def montar(frase):
    mostrarLinha()
    print(f'{frase}')
    mostrarLinha()


montar('Olá, mundo!!!')


def somar(n1, n2):
    s = n1 + n2
    print(s)


somar(2, 6)
# Posso mudar a ordem contanto que eu explicite
somar(n2=3, n1=6)  # Estou explicitando em que variável estou atribuindo


def mult(n1):
    contador = 1
    while contador <= 10:
        s = n1 * contador
        print(f'{n1} x {contador}')
        contador += 1


mult(3)

# EMPACOTAMENTO


def contador(*num):  # Esse * significa desempacotar, neste caso específico, significa que passarei vários parâmetros e não sei a quantidade
    for valor in num:
        tamanho = len(num)  # aqui saberei a quantidade
        print(
            f'Recebi os valores: {valor} e que são {tamanho} numeros', end=' ')


contador(3, 4, 5, 7, 8)


def dobra(lista):  # crio a função como a lista como parâmetro
    posicao = 0  # ele já começa analisando o indice zero da lista
    # enquanto o indice for menor que o tamanho da lista ele vai rodando
    while posicao < len(lista):
        # a cada indice, ele pegará os valores e multiplicará por 2
        lista[posicao] *= 2
        posicao += 1  # e vai incrementando na posicao


# SOMANDO TODOS
def soma(*valores): # passarei vários parâmetros, mas não sei a quantidade exatada que vou passar
    s = 0
    for num in valores: # enquanto existir numeros no valores 
        s += num
    print(f'Somando os valores {valores} temos {s}')
# é importante lembrar que quando utilizamos dessa forma no parâmetro *valores, o que nos é retornado é todos os valores como se estivessem em uma lista