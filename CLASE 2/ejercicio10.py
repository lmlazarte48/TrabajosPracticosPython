#Comparar inversión en plazo fijo 50% anual, y bonos y acciones en la bolsa 25% semestral a 5 años.
dinero=float(input("Ingrese el monto: "))
cf1=dinero*((1+0.5)**5)
cf2=dinero*((1+0.25)**10)
print("Inversión a plazpo fijo: ", cf1)
print("Inversión en bonos y acciones: ", cf2)
if cf1>cf2:
    print("Le conviene el plazo fijo")
elif cf1<cf2:
    print("Le conviene los bonos y acciones")
else:
    print("Le conviene cualquiera de los dos")
