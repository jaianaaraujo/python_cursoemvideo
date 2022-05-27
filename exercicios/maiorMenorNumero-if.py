primeiro = int(input("Digite o primeiro valor:"))
segundo = int(input("Digite o segundo valor:"))
terceiro = int(input("Digite o terceiro valor:"))
#quarto = int(input("Digite o quarto valor:"))
maior = primeiro
if segundo > primeiro and primeiro > terceiro:
    maior = segundo
if terceiro > primeiro and terceiro > segundo:
    maior = terceiro
menor = primeiro
if segundo < terceiro and segundo < primeiro:
    menor = segundo
if terceiro < segundo and terceiro < primeiro:
    menor = terceiro
#if quarto > primeiro and quarto > segundo and quarto > terceiro:
    #maior = quarto

print(f"O menor número digitado foi {menor}")
print(f"O maior número digitado foi {maior}")