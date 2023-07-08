#Calcule el total de una factura tras aplicarle el IVA

def factura(precio, iva):
    total=precio*(1+(iva/100))
    return total

print(factura(100, 10.5))