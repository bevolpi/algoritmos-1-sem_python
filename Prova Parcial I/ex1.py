altura = float(input("Insira a altura do paciente (em metros): "))
peso = float(input("Insira o peso do paciente (em quilogramas): "))

IMC = peso / (altura**2)

print(f"IMC = {IMC:.2f}")

if IMC <= 24.9:
    print("Peso normal.")
else:
    print("Sobrepeso.")