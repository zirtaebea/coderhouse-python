#criando variáveis e inputs
peso = float(input("Digite seu peso em KG (exemplo: 53.5): "))
altura = float(input("Digite sua altura em metros (exemplo: 1.57): "))
imc = round(peso/(altura**2), 2) # ** é operador de exponencial

#imprimindo valor IMC
print(f"Seu IMC é {imc}")