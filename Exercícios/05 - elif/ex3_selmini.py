a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a == b or b == c or a == c:
    print("Valores iguais")
else:
    if a < b and a < c:
        print(f"{a} é o menor valor")
    elif b < c:
        print(f"{b} é o menor valor")
    else: 
        print(f"{c} é o menor valor")