'''Implementar um algoritmo em python para calcular o cos(x). O valor de x deverá ser digitado
pelo usuário da aplicação em graus. O valor do cosseno de x será calculado pela soma dos 15
primeiros termos da série a seguir. cos(x) = 1 - (x**2/ 2!) + (x**4/ 4!) - (x**6/ 6!)'''

x = float(input("x (em graus)= "))
cos_x = 1
sinal = 1

for i in range(15):
    cont = 1
    total = 1
    while cont <= i:
        if i % 2 == 0:
            total = total * cont
            cont = cont + 1
    cos_x = cos_x - (x**i/ total) * sinal
    sinal *= -1
print(f"y = {cos_x}")

