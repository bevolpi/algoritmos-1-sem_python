a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
#ERRADO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
if a > b and b > c:
    print (f"{a, b, c}")
elif a > c and c > b:
    print(f"{a, c, b}")
elif b > a and a > c:
    print(f"{b, a, c}")
elif b > c and c > a:
    print(f"{b, c, a}")
elif c > a and a > b:
    print(f"{c, a, b}")
elif c > b and b > a:
    print(f"{c, b, a}")
else:
    print("Valores iguais")