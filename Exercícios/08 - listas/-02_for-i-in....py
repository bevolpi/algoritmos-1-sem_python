lista = []

for i in range(5):
    lista.append(int(input("Insira um valor: ")))
    
for i in range(len(lista)):
    print(lista[i], end= " ")
    
print()

for elemento in lista: 
    print(elemento, end= " ")
#para elemento dentro da lista (se a lista tiver 4 elementos, o for vai executar 4 vzs)