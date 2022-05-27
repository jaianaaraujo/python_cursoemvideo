# -------------- Manipular cadeia de texto dentro do python

# Para o Python toda cadeia de texto está entre aspas simples ou aspas duplas
# Cada letra  e espaço recebe um número de indice
# O indicie começa com 0


# ---------- FATIAMENTO

# É conseguir pegar pedaços

frase = 'Jaiana Santos da Silva Araújo'

print(frase[9:13])  # Ele vai pegar os caractere de 9 a 12, o 13 ele exclui
print(frase[0:6])
# Ele vai pegar do indice 0 até o indice 5 o 6 ele exclui. e pegara o caracter de 2 em 2
print(frase[0:6:2])
print(frase[8:])  # Nesse caso ele pegará do 8 até o final
print(frase[8::3])  # Coemça do oito até o final pulando em 3 em 3
print(frase[-1]) # Quando utilizamos o - siginifica que pegaremos os últimos, nesse caso do -1 pegaremos o último elementos que é o "O"

# ----------------- ANÁLISE

# É saber algumas informações da string tais como com que letra ela começa, com que letra ela termina, qual o tamanho dela...

len(frase)  # Len vai mostrar o tamanho da array (elemento)
frase.count('o')  # quantas vezes aparece a letra 'o' minuscula
# Quantas vezes aparece a letra 'o' minuscula do zero até o sete
frase.count('o', 0, 8)
# Quantas vezes encontrou 'ana'. ATENÇÃO, quando você coloca no find um valor que não existe ele retornará como resultado o valor -
frase.find('ana') #Ao utilizar o find, ele mostra em que posição está localizado aquilo
'Jaiana' in frase  # Dentro da frase existe a palavra curso.  # Ele só informa se tem ou n 
sorted(frase) # ele ordenará em ordem alfabetica


# -------------- TRANSFORMAÇÃO

# O replace irá substituir o nome Jaiana por Socorro
frase.replace('Jaiana', 'Socorro')
frase.upper()  # Ele colocará as palavras em maiúsculo
frase.lower()  # Colocará as palavras em minusculo
frase.capitalize()  # Ele joga a string toda para minusculo e APENAS a primeira letra ele joga para maiuscula, Na frase que estamos utilizando só o J de jaiana ficaria maiusculo
frase.title()  # Utilizando title podemos alterar a primeira letra para maiusculo de cada palavra que está na frase
frase.strip()  # Removerá todos os espaços em branco no inicio e fim na string, se tiver algum no meio permanecerá, a remoção ocorre apenas no inicio e final
frase.rstrip()  # Vai remover os espaços em branco que estão a direita.
frase.lstrip()  # Removerá os espaços da esquerda, mas permanecerá os espaços da direita, ou seja, o o lstrip remove apenas os espaços da esquerda

# --------------- DIVISÃO

# gera uma lista com todas as palavras da cadeia de caractere. O split()método divide uma string em uma lista.
frase.split()

''' 
txt = "welcome to the jungle"

x = txt.split()

print(x)

***** Resultado no terminal:

['welcome', 'to', 'the', 'jungle']
'''

'-'.join(frase)  # O join coloca como separador, nesse caso o separado será -


# -------------- TESTANDO O CONTEÚDO

frase1 = ' Curso em Vídeo Python '
print(frase1[3::2])
print(frase.upper().count('O')) # Contando a quantidade de 'o' maiuscula da frase foi colocada com maiuscula através do upper
print(len(frase)) #para saber a quantidade de letras que tem, lembrando que ele contabiliza os espaços em branco também 
print(len(frase.strip())) #Quero saber quantidade de letras (caracteres) que tem na frase e ao mesmo  tempo removendo os espaços em branco, então nesse caso, ele retornará apenas a quantidade de letras sme cotar com os espaços em branco que tem no iniicio e final 

frase = frase.replace('Python', 'Android') # Coloco na variável para que o novo valor seja salvo

print('curso' in frase) # Ele só informa se tem ou n 
print(frase.find('em'))

# ---------- IMPRIMINDO O TEXTO INTEIRO
# Coloca 3 aspas duplas e o texto dentro dessas 3 aspas, assim o texto será mosrado como colocamos entre as aspas

print("""Em linguística, a noção de texto é ampla e ainda aberta a uma definição mais precisa. Grosso modo, pode ser entendido como manifestação linguística das ideias de um autor, que serão interpretadas pelo leitor de acordo com seus conhecimentos linguísticos e culturais. Seu tamanho é variável.

“Conjunto de palavras e frases articuladas, escritas sobre qualquer suporte”.[1]

“Obra escrita considerada na sua redação original e autêntica (por oposição a sumário, tradução, notas, comentários, etc.)”.[2]

"Um texto é uma ocorrência linguística, escrita ou falada de qualquer extensão, dotada de unidade sociocomunicativa, semântica e formal. É uma unidade de linguagem em uso."[3]""")
