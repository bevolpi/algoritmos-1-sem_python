
andaimes = int(input("Insira a quantidade de andaimes disponíveis para locação: "))
valor = float(input("Insira o valor diário do aluguel de cada andaime: "))

fatura = ((andaimes * 0.4) * (valor * 30)) * 12
# multa = ((andaimes * 0.4) * 0.08) * ((valor * 0.15) * 30) * 12
estoque = andaimes + (andaimes * 0.2) - (andaimes * 0.05)

print(f"Faturamento anual com aluguéis: R$ {fatura}")
# print(f"Ganho anual com multas: R$ {multa}") <- ANULADA
print(f"Quantidade de andaimes ao final do ano: {estoque}")
