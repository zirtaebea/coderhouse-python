#criando variáveis e inputs
peso = float(input("Digite seu peso em KG: "))
altura = float(input("Digite sua altura em metros: "))
imc = round(peso/(altura*altura), 2)

#chamando inputs
peso
altura

#imprimindo valor IMC
print(f"Seu IMC é {imc}")