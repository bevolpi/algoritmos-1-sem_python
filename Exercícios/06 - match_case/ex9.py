valor = float(input("Insira o preço do produto: R$ "))

if valor < 20:
    print(f"R$ {valor * 1.45:.2f}")
elif valor > 20 and valor < 100:
    print(f"R$ {valor * 1.3:.2f}")
else:
    print(f"R$ {valor * 1.2:.2f}")
        