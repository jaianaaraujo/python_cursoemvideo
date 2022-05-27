dias_semana = ['segunda-feira', 'terça-feira', 'quarta-feira'] # uma lista com os dias da semana, lembrando que as listas começam a ser contadas com o número 0
i = 0
while dias_semana:
    if i == 1:
        print("O dia da semana que corresponde a posição", i, "da lista dias_semana é:", dias_semana[i])
        break
    i += 1
'''
Resultado:
O dia da semana que corresponde a posição 1 da lista dias_semana é: terça-feira
'''