import BIBLIO_operacoes

p = float(input("p = "))
if p == 0:
    print("Não é uma equação do 2° grau")
else:
    q = float(input("b = "))
    r = float(input("c = "))
    deltissimo = BIBLIO_operacoes.delta(p,q,r)
    if deltissimo < 0:
        print('Não tem raiz real')
        x1, x2 = BIBLIO_operacoes.raizes(p,q,deltissimo)
        print(f"x1 = {x1:.2f}")
        print(f"x2 = {x2:.2f}")