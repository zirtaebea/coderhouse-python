# importando biblioteca
import pandas as pd

# criando dataframe
frutas = pd.DataFrame({
    'fruta': ['Banana', 'Maça', 'Pera'],
    'preco': [7.90, 10.20, 11.80],
    'quantidade': [12, 3, 4]
})

# imprimindo resultado
print(frutas)
