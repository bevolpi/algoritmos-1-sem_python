'''Escreva um programa em python que calcule e imprima no terminal o valor da série S a partir de
x e n informados pelo usuário da aplicação. 
S = x + (x**2/2) + (x**3/3) + ... + (x**n/n)'''

x = int(input("X = "))
n = int(input("N = "))
cont = 1
while cont <= n:
    s = s + (x**cont/cont)
    cont += 1
print(s)