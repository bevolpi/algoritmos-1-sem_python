renda = float("Digite sua renda anual: R$ ")

if renda <= 10 * 10^3:
    print("Imposto de renda = Isenção total")
elif renda >= 10000.01 and renda <= 25000:
    print(f"Imposto de renda = {renda * 10.35}")
elif renda >= 25000.01 and renda <= 50000:
    print(f"Imposto de renda = {renda * 25.42}")
else:
    print(f"Imposto de renda = {renda * 29.75}")
