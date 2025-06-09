prova1 = float(input("Valor prova 1: "))
prova2 = float(input("Valor prova 2: "))
trab1 = float(input("Valor trabalho 1: "))
trab2 = float(input("Valor trabalho 2: "))

mediaprova = (prova1 + prova2) / 2
mediatrab = (trab1 + trab2) / 2

media = mediaprova * 0.7 + mediatrab * 0.3

# media = ((prova1 + prova2) / 2) * 0.7 + ((trab1 + trab2) / 2) * 0.3

print(f"Sua média é {media:.2f}")
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")


