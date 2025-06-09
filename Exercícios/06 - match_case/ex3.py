idade = int(input("Insira a idade do nadador: "))

if idade > 4 and idade < 8:
    print("Infantil A")
elif idade > 7 and idade < 11:
    print("Infantil B")
elif idade > 10 and idade < 14:
    print("Juvenil A")
elif idade > 13 and idade < 18:
    print("Juvenil B")
elif idade > 18:
    print("Adulto")
else:
    print("Inválido")