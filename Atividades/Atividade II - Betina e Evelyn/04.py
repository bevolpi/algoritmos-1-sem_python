a = 1
b = 2
soma = 0
while b <= 4000000:
    if b % 2 == 0:
        soma += b
    aux = a
    a = b 
    b = aux + a

print(soma)