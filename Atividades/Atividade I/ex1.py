numero = int(input("Insira um número de 3 digitos: "))

uni = (numero % 10) * 100
dez = (numero // 10 % 10) * 10
cen = numero // 100

inverso = uni + dez + cen 
soma = numero + inverso

uni_s = soma % 10
dez_s = soma // 10 % 10
cen_s = soma // 100

print (cen_s, dez_s, uni_s)

resultado = cen_s + (dez_s * 2) + (uni_s * 3)

print(resultado % 10)
