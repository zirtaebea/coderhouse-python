from datetime import datetime

def dia_semana(data):
#converter string p datetime
    data=datetime.strptime(data, "%d/%m/%Y")
#formata a data para obter o nome do dia da semana
    nome_do_dia = data.strftime('%A')
    
    return nome_do_dia

#usando função
data = '16/02/1999'
print(dia_semana(data))