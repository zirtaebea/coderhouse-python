#importando biblioteca
import as_retangulo as re

#adicionando objeto referenciando a biblioteca de origem
retangulo2 = re.Retangulo(6,7)

#chamando metodos e armazenando em variáveis
area = retangulo2.area()
peri = retangulo2.perimetro()

#imprimindo resultados
print(f"{area} e {peri}")