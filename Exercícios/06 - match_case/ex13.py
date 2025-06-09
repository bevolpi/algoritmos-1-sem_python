sal_atual = float(input("Insira o salário atual: "))
cargo = input("Insira o cargo: ")
tempo = int(input("Insira a quantidade de anos trabalhados: "))

# COMO USAR MATCH
if cargo == "Gerente":
    if tempo >= 5:
        novo_sal = sal_atual * 1.1
    elif tempo >= 3 and tempo < 5:
        novo_sal = sal_atual * 1.09
    else:
        novo_sal = sal_atual * 1.08
elif cargo == "Engenheiro":
    if tempo >= 5:
        novo_sal = sal_atual * 1.11
    elif tempo >= 3 and tempo < 5:
        novo_sal = sal_atual * 1.1
    else:
        novo_sal = sal_atual * 1.09
elif cargo == "Técnico":
    if tempo >= 5:
        novo_sal = sal_atual * 1.12
    elif tempo >= 3 and tempo < 5:
        novo_sal = sal_atual * 1.11
    else:
        novo_sal = sal_atual * 1.10
else:
    novo_sal = sal_atual * 1.05
        
        
print(f"Novo salário: R$ {novo_sal}")
print(f"Salário atual: R$ {sal_atual}")
print(f"Aumento: R$ {novo_sal - sal_atual}")
