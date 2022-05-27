def contadorLetras(texto: str, letra: str) -> int:
    contador = 0
    tam_text = len(texto) - 1
    while tam_text != 0:
        if texto[tam_text].lower() == letra.lower():
            contador += 1
        tam_text -= 1
    return contador

print(contadorLetras("bAnana", "a"))