ListaNombres = ["juan", "maria", "juan", "maria", "juan"]
a = input("Ingrese el nombre: ")
Contador = int(0)
for i in range(len(ListaNombres)):
    if a == ListaNombres[i]:
        Contador = Contador + 1

print(f"El numero de veces que {a} esta en la lista es de: {Contador}")