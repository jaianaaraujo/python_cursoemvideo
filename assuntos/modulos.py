# Importar a biblioteca toda:   import nomeBiblioteca
# Importal algo especifico da biblioteca: from nomeBiblioteca import oqueQueroImportar

import math  # importo tudo aqui
import random
num = int(input('Digite o número: '))
raiz = math.sqrt(num)

print('A raiz de {} é {:.2f}'.format(num, raiz))
print('A raiz de {} é {}'.format(num, math.ceil(raiz)))

numero = random.randint(1, 10)  # um numero inteiro de 1 a 10
print(numero)
