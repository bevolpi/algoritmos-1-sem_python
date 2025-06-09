a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
#aux é uma variável auxiliar
if a > b:
    aux = a
    a = b
    b = aux
#o aux é só p A pular, p B entrar, e dps ocupar o lugar B
if a > c:
    aux = a
    a = c
    c = aux
if b > c:
    aux = b
    b = c
    c = aux
    
print(f"{a} {b} {c}")
    
