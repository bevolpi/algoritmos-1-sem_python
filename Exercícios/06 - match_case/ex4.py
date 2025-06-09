idade = int(input("Insira a idade do nadador: "))
    
match idade:
    #case 5 | 6 | 7
    case idade if idade  > 4 and idade < 8: 
        print("Infantil A")
    #case 8 | 9 | 10
    case idade if idade > 7 and idade < 11: 
        print("Infantil B")
    #case 11 | 12 | 13
    case idade if idade > 10 and idade < 14: 
        print("Juvenil A")
    case idade if idade > 13 and idade < 18:
        print("Juvenil B")
    case idade if idade >= 18:
        print("Adulto")
    case _:
        print("Inválido")