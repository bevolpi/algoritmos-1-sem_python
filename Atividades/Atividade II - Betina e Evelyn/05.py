binario = input("Digite um número na base binária: ")
decimal = 0 
i = 0

valido = True
for digito in binario:
    if digito != '0' and digito != '1':
        valido = False
        break

if valido:
    binario = int(binario)
    while binario > 0:
        digito = binario % 10 
        decimal = decimal + digito * (2**i) 
        i += 1 
        binario = binario // 10
    print(f"O valor decimal é: {decimal}")
else:
    print("O número informdo não está na base binária")