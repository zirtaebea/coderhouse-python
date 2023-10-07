#input
meu_dicionario = {"Mês":["Janeiro", "Fevereiro", "Junho", "Julho"], "Quantidade": [232, 321, 589, 547]}

#verificando dicionario
print(meu_dicionario)

# sendo i o iterador no range do números de itens da chave mês
for i in range(len(meu_dicionario["Mês"])): 
    #itere todos os valores dentro da chave mes
    mes = meu_dicionario["Mês"][i] 
    #itere todos os valores na chave quantidade (SO SERVE QUANDO SABEMOS QUE A OUTRA CHAVE TEM O MESMO COMPRIMENTO)
    quantidade = meu_dicionario["Quantidade"][i] 
    #print do resultado
    print(f"Mês: {mes} / Quantidade: {quantidade}") 
    
