#Restaurant: cantidad de platos que van a consumir gastando todo el dinero
personas=input("Cantidad de comensales: ")
p=int(personas)
dinero=0
while p!=0:
    p-=1
    dinero+=int(input("Ingrese el dinero de la persona "+ str(int(personas)-p) + ": "))
    
precio=int(input("Ingrese el precio del plato: "))
cantidad=dinero//precio
print("Pueden consumir", cantidad, "platos")
    