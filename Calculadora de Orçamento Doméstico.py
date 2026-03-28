agua = float(input("Escreva o valor da sua água: "))
luz = float(input("Escreva o valor da luz: "))
telefone = float(input("Escreva o valor do telefone: "))
salario = float(input("Escreva qual é o seu salário: "))
if salario >= agua + luz + telefone:    
    total = (salario) - agua - luz - telefone
    print(f"O seu salário consegue pagar todas as contas. E restou {total}")
else:   
    print("Salário Insuficiente.")