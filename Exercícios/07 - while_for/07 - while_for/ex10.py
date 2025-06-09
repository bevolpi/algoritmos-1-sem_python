# FOR
n = int(input("Informe o valor maior que zero: "))
y = 0 
denominador = 1
if n <= 0:
   print("Valor deve ser MAIOR Q 0")
else:
   for denominador in range (1,n+1):
         if denominador % 2 != 0:
            y = y + 1/denominador
         else:
            y = y - 1/denominador
   print(f"y = {y}")
   
# WHILE
n = int(input("Informe o valor maior que zero: "))
y = 0 
denominador = 1

if n <= 0:
   print("Valor deve ser MAIOR Q 0")
else:
   while denominador <= n:
      y = y + 1 / denominador
      denominador = denominador + 1
   print(f"y = {y}") #ERRADO!