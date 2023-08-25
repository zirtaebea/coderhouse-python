#gerando senha
senha = 1234

#input
sugestao = int(input("Digite uma senha númerica de 4 digitos: ")) 

#loop while: enquanto a senha for diferente da sugestão do usuario
while senha != sugestao:
    #print essa frase
    print("Tente novamente") 
    # e inicie novamente o input
    sugestao = int(input("Digite uma senha númerica de 4 digitos: ")) 
    #caso o usuario acerte 
    if senha == sugestao: 
        print("Você acertou!")   