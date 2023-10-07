#criando classe retangulo
class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    #metodo para area
    def area (self):
        area = self.base * self.altura
        return f"A área do retângulo é {area}"    
    
    #metodo para perimetro
    def perimetro(self):
        perimetro = (2*self.base) + (2*self.altura)
        return f"O perímetro do retângulo é {perimetro}" 
    
retangulo1 = Retangulo(3,5)

area1 = retangulo1.area()
perimetro1 = retangulo1.perimetro()

print(f"{area1} e {perimetro1}")