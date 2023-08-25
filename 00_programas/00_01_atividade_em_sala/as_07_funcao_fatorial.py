def fun_fatorial(n): #definindo função e argumentos
    i = 1 #iterador
    resultado = 1 #armazenador de resultado
    
    while i <= n: #enuqanto o iterador for menor ou igual a n, execute:
        resultado *= i #o resultado multiplicado pelo valor de i
        i += 1 #acrescentando sempre mais 1 até ser igual a n
    return resultado #retorno resultado
    
resposta = fun_fatorial(3) #resposta armazenada para imprimir

print(f"O fatorial é {resposta}") #print no terminal