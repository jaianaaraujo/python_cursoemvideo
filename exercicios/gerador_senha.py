import random # importando a biblioteca para rondomizar
# senha que tenha números e letras, e o usuário escolhe a quantidade de cada
# FUNÇÃO GERA SENHA

def gerador_senha(quant_letras, quant_num):

    # Gerar os números primeiro
    senha:list = [] # eu crio uma lista vazia
    contador = 1
    while contador <= quant_num: 
        senha.append(random.randint(0, 9)) # pego essa lista vazia e vou colocando os números sorteados entre 0 e 9 a cada rodada. Lembrando que entre esses números de 0 a 9, ele sortea um número entre eles a cada rodada
        contador+=1 

    # Gerar as letras
    letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    contador = 1
    while contador <= quant_letras:
        senha.append(letras[random.randint(0, len(letras)-1)])
        contador+=1
    random.shuffle(senha) # para embaralhar as letras e números dentro da lista
    return senha

print(gerador_senha(3, 5))