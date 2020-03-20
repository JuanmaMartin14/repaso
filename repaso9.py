kg = input("¿Cuál es tu peso en kg? ")
m = input("¿Cuál es tu estatura en metros?")
imc = round(float(kg)/float(m)**2)
print("Tu índice de masa corporal es " + str(imc))
