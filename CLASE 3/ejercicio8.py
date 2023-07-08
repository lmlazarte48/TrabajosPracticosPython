#Pida al usuario un número entero y muestre por pantalla un triángulo rectángulo.
num=int(input("Ingrese un número: "))
num2=num%2
if num2!=0:
    i=1
else:
    i=0
num=num+1
lista=[]
for x in range(i, num, 2):
    lista.append(x)
    print(lista)
#A la inversa
"""for x in range(i, num, 2):
    lista.insert(0, x)
    print(lista)"""
