import numpy as np

# criando array de 10 números aleatórios entre 0 e 100
aleatorios = np.random.randint(0, 100, size=(10))

# imprimindo array
print(f"Array: {aleatorios}")

# imprimindo tipo de dado
# o atributo dtype retorna o tipo de dado do array
print(f"Tipo de dado do array: {aleatorios.dtype}")
