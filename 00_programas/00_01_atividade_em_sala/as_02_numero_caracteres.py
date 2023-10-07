#input
frase = input("Digite uma frase: ")

#separando palavras
frase_array = frase.split(" ")

#verificando se o array foi feito
print(frase_array)

#loop para informar caracteres de cada palavra
for palavra in frase_array:
    caracteres = len(palavra)
    print(f"A palavra {palavra} possui {caracteres} caracteres")