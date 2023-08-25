#definindo função
def primeiro_nome(n_completo):
    array_nome = n_completo.split(" ") #separando por espaços e criando um array de nomes 
    return array_nome[0] #retornando o primeiro nome

#array de nomes
nomes = ["Beatriz Gomes", "João Gabriel", "Leonardo Souza", "Lais Oliveira"]
primeiro = list(map(primeiro_nome, nomes)) #usando o map para executar a função em cada um dos itens do array
print(primeiro)  #printando resultado