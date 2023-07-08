#Recibe una lista de numeros y devuelve el promedio

def promedio(*numeros):
    p=0
    for i in numeros:
        p=p+i
    return p/len(numeros)

print(promedio(5, 8, 4, 9, 2))

