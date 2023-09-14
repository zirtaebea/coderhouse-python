import pandas as pd

# 1) abrindo o arquivo em um DF

# OBS: tive que baixar o arquivo novamente no site do kaggle pq o da pasta do curso estava corrompido, dai o arquivo baixado automaticamente foi em csv
# para ficar fiel ao exercicío e praticar outros métodos, converti csv para excel

# abrindo em csv
consoles_csv = pd.read_csv(
    '00_programas/00_03_desafios_obrigatorios/consoles.csv')

# convertendo para excel
consoles_csv.to_excel('00_programas/00_03_desafios_obrigatorios/consoles.xlsx')

# lendo em excel
consoles = pd.read_excel(
    '00_programas/00_03_desafios_obrigatorios/consoles.xlsx')

# verificando arquivo
consoles.head()


# 2) substitua a palavra NES por Nintendinho e deixe o nome de todos os consoles maíusculos
# substituindo palavra
consoles['Console Name'] = consoles['Console Name'].str.replace(
    'NES', 'Nintendinho')

# verificando substituição
nintendinho = consoles['Console Name'].str.contains('Nintendinho')
nintendinho

# deixando todos os nomes de console maíusculos
consoles['Console Name'] = consoles['Console Name'].str.upper()

# verificando alterações
consoles.head()

# verificando se todos os passos foram aplicados
consoles.loc[consoles['Console Name'].str.contains(
    'NINTENDINHO'), 'Console Name']


# 3) filtre o nome dos consoles com data de release depois de 2010
consoles_above_2010 = consoles.loc[consoles['Released Year']
                                   >= 2010, ['Console Name', 'Released Year']]
consoles_above_2010.head()


# 4) dê um describe e info da base, substitua os missing values pela string 'missing'
# describe
print(consoles.describe().round(1))
# info
consoles.info()

# verificar coluna remarks pois é a única que possui valores null e substituir com o método fillna()
consoles = consoles.fillna("missing")

# verificando se os valores foram alterados
consoles.info()


# 5) filtre os consoles que foram descontinuados a menos que 2 anos da data de release
# fazendo operação entre colunas para descobrir a diferença entre o ano de lançamento e o ano de descontinuação
consoles['diferenca'] = (
    consoles['Discontinuation Year'] - consoles['Released Year'])

# filtrando apenas os valores maiores que zero e menores que 2
diferenca = (consoles['diferenca'] > 0) & (consoles['diferenca'] <= 2)

# aplicando filtro
descontinuados_menos_2_anos = consoles[diferenca]

# verificando
descontinuados_menos_2_anos
