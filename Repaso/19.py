entrada = input("Ingrese 5 numeros: ")

ListaNumeros = list(map(int, entrada.split(",")))
ListaPares = []

for i in ListaNumeros:
    if i % 2 ==  0:
        ListaPares.append(i)

print(ListaPares
