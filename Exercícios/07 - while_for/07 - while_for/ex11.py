'''Escreva um programa em Python que leia os lados de n triângulos. Para cada triângulo
imprima a sua classificação quanto aos lados (equilátero, isósceles ou escaleno). O
programa deverá parar a execução quando o usuário digitar o valor zero para um dos
lados. Observação: para que os valores formem um triângulo é necessário que cada um
dos lados seja menor que a soma dos outros dois.'''
# esse jeito ta fazendo com for, é melhor usar while!! pq o usuario que indica o n, e não
# é o que o ex pede
n = int(input("Insira a quantidade de triângulos: "))

for index in range(n):
    a = int(input("Lado 1: "))
    b = int(input("Lado 2: "))
    c = int(input("Lado 3: "))
    if a == 0 or b == 0 or c == 0:
        break
    elif a < b + c and b < c + a and c < a + b:
            if a == b == c:
                print("Triângulo Equilátero")
            elif a == b or b == c or c == a:
                print("Triângulo Isósceles")
            else:
                print("Triângulo Escaleno")
    else:
        print("Não é triângulo")


