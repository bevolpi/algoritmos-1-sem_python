valor = float(input("Insira o preço do produto: "))
cd_pag = int(input("Insira o código da forma de pagamento: "))

match cd_pag:
    case 1:
        valor = valor * 0.9
        print(f"R$ {valor:.2f}")
    case 2:
        valor = valor * 0.95
        print(f"R$ {valor:.2f}")
    case 3:
        valor = valor / 2
        print(f"Valor de cada parcela: R$ {valor:.2f}")
    case 4:
        valor = valor * 1.1
        print(f"R$ {valor:.2f}")
    case _:
        print("Código inválido")
        
'''
if cd_pag == 1:
    valor = valor * 0.9
    print(f"R$ {valor:.2f}")
elif cd_pag == 2:
    valor = valor * 0.95
    print(f"R$ {valor:.2f}")
elif cd_pag == 3:
    valor = valor
    print(f"R$ {valor:.2f}")
elif cd_pag == 4:
    valor = valor * 1.1
    print(f"R$ {valor:.2f}")
else:
    print("Código inválido") '''