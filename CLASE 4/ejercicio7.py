#Reciba una lista de números enteros, y regrese otra lista que contenga únicamente los números que sean pares

lista=[]

def pares(*numeros):
    for i in numeros:
        if i%2==0:
            lista.append(i)
    return lista

print(pares(5, 8, 4, 9, 2))

