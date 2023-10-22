import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

# DICIONÁRIO REGEX:
# 1. Meta-caracteres
#     .: Representa qualquer caractere, exceto uma nova linha.
#     ^: Indica o início da linha.
#     $: Indica o fim da linha.
#     *: Corresponde a zero ou mais ocorrências do caractere anterior.
#     +: Corresponde a uma ou mais ocorrências do caractere anterior.
#     ?: Corresponde a zero ou uma ocorrência do caractere anterior.
#     |: Operador OU. Corresponde a uma expressão ou outra.
# 2. Quantificadores
#     {n}: Corresponde a exatamente 'n' ocorrências do caractere anterior.
#     {n,}: Corresponde a 'n' ou mais ocorrências.
#     {n,m}: Corresponde entre 'n' e 'm' ocorrências.
# 3. Conjuntos e classes de caracteres
#     [...]: Corresponde a qualquer caractere entre colchetes.
#     [^...]: Corresponde a qualquer caractere que não esteja entre colchetes.
#     \d: Corresponde a qualquer dígito. Equivalente a [0-9].
#     \D: Corresponde a qualquer não dígito.
#     \w: Corresponde a qualquer caractere alfanumérico ou sublinhado.
#     \W: Corresponde a qualquer caractere que não seja alfanumérico ou sublinhado.
#     \s: Corresponde a qualquer espaço em branco (espaço, tabulação, nova linha, etc).
#     \S: Corresponde a qualquer caractere que não seja espaço em branco.
# 4. Grupos e referências
#     (...): Define um grupo.
#     \n: Refere-se ao n-ésimo grupo capturado.
# 5. Afirmações
#     (?=...): Afirmação positiva à frente. Verifica se há uma correspondência à frente, mas não consome caracteres.
#     (?!...): Afirmação negativa à frente.

# 6. Modificadores
# i: Ignora a diferença entre maiúsculas e minúsculas.
# m: Multilinha. Faz com que ^ e $ correspondam ao início e ao fim de qualquer linha.
# g: Global. Corresponde a todas as ocorrências.

# função para identificar placas no formato brasileiro
# def verificar_placa(placa):
#     if re.match(r"^[A-Z]{3}-\d{4}$", placa):
#         # ^[A-Z]{3)-: 3 letras maiúsculas no inicio SEGUIDAS DE UM HÍFEN
#         #\d: Corresponde a qualquer dígito. Equivalente a [0-9].4 DIGITOS NO FINAL
#             return True
#     return False


def email_valido(email):
    if re.findall(r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,4}$', email):
        return True
    return False

# emails = {'email' : [
#     'beagomesnt@gmail.com',
#     'be4atriz.com',
#     'zirtaeb_bea@gmail.com',
#     'zirtaeb.dev@gmail.com',
#     'zirtaeb.dev@gmail.comer',
#     'beatriz@gmail.com.br'
# ]}

# df_email = pd.DataFrame(emails)
# print(df_email)


# df_email['email_valido'] = df_email['email'].apply(email_valido)
# print(df_email)

def data_valida(data):
    if re.match(r'^\d{2}/([0][1-9]|[1][0-2])/\d{4}$', data):
        return True
    return False

# datas = {'datas': ['16-02-1999',
#                 '09/11/1996',
#                 '12/13/2005',
#                 '16/02/2010',
#                 '2000/10/11']}

# df_datas = pd.DataFrame(datas)

# df_datas['datas_validas'] = df_datas['datas'].apply(data_valida)
# print(df_datas)


url = "https://www.amazon.com.br/"
lista_img = []


def count_imagens(url, lista):
    response = requests.get(url)
    link = BeautifulSoup(response.text, 'html.parser')
    link.prettify()
    imagens = link.find_all('img')
    for img in imagens:
        links_imagens = img.get('src')
        lista.append(links_imagens)
    count = len(lista)
    print(f"a página web tem {count} imagens")


count_imagens(url, lista_img)
