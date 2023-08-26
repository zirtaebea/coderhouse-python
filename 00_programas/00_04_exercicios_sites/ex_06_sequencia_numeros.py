n = int(input("Digite um número inteiro: "))
lista = []

#para o iterador no range de números n (que será o valor que o usuário inserir)
for i in range(n): 
    
    #o iterador começando a partir do indice 1 ao invés do zero
    i += 1 
    
    #se i for menor ou igual que n
    if i <= n: 
        #adicione o valor na lista
        lista.append(i) 


# Transforma os números inteiros em strings e junta-os em uma única string
string_sem_colchetes = ''.join(map(str, lista)) #o  '' é referente aos espaços que não devem existir

#chamando resultado
print(string_sem_colchetes)