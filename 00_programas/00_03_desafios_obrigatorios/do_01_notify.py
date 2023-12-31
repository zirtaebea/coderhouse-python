#instalando plyer no terminal (pip install plyer)
#importando bibliotecas
from plyer import notification 
from datetime import datetime


#definindo função de alerta
def alerta(nivel, base, etapa):
    
    #identificando os tipos de alerta com base no nível inserido na função
    #se nivel for igual a 1 então o alerta será baixo
    if nivel == 1:
        tipo_alerta = 'Alerta baixo'
        
    #se nivel for igual a 2 então o alerta será médio
    elif nivel == 2: 
        tipo_alerta = 'Alerta médio'
        
    #se nivel for igual 3 então o alerta será alto
    elif nivel == 3:
        tipo_alerta = 'Alerta alto'
    
    #função de notificação    
    notification.notify(
    title=f"ATENÇÃO: {tipo_alerta}",  # título do alerta
    message="Falha no carregamento da base {} na etapa {}.\n{}".format(base, etapa, str(datetime.now())),  # mensagem do alerta
    app_name="Base de dados",
    timeout=10
    )

#loop para verificar se o valor inserido no input do nível é aceito
while True:
    try:
        meu_nivel = int(input("Insira o número correspondente ao nível do alerta: \n 1 - BAIXO \n 2 - MÉDIO \n 3 - ALTO\n"))
        if meu_nivel in [1, 2, 3]:
            break  #sai do loop se o número for válido
        else:
            print("Número inválido, tente novamente.") #se não for valido aparece essa mensagem
    except ValueError:
        print("Entrada inválida. Insira um número válido.") #se nenhum valor for apresentado ou não for um inteiro aparece essa mensagem

#inputs de base e etapa
minha_base = input("Insira a base que ocorreu o conflito: ")
minha_etapa = input("Insira a etapa na qual ocorreu o conflito: ")

#testando função
alerta(meu_nivel, minha_base, minha_etapa)

