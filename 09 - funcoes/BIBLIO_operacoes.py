from math import sqrt
# função para calcular o valor de delta
def delta(a , b, c):
    deltinha = (b ** 2) - 4 * a * c
    return deltinha

# função para calcular e retornar o valor das raízes de uma
# equação do 2° grau

def raizes(a, b, deltinha):
    x1 = (-b + sqrt(deltinha)) / (2 * a)
    x2 = (-b - sqrt(deltinha)) / (2 * a)
    return x1, x2