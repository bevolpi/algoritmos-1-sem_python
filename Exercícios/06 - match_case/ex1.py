cd = int(input("Insira o código do produto: "))

if cd == 1:
    print("Alimento não perecível")
elif cd == 2 or cd == 3 or cd == 4:
    print("Alimento perecível")
elif cd == 5 or cd == 6:
    print("Vestuário")
elif 8 <= cd <= 15:
    print("Limpeza e utensílios domésticos")
else:
    print("Inválido")