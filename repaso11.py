monto=float(input("ingrese un monto a invertir: "))
anos=float(input("ingrese la cantidad de anos: "))
interes=float(input("ingrese el interes anual: "))
interes2=round(float(anos)%float(interes))
plata=round(float(monto)+float(interes2))
print("capital obtenido: " +str(plata) + "$")
