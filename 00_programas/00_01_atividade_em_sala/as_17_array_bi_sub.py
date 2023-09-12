# importando biblioteca
import numpy as np

# criando matriz 3x3 de numeros inteiros entre 0 e 9
arr_bi = np.random.randint(0, 9, size=(3, 3))

# imprmindo matriz
print(arr_bi)

# mudando elementos da segunda linha para -1
arr_bi[1, 0] = -1
arr_bi[1, 1] = -1
arr_bi[1, 2] = -1
# também posso usar para simplificar: arr_bi[1, :] = -1

# imprimindo resultados
print(arr_bi)
