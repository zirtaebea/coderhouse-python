meu_dicionario = {"Mês":["Janeiro", "Fevereiro", "Junho", "Julho"], "Quantidade": [232, 321, 589, 547]}
print(meu_dicionario)

for i in range(len(meu_dicionario["Mês"])): # sendo i o iterador no range do números de itens da chave mês
    mes = meu_dicionario["Mês"][i] #itere todos os valores dentro da chave mes
    quantidade = meu_dicionario["Quantidade"][i] #itere todos os valores na chave quantidade (SO SERVE QUANDO SABEMOS QUE A OUTRA CHAVE TEM O MESMO COMPRIMENTO)
    print(f"Mês: {mes} / Quantidade: {quantidade}") #print do resultado
    
