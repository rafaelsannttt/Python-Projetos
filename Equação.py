a = float(input("Qual é o valor de A?: "))
b = float(input("Qual é o valor de B?: "))
c = float(input("Qual é o valor de C?: "))
delta = (b**2) - 4 * a * c
if a == 0:  
    print("Não é equação do segundo grau")
elif delta < 0: 
    print("Não há raízes reais")
elif delta >= 0:    
    x1 = (-b + delta ** 0.5) / (2 * a)
    x2 = (-b - delta ** 0.5) / (2 * a)
    print(f"O x1 é {x1} enquanto o x2 é {x2}.")