# importando biblioteca
import numpy as np

# criando array de 10 números aleatórios entre 0 e 1
array = np.random.rand(10)

# imprimindo array
print(array)

# criando um array que multiplica o array inicial por 10
novo_array = (array*10)

# criando array que converte o novo array para tipo int
array_convertido = novo_array.astype(int)

# imprimindo resultados
print(array_convertido)
