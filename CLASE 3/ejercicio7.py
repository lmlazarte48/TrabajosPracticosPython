#Ingresar palabras y luego las muestre por pantalla. si el usuario ingresa la palabra salir, debe terminar.
palabra=" "
while True:
    palabra=input("Ingrese una palabra - Salir: para terminar: ")
    if palabra=="Salir":
        break
    else:
        print(palabra)
    