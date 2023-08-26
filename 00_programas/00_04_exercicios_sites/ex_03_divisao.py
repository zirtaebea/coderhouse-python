a = int(input("Insira um número inteiro: "))
b = int(input("Insira outro número inteiro: "))


def div_int (x, y):
    dint = x // y
    return dint


def div_normal (x, y):
    dinor = x / y
    return dinor


print(div_int(a, b))
print(div_normal(a, b))