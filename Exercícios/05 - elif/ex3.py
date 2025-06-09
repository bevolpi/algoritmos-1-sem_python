a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a < b and a < c:
    print("menor número: a = {a}")
elif b < a and b < c:
    print("menor número: b = {b}")
elif c < a and c < b:
    print("menor número: c = {c}")
else:
    print("Valores iguais")
