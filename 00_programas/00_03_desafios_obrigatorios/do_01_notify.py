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
    app_name="Aplicativo X",
    timeout=10
    )

#testando função
alerta(3, 'Clientes', 'Extração')

