P = float(input("Forneça o valor da aplicação mensal: "))
i = float(input("Forneça o valor da taxa de juros (valor entre 0 e 1): "))
n = float(input("Forneça o número de meses: "))

if 0 <= i <= 1:
    valor_acumulado = P * ((1 + i)**n - 1) / i
    print(f"Rendimento = R${valor_acumulado:.2f}")
else:
    print("Valor da taxa inválido.")
