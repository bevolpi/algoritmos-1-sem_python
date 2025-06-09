''' 1. imprima os nums de 1 a 20
    2.a) ler 2 valores informados pelo usuário
      b) imprimir todos os nums do 1° ao 2°
      c) imprimir só os pares entre os 2 valores. deve imprimir os extremos'''

cont = 1

#1.
contador = 1
while contador <= 20:
    print(contador)
    contador = contador + 1 #não pode ser na frente do print, pq se nao começa por 2
#lembre-se, é um laço de repetição!! 
    #BREAKPOINT + PYHTON DEBUGGER + F11 = P VER ESSE LAÇO 
    
#2.a e b) 
nm1 = int(input("Insira o 1 número: "))
nm2 = int(input("Insira o 2 número: "))
while nm1 < nm2 - 1: 
    nm1 = nm1 + 1
    print(nm1)
    
#2. c)
nm1 = int(input("Insira o 1 número: "))
nm2 = int(input("Insira o 2 número: "))

while nm1 < nm2:
    if nm1 % 2 == 0:
        print(nm1)
    nm1 = nm1 + 1