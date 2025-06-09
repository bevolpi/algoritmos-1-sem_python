salario_minimo = float(input("Valor salário mínimo (litros): "))
agua = float (input("Litros de água utilizados: "))

valor = ((salario_minimo * 0.02) * agua) / 1000

print(f"Valor da conta é: R$ {valor:.2f}")