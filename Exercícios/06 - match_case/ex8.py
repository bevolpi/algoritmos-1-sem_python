renda = float("Digite sua renda anual: R$ ")

match renda:
    case renda if renda <= 10 * 10^3:
        print("Imposto de renda = Isenção total")
    case renda if renda >= 10000.01 and renda <= 25000:
        print(f"Imposto de renda = {renda * 10.35}")
    case renda if renda >= 25000.01 and renda <= 50000:
        print(f"Imposto de renda = {renda * 25.42}")
    case _:
        print(f"Imposto de renda = {renda * 29.75}")
