#Preparar una receta de un pan el panadero
receta={"Harina": 5, "Azucar": 1, "Manteca": 2}
H=int(input("Kilos de Harina: "))
A=int(input("Kilos de Azúcar: "))
M=int(input("Kilos de Manteca: "))
ingred={"Harina": H, "Azucar": A, "Manteca": M}
if receta==ingred:
    print("Si puede realiar la receta!")
else:
    print("No puede realizar la receta")
