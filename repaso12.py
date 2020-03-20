peso_m=75
peso_p=112
munecas=float(input("ingrese la cant de munecas a comprar"))
payasos=float(input("ingrese la cant de payasos a comprar"))
peso_p2=round(float(payasos)*peso_p)
peso_m2=round(float(munecas)*peso_m)
peso=round(peso_m2+peso_p2)
print("el peso es " + str(peso) + "g")
