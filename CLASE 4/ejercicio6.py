#Función que reciba una lista de números y devuelva otra lista con el cuadrado de cada uno de sus componentes

lista=[]

def cuadrado(*numeros):
    for i in numeros:
        lista.append(i**2)
    return lista

print(cuadrado(5, 8, 4, 9, 2))

