#inputs para receber valores inteiros
a = int(input("Insira um número inteiro: "))
b = int(input("Insira outro número inteiro: "))

#definindo função soma
def soma(x, y):
    soma = x + y
    return soma

#definindo função subtração
def sub(x, y):
    sub = x - y
    return sub

#definindo função multiplicação
def mult(x, y):
    mult = x*y
    return mult

#testando funções
print(soma(a,b))
print(sub(a,b))
print(mult(a,b))
