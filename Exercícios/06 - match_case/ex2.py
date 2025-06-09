cd = int(input("Insira o código do produto: "))

match cd:
    case 1:
        print("Alimento não perecível")
    case 2 | 3 | 4:
        print("Alimento perecível") 
    case 5 | 6:
        print("Vestuário")
    case cd if cd >= 8 and cd <= 15:
        print("Limpeza e utensílios domésticos")
    case _:
        print("Inválido")
