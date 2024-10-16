nombre = input("Escriba el nombre que quiere repetir: ")

if nombre:  # Verifica que la entrada no esté vacía
    repeticiones = int(input("¿Cuántas veces desea repetir el nombre? "))
    for _ in range(repeticiones):
        print(nombre)
else:
    print("No se introdujo un nombre.")
