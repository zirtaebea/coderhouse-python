# importando bibliotecas
import numpy as np

# lembrar que o metodo rand cria um array/matriz aleatorio no range de 0 a 1
matriz = np.random.rand(5, 5)

# imprimindo matriz
print(matriz)

# calculando estatísticas
# mean é media simples e average pode ser usado como media simples E ponderada
media = matriz.mean()
minimo = matriz.min()
maximo = matriz.max()

# imprimindo resultados
print(f"Média: {media}")
print(f"Valor mínimo: {minimo}")
print(f"Valor máximo: {maximo}")
