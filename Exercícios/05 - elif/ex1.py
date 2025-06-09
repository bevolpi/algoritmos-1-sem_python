diarias = int(input("Insira o número de diárias: "))
'''
if diarias > 15:
    print(f"Conta = R$ {(300 * diarias) + (22.50 * diarias):.2f}")
elif diarias == 15:
    print(f"Conta = R$ {(300 * diarias) + (56.00 * diarias):.2f}")
else:
    print(f"Conta = R$ ({(300 * diarias) + (88.00 * diarias):.2f}")
''' 

if diarias > 15:
    taxa = 22.50
elif diarias == 15:
    taxa = 56.00
else:
    taxa = 88.00
    
conta = (300+ taxa) * diarias

print(f"Conta = R$ {conta:.2f}")