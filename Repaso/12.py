frutas = ["manazana", "pera", "arroz"]

print(f"las frutas son: {frutas}")

borrar = input("Eliga una fruta a eliminar: ")
if borrar in frutas:
    frutas.remove(borrar)
    print("la fruta ha sido removida")
else:
    print("El elemento no se encuentra en la lista")


