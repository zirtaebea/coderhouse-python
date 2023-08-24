frase = input("Digite uma frase: ")
frase_array = frase.split(" ")

print(frase_array)

for palavra in frase_array:
    caracteres = len(palavra)
    print(f"A palavra {palavra} possui {caracteres} caracteres")