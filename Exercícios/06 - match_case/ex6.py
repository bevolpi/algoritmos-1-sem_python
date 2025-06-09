n1 = int(input("Insira o 1° valor: "))
n2 = int(input("Insira o 2° valor: "))
calculo = input("Insira a operação desejada (+, -, *, /): ")

match calculo:
    case "Adição" | "+":
        print(f"R: {n1 + n2}")
    case "Subtração" | "-":
        print(f"R: {n1 - n2}")
    case "Multiplicação" | "*":
        print(f"R: {n1 * n2}")
    case "Divisão" | "/":
        if n2 == 0:
            print("Não existe divisão por 0")
        else:
            print(f"R: {n1 / n2:.2f}")
    case _:
        print(f"Operação inválida")