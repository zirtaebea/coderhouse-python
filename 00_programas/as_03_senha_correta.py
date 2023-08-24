#gerando senha
senha = 1234
sugestao = int(input("Digite uma senha númerica de 4 digitos: ")) #input

#loop while: enquanto a senha for diferente da sugestão do usuario
while senha != sugestao:
    print("Tente novamente") #print essa frase
    sugestao = int(input("Digite uma senha númerica de 4 digitos: ")) # e inicie novamente o input
    if senha == sugestao: #caso o usuario acerte 
        print("Você acertou!")    #imprima