"""Escribir un programa que pregunte el nombre del usuario en la consola 
   y un número entero e imprima por pantalla en líneas distintas el nombre 
   del usuario tantas veces como el número introducido.

"""

nombre=input("Cuál es tu nombre:")
numero=int(input("escribe la cantidad que quieres que se repita:"))

for x in range(numero):
    print(f"{x+1}.-escribiste el nombre: {nombre}")