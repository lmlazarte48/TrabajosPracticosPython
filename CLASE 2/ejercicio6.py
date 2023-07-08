#Suma de los numeros enteros incluidos entre dos enteros positivos "Programa del ejercicio desafío Clase 1"
a=int(input("Ingrese un entero positivo: "))
b=int(input("Ingrese otro entero positivo: "))
if a!=b:
    if a>b:
        mayor=a; menor=b
    elif b>a:
        mayor=b; menor=a
        
    suma=0  
    mayor-=1
    while mayor>menor:
        suma+=mayor
        mayor-=1
    print(suma)    

    #print(suma+a+b)     #Si Habilito este print me suma también los extremos    