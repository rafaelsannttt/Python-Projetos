import math

graus = float(input("Escreva o valor em graus para um ângulo: "))
radianos = math.radians(graus)
seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)
print("O valor do seno é: ", seno)
print("O valor do cosseno é: ", cosseno)
print("O valor da tangente é: ", tangente)
