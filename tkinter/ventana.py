#tkinter 
#modulo para crear interfaces graficas de usuario


from tkinter import *
import os.path
#crear la venta raiz

ventana = Tk()
#propiedades
ventana.title("interfaz grafica con python")
#icono
ruta_icono=os.path.abspath('./imagenes/hotel.png.c')

if not os.path.isfile(ruta_icono):
    ruta_icono = os.path.abspath('.tkinter/imagenes/hotel.png')
    
ventana.iconbitmap()
                           
#tamano de ventana
ventana.geometry("750x450")
#bloquear tamaño de la ventana 
ventana.resizable(0,0)
#arrancar y mostrar  hasta que se cierra
ventana.mainloop()
