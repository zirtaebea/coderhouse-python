import pandas as pd

cancer = pd.read_csv(
    '/home/bgsantos/Documentos/coderhouse-python/08_manipulacao_dados_pd/Cancer_Data.csv')
# print(cancer.head())

# 1) contando quantas linhas tem o dataframe com diagnosis = B
cancer_b = cancer['diagnosis'] == 'B'
cancer_filtrado = cancer[cancer_b]
print(cancer_filtrado.shape[0])


# 2) substituindo a coluna diagnosis seguindo a regra:
# B = para benign cancer
# M = para malignant cancer
cancer['diagnosis'] = cancer['diagnosis'].str.replace('B', 'benign cancer')
cancer['diagnosis'] = cancer['diagnosis'].str.replace('M', 'malignant cancer')

print(cancer.head())

# 3) filtrando ids dos malignant cancer com raio  maior que 25
print(cancer.loc[(cancer['diagnosis'] == 'malignant cancer') & (
    cancer['radius_mean'] > 25), 'id'])
