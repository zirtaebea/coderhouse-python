from datetime import date #importando biblioteca

def data_dia(data): #definindo função
    semana = ["segunda", "terça", "quarta", "quinta", "sexta", "sabado", "domingo"] #identificando dias da semana em um array, o seu indice vai servir para identificar o numero com o nome
    dia_semana = date.weekday(data) #usando o metodo weekday para identificar o dia da semana da data informada
    return semana[dia_semana] #retornando nome de acordo com o numero do weekday

meu_dia = date(2023, 8, 24) #chamando meu dia
print(data_dia(meu_dia)) #printando resultado