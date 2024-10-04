"""
Ejercicio. Hacer un programa que tenga una lista de 8 números enteros y haga lo siguiente
-Recorrer la lista y mostrarla
-hacer una funcion que recorra listas de numeros y devuelva un string
-Ordenarla y mostrarla
-Mostrar su longitud
-Buscar algún elemento(que el usuario pida por teclado)
"""

#Crear lista
numeros=[23,23,24,5,56,7,34,57,34,2]

#Recorrer y mostrar
print ("#### Recorrer y mostrar ####")
for numero in numeros:
    print (numero)

#funcion mostarLista
def mostarLista(lista):
    resultado=""
    for elemento in lista:
        resultado +="ElementoFuncion: " +str(elemento)
        resultado+="\n"
        
    return resultado

print(mostarLista(numeros))

#Ordenar y mostrar
print("####Ordenar y mostrar####")
numeros.sort() ##sort sirve para odenar una lista
print (mostarLista(numeros))

#mostrar su longitud
print("####longitud####")
print(len(numeros))


#busqueda y mostrar
print("####busqueda y mostrar####")

busqueda= int(input("introduce el número"))

comprobar = isinstance(busqueda, int)
while not comprobar or busqueda <=0:
    busqueda=int(input("introduce el número: "))
else:
    print (f"Buscar en la lista el número {busqueda} ####")
    
search=numeros.index(busqueda)
print(f"El número buscado de la lista es {search}")