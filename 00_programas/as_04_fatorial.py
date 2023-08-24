n = int(input("Digite um número inteiro"))

i = 1
resultado = 1

while i <= n: #enquanto i for menor que n
    resultado *= i #resultado multiplicado pelo valor de i
    i += 1 #iterador
print(resultado)