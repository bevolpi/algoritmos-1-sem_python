'''Escreva um programa em Python que leia 3 valores inteiros. O programa deverá
ter uma função para determinar e retornar o maior valor digitado'''

def maior(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    return c

x = int(input("a = "))
y = int(input("b = "))
z = int(input("c = "))

maior = maior(x, y, z)
print(f"{maior}")