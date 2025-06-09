binario = int(input("Escreva um número formado por 4 bits: "))

mil = binario // 1000
cen = binario % 1000 // 100
dez = binario % 100 // 10
uni = binario % 10

conversao = (mil * 8) + (cen * 4) + (dez * 2) + (uni * 1)

print(f"{binario} = {conversao}")

