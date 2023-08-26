n = int(input("Digite um número inteiro: "))
lista = []

for i in range(n): #para o iterador no range de números n (que será o valor que o usuário inserir)
    i += 1 #o iterador começando a partir do indice 1 ao invés do zero
    if i <= n: #se i for menor ou igual que n
        lista.append(i) #adicione o valor na lista
        

# Transforma os números inteiros em strings e junta-os em uma única string
string_sem_colchetes = ''.join(map(str, lista)) #o  '' é referente aos espaços que não devem existir

#chamando resultado
print(string_sem_colchetes)