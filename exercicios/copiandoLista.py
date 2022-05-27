
# EXEMPLO DE COMO COPIAR CORRETAMENTE UMA LISTA PARA OUTRA

a = [2, 4, 5, 6, 7, 8, 9, 10]
b = a[:] # dessa forma o python não vai criar ligação entre elas, apenas copiará
b[2] = 88889
print(a)
print(b) 
# Observe que ao imprimir ambas as listas, a alteração ocorreu apenas na lista b
# No entanto, se fizermos assim: b =a estamos dizendo ao Python que ambas são iguais e estarão relacionadas, então ao fazer qualquer alteração em alguma dessas listas, automaticamente estarei alterando em ambas as listas e não somente em uma 