#Pregunte al usuario su edad y muestre por pantalla cuanto debe abonar para ingresar al parque.
valores=[0, 100, 200, 400, 1000, 500]
edad=int(input("Ingrese la edad: "))
if edad<2:
    print("Debe pagar $", valores[0])
elif edad<=4:
    print("Debe pagar $", valores[1])
elif edad<=10:
    print("Debe pagar $", valores[2])
elif edad<=18:
    print("Debe pagar $", valores[3])
elif edad>18:
    while True:
        jub=input("Es jubilado? S/N:")
        if jub=="S" or jub=="s":
            print("Debe pagar $", valores[5])
            break
        elif jub=="N" or jub=="n":
            print("Debe pagar $", valores[4])
            break
        else:
            print("Respuesta no válida")
            