#input dos números inteiros
a = int(input("Insira um número inteiro: "))
b = int(input("Insira outro número inteiro: "))

#definindo função que retorna apenas o valor inteiro da divisão
def div_int (x, y):
    dint = x // y
    return dint

#definindo função que retorna divisão com casas decimais
def div_normal (x, y):
    dinor = x / y
    return dinor

#testando funções
print(div_int(a, b))
print(div_normal(a, b))