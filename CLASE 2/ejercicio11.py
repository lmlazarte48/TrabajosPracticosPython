#Comparar inversión en plazo fijo 50% anual, con otro de 42% con cobro de dividendos mensuales.
dinero=float(input("Ingrese el monto: "))
cf1=dinero*((1+0.5)**1)
cf2=dinero*((1+0.035)**12)
print("Inversión a plazo fijo tasa anual 50%: ", cf1)
print("Inversión a plazo fijo tasa mensual 3.5%: ", cf2)
if cf1>cf2:
    print("Le conviene el plazo fijo 50% anual")
elif cf1<cf2:
    print("Le conviene palzo fijo 3.5% mensual")
else:
    print("Le conviene cualquiera de los dos")