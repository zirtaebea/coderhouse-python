#input do valor inteiro
n = int(input("Insira um número inteiro não negativo: "))

# para o iterador no range de n (sequencia de números no tamanho de n)
for i in range(n): #não inclui o nº 5
    print(i**2)