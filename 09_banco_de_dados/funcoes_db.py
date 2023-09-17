import pandas as pd
import sqlite3

# 1) dataframe com as tabelas do banco de dados


def tabelas_bd():
    # fazendo conexão
    conn = sqlite3.connect('coderhouse.db')

    # definindo query
    query = "SELECT name FROM sqlite_master WHERE type='table'"

    # salvado os dados em um dataframe
    schema = pd.read_sql(query, conn)

    # imprimindo resultados
    print(schema)

    # fechando conexão
    conn.close()


# 2) salva dataframe df na tabela nome_tabela
def salva_bd(df, nome_tabela):
    # fazendo conexão
    conn = sqlite3.connect('coderhouse.db')

    # salvando dataframe na tabela
    df.to_sql(nome_tabela, conn, if_exists='replace', index=False)

    # fechando conexão
    conn.close()


# 3) carrega tabela nome_tabela num dataframe
def carrega_bd(nome_tabela):
    # fazendo conexão
    conn = sqlite3.connect('coderhouse.db')

    # fazendo a consulta da tabela nome_tabela
    query = f"SELECT * FROM {nome_tabela}"

    # salvando resultado em uma variavel
    consulta = pd.read_sql(query, conn)

    # fechando conexão
    conn.close()

    # retornando resultado obtido da consulta
    return consulta


# 4) realizando testes com o o excel fastfood
fastfood = pd.read_excel("09_banco_de_dados/fastfood.xlsx")
print(fastfood.head(2))

# 4.1) inserindo tabela produtos
# conectando ao banco de dados
conn = sqlite3.connect('coderhouse.db')

# criando dataframe produtos
df_produtos = pd.DataFrame({
    'nome': ['ovos', 'manteiga', 'peixe'],
    'valor': [10, 20, 30]
})

# escrever o dataframe na tabela 'produtos'
df_produtos.to_sql('produtos', conn, if_exists='replace', index=False)

# fechar a conexão
conn.close()


# 4.2) usando a primeira função
tabelas_bd()

# 4.3) segunda função para salvar uma tabela no banco de dados + utilizando a primeira função novamente para ver se foi inserido corretamente
salva_bd(fastfood, 'fastfood')
tabelas_bd()

# 4.4) carregando a tabela em um dataframe
teste_fastfood = carrega_bd('fastfood')
print(teste_fastfood.head())
