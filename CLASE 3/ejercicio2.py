#Ingresar su año de nacimiento y devuelva como resultado si es mayor o menor de edad.
from datetime import datetime
año = datetime.now().year
nac=int(input("Ingrese su año de nacimiento: "))
edad=año-nac
if edad<18:
    print("Es menor de edad")
else:
    print("Es mayor de edad")


