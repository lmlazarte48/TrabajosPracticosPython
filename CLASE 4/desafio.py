#Recibe una lista con los nombres de los alumnos de un curso, sus promedios y el valor mínimo necesario 
#para aprobar y muestre solamente los que no deben recursar la materia, ordenados por orden alfabético.

aprobados=[]
nota=7

def pares(*alumnos):
    print (alumnos)
    for i in alumnos:
        if type(i)==int:
            if i>=nota:
                a=alumnos.index(i)-1
                aprobados.append(alumnos[a])
    return sorted(aprobados)

print(pares("Martinez", 6, "Nuñez", 9, "Perea", 7, "Fernandez", 10, "Sosa", 5, "Ardiles", 8, "Dominguez", 3))

