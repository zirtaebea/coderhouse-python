#input do número inteiro
n = int(input("Digite um número inteiro: "))

#se o numero for impar ele é estranho
if n % 2 != 0: 
    print("Weird")
    
#se o numero for par E estiver no intervalo inclusivo de 2 <= n <=5, ele não é estranho   
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
    
#se o numero for par E estiver no intervalo inclusivo de 6<=n<=20, ele é estranho    
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
    
#se o número for par E maior que 20, ele não é estranho    
elif n % 2 == 0 and n > 20:
    print("Not Weird")