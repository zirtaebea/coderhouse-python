#criando conta
class Conta:
    def __init__(self, titular, saldo = 0):
        self.titular = titular
        self.saldo = saldo
    
    #metodo de verificar saldo
    def meu_saldo(self):
        print(f"Olá {self.titular}! Seu saldo é de {self.saldo} reais")    
    
    #metodo de depositar
    def depositar(self, valor):
        self.saldo += valor
        return f"O seu saldo é {self.saldo}"
    
    #metodo de sacar
    def sacar(self, saque):
        if self.saldo >= saque:
            self.saldo -= saque
            print(f"O seu saldo é {self.saldo}")
        else:
            print(f"Saldo insuficiente!")


#adicionando objeto beatriz a classe conta
beatriz = Conta("Beatriz")

#depositando
beatriz.depositar(47)

#conferindo valor
beatriz.meu_saldo()

#sacando com valor menor que o saldo
beatriz.sacar(35)

#sacando com valor maior do que o disponível
beatriz.sacar(13)