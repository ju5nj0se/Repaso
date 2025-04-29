licencia = input("Tiene licencia?: ")
casco = input("Tiene casco?: ")

if licencia == "no" or casco == "no":
    print("No puede conducir")
else:
    print("Puede conducir")