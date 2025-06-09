sal_min = float(input("insira valor salário mínimo: "))
kw_resid = float(input("insira quantidade de kw na residencia: "))

valor_cada = (1/7 * sal_min) / 100

valor_resid = (kw_resid * valor_cada)

valor_desc = valor_resid * 0.9 

print(f"Valor de cada: R$ {valor_cada:.4f}")
print(f"Valor residencia: R$ {valor_resid:.4f}")
print(f"Valor desconto 10%: R$ {valor_desc:.4f}")


