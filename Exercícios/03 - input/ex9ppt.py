original = int(input("Escreva um número de 3 dígitos: "))

uni = original % 10
dez = original // 10 % 10
cen = original // 100

uni_cen = uni * 100
dez_dez = dez * 10

print(f"O inverso é {uni_cen + dez_dez + cen}")