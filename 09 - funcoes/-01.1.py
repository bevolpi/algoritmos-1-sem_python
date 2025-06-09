#definição da função para somar 2 números
def somar():
    resp = v1 + v2            #resp = variável local
    print(f"soma = {resp}")

#entrada de dados
v1 = int(input("V1 = "))      #v1 = variável global
v2 = int(input("V2 = "))

#chamar a função para execuçao do comando
somar()

#MAS essa forma ta ruim, o print precisa ser fora! 
#----------------------------------------------------------------

def somar():
    resp = v1 + v2       
    return resp
    
#entrada de dados
v1 = int(input("V1 = "))   
v2 = int(input("V2 = "))

resultado = somar()      #resultado é p ser "resp" pq é mais lógico, só deixei nomes diferente p 
                         #tu entender
print(f"soma = {resultado}")