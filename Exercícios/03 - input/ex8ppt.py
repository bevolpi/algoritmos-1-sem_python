original = int(input("Escreva um número de 3 dígitos: "))

uni = original % 10
dez = original // 10 % 10
cen = original // 100

print(f"a dezena é: {dez}")