#input
n = int(input("Digite um número inteiro"))

#variaveis para a iteração
i = 1
resultado = 1

#enquanto i for menor que n
while i <= n: 
    #resultado multiplicado pelo valor de i
    resultado *= i 
    #iterador
    i += 1 
print(resultado)