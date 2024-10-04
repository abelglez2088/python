from  io import open
import pathlib 

# abrir archivo

ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
file = open(ruta,"r")



# Leer contenido 
#contenido = file.read()
#print(contenido)


# Leer contenido y guardar en lista
lista = file.readlines()
file.close()

print(lista)