#Verificar si contraseña ingresada coincide con 123456 y mostrar un texto que diga si se acepta el ingreso o no.
lista=[123456, "Aceptada", "Rechazada"]
cont=int(input("Ingrese la contraseña: "))
if cont==lista[0]:
    print(lista[1])
else:
    print(lista[2])
    