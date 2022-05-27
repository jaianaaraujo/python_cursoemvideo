# 1) INTERECTIVE HELP
#help() 
# Quando executo essa função, aparecerá um terminal próprio do python, nele eu posso pesquisar manuais dos comandos python e dos métodos, a exemplo do print
# EXEMPLO:
#help(print) # aqui receberei o manual de como funciona o help

# 2) DOCSTRING
def contador(inicio, fim, pulaPassos):
    """
    -> Faz contagem e mostra na tela
    :param inicio: inicio da contagem
    :param fim: final da contagem
    :param pulaPassos: passos da contagem
    :return: sem retorno
    """
    c = inicio
    while c <= fim:
        print(f'{c}', end='')
        c+=pulaPassos
help(contador) # uma forma de executar a função para saber o seu manual (DOCSTRING)


# 3) PARÂMETRO OPCIONAL

def somar(a, b, c=0):
    s = a + b + c
    # Nesse caso, coloquei como valor opcional no c, então mesmo ao chamar a função e não estipular valor real

# ESCOPO DE VARIÁVEIS 
""" 
-> Escopo local: Quando atribuo dentro do método ou função
-> Escopo Global: Quando declaro fora de um método ou função e posso utilizá-la em qualquer local do meu código. 

"""

# 4) RETORNANDO VALORES:
""" 



"""