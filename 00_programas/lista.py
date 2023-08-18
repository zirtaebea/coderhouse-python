#criando lista vazia
lista = []

#enquanto o tamanho da lista for menor que 5, faça o input de numero e adicione cada numero no final da lista
while len(lista) < 5:
    numero = int(input("Digite um número: "))
    lista.append(numero)

#imprimindo lista
print(f"Sua lista completa é {lista}")