tempo = float(input("Digite quanto tempo (h) durou a viagem: "))
velocidade = float(input("Digite a velocidade média (km/h) do veículo: "))
automovelfaz = 10.5
# precisamos saber a quantidade de litros -> temos h, km/h e 10.5km/l, ent precisamos saber o km primeiro

distancia = velocidade * tempo # descobre km
combustivel = distancia / automovelfaz  # descobre L

print(f"A quantidade de litros de combustível gasta em uma viagem é {combustivel:.4f}")