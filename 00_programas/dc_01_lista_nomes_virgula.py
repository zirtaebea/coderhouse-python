#input para pegar nomes separados por virgula
nomes_com_virgula = input("Digite uma lista de nomes separados por virgula: ")

#fatiando input a cada virgula inserida
lista_nomes = nomes_com_virgula.split(',')

#imprimindo lista final
print(lista_nomes)